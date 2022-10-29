import urllib
from bs4 import BeautifulSoup
from pytube import YouTube
import cv2
import os
import glob

def get_urls(text, limit=10):
    query = urllib.parse.quote(text)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    urls = []
    for i, vid in enumerate(soup.findAll(attrs={'class':'yt-uix-tile-link'})):
        if i < limit:
            urls.append('https://www.youtube.com' + vid['href'])
    print(f"Found {len(urls)} video links for {text}")
    return urls

def download_video(url, path=None, max_duration=10):
      try:
        yt = YouTube(url)
        duration = int(yt.player_config_args['player_response']['streamingData']['formats'][0]['approxDurationMs'])
        if duration < max_duration*60*1000:
            yt = yt.streams.filter(file_extension='mp4').first()
            out_file = yt.download(path)
            file_name = out_file.split("\\")[-1]
            print(f"Downloaded {file_name} correctly!")
        else:
            print(f"Video {url} too long")
    except Exception as exc:
        print(f"Download of {url} did not work because of {exc}...")

def extract_images_from_video(video, folder=None, delay=30, name="file", max_images=20, silent=False):    
    vidcap = cv2.VideoCapture(video)
    count = 0
    num_images = 0
    if not folder:
        folder = os.getcwd()
    label = max_label(name, folder)
    success = True
    fps = int(vidcap.get(cv2.CAP_PROP_FPS))
    
    while success and num_images < max_images:
        success, image = vidcap.read()
        num_images += 1
        label += 1
        file_name = name + "_" + str(label) + ".jpg"
        path = os.path.join(folder, file_name)
        cv2.imwrite(path, image)
        if cv2.imread(path) is None:
            os.remove(path)
        else:
            if not silent:
                print(f'Image successfully written at {path}')
        count += delay*fps
        vidcap.set(1, count)
