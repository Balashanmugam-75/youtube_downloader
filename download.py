from os import path
from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil


def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    get_link = link_field.get()
    user_path = path_label.cget("text")
    screen.title('Downloading....')
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4_video)
    video_clip.close()
    shutil.move(mp4_video,user_path)
    screen.title('Download Complete!')

screen = Tk()
title = screen.title('Youtube Downloader')
canvas = Canvas(screen,width=500,height=500)
canvas.pack()

logo_img = PhotoImage(file="ytlogo.png")
logo_img = logo_img.subsample(2,2)
canvas.create_image(250,80,image=logo_img)

link_field = Entry(screen,width = 50)
link_label = Label(screen,text = "ENTER THE VIDEO LINK ",font = ('Bold',15))

path_label = Label(screen,text = "SELECT PATH FOR DOWNLOAD",font = ('Bold',15))
button2 = Button(screen,text = "Select",command = select_path)

canvas.create_window(250,280,window = path_label)
canvas.create_window(250,330,window = button2)

canvas.create_window(250,170,window = link_label)
canvas.create_window(250,220,window = link_field)

button1 = Button(screen,text = "Download File",command = download_file)
canvas.create_window(250,390,window = button1)

screen.mainloop()
