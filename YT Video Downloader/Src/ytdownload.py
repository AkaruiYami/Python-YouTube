import sys
from pytube import YouTube


def main():
    download_path = r"C:\Users\AkaruiYami\Desktop\Developer\P001\Python 3.10\YouTube2022\YT Video Downloader\Downloads"

    link = sys.argv[1]
    yt = YouTube(link)

    print("Title: ", yt.title)
    print("Author: ", yt.author)

    ytv = yt.streams.get_highest_resolution()
    ytv.download(download_path)

    print("Download Complete!")


if __name__ == "__main__":
    main()
