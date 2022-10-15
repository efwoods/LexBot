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
    #Getting the highest resolution possible
    ys = yt.streams.get_highest_resolution()

    #Starting download
    print("Downloading...")
    ys.download("/Volumes/WD_BLACK/Lex")
    print("Download completed!!")