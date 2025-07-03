from flask import jsonify
from pytubefix import YouTube
from pytubefix.cli import on_progress
from datetime import timedelta


def get_data(url):
    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title) 
    print(yt.author)
    print(timedelta(seconds=yt.length))

    return {"title": yt.title,"author": yt.author,"length": str(timedelta(seconds=yt.length))}, 200