from tkinter import *
from tkinter import filedialog, Text
from pytube import YouTube
import os
import moviepy.editor as mp
import re
import numpy

app = Tk()
fileSaved = []


def save_music():
    directory = filedialog.askdirectory()
    fileSaved.append(directory)
    print(fileSaved[0])


def download_music():
    youtube_link = link_text.get()
    w = YouTube(youtube_link).streams.first()
    w.download(output_path=fileSaved[0])

    clear_text()


def convert_music():
    tgt_folder = fileSaved[0]
    out_folder = fileSaved[0]

    for file in [n for n in os.listdir(tgt_folder) if re.search('mp4', n)]:
        full_path = os.path.join(tgt_folder, file)
        output_path = os.path.join(
            out_folder, os.path.splitext(file)[0] + '.mp3')
        clip = mp.AudioFileClip(full_path).subclip(
            10,)  # disable if do not want any clipping
        clip.write_audiofile(output_path)

    for file in os.scandir(tgt_folder):
        if file.name.endswith(".mp4"):
            os.unlink(file.path)


def clear_text():
    link_entry.delete(0, END)


# Link
link_text = StringVar()
link_label = Label(app, text='Paste Link', font=('bold', 30), pady=50)
link_label.grid(row=0, column=0, sticky=W)

link_entry = Entry(app, textvariable=link_text, width=100)
link_entry.grid(row=0, column=1, padx=10, pady=20, ipady=6)

# Buttons
save_btn = Button(app, text='Izberi Mapo za shranjevanje',
                  width=50, height=5, command=save_music)
save_btn.grid(row=1, column=1)

add_btn = Button(app, text='Download music', width=50,
                 height=5, command=download_music)
add_btn.grid(row=3, column=1)

add_btn = Button(app, text='Convert music', width=50,
                 height=5, command=convert_music)
add_btn.grid(row=4, column=1)


app.title("Youtube to mp3")
app.geometry("900x450")
app.mainloop()
