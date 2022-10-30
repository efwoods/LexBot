# LexBot
## A tribute to the life and work of Lex Fridman.
Inspired by the life and work of Lex Fridman's podcast, you will find here a compendium of AI works based off of his likeness. The purpose of this repository is to serve as tribute, show respect for, and have a bit of fun immortalizing the eloquent yet questionably-human, Lex Fridman. 

Should by some rare chance this is viewed by him, Lex Fridman should know that I give full rights and control over the full lifecycle of this data and any works which may spring tangent off it. The life was yours, and this work should reflect your life as you see fit.

## Table of Contents
 - [Natural Language Processing](#natural-language-processing)

## Future Goals
- [Audio Processing](#audio-processing)
- Visual Recognition
  - Create a classifier to detect images of Lex Fridman 
- Pose Mapping & Movement
  - Create a dataset of Lex Fridman's body position's and movements
- Miscellaneous
  - [Omnia](#inspiration-omnia) 
  - Deepfake Lex onto:
    - his guest
    - a real time stream (mechanically turk as Lex Fridman)
  - [x] download video
  - [x] download transcript
  - [ ] personality insights
  - [ ] 
  - [ ] speaker automatic detection (audio/text)
  - [ ] audio manipulation of the way things are spoken...
  - [ ] [detect speaker with respect to transcript timestamp](https://www.youtube.com/watch?v=ZLIPkmmDJAc)
  - [tf audio classifier](https://www.tensorflow.org/lite/inference_with_metadata/task_library/audio_classifier)
  - Display Lex through an app on my phone 
    - I would like to scale the pipelines here to accept a playlist of videos
    - I would like to add generative video & audio based off of Lex Fridman's data
    - I would like to host this work on a website for others to view/query/experience 

## Audio Processing
### Inspiration: [Searchable Autobiographical Statements](https://www.youtube.com/watch?v=cdiD-9MMpb0) 
How many times do people repeat themselves if given a search of everything they've ever said?
### Process 
  1. ID Lex's voice by audio (use introductions as training for nn)
  2. get timestamps of when Lex speaks
  3. accumulate a compendium of phrases only said by Lex
  4. search for the exact phrase
  5. return the results


## Natural Language Processing 
### Inspiration: Greatness 
How does one leverage GPT-3 & Lex's podcast interviews to answer the question, "What is great engineering?"

- download lex podcast transcripts
- find every reference of "great engineering"
- upload to GPT-3: The definition of great engineering as reffered from the Lex Fridman podcasts. 
- query: What is great engineering?
- (opt): create audio of lex's voice

### [Notebook: NLP.ipynb](NLP.ipynb)

### Process
1. youtube_video_to_json_transcript
2. read_json_file (to store it into an object)
3. select a search_term (in this case, looking for references of 'greatness')
4. identify_entries  --- (find where in the video the phrases are mentioned)
5. convert entries to full sentences (use n entries per found phrase)
6. append entry to prompt of the response of the openai lexbot
7. send a request about the searched_term using openaiAPI


## [Inspiration: Omnia](https://www.youtube.com/watch?v=eF-E40pxxbI)
What is a sentient AI like as imagined by Liv Boeree?