from pytube import YouTube

if __name__ == "main":
    link = input("Enter the link: ")
    yt = YouTube(link)
    ys=yt.streams.get_highest_resolution()
    ys.download('/Volumes/WD_BLACK/Lex')