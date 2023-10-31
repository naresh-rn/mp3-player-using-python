from tkinter import *
import tkinter as tk
from tkinter import ttk,filedialog
import fnmatch
import os
from pygame import mixer

root = tk.Tk()
root.title("Music Player")
root.geometry('600x400')
root.configure(bg="#A8d6d3")
root.resizable(False,False)

rootpath = 'D:\musix'   #songs folder
pattern = "*.mp3"       #data formate
mixer.init()

def select():
    label.config(text=list_box.get("anchor"))
    mixer.music.load(rootpath + "//" + list_box.get("anchor"))
    mixer.music.play()

def previou_song():
    next_song = list_box.curselection()
    next_song = next_song[0] - 1
    next_song_name = list_box.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(rootpath + "//" + next_song_name)
    mixer.music.play()

    list_box.select_clear(0, "end")
    list_box.activate(next_song)
    list_box.select_set(next_song)

def next_song():
    next_song = list_box.curselection()
    next_song = next_song[0] + 1
    next_song_name = list_box.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(rootpath + "//" + next_song_name)
    mixer.music.play()

    list_box.select_clear(0, "end")
    list_box.activate(next_song)
    list_box.select_set(next_song)

def pause_song():
    if pause["text"] == " | | ":
        mixer.music.pause()
        pause["text"] = "play"
    else:
        mixer.music.unpause()
        pause["text"] = " | | "

def open_folder():
    path=filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
        # print(songs)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)

def stop():
    mixer.music.stop()
    list_box.select_clear('active')

list_box = tk.Listbox(root,fg='cyan',bg="black",width=75,font = ('Clarendon Condensed',10))

list_box = tk.Listbox(root,fg="#57a49c",bg="white",width=75,font = ('Clarendon Condensed',10,"bold"),borderwidth=0)
list_box.pack(padx = 45,pady=45)

label = tk.Label(root,text="",bg="#A8d6d3",fg="#33766f",font=('Clarendon Condensed',12,"bold"))         #33766f
label.pack(padx=10)


top = tk.Frame(root,bg="#A8d6d3")
top.pack(padx = 30, pady=25,anchor = 'center')


class PhotoImage:
    pass

play_button=tk.PhotoImage(file="C://Users//user//PycharmProjects//codes of pythons//plaay.png")

play = tk.Button(root,text="Play",bg="#c9d6ff",font=("Britannic Bold",10),command=select)
play.pack(padx=15,in_=top,side="left")
previous = tk.Button(root,text=" < ",bg="#acb6e5",font=("Britannic Bold",10,'bold'),command=previou_song)
previous.pack(padx=15,in_=top,side="left")
pause = tk.Button(root,text=" | | ",width=3,fg="black",bg="#a1c4fd",font=("Britannic Bold",10,'bold'),command=pause_song)
pause.pack(padx=15,in_=top,side="left")
next_ = tk.Button(root,text=" > ",bg="#acb6e5",font=("Britannic Bold",10,'bold'),command=next_song)
next_.pack(padx=15,in_=top,side="left")
stop = tk.Button(root,text="Stop",bg='#c9d6ff',font=("Britannic Bold",10),command=stop)
stop.pack(padx=15,in_=top,side="left")

for roott,dirs,files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        list_box.insert("end",filename)

root.mainloop()