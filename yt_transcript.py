import sys
from youtube_transcript_api import YouTubeTranscriptApi

link = input("Enter video id: ")
transcript = YouTubeTranscriptApi.get_transcript(link)

og_stdout = sys.stdout
with open('transcript.txt', 'w') as f:
    sys.stdout = f
    print(transcript)
    sys.stdout = og_stdout