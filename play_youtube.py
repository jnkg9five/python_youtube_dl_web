# play_youtube.py

import tkinter as tk
from tkinter import messagebox
import webbrowser
import re

def is_valid_ytb_url(url):
    #User regex to check if input url is a valid YouTube link
    regex = re.compile(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+')
    return regex.match(url) is not None

def link_submit():
    url = url_entry.get()
    if is_valid_ytb_url(url):
        messagebox.showinfo("Valid YouTube URL entered!, YouTube Webpage will open.")
        #open webbrowser and play YouTube video.
        webbrowser.open(url)
    else: 
        messagebox.showerror("Invalid YouTube URL. Please enter a valid YouTube URL.")
    
# Create the input prompt window
root = tk.Tk()
root.title()

#Create and place window widget
tk.Label(root, text="Enter a valid YouTube URL: ").pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

submit_button = tk.Button(root, text="Submit", command=link_submit)
submit_button.pack(pady=10)

root.mainloop()



