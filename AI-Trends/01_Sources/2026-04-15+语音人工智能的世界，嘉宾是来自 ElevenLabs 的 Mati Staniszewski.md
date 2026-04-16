---
type: "source"
title: "语音人工智能的世界，嘉宾是来自 ElevenLabs 的 Mati Staniszewski"
date: "2026-04-14"
source_name: "Stripe"
source_url: "https://www.youtube.com/watch?v=zA1zdqIYER4&list=WL&index=4&t=11s&pp=iAQBsAgC"
company: ["ElevenLabs"]
theme: ["语音入口", "AI音频", "AI代理"]
signal_type: "interview"
importance: "high"
confidence: "high"
time_horizon: "mid_term"
status: "processed"
summary: "这期 Stripe 访谈介绍了 ElevenLabs 如何把高拟真语音扩展到情感表达、工作流代理和更广泛的音频场景。语音不再只是输出模态，而正在变成人机交互和代理执行的重要入口，这也是 ElevenLabs 被高估值重估的核心原因之一。对趋势跟踪来说，这是一条非常典型的“语音入口重新成为平台机会”的来源。"
my_take: "语音入口一旦和代理真正结合，竞争可能就不只是模型音色，而是整条交互链路。"
related_notes: ["[[ElevenLabs]]", "[[语音入口]]", "[[AI音频]]", "[[AI代理]]"]
tags: ["source", "ElevenLabs", "语音入口", "AI音频", "AI代理"]
---

# 语音人工智能的世界，嘉宾是来自 ElevenLabs 的 Mati Staniszewski

## 来源信息

- 原始链接：[查看原始来源](https://www.youtube.com/watch?v=zA1zdqIYER4&list=WL&index=4&t=11s&pp=iAQBsAgC)
- 来源平台：Stripe
- 发布时间：2026-04-14
- 整理状态：processed

## 三句话摘要

1. 这期 Stripe 访谈介绍了 ElevenLabs 如何把高拟真语音扩展到情感表达、工作流代理和更广泛的音频场景。
2. 语音不再只是输出模态，而正在变成人机交互和代理执行的重要入口，这也是 ElevenLabs 被高估值重估的核心原因之一。
3. 对趋势跟踪来说，这是一条非常典型的“语音入口重新成为平台机会”的来源。

## 原始转录

00:01 Mati Staniszewski cofounded ElevenLabs in 2022, and has since scaled it to the $11 billion leader in AI audio. He's credited it with capturing the humanness of speech through realistic emotional inflection, and they're now expanding into everything from agentic workflows to music.

00:16 Cheers. Thanks for having me. Maybe a good place to start is, describe to me how… I know how an LLM works at a high level. Describe to me how an audio model works.

00:30 If we were Karpathy-style looking to build a toy one from scratch, how does it work? In the early days, you try to replicate it exactly like you would replicate it with the human body. You would completely try to reproduce a machine, analogue machine, that would create a vocal tract effectively.

00:47 Then that progressed into trying to create effectively a digital signal for speech. Bell Labs was one of the first to try to create a structured set of signals that would represent the speech. That is a first precursor to what we would do today. Then you would try to stitch in phonemes, effectively different sounds of how we

01:07 would speak as humans, and then try to concatenate them together. It's another important part in that equation where you would... Based on the most probabilistic approach of the next word, you would effectively try to bring the phonemes from your library of phonemes and bring them together.

01:22 Then down to the modern history where now we effectively do similar neural nets in other domains. You predict the next sound based on, of course, the context of the previous sounds if it's a streaming speech. If it's, let's say, a context of audio, you will use combination of predicting

01:42 of the phonemes, but you also use the contextual text element of that work. Here, credit to my co-founder, Piotr, who effectively came with that new idea of how you can now create voice models which are both reliable, high quality, quick, where you would bring a lot of the ideas from transformer models, from diffusion models, into the speech space.

02:01 That prediction of the next token in the phoneme space wasn't something that was possible. We spoke briefly about this, of how you can operate on the text, on the waveform space. There's also Mel spectrogram space.

02:13 Usually, you do text, Mel spectrogram, waveform. Sorry, what's the spectrogram space? It's like a visual representation of how the speech sounds across pitch, across energy, and then you transform that into a waveform. When WaveNet came along and Tacotron models, they would effectively use text

02:30 to Mel spectrogram, so that visual representation, and then how you decode and encode that into the waveform to bring it across. Piotr figured out how to abstract some of those steps and decode and encode them a lot better. That predicting of the next phoneme was one of the big piece.

02:46 Second big piece was, how do you bring that context into the equation? What I mean by context is, if a voice actor was reading a textual copy, you would know that, okay, this is a dialect sequence. I need to produce a dialect. If it's a happy sentence, I might need to pronounce as a happy sentence.

03:01 But what happens before and after comes into the equation, and you need to bring that across. Then there's a last big piece. Voice model has the sound of how you intonate the given fragment. But the second big part is the voice itself, the characteristics of accent,

03:20 of style, of prosody across that voice. When you actually try to vocalize something, when you create that voice model, you turn text into audio, you need the text. You also the voice reference of how you want it to be spoken. Here was the second big innovation.

03:35 Apart from context, it's how you decode and encode those features. When Bell Labs came with their initial representation of speech, the big piece there was you would have effectively hard-coded parameters for that speech. With ElevenLabs models—

03:50 Hard-coded parameters for enthusiastic speaker, British accent, that kind of stuff? Exactly, that kind of stuff. The set of pitch elements that you can select, set of energies, spectrograms you can select from. In our approach, effectively, you would give the model open-ended ability

04:06 to select what those parameters should be. It's not going to be British, Polish, Spanish, English speaker, but the model will deduce them themselves. The same for other sets of parameters that are not hard-coded, whether it's the enthusiasm, whether it's the sadness, et cetera.

04:21 You're saying Britishness is an emergent property in your voice models? Exactly. Those two big parts, so it's encoding and decoding of how you create the voice. Super hard problem before, and figured out, too. How you then construct that in a sentence, how you get the context across so you can

04:39 predict the next volumes, so how you bring them together in a reliable and stable way while doing it quick. These were the two first big innovations in the voice models that continue to today. But okay, so if LLMs reason about text and word subparts tokens as the way

04:56 they think about the world, what is the equivalent of a token in a voice model? You mentioned phonemes a bunch. What is that representation? We start the voice embedding effectively for the speaker. You need that reference when you produce and create the speech.

05:13 Of course, in the input to the voice model, you still get the text, and you bring the speaker and coding. Then, when you produce speech, you do operate on the waveform or effectively on the phoneme level of that speech. Then when we go the opposite, so of course when we—

05:31 Sorry, what is a phoneme? Fill in my understanding. It's like a syllable deconstructed even to smaller elements. These are effectively the human sounds you can produce. These would be the most close to that representation.

05:44 But of course, in our models, now it's going to be a combination of not only operating on phoneme level, you also operate on the text level. You operate both in sync because when you are predicting the context, you need to understand how that sentence will get constructed, and especially if it's more of a streaming

06:01 real-time use case in a voice agent setting, you need both parts to work across. It's similar to how you operate on the token level on the tech side, we operate on the token level on the audio side. It feels like a big part of the magic of Eleven was your voices

06:17 were much more human-sounding. How did you accomplish that? I'll give you a quick synopsis of how we think about the models on the text-to-speech side today. In any model, you need the architecture, you need to compute, you need data.

06:31 Architecture innovations were one thing. The data part was the second big thing. With audio, you will have a lot of audio data available, but frequently you will not have it annotated in the right way. You won't have which speaker is speaking when.

06:48 Some of the "what" is annotated, but the "how" isn't. As we are speaking now, what's the emotions that we use? What are the accents that we use? We would invest a lot internally on effectively creating our own data labellers, our own team, to be able to create those

07:04 data sets that will be better. That was a combination of, of course, semi-automatic techniques and then manual techniques. Actually, a lot of the models that we did afterwards actually span out from a lot of that research, too.

07:16 Speech-to-text model initially was a model we did for ourselves because the models on the market just weren't good to annotate that data. Then another brilliant research area on our team was being able to construct it so we could span it out as a model that we brought to the customer. You've just been doing useful stuff in voice, and that has

07:34 emerged with a whole bunch of products that you might not have expected because you find you're building useful stuff. Exactly. That's a combination of data, of being able to do it automatically, create a team that's coached on voice, on how to describe it, because most of the labellers out there just aren't

07:51 as well-versed on understanding the audio and voice, helped us a lot to bring that back. Then, of course, deploying those models in production, seeing how customers interact with them, having them annotate all of the data helped us refine those models over time.

08:04 A very interesting thing on the side. We spoke about the speech representation. The first guy who created the speech representation is a guy called Kempelen, Wolfgang von Kempelen. He created those analogue machine that would represent effectively a human

08:18 vocal tract and try to produce that sound. He had to spend decades on that, and that started producing valves. But that was the same person that created a chess machine, the first viral, let's say, chess machine that would simulate playing chess. Is this the Mechanical Turk?

08:36 It was called Turk. But the crazy thing behind it, it was operated by a human, and it was all a fluke. That's where the Mechanical Turk came from, which actually we use in our data labelling production to make that work there.

08:52 Sorry, we jumped right in. But if you describe the Eleven business today, people think of you as the speech company. How should they actually think of your business to the extent you can describe the big areas?

09:03 Text-to-speech, speech-to-text, voice agents. Just break down the business for us. In a nutshell, I'll describe ElevenLabs as a research and product deployment company. We build foundational audio and voice models, and then build a platform for businesses to transform how they communicate with their customers,

09:26 with their employees. That will apply through AI agents from customer support, sales, hiring, training, all the way through to marketing and storytelling for our creative tools. In that set, we've created all types of foundational audio models.

09:43 Text-to-speech models for producing speech, speech-to-text models that work over 100 languages and happily beat others on benchmarks, all the way through to conversational models of how you loop them together to music, to other domains of audio. Then, of course, beyond the models, when you actually bring them

10:01 to production, that's where the second level of the platform comes in, where that meets the businesses on the specific use case. On the agent-specific example, it would be how you now connect those models to the knowledge base, to telephony, to the integrations that you need to perform the actions, how you evaluate and monitor the agent

10:19 that it behaves in the right way, how you build the right safeguards. On the creative side, on the marketing side, it's how do you create a good ad so you can create a good video voiceover for one of the campaigns. How you create an article that's narrated with a specific voice that represents

10:37 the brand in a good way. That's where we combine the models and understanding of the customers we work with into one policy platform. Every platform company has this question about how far they go into applications. How do you think about where you go horizontal and power

10:52 the whole ecosystem versus where you develop application? Because you can imagine there being a whole ecosystem of closed captioning tools that grow up that, again, are built on the ElevenLabs tech. It's not necessarily a space that you would have to go after yourself. I think the big difference between...

11:07 In your question, today, we see ourselves as a platform where if you're building a horizontal use case in your business, a great place to come. If you have a lot of domain specificity, that's where I see a lot of the application companies forming over time, where that's specifically not the spaces we will go into.

11:28 I think it also is interesting when the tech is moving as quickly as it is here. It's one thing with SaaS where you get these vertical-specific providers, but I would imagine one of the biggest risks for you guys in being intermediated is if there is, like in this example, a closed captioning service that is on a two-versions-old version of ElevenLabs and hasn't upgraded.

11:52 That's a problem because you want people to be using the latest and greatest model that you've developed, and you'll be deploying new capabilities every week. I presume that's part of your thinking, is that just when it's moving that quickly, you need to go direct in a lot of cases. That's right.

12:05 In the closed captioning, here already now, we know that our services is going to be able to tackle 99.9% of the cases that customers have. Then there's added benefit of we work with healthcare customers where we will create a custom model for those customers where we'll get that

12:23 transcription perfectly. The context is the tricky thing in closed captions, where we talk a lot about a lot of technical stuff on this. Yeah, for sure. That's where you need effectively a dictionary of where you do the tech beforehand, which, as we work with the businesses, we know

12:39 we need to embed in that creation process. We're talking a bit about product here, and one thing I note is that LLMs are amazing, and you have the usage stats of ChatGPT and Gemini and all the popular LLMs where they're working and people use them a ton. It feels like there's a big product overhang when it comes to voice,

13:01 where the leading-edge voice models are incredibly capable. Yet, I was driving home the other day, and I needed to read a PDF, but I was driving. I said, "Okay, I'll just have my phone read the PDF to me." You can try and hack it with iOS screen reader, but it doesn't really work with the scrolling. Then in theory, you can upload it to Gemini,

13:19 but you're trying to get it to not summarize it, and it actually just hung when I tried to press the Read This to Me button. There was no way I could get my phone to read me something, which seemed like a fairly basic feature. All cars advertise voice control, and yet, it sucks.

13:36 Separately, if you want to input something to the navigation, just no car has a good version of that yet. Maybe Tesla does, and, and, and... Why does it seem like with LLMs and Claude Code and everything, we are using all the capabilities of the intelligence, whereas with voice,

13:54 we're living 10 years ago somehow? Well, I'm thinking would I agree with the premise that we are 10 years behind. In the lived experience of people day to day, they're using Siri's transcription, which has gotten better, and it's still way behind the leading edge.

14:09 There's definitely a piece of… I think the technology in many of those cases already, there's a deployment gap to what you are saying. It's like an automative for some of the big companies are not adopting that quickly enough or bringing that into the production.

14:23 But plenty of different problems that you need to fix along the way. The quality of voice models for them to actually sound good, this is only a last three years thing. Yeah, but it's three years. It's a three years thing.

14:36 Cars have over-the-air software updates now. That's three years for the first voice model that can narrate text async. Two years ago, we can start seeing the real-time version of that. I think the real break was a year ago, where you could start seeing that in production.

14:51 Then I think over 2025, the big piece that hasn't been possible is how you connect now the real-time voice interaction with something which I think you're referring to. It has context of what you want to do, what is the material that you want to read, how does it connect to set off your preferences

15:07 from the past and get that across. I think that only recently became possible, and where we've seen the big adoption across the enterprises leading on the technical side. I think this year, it should be in the automotive side too, or some of the applications.

15:23 You think we'll start seeing great voice models in cars this year? This year for their own cloud use cases. On car, in car, so without connectivity, not yet. There's deployment, of course, gap, of how you bring that into the gaps. But I think the next two years, three years.

15:41 How about the PDF reading use case? That should work. Yeah. But how should I have done it? Back in the day... I'll pre-empt this with a story to cue ElevenReader, but we had this problem.

15:56 We had so many audiobook authors come into ElevenLabs. 2023, we released the first software. We had a lot of creators and then a lot of audiobook authors or book authors that couldn't afford professional narration and wanted to create an audiobook.

16:08 However, none of the companies accepted AI audiobooks. You can't sell an AI audiobook on Audible or something? Exactly. Audible would block AI content. We had no choice. We need to create an avenue for them to— Ah, because there was no distribution for AI audiobooks.

16:24 Exactly. We created ElevenReader, and that came with a functionality where you can upload your PDF, you can upload your text, and have it read out loud with a number of incredible voices, whether it's Sir Michael Caine all the way through to estate and working together

16:39 with Sir Richard Feynman, where you can have that— You are working with the Sir Michael Caines of the world? Exactly. Then you can actually read it out loud. That works extremely well. That works. Now, how can you do it?

16:50 Gosh, I do want everything read to me by Michael Caine. It's a great voice. Shouldn't you guys have a consumer app where I can just do the common voice things? I want to be able to have an Eleven app on my phone, and then if I upload a PDF

17:03 to it, it can do the common things that I would like, such as have it read it to me. Yeah, that's exactly ElevenReader. That works. The phone makers allow third-party keyboards. Do they allow third-party transcription engines? Will they, do you think? The phone makers you said.

17:18 Like Apple and Google. The OS makers. Yeah, not all of them. With Android, you can work through it. There's variations of that, Nothing. tech, and others.

17:30 I feel like if you had a popular Eleven app that allowed for transcription, people would use it a bunch, and maybe eventually, Apple would say, "Oh, we should allow third-party transcription engines if that's what people want." It seems like they might be going in that direction.

17:41 Recently, they announced that it will open up the LLM ecosystem. Hopefully, they will do the same with voice ecosystem, which is similar. I think it's rational to do when it's moving so quickly. The voice assistant paradigm is one of the oldest UI paradigms in computing, like the, "Open the pod bay doors, HAL," from 1969.

18:04 I will claim it's not working yet. Siri doesn't have the intelligence. Then on Gemini and ChatGPT and those apps, I want to use the voice mode, but I don't know about you, it just doesn't work.

18:19 Sometimes I'll be using my phone, and I'll use the iOS keyboard transcription to type in the field and then say a bunch of stuff, and then send it off. But this suggests to me that consumers really want voice mode that works, and yet it's just not working yet for the major LLM apps or for anyone.

18:40 Why isn't it working yet? It is pretty hard to do because you want two things. You want to be able to say things that you want, but you want sometimes for it to execute it, sometimes to wait for you to finish and add something in the sentence.

18:52 Sometimes you want it to be interactive, so it asks you questions back to clarify and get some of the additional detail. All of that is actually pretty hard. That's where the magical ideal version of a voice agent for us comes through, where you need the speech-to-text element, you need the transcription side,

19:08 you need then the turn-taking mechanism. When do you finish sentences? When is it likely based on silence, based likely on the context? Then sometimes you want it to speak back and clarify, or at least give you the text back to clarify, and then maybe execute a set of instructions.

19:24 That problem is still very hard. I agree with the claim that this orchestration side has not passed a true conversational agent Turing test, where it behaves as you would expect from another person, where you can say— That's the simpler way of saying what I'm saying is that we have passed the Turing

19:40 test with text LLMs a long time ago. We're actually nowhere near that on voice LLMs. It's interesting how that's a final frontier. I feel like it's going to work in specific domains. In customer support calls, passes the voice Turing test.

19:55 It works well. Let's take another spectrum of that. An interactive gaming experience, a truly interactive as you would have with another human in that game, it's so hard and further out there, we haven't passed it yet there.

20:10 Yes, that makes sense. But I think that's a combination of even a simpler version of within that. Sometimes you might give a response immediately back. Sometimes you need a tool call to get additional information from the database, how you orchestrate that.

20:24 That's probably the most common thing we see as we work with some of the companies out there is you want those systems to orchestrate extremely well where if it's a conversational use case, pretty simple, you can root the agent to speak with it. But if you need to authenticate, if you need to pull additional information

20:38 from the database, what do you do? How do you handle that graciously? That's where it gets tricky. To that extent, I would say that that's just getting there. We'll hopefully see that.

20:50 Our goal is to pass the voice Turing test in all those cases or the Turing test for all conversational agents outside of voice, too. I hope we will all be there in the next year or so. For subscription businesses, a lot of revenue is lost in that last few seconds before the checkout.

21:07 Someone has to get up and find their wallet, or they mistyped their card number, or they hit an error, and they just give up, and you lose the sale. For a company like ElevenLabs, adding hundreds of thousands of subscribers, even a tiny bit of friction like that, it would really add up.

21:20 But that's why ElevenLabs uses Link from Stripe. Customers save their details once, and then they can check out in seconds across more than a million businesses with saved credentials. If you want a faster checkout for your customers, you should turn on Link from Stripe.

21:36 Are you guys working on personalized voice transcription where it feels like part of the way we're making it hard for ourselves is when I speak to Siri, I have a bit of an accent, and so it sometimes has a hard time understanding me.

21:54 But my accent doesn't change. It could just get good at listening to John. But my understanding is it's not, it's just running the global voice recognition model. I'm guessing it's the same for ElevenLabs where you're running the global

22:06 voice recognition model. But again, you have an accent. If you walked up to someone in a coffee shop and said two words, they might have a hard time understanding it because they're not putting it through their Mati Polish accent filter. Where's this going with actually interpreting the person that you

22:22 know to exist on the other side? I have a very tricky one to detect. My voice is frequently used in the tests. You're part of the test suite. For text-to-speech, for speech-to-text, for everything.

22:34 It's pretty— But again, trying to parse your voice in a global model is just making life hard. It's like, have a Mati-specific model. On the speech-to-text, by transcription, exactly. The big part now that we are bringing in is you have two parts.

22:48 One, effectively a person or a voice-specific detection, which is true for the accent side, but it's also true for a crowded room. We have an incredible research team that's able to continually do both the accuracy high, but also add things like speaker detection, of course, noise reduction.

23:10 But then the second part is also keyword detection. There are specific words that you would want to say in those settings that you want to effectively monitor for. We spoke about, let's say I'm going to the coffee shop and order things. The set of actions the coffee shop would expect me to do.

23:26 This is information theory. It's like they can just listen out for the coffee words. Exactly. Then try to match it to the closest proximity. Both things will help.

23:35 In a setup where you have my voice, perfect. You can decode it and code it on that. If you don't have my voice or even if you want to double amplify it, we already support effectively keyword detection, which is useful for real-time setting and async setting.

23:52 Back to Cheeky Pint transcription, you could effectively pre-generate that from the previous podcast and look for a set of words that you would use traditionally in that. You do the keyword detection already, but how hard are the… I want to get superhuman transcription performance by feeding it an hour of Mati

24:11 audio before it listens to Mati, and then it should be able to do a much better job transcribing. Is that just a really hard research problem? No, solvable. We think we can roll it out in one of the next

24:23 versions, which is hopefully in the next month. You think this year you're doing person-specific transcription? Person-specific transcription. We can already dial our speakers extremely well. If we are speaking, we can, of course, dissimulate who is speaking when,

24:39 which is in transcription side, apart from accuracy, diarization is one of the harder problems. We do that extremely well. Now it's going to be effectively what you're saying, fine-tuning based on the speaker that I want to listen to,

24:52 which we know will be important. In a healthcare setup, it's such an important part. You're in an operating room, you're a doctor, you want to say a command, then you want to really be able to listen to that one person's specific piece.

25:03 You have a hardware device at home, let's say it's a pilot that helps you control the TV. Here, too, you will want that to listen to you versus, let's say, the family running around. Or maybe you want it to everyone.

25:15 You could decide that, but in many cases, you want to be able to specify that. That's really exciting. It's great because there's still so many unsolved research problems. Yeah, there's just breakthrough after breakthrough coming in the domain of voice models.

25:31 How about on the flip side, when it comes to speech generation? In the Zoom "touch up my appearance" feature, I've always thought about that in the context of voice, where... Should you offer a de-accenting filter for voices? Or even there's one podcast that I like to listen to, but the voice is a little

25:49 mumbly, and I always thought they should put it through a de-mumbling filter just to make the—Or slow it down. Yeah, make the enunciation a little better. But all these things, again, like Photoshopping an image, there's no reason that the…

26:02 Have you thought about voice-to-voice, basically, rather than voice-to-text or text-to-voice? Yeah. There are two big parts. One on the speed generation side, similar. So many innovations still there.

26:14 There's a wider piece, and we released the V3 model that we're solving that for the first time. It's like, can you control speech? You can have the text-to-speech. You generate something that sounds emotionally great.

26:28 Previously, until the end of last year, effectively, you would rely on the model to decide what's the best performance. You could regenerate it, but ultimately, model decides the best performance. That's where the controllability came in, where we can finally give it cues of, say it in a slower way or change how you deliver the dramatic pause

26:44 or any cues that you give. To be able to do that, you need the architectural changes and the data that we created over time where you annotated what was said and how it was said, so you can actually train the model to do that. Today, finally, you can have both speed

26:59 generation or entire voice agent experience with what we call expressive mode, where the agent knows the emotions on the other side. If the person is stressed, it can react and be reassuring, and that's generating an LLM response on the reassuring side and response

27:15 in that set of emotions, too. That breakthrough was super hard to do. That, of course, stretches to a lot of what you said. It could be some version of speech enhancement, either real-time or in a pulsed setup to change how that's delivered.

27:31 That's relatively recent innovation, and we know it can still be so much better. The edge cases of how you want to describe it is pretty large. That's one. Then the second part of the question, which is a huge question, that's speech-to-speech models.

27:46 As you said, our approach, as you think about voice agent, conversational agent, is effectively a cascaded approach. You use transcription or speech-to-text, LLM, text-to-speech, and orchestrates all of that together. Then you have a speech-to-speech, which goes directly from speech,

28:00 and there's a speech response on the other side. When we say speech-to-speech, is that the idea that it doesn't go through text as an encoding in the intermediate? Exactly. Oh, interesting. For performance reasons?

28:11 For accuracy reasons? You usually do it for latency. It is faster to run a model that does not have to transcribe and then generate. Exactly. It's quicker, but on the flip side, you lose reliability.

28:23 You lose like all visibility into the parts of the pipeline. In emotionality, we think you can deliver both on both sides extremely well, and maybe you can make it more controllable, too. Today, we are optimizing heavily on a cascaded approach. I'm sorry, a cascaded approach is?

28:37 Is the speech-to-text... Going through the text layer. As we work with a lot of the businesses and enterprises, they will need that visibility into what happens. They will want to execute certain tasks on top of that.

28:50 They want a good visibility into each of the steps and great accuracy of all the models. But beyond that, they can abstract away what's the LLM layer, what's the intelligence layer, the integrations are easier in that system. That's where we are betting a lot of the research work of how you can make

29:05 that great, and we think we can make that great. In speech-to-speech, as you think about maybe more of a companion version of the applications, that's where that will flourish because maybe the hallucinations aren't as important, but the latency is a little bit more, and

29:19 maybe hallucinations are even a feature. Maybe in the future-future, just to finish that part, you will have some version of combination of the models. That for low complexity, easy models, you will have speech-to-speech, and for higher complexity we will have to cascade it.

29:33 I was going to ask about this. You know the way there is research on how the invention of writing changed human brains and just changed the neural pathways in ways beyond the actual written language. Do you observe that speech-to-speech models think differently

29:54 than cascaded models? It sounds like they're dumber. They are definitely dumber. You need a smaller model. But that's interesting, that forcing models to reason about text.

30:07 I know they just have much more in there as well, but they're smarter. Yeah, but it's like, if you are getting speech-to-speech, usually you will use smaller models, so it's still quick. I see. It's also just a model size thing. But are there interesting differences beyond correlates like size?

30:24 What I can say is slightly different to your question. The people interacting for voice and the performance we see for how they interact with the business changes just by nature of interacting with us. A good example, you can contact ElevenLabs and register for your interest,

30:41 you go through the form, and at the end of that, we have supplemented that, that instead of going through the form process, you can speak with our agent and leave more details. What happened there are two things. One, people were actually much more keen to leave the forms through speaking

30:56 with the agent, so we would go through the form a lot easier. But second, they would be a lot more open-ended in terms of what the use case are. They would start giving us information about the wider set of use cases, the complexity of the use case.

31:09 The writing out was tedious and tricky— This is like an open-ended adventure game. Open-ended. You could ask follow-up questions, you could clarify. But people were just more at ease and could trust the system while doing that, that it's working.

31:23 That helped us a lot. Then free, which maybe it's more of a technological barrier, it also works across all languages. Now we have leads from all parts of the world coming in and leaving their details. We did that use case, and now we have a few different companies

31:36 building their SDR versions of that, too, to help them capture the leads coming in from banks all the way to actually one of the automotive companies that leaves that where people are just more keen to speak through voice. I want to ask about this second-order effects. You've talked in the past about how growing up in Poland,

31:57 I guess the dubbing of TV shows, they were cheap, and so they would only have one voice actor for a TV show. No matter all the parts, male and female, they're like, "I love you." "I love you, too." There's one voice actor doing all of them. Now, thanks to better voice models, you'll be able to just have really good

32:15 voices, AI-generated, for all the dubbing. Because again, it's not like it's taking jobs from great dubbing that was happening previously. It was awful dubbing happening in Poland previously. That's one example of the second-order effect.

32:28 What are the other second-order effects you're seeing of ubiquitous good text-to-speech, speech-to-text? It seems like across a broad array of languages, because whatever in English, just this didn't exist in Polish or Irish or, pick your language.

32:44 One, breaking down the language barrier. The inspiration came from the movie side, but it also applies in any communication setup. Could in the future, could I travel to another country and speak Polish or speak English and that language isn't being

33:00 understood in the local native language? From The Hitchhiker's Guide to the Galaxy, this version of the Babel fish. That you can actually understand the world. Voice, of course, will be an interaction layer. But similarly, all of us will have our own extension and voice agents

33:14 that can help on our behalf. There are very clear and great examples of that of people that lost their voice and can get it for the first time back. We see that everywhere, whether that's people that lost it due to ALS or throat cancer that can get it back.

33:28 Just recently, there was an example of a patient that had Neuralink. We worked with them to bring the voice that that person could speak with their own voice back with the family around. We worked with a lady that lost her voice before she got married. Then finally, the technology became possible.

33:49 We were able to recreate that voice. For the first time, she could replicate the marriage ceremony and speak the vows together, which was such a heartfelt moment. That's really sweet. It's probably the most important from all the work that we do.

34:03 When you guys talk about voice agents, is a voice agent just the idea that you have some long-running or persistent agent that is going out and interacting with the world through voice? Customer service would be one example of it. In the other direction, your Claw going and making you

34:26 a restaurant reservation and actually calling up the restaurant. Is that how I should think voice agents? That's right. Exactly. Whether it's the reactive side of being able to interact with the customer or the proactive to call it back.

34:38 We recently had a very interesting one, topical because it was a Guinness-related one where there was a developer developing a Guinndex, effectively. Oh, I saw that. They were calling all the pubs in Ireland to check on the price of a pint. You could ask that or report information.

34:53 The Guinndex was built with ElevenLabs technology? It was built with ElevenLabs, too. People could actually do both sides. Could proactively reach out, reactively reach out, always capture full voice. Then 3,000 different entities could report their prices and get that across. Have you, by the way, hooked up your OpenClaw to ElevenLabs?

35:18 Is the OpenClaw-ElevenLabs combo something that a lot of people at Eleven are doing? As you know, the OpenClaw will look for the most popular tools frequently where it tries to cook up. ElevenLabs is one of the recommended ones. It's the top option for voice.

35:30 Can you tell me a bit about the business of voice models? I think people have an intuition around big LLMs where there are these very expensive training runs, and yes, they depreciate quickly, but there's so much usage that all of the models trained to date have paid off their training runs and then some.

35:51 Then there's this ever larger CapEx going into… I mean, a lot of it is inference these days, but also training. People have some intuitions from the LLM world. I'm curious just how I should think about voice, where one, how expensive is training the voice models?

36:08 Is the expense in the researchers? Is the expense in the training runs? The economics is presumably simple where it's just per-usage. But yeah, just talk us through the business. Definitely cheaper than the LLM and image-video models.

36:26 Significantly smaller models. The models are smaller? Smaller. What's the parameter count for a leading-edge voice model? A few billion to tens of billion per meter models. For context, I think the…

36:41 CPUs moved away eventually from gigahertz as the metric as they move to more cores. I think we've mostly moved away from just raw parameter count, but I think the leading edge LLMs are in the hundreds of billions of parameters. I think the leading ones, yes, but of course, you have the variations that you will use at lower scale.

36:58 CapEx is still pretty high. We've, of course, raised recently a half a billion at 11 billion valuation. Makes sense. Makes sense. To continue being able to build the best models in the world. Researchers, of course, you want the best people in the world.

37:15 I think we have those people working in audio and my co-founder who is leading that work. That's definitely a big piece of, not financially, but even how you keep the ambitious deployment, so you continue building leading models, helps you attract more talent in building that.

37:36 Then on how we service, of course, inference is correlated with how the models are used. For us, we've seen incredible growth across the work. Mostly this is charged per… If it's input text or text-to-speech, it's usually per text token.

37:52 If it's voice agent or transcription, then it's per minute. We see that being the bigger part. But usually, broadly, it's per token basis. Of course, as we work with businesses, it's like an annual agreement. The bigger the spend, the bigger the commit, the bigger

38:06 the discount to get it across. The way we usually do is when we have a new model, we try to give it at cost to a lot of the customers so they can experience the best. It's still usually not as reliable— That's interesting. The newest thing is often the most expensive, whereas you make the newest

38:23 thing the most economically attractive one? We try to make it attractive so the customers are… It's more expensive for us than any previous generation. The quality is higher, so we try to keep the prices still competitive. I see.

38:36 You subsidize it, but it's inherently more expensive as a bigger model. Exactly. Over time, we might do some tricks to optimize it, but we want the customers to experience… Because of research, the big thing that we've seen is the reliability of the model

38:50 in the early days might not be there. Then two, people don't even know what's possible with that model. You want the widest set of distribution, so people can show the world what's possible. You can have it, of course, as the distribution mechanism,

39:06 learn yourself what to improve, what to change, and then get it out there. Are the voice models just getting bigger and bigger? Will we have voice models in the hundreds of billions of parameters, or have we found… It seems like for certain types of model architecture, there's an upper

39:22 limit on the natural size. Have we found that upper limit for voice models? It feels like for specific use cases, like say, audiobook narration, you probably found that size. You probably don't need to stretch it much bigger to make the quality much higher,

39:35 but for certain use cases, that will probably grow. The thing that I hesitated on the question is in a cascaded approach, you probably will not see dramatic size changes. You inherently want the models to be quick and reliable. You want to orchestrate them in a smart way.

39:53 In a fused approach, probably that will get into tens, hundreds, billion-per-meter models because you combine, of course, the LLM side and the voice side, so that will get bigger, but on the just voice, I think it will keep being small. There are certain domains where we'll see bigger models.

40:10 Yeah. That's so interesting. It does seem fun, from a research point-of-view, how there are still these various unsolved aspects, and how you guys are just making technical breakthroughs and then releasing them down the product pipeline. That's a really fun stage of a company's life cycle.

40:27 For sure. It's fun because it feels like we can do innovations on both sides. There's so much on the research side, so much on product side. Ultimately, the biggest part is how we deploy it to the customers, where SMB will have a very different dynamic than the enterprise.

40:45 It's not vendor/SaaS relationship where you just give the product out there for the biggest companies out there, but you are more of a partner in their AI transformation part. You want the resources to work alongside them, to work on the frequently very new use cases that were impossible to help create and bring those

41:04 voice agents to production. That's a big shift. The biggest focus is how we bring the conversational agents out there to the businesses around the world. When you say bring conversational agents is the biggest priority, is this

41:18 for customer service-type use cases? What are the most popular use cases for conversational agents? We want to be a partner for full interactions between businesses and their customers or their audience. I'm saying their audience because that will apply in support.

41:34 Support is the easiest one because that's where it's most ready. That's maybe the big difference to how we see ourselves to some of the other companies in the space. This can also apply to sales. You can have the proactive side of reaching back.

41:46 You can have AI SDR versions of that. Then you can have all the way to the marketing use cases where we are your partner for working even outside of the conversational agent space of how you create a great marketing campaign. How does this break down between…

42:03 We had Des Traynor from Intercom on here and they have Fin, their agent, and it's a thing on the website that you can go talk to. He described a very similar phenomenon that you described, which is, you start maybe thinking, "Oh, this will help me answer customer support queries." It becomes like a generic UI

42:24 for the website, where it's a box you can type in to go do things and understand things. Why wouldn't you read the docs and design your integration that way? Whatever. Will I have one for text and then one for voice?

42:39 Will you guys do text, too? How does that... Because it seems like this is also succeeding at the text level with Fin and Sierra and all these things. The places where we know we will be able to provide the biggest value is where,

42:53 ultimately, today you will have either a big portion or most of the interactions coming for voice. If that intersection is there, that's where we can provide higher value. Of course, if you need a text chatbot there… If you fix the voice agent, you have fixed text piece inherently as well.

43:13 The place where we do optimize today is going to be like, how do you select the right voice for the right customer interaction, how you pull that in there. In the pretty complex case of what you mentioned earlier, of how you orchestrate that to pause or look for something deeper into the docs, how it can be extension of

43:30 entirety of the business, so not only in support, but across the entire user journey. The bottom line is we want to be able to provide you across the entirety of the interactions. Voice is usually a big part of those interactions.

43:45 We need to solve the integrations, we need to solve the knowledge, we need to solve text as part of that. We wouldn't, for example, go into what I think will happen in a lot of those cases, very deeply into reasoning version of those use cases where you maybe need the multitouch.

44:01 Yeah, and a lot of complex actions. A lot of financial analysis. That would be not something we optimize for. Can we talk about your revenue ramp? You're just one of the fastest-growing startups, period, of the past few years.

44:14 What's your most recently announced revenue figure? Most recently announced was end of 2025. Whatever number you want to give us. Most recently announced was 350 at the end of 2025. The best proof of the technology working...

44:26 Recently, we were in our work with Deutsche Telekom and T-Mobile with Revolut, with Klarna, with Meta, with IBM, a wide set of use cases. This quarter was one of the best for enterprise growth where we had the first quarter hit 100 million in additional ARR growth, which is crazy. In net new ARR. In net new ARR.

44:48 If you're thinking this quarter was 100 million net new ARR and 350 million at the end of the year, I'm no mathematician, but it's up in the 450 million range. Versus this time last year, that's a several-fold increase. Just, what's working?

45:04 From the outside, I would assume that there's really strong cohort growth within accounts, and then you seem to have self-serve and enterprise businesses that both contribute a lot. I don't know how big self-serve is, but as a user, I like to be able to fiddle with ElevenLabs and not have to go talk to sales.

45:21 Maybe you can just talk about what worked to reach 450 million plus of ARR so quickly. We are over 50% is now sales-led enterprise. I think largely that technology powers a lot of their agentic interactions just became reliable at the same time as high quality over the last year,

45:44 year and a half. Frequently, you know this extremely well, you will start the account, and then, of course, it continues expanding. We see there's definitely land and expand motion across ElevenLabs. We bring—What does that expand look like?

46:00 Is it new departments? Is it just the usage starts taking off? When a customer expands—Both. Usually, the first part, too, it's like we try to make it very easy for our customers.

46:11 Maybe against ourselves, where we give the technology a pretty attractive economics because we so much believe in the technology providing value. You can actually try it and test it. Then within that one department— You think you'll make it up in usage, basically.

46:26 Exactly. That usage, the commitment continues increasing because you know it's providing value. Then it's so much easier to make that a choice. Then, of course, cross-department pollination is there, too.

46:38 Our work with Deutsche Telekom started with marketing side. We did Magenta work and podcast generation. Then it expanded to customer support. Then it expanded to us working on an agent across the entirety of the network, so people can call in and have the agent.

46:53 You could see those step changes across. We are now 470 people as a company, so we keep on growing. Some of the things that stay consistent is small teams. We have less than 10-people teams for each of the product or research initiatives or

47:13 even, as you think about sharding some of our go-to-market strategy, there will be smaller teams understanding the industry in-depth, understanding the market in-depth, and going independently and going quickly. That definitely contributed largely to that. Two, especially on the biggest enterprises, what we found works is

47:30 we have the full spectrum: self-serve, PLG motion that helps drive distribution, drive awareness of ElevenLabs. On the completely other spectrum, we have the high-touch for deployed engineering working side-by-side with the customers to customize the entirety of their work together.

47:50 Why did you guys do self-serve? Because I presume you have a lot of competitors where they have tech, and it's behind a contact sales form, and you have to go talk to an SDR and then talk to an AE. You guys just offer the tech available on the side.

48:04 I'm a huge believer in this. A huge part of Stripe's growth has been driven by the fact that we just made Stripe available to anyone and built a lot of products around that adoption pattern, but so many companies seem to skip it. I'm curious how you guys came to— So many reasons.

48:19 I think the quick ones that come to mind is feedback loop. You have immediate understanding of how good your technology is. Two, which is an extension of that. We stand behind our tech. We believe it's the best in the world for models, for voice agents, for deployment.

48:37 We want people to experience that. I think you do that the same in Stripe, where the best version of the technology is available to everyone, which is so attractive to actually try it out. We always try to make everything we built for the highest end use cases, bring it back to the ecosystem free.

48:53 Frequently, the newest of the use cases... For enterprise, you will need reliability, you need compliance, you need to scale, which we deliver. Frequently, as you develop new technology, it might not be ready for a lot of those parameters, but it's definitely ready for developers and SMBs.

49:10 We love what they are doing because they are showing us the future and effectively helping us find a trajectory of where ElevenLabs should go. I'm totally convinced. I'm just always amazed that more companies don't pursue it, where it feels like they're really shooting themselves in the foot by not.

49:24 Did you guys self-serve on Stripe? Or did you— We self-serve on Stripe. For example, Eleven is a huge company, and yet you started on Stripe on a self-serve basis. Initially, we were two of us at the beginning.

49:37 You try to see what's working in the industry, but you try to think from first principles. You want to try it out. You want to understand how it works. The more friction elements before you're trying it out, the less you trust whether it's available, whether it'll be additional payment

49:51 that's hidden behind some of those steps. You don't want to go through them. It's so much. Speaking of Stripe, do you have any Stripe feedback for us? Anything you want us to fix? My most common feedback until recently is like, why don't you give us pay-as-you-go,

50:04 usage-based billing type version? One of our finance leads, Maciej, I know was speaking with your team, and that was day before. He was great. He was thinking about it for a long time. He's great.

50:16 Was it he who said, "You guys should buy Metronome?" You should buy Metronome. Then the next day, Metronome acquisition was announced. Now you have it. That was my most common feedback, and we'll be launching.

50:27 That's a good announcement for this podcast: we'll be launching usage-based billing to everyone. Sorry, I'm shocked. As in previously—Pay-as-you-go. Previously, you had it on an enterprise basis, but everything on the self-serve basis for like—

50:43 We had the subscriptions, yeah. Subscription plans, you could go over them, but now we are launching a full pay-as-you-go experience. You can just try out voice engine, which is effectively this orchestration loop all the way through to any of the models directly.

50:56 Going back to self-serve, I think a new thing in AI is that all self-serve products should have pay-as-you-go as an option. Maybe you want to have a subscription with some unlimited tiers, but I don't know if you had the experience of you're using Claude, and you're typing away your queries, and eventually you hit some rate limit,

51:13 and it's like, "Sorry, you've hit your usage limit," and you want to be able to do the thing that you can do with Claude Code, which is just pay per API. It's like, I'll pay for it. It's very funny as a consumer to not have the option to pay more,

51:25 to use the product more. I think every AI product will need… They probably want to have some all you can… Most of what you can eat subscription with limits and then the ability to pay for overages.

51:36 It sounds like that's what you're doing. Yeah, exactly. That's what we're doing. The only thing I wanted to ask you about is, I feel like all CEOs of larger companies today are trying to figure out how do all these AI advancements change the nature of the organization and how do you redesign your organization

51:58 a bit around all this new intelligence. That could be about what the scaling factor is of the number of people you need to do the work. It also should be like, do you need more senior people because they're better able to direct the AIs, and the AIs are maybe you can do the work

52:13 of what previously would have been junior people. Do you need more junior people because they're going to be more AI-native in how they work? Do you want smaller teams? Do you want bigger teams? How do you actually go do the process engineering of...

52:24 Your finance team should be using Claude extensively. Finance teams do not historically have a lot of home-built software. There's all these questions that are floating around, and you have very rapidly built a much more AI-native company. I'm curious what lessons we should all be learning from ElevenLabs as a

52:44 large business recently built, and so without the baggage of decades of "how we've always done it." We started in 2022, which is a year when the two topics of the day were crypto and metaverse. Just before, and then, of course, AI flow start—

53:01 Yeah, because you scaled in the AI— Exactly. We could have the privilege of scaling through the world when it was all happening. For us, what works, and we really believe in that being the big part of the future. The first is small teams, keeping the teams small and super flat.

53:20 Both me and my co-founder will have over 15 direct reports each that we'll work with. Most of those people will have that same scale of direct reports. Your span of control is way larger than a traditional company. Normally, it would be eight, you have double that, and obviously,

53:33 that's an exponential. Exactly. Of course, there are some teams which in the short term might not do that, but ultimately, that's where we think it's going to be headed. It's roughly 10 team size within each of those work items. Startups, no offense, but startups often have pretty wacko management ideas.

53:49 There was a funny tweet: Lord, grant me the confidence of an early-stage startup founder blogging about their management theories. You think this is not a startup effect? This is an AI effect where basically— No, it's definitely a little bit of a startup effect.

54:04 I figured out it's the hindsight benefit. I'm canceling our Stripe changes. No, it's like I need to pre-end it. The hindsight of this may be working. We'll see in next five to 10 years.

54:18 Much flatter org. Much flatter org. Smart teams. It works for us, might not work for all the companies. There are some parts where go-to-market, we still are trying to figure out what's the best way. But smaller teams, flatter org.

54:30 I think there are two paradigms, but generally people being more technical, or if not technical, even in non-technical teams, having a technical resource. We will have a person in ops or in talent that will… We have effectively a tech lead for that team that helps them automate a lot of that work and helps up-level the rest of the team, too.

54:50 There are two parts that are helping. Talk me through this in talent or something like that. Is it that you are building your own software where other companies might have bought software, like a Workday or a Greenhouse or something? Is it that they are using the existing software you have better?

55:08 Is the process that will be spreadsheets in a traditional company are built with software? How do you use the software in these organizations? Sometimes, but we still use a lot of the traditional vendors. One pattern is, of course, LLM-ifying everything,

55:24 making the data explorable for you to be able to interact with it of who's in the pipeline, what worked, who does the best references, all of that work, so you can double down on that. Two, it's frequently things that you manually do that a lot of the… There's a gap between where the agents are today versus what you could do if

55:44 you have the technical skill set. A good example is, how do you scrape all the right profiles to be able to reach out to the right candidates? You analyze whether it's… I don't know how much I want to say, but try to detect specific

56:00 things that we know worked. You bring that across to the people. On go-to-market side, there's just so many things you can do with additional amplifiers. It goes from understanding what case studies are relevant and creating a good

56:18 pre-read for you before you go to the meeting through creating the AI SDR experience that we spoke about, to creating an entire deck experience. You have a pre-populated deck with the right numbers that is customized to that customer, which you want still the person to go through and develop, but ultimately is in there.

56:36 There are plenty of those additional things that you know will amplify the work of the people around, potentially replace some of those easier tasks that are done. Then we wanted for people to explore the culture at ElevenLabs. We created a voice agent that people can speak with and see what's the culture,

56:53 but also get prepped for the interviews. I think across many of those teams, additional benefit of what they can do. Interesting piece. Of course, in Ukraine, we're doing ongoing work. They need to rethink a lot of how their development, their systems, their support,

57:08 works for the citizens across the country. People that are in the war zone, they don't have the same access to the information. They cannot rely on the same phone lines. They cannot rely on the same physical services around the country. They've developed effectively a central—

57:22 Is it your employees in the Ukraine? We had a few, but they reached out because they were developing their central map called DIIA. They developed it over the years, but now before, they were doubling down on how this can be a way of supporting the citizens.

57:39 Of course, there's an easy part of how you create a first agentic government where you have a help with the benefits and what's happening on the front line or education. That's delivered to everyone. Or healthcare, so you can book your checkup or appointment.

57:52 How you create all of that. Of course, we travel to Kyiv, we worked with them on bringing that and making that available for voice so everybody can access it. But the thing we've learned while being there was that model of what we speak about where you have technical resources in each of the teams, they actually have

58:09 the same in every of the ministries. Every ministry had technical resources working on creating that agentic version of their work. Then it was a central digital transformation team that would assemble this all together to deliver that through the central citizen support,

58:24 which I thought was brilliant. That's very tech-forward by Ukraine. So tech-forward. The most advanced set of work we've seen. We got a little bit validated. Maybe technical resources in each of the teams is a good idea.

58:36 That works heavily for us. You mentioned some of the other parts, like do you hire the senior or younger... Main thing we try to filter for, of course, the culture piece is so important. You could scale people, but scaling culture is much harder.

58:51 You want to optimize for that being right. In our case, it's first principles, taking ownership, striving for excellence but staying humble. The main thing that's in that ownership part that I think works well for the AI world is agency.

59:04 If you have that agency to explore, regardless of where you are in the experience cycle, it's going to be a tremendous amplifier to your work. My biggest takeaway from all this has been that around agency, where I feel like high-agency people are the winners of the advances in AI, and within organizations, low-agency people will lose out.

59:28 Yeah, completely agree. It's probably the most proud thing that Piotr and I are as we scaled ElevenLabs, the people that are at ElevenLabs, it's been just the culture and seeing the expansion of the culture, where culture builds the company now rather than any single person or any

59:44 single product builds the company. That is probably the biggest validation and happiness. There's the other angle of that where I think people are striving to be incredible in their craft and their work, but at the same time have fun in a lot their work. That combination of agency and just enjoying what you do is

01:00:05 probably the best thing we've been able to do today at ElevenLabs. It sounds like a really fun stage, like we were saying. Interesting research breakthroughs, really fast-growing business. I'm sure you're enjoying it. Mati, thank you. John, thank you so much.
