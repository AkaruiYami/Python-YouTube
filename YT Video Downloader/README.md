# YouTube Video Downloader

In this project, we going to create a program that can download a video from YouTube by giving it the link to that particular video.

Before we started, make sure that we are using Python 3.4 or newer since we are oing to use `pathlib` which is a library available for Python 3.4 and higher.

We also need to install `pytube` using `pip install pytube`.

## Setting Up The Project

First, create a folder called `Downloads` in our project folder. This will ber the location where we goint to save our video later on.

Then, we going to create a variable to hold the location for our download folder as below:

```python
from pathlib import Path

download_path = Path(__file__).parents[1].joinpath("Downloads")
```

## Pass Arguments Through CMD / Console

Instead of asking the user for input after running the code, why not we accept the input when we about to run the code.

Normally, when we going to run our code, we will normally type

```
python ytdownload.py
```

and then our code will run. We can actually pass arguments to it when we about to run our code as below:

```
python ytdownload.py link1
```

As shown above, we pass 1 arguments which is link1. To access the argument, we need to import `sys`

```python
import sys
link = sys.argv[1]
```

Notice that we took from index 1 and not 0. This is because, `sys.argv[0]` is the file name.

## Download the Video

Since we already able to obtain the link to the video that we want to download, now we can initialize the YouTube object using YouTube class from `pytube`.

```python
yt = YouTube(link)

print("Title: ", yt.title)
print("Author: ", yt.author)

ytv = yt.streams.get_highest_resolution()
ytv.download(download_path)

print("Download Complete!")

```

As shown above, we first create a YouTube object by giving it the link to our YouTube video. We then able to get information about our video, for example, here we get the title of the video ad also the author.

To download the video, we first need to get the video stream which in this project, we get the highest resolution and then we use method `download` and give the folder path to where we want that video to be store.
