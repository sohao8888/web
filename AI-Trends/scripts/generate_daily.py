from __future__ import annotations

import argparse
import ast
import json
import re
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIRS = [ROOT / "01_Sources", ROOT / "02_Signals"]
DAILY_DIR = ROOT / "07_Daily"
TEMPLATE_PATH = ROOT / "90_Templates" / "daily-template.md"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.S)


@dataclass
class Note:
    path: Path
    note_type: str
    title: str
    date: str
    source_name: str
    source_url: str
    company: list[str]
    theme: list[str]
    signal_type: str
    importance_raw: str
    confidence_raw: str
    status: str
    summary: str
    my_take: str
    related_notes: list[str]
    body: str
    modified_at: datetime
    why_important: str = ""
    impacted_points: list[str] = field(default_factory=list)
    watch_points: list[str] = field(default_factory=list)

    @property
    def importance_score(self) -> int:
        return normalize_level(self.importance_raw)

    @property
    def confidence_score(self) -> int:
        return normalize_level(self.confidence_raw)

    @property
    def is_signal(self) -> bool:
        return self.note_type == "signal"

    @property
    def is_source(self) -> bool:
        return self.note_type == "source"

    @property
    def wikilink(self) -> str:
        return f"[[{self.path.stem}]]"

    @property
    def rank_score(self) -> tuple[int, int, int, int, float]:
        status_bonus = 1 if self.status not in {"draft", "archived"} else 0
        company_bonus = 1 if self.company else 0
        return (
            self.importance_score,
            self.confidence_score,
            status_bonus,
            company_bonus,
            self.modified_at.timestamp(),
        )


def normalize_level(value: Any) -> int:
    if isinstance(value, (int, float)):
        return max(0, min(5, int(value)))
    if value is None:
        return 0
    text = str(value).strip().lower()
    mapping = {
        "high": 5,
        "medium": 3,
        "low": 1,
        "critical": 5,
        "processed": 3,
        "draft": 1,
    }
    if text in mapping:
        return mapping[text]
    try:
        return max(0, min(5, int(float(text))))
    except ValueError:
        return 0


def parse_scalar(raw: str) -> Any:
    raw = raw.strip()
    if raw == "":
        return ""
    for parser in (json.loads, ast.literal_eval):
        try:
            return parser(raw)
        except Exception:
            pass
    return raw.strip('"').strip("'")


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text

    frontmatter: dict[str, Any] = {}
    for line in match.group(1).splitlines():
        if ": " not in line:
            continue
        key, raw = line.split(": ", 1)
        frontmatter[key.strip()] = parse_scalar(raw)

    body = text[match.end() :]
    return frontmatter, body


def clean_text(text: str) -> str:
    lines = [line.strip() for line in text.strip().splitlines() if line.strip()]
    return " ".join(lines)


def extract_section(body: str, heading: str) -> str:
    pattern = rf"^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)"
    match = re.search(pattern, body, re.M | re.S)
    if not match:
        return ""
    return match.group(1).strip()


def parse_bullet_section(body: str, heading: str) -> list[str]:
    section = extract_section(body, heading)
    points = []
    for line in section.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            points.append(stripped[2:].strip())
    return points


def parse_note(path: Path) -> Note:
    text = path.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(text)
    note = Note(
        path=path,
        note_type=str(frontmatter.get("type", "")).strip(),
        title=str(frontmatter.get("title", path.stem)).strip(),
        date=str(frontmatter.get("date", "")).strip(),
        source_name=str(frontmatter.get("source_name", "")).strip(),
        source_url=str(frontmatter.get("source_url", "")).strip(),
        company=ensure_list(frontmatter.get("company", [])),
        theme=ensure_list(frontmatter.get("theme", [])),
        signal_type=str(frontmatter.get("signal_type", "")).strip(),
        importance_raw=str(frontmatter.get("importance", "")).strip(),
        confidence_raw=str(frontmatter.get("confidence", "")).strip(),
        status=str(frontmatter.get("status", "")).strip(),
        summary=clean_text(str(frontmatter.get("summary", "")).strip()),
        my_take=clean_text(str(frontmatter.get("my_take", "")).strip()),
        related_notes=ensure_list(frontmatter.get("related_notes", [])),
        body=body,
        modified_at=datetime.fromtimestamp(path.stat().st_mtime),
    )

    if note.is_signal:
        note.why_important = clean_text(extract_section(body, "2. 为什么重要"))
        note.impacted_points = parse_bullet_section(body, "3. 影响谁")
        note.watch_points = parse_bullet_section(body, "4. 未来 3 到 12 个月值得继续观察什么")

    return note


def ensure_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if value in (None, ""):
        return []
    return [str(value).strip()]


def collect_recent_notes(hours: int) -> list[Note]:
    cutoff = datetime.now() - timedelta(hours=hours)
    notes: list[Note] = []
    for directory in SOURCE_DIRS:
        if not directory.exists():
            continue
        for path in sorted(directory.glob("*.md")):
            if datetime.fromtimestamp(path.stat().st_mtime) >= cutoff:
                notes.append(parse_note(path))
    return dedupe_notes(notes)


def dedupe_notes(notes: list[Note]) -> list[Note]:
    deduped: dict[tuple[str, str], Note] = {}
    for note in notes:
        key = (note.note_type, note.title)
        current = deduped.get(key)
        if current is None or note.modified_at > current.modified_at:
            deduped[key] = note
    return sorted(deduped.values(), key=lambda item: item.modified_at)


def pick_top_signals(notes: list[Note], limit: int) -> list[Note]:
    signals = [note for note in notes if note.is_signal]
    processed = [note for note in signals if note.status not in {"draft", "archived"}]
    drafted = [note for note in signals if note.status in {"draft", "archived"}]
    ranked = sorted(processed, key=lambda item: item.rank_score, reverse=True)
    if len(ranked) < limit:
        ranked.extend(sorted(drafted, key=lambda item: item.rank_score, reverse=True))
    return ranked[:limit]


def group_by_entity(notes: list[Note], attr: str) -> list[tuple[str, list[Note]]]:
    buckets: dict[str, list[Note]] = defaultdict(list)
    for note in notes:
        values = getattr(note, attr)
        for value in values:
            buckets[value].append(note)

    def bucket_score(item: tuple[str, list[Note]]) -> tuple[int, int, float]:
        _, bucket_notes = item
        signal_count = sum(1 for note in bucket_notes if note.is_signal)
        top_score = max((note.rank_score for note in bucket_notes), default=(0, 0, 0, 0, 0.0))
        return (len(bucket_notes), signal_count, top_score[-1])

    return sorted(buckets.items(), key=bucket_score, reverse=True)


def summarize_company(company: str, notes: list[Note]) -> str:
    top_signal = next((note for note in sorted(notes, key=lambda item: item.rank_score, reverse=True) if note.is_signal), None)
    top_source = next((note for note in sorted(notes, key=lambda item: item.rank_score, reverse=True) if note.is_source), None)
    focus = top_signal or top_source
    titles = "、".join(note.title for note in sorted(notes, key=lambda item: item.rank_score, reverse=True)[:2])
    judgment = focus.my_take or focus.summary if focus else "暂时观察。"
    watch = first_watch_point(focus)
    return (
        f"- `{company}`：相关笔记 {len(notes)} 条，重点集中在 {titles}。"
        f"判断：{judgment or '暂时观察。'}"
        f"继续观察：{watch}。"
    )


def summarize_theme(theme: str, notes: list[Note]) -> str:
    top_signal = next((note for note in sorted(notes, key=lambda item: item.rank_score, reverse=True) if note.is_signal), None)
    focus = top_signal or sorted(notes, key=lambda item: item.rank_score, reverse=True)[0]
    judgment = focus.my_take or focus.summary if focus else "暂时观察。"
    watch = first_watch_point(focus)
    links = "、".join(note.wikilink for note in sorted(notes, key=lambda item: item.rank_score, reverse=True)[:3])
    return (
        f"- `{theme}`：今天的相关信号主要集中在 {links}。"
        f"判断：{judgment or '暂时观察。'}"
        f"继续观察：{watch}。"
    )


def first_watch_point(note: Note | None) -> str:
    if note and note.watch_points:
        return note.watch_points[0]
    return "暂时观察，等待更多同类信号或更强证据"


def who_benefits(note: Note) -> str:
    if note.company:
        return "、".join(note.company[:4])
    if note.impacted_points:
        return note.impacted_points[0]
    return "暂时观察，当前笔记没有明确给出直接受益方"


def who_is_pressured(note: Note) -> str:
    text = f"{note.title} {note.summary} {note.my_take}".lower()
    if "代理" in note.title or "代理" in note.summary:
        return "传统搜索分发、只卖前端界面的 SaaS，以及缺乏代理适配能力的工作流产品"
    if "推理" in note.title or "基础设施" in note.summary or "电力" in note.summary:
        return "依赖廉价无限推理假设的模型和应用公司"
    if "治理" in note.title or "合法性" in note.title or "信任" in note.title:
        return "治理结构争议更大、公共信任更弱的头部实验室"
    if "语音" in note.title:
        return "只把语音当附属模态、而不是主入口的产品"
    if note.status == "draft" or note.confidence_score <= 1:
        return "暂时观察，当前证据不足以明确给出受压方"
    if "product" in text:
        return "暂时观察，可能受压的是旧产品形态和旧工作流"
    return "暂时观察，当前笔记没有明确给出直接受压方"


def build_top_change_section(note: Note) -> str:
    support_links = [note.wikilink] + [link for link in note.related_notes[:3] if link.startswith("[[")]
    support_text = "、".join(dict.fromkeys(support_links))
    fact = note.summary or note.title
    judgment = note.my_take or note.why_important or "暂时观察。"
    watch = "；".join(note.watch_points[:3]) if note.watch_points else first_watch_point(note)
    return "\n".join(
        [
            f"### {note.title}",
            "",
            f"- 事实：{fact}",
            f"- 判断：{judgment}",
            f"- 谁受益：{who_benefits(note)}",
            f"- 谁受压：{who_is_pressured(note)}",
            f"- 接下来观察：{watch}",
            f"- 支撑笔记：{support_text}",
        ]
    )


def build_top_signal_line(note: Note) -> str:
    watch = first_watch_point(note)
    return f"- {note.wikilink}：{note.summary or note.title} 接下来观察：{watch}。"


def build_judgments(top_signals: list[Note]) -> str:
    lines = []
    for note in top_signals[:3]:
        lines.append(
            f"- {note.title}：{note.my_take or note.summary or note.title}"
            f" 谁受益：{who_benefits(note)}。"
            f" 谁受压：{who_is_pressured(note)}。"
            f" 接下来观察：{first_watch_point(note)}。"
        )
    return "\n".join(lines) if lines else "- 暂无足够信号形成初步判断。"


def build_temporary_observations(notes: list[Note]) -> str:
    candidates = [
        note
        for note in sorted(notes, key=lambda item: item.rank_score, reverse=True)
        if note.status == "draft" or note.confidence_score <= 1
    ]
    if not candidates:
        return "- 暂无明显需要单列为“暂时观察”的条目。"
    lines = []
    for note in candidates[:5]:
        lines.append(f"- {note.wikilink}：{note.summary or note.title} 暂时观察，等待更多证据。")
    return "\n".join(lines)


def build_related_links(notes: list[Note]) -> str:
    sources = [note.wikilink for note in notes if note.is_source][:10]
    signals = [note.wikilink for note in notes if note.is_signal][:12]
    lines = []
    if sources:
        lines.append(f"- Source：{'、'.join(dict.fromkeys(sources))}")
    if signals:
        lines.append(f"- Signal：{'、'.join(dict.fromkeys(signals))}")
    return "\n".join(lines) if lines else "- 暂无相关笔记链接。"


def build_topics(top_signals: list[Note]) -> str:
    if not top_signals:
        return "\n".join(
            [
                "- 《今天的 AI 趋势信号里，哪一条最值得继续跟》",
                "- 《从最近 24 小时笔记看，AI 行业判断有没有发生变化》",
                "- 《哪些方向仍然只是暂时观察，而不是趋势》",
            ]
        )

    topics = []
    for note in top_signals[:3]:
        topics.append(f"- 《{note.title}：谁受益，谁受压，接下来观察什么》")
    return "\n".join(topics)


def load_template_frontmatter() -> dict[str, Any]:
    defaults = {
        "type": "daily",
        "title": "",
        "date": "",
        "source_name": "",
        "source_url": "",
        "company": [],
        "theme": [],
        "signal_type": "daily_report",
        "importance": "",
        "confidence": "",
        "time_horizon": "short_term",
        "status": "draft",
        "summary": "",
        "my_take": "",
        "related_notes": [],
        "tags": ["daily", "ai-trends", "日报"],
    }
    if TEMPLATE_PATH.exists():
        template_text = TEMPLATE_PATH.read_text(encoding="utf-8")
        parsed, _ = parse_frontmatter(template_text)
        defaults.update(parsed)
    return defaults


def dump_frontmatter(data: dict[str, Any]) -> str:
    lines = ["---"]
    ordered_keys = [
        "type",
        "title",
        "date",
        "source_name",
        "source_url",
        "company",
        "theme",
        "signal_type",
        "importance",
        "confidence",
        "time_horizon",
        "status",
        "summary",
        "my_take",
        "related_notes",
        "tags",
    ]
    for key in ordered_keys:
        lines.append(f"{key}: {json.dumps(data.get(key, ''), ensure_ascii=False)}")
    lines.append("---")
    return "\n".join(lines)


def generate_daily_content(target_date: datetime, notes: list[Note], hours: int) -> str:
    top_signals = pick_top_signals(notes, limit=5)
    top_changes = top_signals[:3]
    company_groups = group_by_entity(notes, "company")
    theme_groups = group_by_entity(notes, "theme")

    related_notes = []
    for note in top_signals[:8]:
        related_notes.append(note.wikilink)
        related_notes.extend(link for link in note.related_notes if link.startswith("[["))
    related_notes = list(dict.fromkeys(related_notes))

    company_values = []
    for company, _ in company_groups[:10]:
        company_values.append(company)
    theme_values = []
    for theme, _ in theme_groups[:10]:
        theme_values.append(theme)

    template_data = load_template_frontmatter()
    template_data.update(
        {
            "title": f"{target_date.strftime('%Y-%m-%d')} AI趋势日报",
            "date": target_date.strftime("%Y-%m-%d"),
            "company": company_values,
            "theme": theme_values,
            "importance": "high" if top_signals else "low",
            "confidence": "medium" if top_signals else "low",
            "status": "draft",
            "summary": build_summary(top_changes),
            "my_take": build_take(top_changes),
            "related_notes": related_notes,
        }
    )

    top_change_blocks = [build_top_change_section(note) for note in top_changes] or ["- 暂无足够信号生成今日变化。"]
    company_lines = [summarize_company(company, bucket) for company, bucket in company_groups[:8]] or ["- 今天没有足够的公司级更新。"]
    theme_lines = [summarize_theme(theme, bucket) for theme, bucket in theme_groups[:8]] or ["- 今天没有足够的主题级更新。"]
    top_signal_lines = [build_top_signal_line(note) for note in top_signals[:5]] or ["- 暂无可跟踪 signal。"]

    sections = [
        f"# {template_data['title']}",
        "",
        "## 扫描范围",
        "",
        f"- 扫描日期：{target_date.strftime('%Y-%m-%d')}",
        "- 扫描目录：`01_Sources`、`02_Signals`",
        f"- 最近 {hours} 小时更新笔记：`01_Sources` {sum(1 for note in notes if note.is_source)} 条，`02_Signals` {sum(1 for note in notes if note.is_signal)} 条",
        "- 说明：脚本按最近 24 小时修改时间读取笔记，优先提炼真正改变行业判断的 signal；同日文件会直接覆盖更新。",
        "",
        "## 今日真正改变行业判断的 3 条变化",
        "",
        *top_change_blocks,
        "",
        "## 按公司看今天发生了什么",
        "",
        *company_lines,
        "",
        "## 按主题看今天的信号",
        "",
        *theme_lines,
        "",
        "## 今天最值得继续跟踪的 5 个信号",
        "",
        *top_signal_lines,
        "",
        "## 今天形成的初步判断",
        "",
        build_judgments(top_signals),
        "",
        "## 暂时观察",
        "",
        build_temporary_observations(notes),
        "",
        "## 相关笔记链接",
        "",
        build_related_links(notes),
        "",
        "## 适合继续写成内容的 3 个选题",
        "",
        build_topics(top_signals),
        "",
    ]

    body = "\n".join(sections).replace("\n\n\n", "\n\n")
    return f"{dump_frontmatter(template_data)}\n\n{body}"


def build_summary(top_changes: list[Note]) -> str:
    if not top_changes:
        return "最近 24 小时没有足够的 source 或 signal 可用于生成日报。"
    titles = "、".join(note.title for note in top_changes[:3])
    return f"最近 24 小时纳入日报的更新笔记显示，最值得关注的变化集中在：{titles}。"


def build_take(top_changes: list[Note]) -> str:
    if not top_changes:
        return "暂时观察。"
    return "；".join(note.my_take or note.summary or note.title for note in top_changes[:3])


def write_daily(target_date: datetime, content: str) -> Path:
    DAILY_DIR.mkdir(parents=True, exist_ok=True)
    target_path = DAILY_DIR / f"{target_date.strftime('%Y-%m-%d')} AI趋势日报.md"
    target_path.write_text(content, encoding="utf-8")
    return target_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate or update the daily AI trends note.")
    parser.add_argument(
        "--date",
        help="日报日期，格式 YYYY-MM-DD。默认使用本地今天。",
    )
    parser.add_argument(
        "--hours",
        type=int,
        default=24,
        help="向前扫描最近多少小时更新的文件，默认 24。",
    )
    return parser.parse_args()


def resolve_target_date(date_arg: str | None) -> datetime:
    if not date_arg:
        return datetime.now()
    return datetime.strptime(date_arg, "%Y-%m-%d")


def main() -> None:
    args = parse_args()
    target_date = resolve_target_date(args.date)
    notes = collect_recent_notes(hours=args.hours)
    content = generate_daily_content(target_date=target_date, notes=notes, hours=args.hours)
    output_path = write_daily(target_date=target_date, content=content)
    print(f"Updated daily note: {output_path}")
    print(f"Recent notes scanned: {len(notes)}")


if __name__ == "__main__":
    main()
