from pytube import YouTube


if __name__ == "__main__":

    #ask for the link from user
    link = input("Enter the link of YouTube video you want to download:  ")
    yt = YouTube(link)

    #Showing details
    print("Title: ",yt.title)
    print("Number of views: ",yt.views)
    print("Length of video: ",yt.length)
    print("Rating of video: ",yt.rating)

    # Get Captions
    caption = yt.captions
    f = open("captions.txt", "a")
    f.write(caption.generate_srt_captions())
    f.close()
    print(caption.generate_srt_captions())

    #Getting the highest resolution possible
    ys = yt.streams.get_highest_resolution()

    #Starting download
    print("Downloading...")
    #ys.download("/Volumes/WD_BLACK/Lex")
    ys.download()
    print("Download completed!!")

def get_captions():
    #ask for the link from user
    link = input("Enter the link of YouTube video you want to download:  ")
    yt = YouTube(link)

    #Showing details
    print("Title: ",yt.title)
    print("Number of views: ",yt.views)
    print("Length of video: ",yt.length)
    print("Rating of video: ",yt.rating)

    # Get Captions
    caption = yt.captions.get_by_language_code('en')
    f = open("captions.txt", "a")
    f.write(caption.generate_srt_captions())
    f.close()
    print(caption.generate_srt_captions())