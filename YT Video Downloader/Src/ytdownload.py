import sys
from pathlib import Path
from pytube import YouTube


def main():
    download_path = Path(__file__).parents[1].joinpath("Downloads")

    link = sys.argv[1]
    yt = YouTube(link)

    print("Title: ", yt.title)
    print("Author: ", yt.author)

    ytv = yt.streams.get_highest_resolution()
    ytv.download(download_path)

    print("Download Complete!")


if __name__ == "__main__":
    main()
