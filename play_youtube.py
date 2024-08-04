# play_youtube.py

import webbrowser
import re

def is_valid_ytb_url(url):
    #User regex to check if input url is a valid YouTube link
    regex = re.compile(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+')
    return regex.match(url)

def get_ytb_link():
    while True:
        url = input("Enter a valid YouTube URL: ")
        if is_valid_ytb_url(url):
            return url
        else:
            print("This is an invalid YouTube URL. Try again.")

def play_ytb_video(url):
    webbrowser.open(url)

def main():
    #prompt user to enter a valid YouTube URL.
    url = get_ytb_link()
    #open webbrowser and play YouTube video.
    play_ytb_video(url)
    print("Playing YouTube Video: ")

if __name__ == "__main__":
    main()