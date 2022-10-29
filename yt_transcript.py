import sys
import json
from youtube_transcript_api import YouTubeTranscriptApi

link = input("Enter video id: ")
transcript = YouTubeTranscriptApi.get_transcript(link)

with open('transcript0.json', 'w') as f:
    json.dump(transcript, f)
