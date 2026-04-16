---
type: "source"
title: "Vercel CEO：我们70_的流量现在来自AI代理，“谁也没料到” Anthropic、OpenClaw、OpenAI"
date: "2026-04-10"
source_name: "More or Less Podcast"
source_url: "https://www.youtube.com/watch?v=f43JCxhKLEg&list=WL&index=10&pp=iAQBsAgC"
company: ["Vercel", "Anthropic", "OpenAI"]
theme: ["AI代理", "开发者工具", "流量入口"]
signal_type: "podcast"
importance: "high"
confidence: "high"
time_horizon: "short_term"
status: "processed"
summary: "Vercel CEO 提到其文档流量中约 70% 已来自编码代理，说明开发者信息入口正在从“人类搜索”转向“机器读取”。这意味着文档、框架和 API 设计不仅要面向开发者，还要面向代理检索、调用和执行。对 OpenAI、Anthropic 等模型平台来说，这也是“代理成为新分发层”的强烈信号。"
my_take: "这类信号很强，后续可以重点关注 docs、SDK 和 API 说明文档是否普遍开始为 agent-first 重写。"
related_notes: ["[[Vercel]]", "[[Anthropic]]", "[[OpenAI]]", "[[AI代理]]", "[[开发者工具]]", "[[流量入口]]"]
tags: ["source", "Vercel", "Anthropic", "OpenAI", "AI代理", "开发者工具", "流量入口"]
---

# Vercel CEO：我们70_的流量现在来自AI代理，“谁也没料到” Anthropic、OpenClaw、OpenAI

## 来源信息

- 原始链接：[查看原始来源](https://www.youtube.com/watch?v=f43JCxhKLEg&list=WL&index=10&pp=iAQBsAgC)
- 来源平台：More or Less Podcast
- 发布时间：2026-04-10
- 整理状态：processed

## 三句话摘要

1. Vercel CEO 提到其文档流量中约 70% 已来自编码代理，说明开发者信息入口正在从“人类搜索”转向“机器读取”。
2. 这意味着文档、框架和 API 设计不仅要面向开发者，还要面向代理检索、调用和执行。
3. 对 OpenAI、Anthropic 等模型平台来说，这也是“代理成为新分发层”的强烈信号。

## 原始转录

00:00 70% of traffic to Vercel Docs is now coming from coding agents and only 30% of pages are coming from humans. >> Oh, wow. >> What was it before? The timeline is that

00:10 I think last year it was like 90% humans. Like like that's just how insanely fast it's changed. >> Well, your growth rate is also crazy, right? Like is this all because of the

00:21 agent swarm? >> Yeah, it's because it's that same intuition. Vercel's growth was capped by how many humans exist and how many times they deploy by submitting PRs. If now

00:30 coding agents start taking that job of writing the code and deploying it and testing it and submitting PRs, all of a sudden our infrastructure has like 100 times the demand. Seems like agents are

00:41 the new computer. >> [music] [music] [music] >> Welcome back to another episode

01:07 >> We're so back. >> Oh my god, you didn't even let me do the intro, Guillermo. >> [laughter] >> That's how we intro. Okay, that's how we

01:13 intro. More or Less it's the most casual tech podcast out there. Definitely not TBPN that just got bought for hundreds of millions of dollars, but we're rolling with it and we're going to get

01:22 to that news today. >> What's going to happen with that? >> Well, we're going to talk about that today, but first let me introduce who you are and where the lessons are cuz we

01:28 are less lessons this week. Just Sam and Jess. >> break. >> Well, I know, but you know, we have spring break, too, and we're still doing

01:35 the pod. Just saying. >> Well, we're on a different side of the planet. >> Lucky for us, our friend and Japanese gallivanter, who we were with last week,

01:44 Guillermo Rauch, CEO of Vercel, one of the hottest companies on the internet right now and in AI and everything, and our favorite Argentinian executive >> [laughter]

01:54 >> is here with us today. And and and we are excited to just shoot the with you because so much is happening in the world of AI yet again this week. And, you know, frankly, we

02:04 also just like to talk about slop cannons and Japanese culture and everything else. So, [laughter] how are you doing today, Guillermo? >> Excellent. It's good to be back in SF

02:13 from Japan. Now, I have to mention you This is your second time on our podcast. The first time you were on, I think your company was valued at like two to three billion. Would've been a good time for

02:22 anyone to invest. Now we're talking nine, 10, what something like that? >> Yeah, we 5x the guess. That's good. >> Great. Congratulations. So, next time you have me, we'll 5x again.

02:32 >> Yeah, we're only bringing you back if you raise another round. Done. >> [laughter] >> Okay, perfect. Okay, so I have to kick it off because there's a lot of news

02:39 that's happening. I'm going to try to do my best on the Jessica lesson front, but we have everything from like the Open Claw and Anthropic debacle. By the way, I'm just going to list some stuff and

02:46 you guys choose where to jump in. Open Claw and Anthropic, OpenAI and Anthropic, OpenAI on steroids with, you know, the Sam Altman New Yorker article, their white

02:56 paper that timely enough happened right alongside it, the industrial policy for the intelligence age. Um the CFO now not reporting to Sam Altman, and of course the acquisition of the tech podcast

03:07 TBPN. And then we also have more Anthropic news. They announced Project Glasswing and using Mythos, the new model for a bunch of cybersecurity safeguards. And then lastly, we also

03:18 have Meta. Meta's coming in hot with both new Spark, the first model launched under Alexander Wang, which they paid a hefty price for, but also, I think this is interesting, it didn't get that much

03:28 play yet, so I think it might be worth doubling into, Instagram Plus, their first subscription offering on Instagram. So, where should we start, guys? Where do we want to go today?

03:37 >> Well, there's there's so much. I don't even know where to go. I think Open Open Claw, let's start with Open Claw because it's been so top of mind for us, especially during the Japan trip, and we

03:46 we were at the Open Claw conference and meet up in Tokyo, so ClawdCon. >> Yeah, just to back up, I mean, last year last week we mentioned it on this pod, but we Dave and I and a bunch of others,

03:56 including Guillermo, were in Japan last week for kind of an annual trip we do with founders and exacts across the startup scene, and we hosted ClawdCon Tokyo with Peter, the Open Claw founder

04:07 himself. And days later, Anthropic announced that they are shutting off access for Claude Pro and Max users who are Open Claw users to use their product. Dave, what's going on? I mean,

04:19 that's what's going on. It's been a crazy few days. We've had some long conversations with Anthropic about this. They've got a immense amount of load. I mean, Guillermo can probably talk about

04:30 this, but agentic workloads are something that I think nobody was prepared to handle from an infrastructure perspective. And so, Anthropic, everyone who's dealing with

04:42 the traffic of our army of millions of claws is dealing with an immense sort of infrastructure challenge. And so, if anything, that's maybe the story we should talk about a

04:52 little bit because I think it's less reported on than the noise on the internet. You know, if you go on Twitter, there's a lot of people that are frustrated um that they can't use

05:02 their Claude Pro and Max subscriptions for Open Claw workloads, but I think there's a deeper infrastructure story here that's not being told, which, you know, Guillermo, you might

05:14 have some thoughts on. >> Yeah, I think agents have taken everybody by surprise. I've been sharing with people that I think even Anthropic has been surprised cuz I remember when

05:22 one of their researchers was in a podcast, Sholto, talking about how in order to get an an agent to be a very good product, you needed to have this chain of events, all of which needed to

05:33 have a high probability of success happening in a row, and agents sounded like something was far away. But then Claude code happened, which is a coding agent. And I think one of the key

05:43 features of a coding agent is that it does a lot of problem solving, just like a human engineer does. You'd never write code that's perfect in the first try, unless you're Dave Moran. But like

05:53 typically like you write some code, you get a syntax error, and then you have to call this tool, I forgot to install this package, and you do this, and you do that. Turns out that a coding agent was

06:04 a necessary DNA for full personal agents and general purpose agents to grow from. And that's been the I think I I'll you know, I'll credit Pete, uh Open Claw, with the discovery basically of like,

06:18 well, what if I just toss a coding agent into a container of sorts and I give it access to messaging platforms, and I give it a bunch of tools that are useful like a CLI that can read your email.

06:29 It's fundamentally a heart of coding agents. And so, I think there's been an emergence that no one expected. You know, I've I've spoken with a bunch of people about this at at every other lab,

06:39 and they themselves have been surprised that a coding agent was is the most promising path to AGI. They were like, oh yeah, it wasn't in our training set to do so much tool calling or get

06:49 getting so good at calling CLIs and shells and things like that. And so, that's been surprising. The other thing that's been surprising to us at Vercel is just By the way, it's intuitive in a

06:59 sense, but it's still surprising is that the amount of compute in the world necessary for responding to human intent is kind of predictable. You know, you're awake a certain number

07:10 of hours in a day, and then you prompt, and we need to do stuff based on that prompt. Agents can just do stuff in the background, and they can quote unquote, we talked about this in Japan with uh

07:20 crazy conference about artificial life, they can reproduce and call each other and fork themselves and claw as Pete has said, claw into other places. And so, the demands of compute that an agent

07:33 will put on the world is just so much greater. And maybe a a data point from Vercel that haven't shared broadly uh that is super interesting is we're uh actually an agent told me about an

07:44 insight in our data that is nearly 70% of traffic to Vercel Docs is now coming from coding agents. 70% and only 30% of pages are coming from humans. >> Oh, wow.

07:57 >> What's the time What's the timeline on that that that start difference? Like what was it before? >> The timeline is that I think last year it was like 90% humans. I can't remember

08:05 that. But like >> Like a literally a year ago, 12 months ago. >> Yeah, like that's just how insanely fast it's changed.

08:12 >> Well, and I saw like your your growth rate is also crazy, right? Like is this all because of the agent swarm? Yeah, it's because it's that same intuition, right? That like humans

08:24 Vercel's growth was capped by how many humans exist and how many times they deploy by submitting PRs. If now coding agents start taking that job of writing the code and deploying it and testing it

08:35 and submitting PRs, you know, GitHub also published their data and it's it's insane. Now all of a sudden our infrastructure has like 100 times the the demand. Our sign-ups are growing by

08:45 50% month over month. My high school friend who's never written a line of code in their life came to our office yesterday and he's like, by the way, I I've been following you obviously and

08:53 what you've been doing for years, and in Argentina there's always news and whatever, but I never understood what Vercel was, but now Claude introduced me to Vercel. And so, there's this new like

09:03 agentic driven interaction, and I fully expect agents to be signing up for services directly, zero human intervention soon, making payments on behalf of people

09:14 imminently, you know, getting credit cards and budgets and solving entire problems for for people where the service provider becomes an a vendor of the agent, not a vendor of the human.

09:26 >> Yeah. Yeah, I mean, it seems like that future is already here. Like it seems like that future's already here. I've been trying to think through what does the business model look like? Is it as

09:35 simple as the application of the entire SaaS business model set to agents, or is there something more interesting here? Like it's really kind of hard to tell where the business is going to emerge.

09:47 I'm like playing the Sam role all of a sudden on the pod. Yeah, okay. It all goes to zero, Dave. None of this is all electricity, Dave. None of this matters. It's just AI.

09:56 >> Actually, it's closer to It's probably closer to like it's all electricity but on steroids in the sense that one of the things that Vercel had embarked on that was very timely for this AI revolution

10:06 is the switch to consumption-based business model, right? I was actually sharing the story to a group of founders today that I think people underestimate just how complex the problem of like

10:15 building per token or building per CPU cycle is at the scale of providers like us and just how many how many teams we had to like basically devote to the to the problem of just counting uh in

10:28 billing tokens. And now we're trying to like basically like share that back with the world and and provide the infrastructure so that you can build agents that can charge by token and and

10:38 participate in this emergent economy, but the barrier to entry is the fact that agents will basically will be very much pay-per-use. The SaaS business model definitely gets disrupted because

10:48 it was predicated on selling seats. Yeah, I mean, I was thinking about this while we were in Japan and then doing some research on it the last few days, but the ARR business model seems to be

10:59 completely out the window, right? Like people Like I'm still seeing this in pitches from startups every week uh every day. I took one this morning. ARR is no longer a viable metric when the

11:11 actual business model is pay per token. And I've been saying this on the pod for a really long time that the business model of AI is not ARR. It's actually computer, right? Like it's more like

11:22 Apple's business model where you're selling people a computer that they can use for some period of time or they're sort of buying their access to computer and it's not this like recurring thing

11:34 necessarily. And when you look at especially this move that um Anthropic just made, they're basically saying like, "Hey, the ARR business doesn't work for us because people are scaling

11:46 up their token use dramatically and that's putting an incredible strain on this like ARR-based subscription model that we have. Like we just need you to pay for your tokens. Like whatever level

11:57 of token you want to use, like go for it, but you need to pay for pay for your tokens." >> By the way, one prediction that I that I'll make is that it's going to continue

12:06 to get more and more complicated for them to sustain the subscription thing because it's almost an impossible problem. We we confronted this at Vercel early on because what customers really

12:15 want is predictability. And and they want to know exactly how much they're paying. But I don't know exactly how much I'm paying AWS in and the world that we're going in is so incredibly

12:26 dynamic. So I would try to explain to e-commerce companies, "Look, on Black Friday, you're going to use 10 times as much Vercel. So I have to meter you on each unit of consumption of what you're

12:38 producing and and and and consuming on because it's going to be highly fluctuating." And I think this is the problem with selling you $200 Claude Code Max is that they're trying to say

12:48 like, "Look, most people hopefully will not use it." But the thing here in the unit of intelligence is so valuable that why wouldn't you use it? Why wouldn't you use whatever high ceiling there is,

12:59 which may be like $5,000 worth of inference or whatever? You're going to want to use the 5,000. And that's what we realized is that it becomes this insane game of cat and mouse because

13:09 once people realize the value that is behind the illusion of predictability, they will try to maximize its utilization. Well, and and that goes back to the electricity point, right?

13:19 You're just buying what you're utilizing, right? And I'm a little confused though. So So just today Claude also then announced it has managed agents. So a new way for businesses to

13:29 build and deploy AI agents, build harnesses around them, etc. So they're blocking open Claude's Pro and Max subscriptions, but they're launching managed agents and I didn't see the

13:41 business model behind this. I don't know if you either of you did. >> Well, it's actually in my I haven't looked into it too deeply yet, but my it seems like a continuation of the same

13:49 strategy of can we verticalize as much as possible? >> Yeah, yeah, by subsidizing it, right? Like by doing these like subscription predictable things, you're basically

13:59 saying like you're willing to subsidize using your investors' capital like getting certain verticals on board, right? And like ultimately in the end Guillermo's right. Like you have to

14:09 meter this properly. Like you have to meter this at the price of supply and it's like a supply and demand pricing exercise, right? Like if you have enormous demand like on whatever day for

14:21 a certain type of commute, you have to price it properly. And the only way to make a subscription work is to subsidize the delta. Um that's it. >> There And there's two ways that they can

14:31 subsidize. One is investor money and the other one is growing a formidable enterprise business such that you focus on the subscription for individuals and engineers that are working on their own

14:42 and whatnot. But there's also another third one, which is they train on the the subsidy, right? So like if if you agree to getting cheaper or or more high rate limits or whatever, they you become

14:54 the product, you become the data. Funny enough, I was just joking when I was tweeting before we kicked off. We announced today on Vercel AI Gateway zero data retention guarantees so that

15:03 you can turn it on and say, "Vercel has a negotiated contract with all of the AI labs on zero data retention. We will not allow a single token through these pipes that can put you at risk of being

15:15 trained on." Because that's going to be the other uh encroachment is that, "Yeah, here's a bunch of AI playing the casino money, but I'll learn from everything you do. I'll I'll upload your

15:25 code base into my training data set, right?" And on managed agents, it goes back to like the way that you justify a subsidy is can you lock the customer in to your ecosystem? Uh for example, I

15:36 don't know if they've adapted yet, but Anthropic for a long time was not playing ball with agents.md. You could only call their uh instructions Claude.md. To their credit, they I

15:46 actually pioneered a number of open spec solutions. I actually think they've been a really good actor on the open ecosystem side. There's a case to be made that their business incentive is to

15:56 verticalize. Only do things in the Claude ecosystem. Store your data there. Store your file attachments, artifacts, PDFs. Store your vector DB there. Run your sandbox compute there. And Vercel's

16:10 answer is the exact opposite. It's like, "No, no, no, no, like get the tokens there. Reserve the optionality of using Codex if you want. And here's all the services to to build a managed agent

16:21 that doesn't lock you into a particular vertical model app stack." Right, which is what most people want. And I think that's why open Claude, etc. has been so enormously popular. Uh people can have

16:32 their own agent, they can switch models, they can they can keep all their data personal, local, etc. >> There's too many people that want their own AI, right? Like they want literally

16:41 like an open model living in their house. And that's [laughter] how they want to use open Claude. And so that's why this I think this is the solution that's always going to win. Guillermo,

16:49 how do you think about the transition in your business between these two new worlds? You know, like you kind of pioneered this sort of edge, you know, edge function sort of TypeScript, you

17:00 know, world where you had a totally different server architecture that you've really pioneered and that was like extremely successful in this sort of human-driven internet. The it the

17:11 sort of I don't know what we're going to call it, the agentic internet I get it. I like the agentic internet. kind of requires a different type, you know, you've got this new Vercel sandboxes,

17:21 you know, it requires kind of a different kind of thinking. Like you're right, people do want They want a box, right? And so I'm hearing a lot of people use Digital Ocean or, you know,

17:31 some people that want to go through the pain or using AWS and their crazy interface. But like how are you thinking about this transition in terms of the product set that you need to offer? Like

17:41 does it change the way you have to think about your strategy? Yes. So the agentic internet requires agentic infrastructure. So that's the that's the focus of the company right now. Build

17:51 being the AWS of agentic infrastructure. Do you have to change the way you think about I mean, I guess it it really does change a lot of things for you. Or is it Is this sort of easy stuff for you guys

18:03 to to stand up, you know, entirely new architectures and things like this? >> I was going to say there is an important but, which is that the existing business was also at the right time and the right

18:15 place because when you deploy all these apps and and they we when we were in Japan the previous trip, we were talking about the dream of personal software. And then we were joking it only took a

18:25 year and now we have real personal software. It's kind of nuts. I remember actually when I was in the plane to Okinawa, I was like sent tweets. And I felt like every good banger, I felt a

18:36 little bit of like, "Hmm, I don't know if this is just me being high on my own supply." And to put this in context, that tweet was what? Less than 18 months ago. And remind people what the tweet

18:46 was. Yeah, it was this idea that generating software it was in competition now with Googling for software. But now generating software is not just in competition, it's going to

18:57 win. It means that everyone can produce their own software for personal use or for enterprise use. Because why would you go through the hard work of procuring a new vendor if you've already

19:09 procured Vercel, you plug it into Codex or Claude Code, and now you generated the software that you thought you were going to procure? Like this is literally happening as we speak. What makes Vercel

19:19 really good for this hosting solution for generative software? One of the things that we bet on was serverless. Serverless has this property of scale to zero. A lot of software will be so

19:31 spontaneously created and used that it may just get intense use for 5 minutes, for 2 weeks, maybe a year, maybe it's just for me, maybe it's for a medium-size group, maybe it takes off on

19:43 X. Like literally every day there is a new generative personal app that takes over the world on X. There's one called the Monitor, which is Vibe Coded Palantir. It literally became one of the

19:54 top 100 host names on Vercel for a week because everyone in the world was talking about it. And so >> it died? What happened? Like it just goes away?

20:03 >> It actually surprisingly is still very high. Oh, okay. But some of these probably like how are blips in time. They rise, they fall. This speaks to the durability of some of the Vibe Coded

20:12 software. Another example is J Mail. J Mail was a group of of guys saying like, "Oh, like what if we produce a better UI to the Epstein files?" Oh, yeah. I love that. Lo and behold, you have a massive

20:25 It's It's become the Wikipedia of that whole case that everyone is talking about and whatever. And so we What do we call our compute infrastructure? It's fluid compute. Fluid implies again, it

20:37 has the fluidity that CPU cycles might go down to zero or CPU cycles might go so high that you're running something that's bigger than New York Times. Maybe for a week, maybe for a year, who knows.

20:47 And so we we made the right investments to be very well positioned for this era. But now the agentic era also requires innovations. The sandbox is the is the most prescient one, which is that very

21:01 fascinating thing about agents is the more power an agent has, the more intelligently it performs. And so if an agent has an entire computer, like a Mac Mini, it you feel like you have AGI in

21:14 your hands. Mhm. If your agent only And this is the problem that people I think run into is if your agent only has access to your rack database and one tool that one

21:24 engineer wrote, it's like you're wasting this incredible IQ capacity that you just purchased. >> Yeah. And that was again Pete's brilliance in that he was like, "No, no,

21:33 no, no. Give the agent everything it needs." Yeah. And so I think what I want what I'm helping enterprises do now is how can we get them to achieve that power but not exfiltrate all their

21:45 precious data and IP and uh and the [clears throat] keys to their kingdom. And so that's the fine balance that And again, requires innovations like we invented a new kind of firewall for

21:54 Vercel sandbox that literally did not exist in the world and things like that. So what I think is so interesting about you and Vercel is you're kind of like Switzerland amongst all of these

22:03 frontier labs. And there's there's so much happening almost every day. Like can you say like are there some of these companies you're more bullish on, less bullish on? Do you think that You can

22:14 talk in the macro. Like we're in the AI wars, you know. I feel like there's like a lot of opposition research happening. This week alone, you know, we had all the Sam Altman stuff coming out. There's

22:24 like Dario watching Glasswing. Elon is like suing Sam. Is this Is this like all going to play itself out or like what do you think is the long game here?

22:35 >> I'm very bullish on whoever focuses on coding because as I mentioned, I think the foundation of a successful agent for personal use or enterprise use is the ability to code. In fact, one of the

22:47 things that we learned with the agent that helps us run Vercel internally is that you still need to give feedback to the agent. So Dave and I were talking about soul.md

22:57 Like we're talking about a soul.md hat. >> No, no, you can't tell everybody about this. [laughter] We're going to sell these. It's coming. It's merch. We're making soul.md hats. But now you know, I

23:07 did this feature this Well, dreams, Dave. You have to do dreams.md. I worked on this feature on Open Claw this week called dreams.md, which is pretty fun. But Uh what's another amazing emergence

23:18 from agents and from Open Claw? And by the way, this is also the sharp edges, by the way. I literally saw that tweet from Gary Tan today that said, "I told my agent to improve itself. I literally

23:28 knocked itself offline and I had to SSH into the machine and reboot it." >> Yeah, it does that a lot. >> And we're in the Apple One phase of uh personal agents.

23:38 But this is a good problem to have because when uh I really think that, you know, Open Claw is like Linux. And I agree with Jensen Huang

23:47 that when Linus Torvalds introduced introduced Linux on the mailing list, he said, "I have this toy kernel, totally not for production use. Here you guys go." And that got an entire ecosystem of

23:59 early adopters excited about it. And then he went from toy to literally now every web server on the planet runs on Linux. I think Open Claw has similar potential because it's it's it's used by

24:11 early adopters, advocates, people that know that when they it gets itself into a bad state, you have to reboot it and all these things. But going back to my original point, the ability for an agent

24:21 to mutate itself and improve itself over time is extremely important. It doesn't know everything about how you like to work. It doesn't know everything about how to work with your data. It doesn't

24:30 know everything how to work with your code base. But it can very quickly learn, especially if it knows where to put the data about how to when you give it feedback on uh

24:42 Does it edit, you know, dreams.md? Does it edit skills? Does it edit the system Whatever it needs to do. And so I guess the next how to enable that. Because if we let it edit everything about itself,

24:53 it can edit itself out of existence. It's like emo. Like I'm done. I'm done with this world. Or it can just get into itself into a bad state, right? That was part of, you know, the reason we worked

25:03 on the dreaming feature this week. It's a old Peter one of my favorite ideas that Peter talked about early on when I was first talking to him was this idea of what if the agents can dream. You

25:14 know, he I think one of the brilliant things about Open Claw is that it beyond the technical things that we're talking about is that there are these like very basic files that

25:26 have very interesting names. You know, he took the idea of soul.md, which was a idea written by somebody else, but Pete was kind of I think the first to implement it in this sort of very

25:36 beautiful root level way where this agent has a soul. You should define its soul. You should figure out how you want it to be, how you want it to show up, what it's what what it's essence is, and

25:49 it should be different for you. Like your your agent and my agent should be, you know, very very different. And then he also added this memory.md flat file. Just like here's the things the agent

25:59 has remembered from all of its interactions with us. And the thing that we implemented this week was this idea that as time goes on, your agent, you know, you talk to your agent a lot, you

26:10 have like all these long session files, there's many many many many memory files, there's a daily log in the Open Claw agent, and all of this stuff has things to learn from. Like the agent

26:22 should be able to improve itself, right? And there's a lot of really complex technical ideas out there about how agents can have these really complex, interesting technical solutions around

26:33 self-improvement and blah blah blah blah blah. And our thought my thought here was just let's make this very simple for people and just give it a dream.md file, give it a very basic system that churns

26:44 through all of these different files that the agent generates every day. And ranks things from them that should be promoted into this sort of dreams file and then makes it human readable in a

26:56 way where when the human wakes up every day, you can actually just read this dream journal that kind of helps you think about where the agent is evolving and where it's going. And it does this

27:07 in a very basic and smart way so that it is, quote unquote, self-improving, but it does it in this kind of lightweight way that we think of and we understand from a human perspective. And so that's

27:18 also I guess one of my great interests in this, which is how do we create a theory of mind for agents that can be also trans transportable across intelligence, right? Cuz like one of the

27:30 other things that we're seeing a lot of is that, you know, if Anthropic decides that they need to shift their business model or whatever, whatever intelligence you're using underneath your agent, you

27:40 still want its soul and its memories and its understanding of you to come with you as these things change that are the underlying compute. And so that was kind of a big thing that we worked on for

27:51 Open Claw this week that I'm proud of and um it seems to be something the whole industry is has been interested in. I This essay that I wrote went more viral than anything that I've written

28:01 recently. And so I hope that people are inspired to think in this way. There There's sort of a a seam between humanity and agents that I think is important as we're as we're working

28:12 through this. >> One of the things that I've been trying to figure out is how do I take that concept and apply it to the agent our internal company agent because when

28:20 people work at Vercel, I was actually literally just talking to my video team and they were saying, "Oh, we're using Riverside." I asked our agent, "How do we use Riverside? How does Riverside use

28:31 Vercel? How do How can they have better context going into a conversation with the Riverside team?" And it's amazing because like in the past, questions about customers would happen through

28:43 maybe there's a Salesforce account open and the data team did data integration. And if it's a very complex question, I have to ask a data analyst. All of that is going through an agent

28:55 now. So what we're trying to figure out now is like what is the I'll use the term enterprise ready self-improvement loop for this agent. On one hand, there is different domain

29:06 experts for the different skills that the agent has. For example, the finance team is more equipped Funnily enough, I'll connect it to your earlier discussion around ARR. Forecasting

29:16 widely dynamic revenue for a business like Vercel requires a ton of work and expertise. And and there's certain people in the finance team that can do that. And they're the

29:25 ones that are more most equipped to review and give feedback to the agent on the skill set around MRR or ANR, annualized revenue, or forecast, or definitions because one of the things

29:39 about a data analyst agent is that it should correct you in your terminology. If if Brit comes into Vercel and says, "Tell me how many weekly active users we have." The way Wait, wait, wait, wait,

29:50 wait, wait. At Vercel, we have weekly active developers and weekly active contributors. Who are you talking about? You also want a nation that pushes back. Right? And so, all of that is rooted in

30:02 expertise that is first has to continue to learn over time, but also has dedicated people that are experts in that domain. So, that's one side of it. The other one is that there is a

30:11 personal relationship between me and the agents that is more like the episodic memory that you're talking about. Anytime I interface with this agent, I actually

30:19 give you a very concrete example. I have a lot of people that prefer to talk to the agent in their natural language, like in their in their mother tongue, because they can talk to this agent

30:26 privately. So, they speak to it in, I don't know, Argentinian Spanish. And by the way, do you mean by voice or by typing? >> This is all Right now, it's mostly

30:34 through Slack and a web interface that we built for it. Yeah. But yeah, it should also be through voice. And when when I, Rauch G, interface with the agent, it should pick up, in addition to

30:44 all the stuff that we just talked about, it should learn about the its relationship with me. And obviously, there's context that's relevant because it knows about the conversations that

30:51 we've had. Maybe it knows about frequent mistakes that I make. Like, I keep talking about weekly active users, and it's like, "Ah, yeah, I know what he means. We already went through this."

31:02 >> [laughter] >> Right? And so, there's levels of personalization of the memories and skills that deal with who's the user interface. This is

31:10 again for multi-user agents. You guys are mostly focused on like the personal one-to-one. Guillermo, have you had just I think Vercel is probably one of the more advanced companies, I'm guessing,

31:20 that is really using agentic software internally. Your finance team is thinking in these new ways. Your video team's thinking in these new ways. Like, are you training people to do this? Are

31:31 you only hiring people that think this way? Like, what is the modern founder or CEO's playbook for how to cultivate a company that does things this way? I think because we build a lot of the AI

31:43 stuff, it's been a self-fulfilling prophecy of inspiring people to think that way. I never explicitly told the video team to write code their own tools to make themselves more productive, but

31:53 they were literally showing me a couple weeks ago their video generation tool that meets their exact needs and produces high-quality output. And I tweeted about it, and it actually

32:03 surprised a lot of people. I tweeted about the design team, including people that never wrote a line of code in their lives, have created design tools, automated their job, right? Like, we

32:14 have an agent that produces uh social media cards. And what's really cool is that this actually is reassuring for the future of human jobs, because the designer job at Vercel has become

32:25 the steward of the agent. Of course, I don't want a tool that it spits out any wildly off-brand social card with six fingers or bad typography or whatever. But I also don't want the other extreme

32:37 that is that anytime that I need to tweet something out, the team is bottlenecked because the creative has not produced the asset yet. And they have a long to-do list. And so,

32:48 basically, everyone at Vercel is now kind of like the steward of the agent. And that's our new job expectation, and now it's become part of our job screening, which actually forces the

32:58 hiring manager to think about, "I'm hiring a roboticist. I'm not hiring a Interesting. uh doer of the job." And so, they set up the hiring challenge, "Walk me through how you would create

33:12 the agent that solves the job that traditionally someone in your position would do." And so, now it's become part of our hiring pipeline. I was also looking I I don't remember if it was

33:22 also Garry Tan or somebody else on Twitter this week that was talking about how apprenticeships are going to be the new normal rather than traditional Oh, 100%. hiring friends, because you just

33:31 have to like see how In what context? Like, robot apprenticeship? >> Oh, no, just like you need to see how these people work and like because they're going to have fake their resume

33:39 or like AI slop everything in the interview. And like, you just need to get some real like reps in with people to understand if they're going to be a good fit for your company.

33:51 >> a bunch of different platforms that we can use for AI native screening, because there's two sides to the job interview. By the way, I actually love your theory of minds,

34:00 Dave. I'm also a hobby part-time philosopher. Nice to meet you. >> [laughter] >> And my theory of mind is, you know, intelligence is three parts. There's a

34:10 raw EQ part that we all have a foundation model of sorts. There's the knowledge, which is that I hire you because you've been a designer for a megazillion years.

34:21 But then there's skills, which is your ability to obtain new knowledge over time and your your ability to do to do tasks to completion, to ship things. And so, you have to have

34:31 all three. And so, when when I'm hiring, I'm trying to assess all three. And I love the AI skill set. I love the agentic skill set. If you've shown that you can use ChatGPT, V0, Claude Code

34:42 really well, I'm happy for you. And I'm let you finish. But I also want to see what raw materials I'm working with. And for that, we actually do a zero AI interview. And and I basically need a

34:53 platform for the zero AI interview with clue detection. And then a and and North Korean speak ill of Kim Jong-il detection. And then I need the

35:05 [laughter] opposite. I need the can you actually agent max part of the interview. And that's the secret, is that you need both.

35:13 >> And G, I know that you also, outside of running Vercel, are an investor yourself. You do a ton of angel investing in all kinds of things. What are you looking for these days? You

35:24 know, again, if if our friend Sam was on the pod, he would tell you, you know, software is uninvestable. Uh there's nothing investable on the internet right now. It's, you know, other than

35:33 creators. Yeah, Sam tells you in Riverside that through this streaming platform that software is uninvestable. I think it's about anticipating these problems that look so niche and so

35:43 Silicon Valley, and are going to be everyone's problems in in a few years. I've been particularly interested in everything around risk mitigation for agents, obviously, for obvious reasons.

35:53 I mean, we we just talked about one of the topics on the laundry list with Mythos. And it's a very real danger that agents can just go off the rails. Yeah. I One of the tweets that I got out

36:05 recently that also shocked people was I had this escalation from a customer, by the way, using Open Claw. By the way, my new customer is someone that barely knows what the cloud is, which is funny

36:16 because [clears throat] to to Dave's point about AWS is hard to figure out or whatever, that was kind of already the case. But it was a silly customer that knew enough front-end engineering that

36:25 they knew they needed infrastructure. Their new job is to figure out what the agents are going to need that even the humans don't know that they're going to need. Yeah, there's a super that agents

36:36 need to deploy, like your son who you were telling me >> [laughter] >> they Claude Codes and deploys to Vercel. And

36:43 I'm hearing this story every day, and like this customer that came to me was like, "I'm filing a ticket with you guys, but I don't even know who you guys are, by the way. Nice to meet you. My

36:53 agent got me here." By the way, one of the most inspiring things, you know, and I know, you know, Sam hosted a Well, we were in Japan, they hosted a creator summit, and I got some of the reports

37:03 out of it. And they brought together, you know, all of the creators in the Slow Venture creator fund in San Francisco. I think they had like 50 creators, and

37:13 they taught them like a very basic stack, right? It was like, "Here's what Claude Code is. Here's what Digital Ocean, Vercel are. Like, here's what, you know, here's how to think about what

37:24 you can do with this." And it was amazing the stuff that people are creating. And these are all like, you know, some of them are sophisticated creators, but some of them are fishermen

37:33 or pro skiers or, you know, whatever. Their expertise is not technology. Their expertise is their community, right? And or their customer. And I'm hearing this over and over

37:43 again, right? >> talked to a neurosurgeon yesterday. You know how everyone wants to crack the problem like radiology with AI. And you know why we haven't cracked it yet?

37:53 Because no one has the credibility to solve that problem. I don't think you can you know, random engineer off the street and say like, I mean, sufficiently

38:02 motivated ones, like the Elon types, will. But it was amazing to hear. I was at Y Combinator this lady who's a trained neurosurgeon, has worked with radiologists during her entire career,

38:12 and she's taking a stab at the problem, and she's using these tools that a year ago, to your point, she didn't know existed. She'd written nary a line of code in her life. Of

38:23 course, if you've been able to complete a neurosurgery degree, you have the raw Going back to my raw material, what are you What are we working with here? She clearly has the raw material to like

38:32 solve any problem in her life. Uh and so, I think there's going to be a lot of power to the people with the domain expertise. And cuz her problem that she's telling me about is figuring

38:43 out the the integration into existing systems. The the AI part is the easy part. We can all upload a scan to NanoBanana, and NanoBanana can even like draw a rectangle around the tumor or

38:55 whatever, right? But the problem is the integration in in the disparate systems and the regulations and the credibility and the authority. And so, I'm still super bullish on on on those kinds of

39:06 people solving massive problems for humanity. I just think this is a beautiful the most beautiful thing going on right now. And this is something that P and I talk about in the context of the

39:16 Open Claw Foundation, you know, all of us talked about this a lot on the trip last week. But this idea that bringing people closer to AI and showing people that they can just talk to these things.

39:29 And if you're that radiologist or you're the, you know, the person with expertise in your community or your knowledge area, to your point, Guillermo, you can just talk to them, and it will it will

39:40 help you figure it out, way more powerfully than I think everybody realizes. And that's actually the beautiful moment we're in globally, but most people just need help you know, A

39:51 trying it and then to your point, the Versels and the people that have specialized in the infrastructure over the years have to kind of accept this new reality that like you're now serving

40:01 the agents that are serving the humans because the humans that are asking the agents for things know something. >> It's a new kind of customer. >> Yeah. It's

40:09 creates a huge amount of empathy, too. And it's a new kind of design challenge, by the way. Cuz at some point they'll go to your platform and they'll have questions and they'll want to review

40:18 things and their their mental model was how the agent was interacting with them. So they need to be able to translate and and and regain that context when they interact with you directly. And they're

40:29 not going to be technical, you know, they're not going to They may not even They may not even be interested in like It's a new kind of technical. >> not or whatever. Yeah, it's like a new

40:37 technical. >> technical. It's a new The new technical is that you use AI tools so well that would be People used to take pride in being technical on is now an

40:46 implementation detail that is less important. >> Right. Everyone's an orchestrator. >> When I worked at Apple, you know, there was I I loved it. There were these guys

40:54 that they literally had wizard beards and they were the guys who knew assembly. Like they were the guys that could still speak assembly and they had their whole own wing at Infinite Loop

41:05 and they were really interesting guys and they had been doing this for a long time, but it's it's not like everybody everybody that worked at Apple understands what the compiler was

41:13 turning into assembly, right? Like most of the people at Apple when I was there were working in C, right? And sort of this objective version of C that was really, really useful for building

41:24 things on top of the compiler, right? And so it We're kind of like just moving up the compiler stack again and that's like kind of cool. And there's always going to be the guys that know the next

41:34 level down, right? But to your point, like it There's a new technical now and um that That's really interesting. So I want to bring us, unfortunately, to a close cuz some of us have have other

41:45 things >> gone on for 5 hours. >> We We could have gone on for 5 hours. [laughter] I wish we could. That would be We'll do Let's do the 5-hour edition.

41:52 >> get to the laundry We got to some of the laundry >> that. >> But you know, yeah, let's do a 5-hour or do a long form.

41:58 >> long form. >> A pod-a-thon. >> Yeah, if Joe Rogan can do it, we can do it. I want to I want to end by asking you this. Yes.

42:05 >> I will say I've got I've had a few people in our network, you know, over the years we've had these eras where we do these jam sessions. Mhm. Gary V and

42:16 Ashton and a lot of us we used to host these jam sessions at South by Southwest and for years this was a thing and then it kind of died down when the when the sort of 2010s turned into SaaS things.

42:28 Let's do a jam sesh podcast with like eight people. Yeah, Gary Gary V called me yesterday and said, "Dave, we need to do a multi-day jam session in San Francisco."

42:38 >> it. Okay, and we're recording it. Amazing. Gary V, we're coming for you. Like let's do it. You last came on the pod a little over a year ago. The world was different then than it is now. What

42:47 do you predict happens a year from now and the next time you come back on the pod? Where are we at? The next short pod. To me, it seems like agents are the new computer. And you know, the biggest

43:00 problem right now is that the friction that exists that we've all wired our brains to work with a different kind of computer. And uh my prediction is going to be that we're going to continue

43:10 hearing of this case is where someone that came in fresh with very little context on how things worked in the past. Maybe even like a baby. Like imagine a baby like

43:20 If a baby could actually articulate thoughts, that would be the ideal environment, right? Or the ideal user of of this new technology because like funny enough today uh we gave an

43:31 offer or we finalized an uh the offer got signed by a mother. Why? Because we hired someone that's 17 years old that we went through the trouble of like doing it lawfully,

43:43 obviously, and having his parents approve because this person is so overwhelmingly competent. I call this the advent of the super geniuses. Our children will be born into a world of

43:55 endless possibility. And one of the consequences that we're going to hear stories that are just in insane, unbelievable. Like uh someone creating a massive company. I mean, it's a tired

44:04 trope by now because it kind of already happened and it's debatable, whatever, but like a single person creating a unicorn. Single person having a scientific breakthrough.

44:13 Startups stay like 10-person companies reaching insane levels of revenue. The The continue One thing I'll I also predict is that the stress on infrastructure is going to be

44:24 bewildering. Who gets allocation of hardware is going to become a big battle. Again, it's not just GPUs, by the way, it's also CPUs. Who gets access to raw metal to satisfy the endless

44:35 thirst and appetite from these agents to have cuz we're seeing this with sandboxes. We're seeing this with functions. like there's just endless demand for infra. And so I think we are

44:44 underestimating the the stress that this is going to put on the system. We're seeing a lot of outages. We're seeing a lot of cybersecurity attacks. Those sadly will continue. As far as, you

44:53 know, the global macro and and geopolitical landscape, the the attacks that have happened recently, our region in Dubai got taken offline because of war. You know, two of our availability

45:04 zones hosted by AWS were droned. So we had to reroute an entire region we we'd never done outside of one exceptional case in 10 years, which is US East 1 had a really, really, really bad outage and

45:17 we had to reroute traffic to US East 2, Ohio, which so much traffic we sent that it took Ohio offline. And so we had to reroute Dubai and then it happened again in Bahrain. And so hopefully I'm I'm I'm

45:31 I'm always a rooter rooter or optimist for peace, but I think we're going to continue to see how our our cloud infrastructure becomes the target because the most valuable thing will be

45:40 the computers being online and doing number crunching and processing and disseminating intelligence. So I mean, bag of predictions there, but uh it's

45:48 going to be a fun year. Sounds like a lot of optimism and a lot to be a little nervous about, but we're here for it. We'll hope We'll maybe we'll have you back sooner than that so that we can get

45:56 some status updates. We're going to do this long pod. >> Yeah. Guillermo, thank you so much for being here today. >> And for everyone that's listening or

46:03 watching, please make sure to follow. Follow Where Where can they follow you? >> Follow, like, and subscribe. >> Okay, there you go. Well, no, what No, where can they follow you? Give them

46:11 your Give them your follow. >> Oh, @rauchg on X, the X platform, the everything app. That's [laughter] the That's the main one. All right, that's r a u c h g, by the way. And you

46:22 can follow, like, and subscribe the More or Less pod wherever you are. We've gotten some great traction, by the way, on YouTube lately, so go check us out there if you missed anything. And

46:30 hopefully the Lessons will be back next week and so we will all see you back here for another episode of More or Less very soon. Bye-bye, guys. >> Thanks, everyone.

46:39 If you enjoyed [music] this show, please leave us a virtual high five by rating it and reviewing it on Apple Podcast, Spotify, YouTube, or wherever you get your podcast.

46:50 Find more information about each episode in the show notes and follow us on social media by searching for @moreorless, @davemorin,

47:00 @lesson, @jaylesson, and as for me, I'm @brit. >> [music] >> See you guys next time.
