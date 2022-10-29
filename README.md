# LexBot
 LexBot

## Process
Detect images of Lex Fridman
Segment these images 
Deepfake Lex onto:
- his guest
- a real time stream
- onto an app on my phone 

### Correct Pronunciation of "au courant"
- [au courant clip](https://youtube.com/clip/Ugkx45pooOJs7vVvMNgQSBuJchfYoe_x1vXD)
- [real time voice cloning](https://github.com/efwoods/Real-Time-Voice-Cloning?organization=efwoods&organization=efwoods)
- [pytorch voice changing tutorial](https://www.youtube.com/watch?v=12rdn9jazwE)
- [google pronunciation of "au courant"](https://www.google.com/search?q=Au+courant&rlz=1C5CHFA_enUS1010US1010&ei=MRhVY_K9K-elqtsPide5gAc&ved=0ahUKEwiymrKDk_b6AhXnkmoFHYlrDnAQ4dUDCBA&uact=5&oq=Au+courant&gs_lcp=Cgdnd3Mtd2l6EAMyDQgAEIAEELEDEEYQ-QEyEQguEIAEELEDEIMBEMcBEK8BMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6CggAEEcQ1gQQsAM6BQgAEKIEOgcIABAeEKIEOgUIIRCrAkoECEEYAEoECEYYAFCaA1i0HmCXIGgCcAF4AIABeIgBxgKSAQMxLjKYAQCgAQKgAQHIAQjAAQE&sclient=gws-wiz)
- [Lex Fridman & balaji srinivasan](https://www.youtube.com/watch?v=VeH7qKZr0WI)

## Resources
- [playlist](https://www.youtube.com/watch?v=ZFntEFXKDHM&list=PLrAXtmErZgOdP_8GztsuKi9nrraNbKKp4&index=1)
- [C++](https://www.w3schools.com/cpp/)
- [pytorch](https://pytorch.org)
- [tensorflow](https://www.tensorflow.org/)
- [custom gpt-3 chatbot](https://towardsdatascience.com/custom-informed-gpt-3-models-for-your-website-with-very-simple-code-47134b25620b)
- [Modifying emphasis](https://gfx.cs.princeton.edu/pubs/Jin_2017_VTI/Jin2017-VoCo-paper.pdf)

## Digital Necromancy
What I would like to do:
- [x] download video
- [x] download transcript
- [ ] [detect speaker with respect to transcript timestamp](https://www.youtube.com/watch?v=ZLIPkmmDJAc)
  - [tf audio classifier](https://www.tensorflow.org/lite/inference_with_metadata/task_library/audio_classifier)
- [ ] pose estimation
- [ ] object detection (could use to id speaker)
- [ ] personality insights
- [ ] speaker automatic detection (audio/text)
- [ ] audio manipulation of the way things are spoken...

## Omnia
https://www.youtube.com/watch?v=eF-E40pxxbI


## Greatness 

What is great engineering?
- download lex podcast transcripts
- find every reference of "great engineering"
- upload to GPT-3: The definition of great engineering as reffered from the Lex Fridman podcasts. 
- query: What is great engineering?
- (opt): create audio of lex's voice

## Notes: 
- I would like to scale the pipeline to accept a playlist of videos
- I would like to add generative video & audio based off this data
- I would like to host this for others to view/query
- TorchText may help with full phrases

## Question:
What if I just used the entire transcript? I think it would be too long for the OpenAI API. Also, I would like to associate sentiment analysis, video generation, and other data to the response to make the AI seem more life-like. 

### Data Pipeline
#### transcript_greatness.ipynb (the process of grabbing text)
1. youtube_video_to_json_transcript
2. read_json_file (to store it into an object)
3. select a search_term (in this case, looking for references of 'greatness')
4. identify_entries  --- (find where in the video the phrases are mentioned)
5. convert entries to full sentences
6. append entry to prompt of the response of the openai lexbot
7. send a request about the searched_term using openaiAPI


