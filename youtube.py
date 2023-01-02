import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import filedialog, messagebox
def wid():
    link = Label(root,text="YouTube URL:", font= "arial 14 ",bg="#D9BD1D")
    link.grid(row=1,column=0,padx=5,pady=5)

    root.linktext= Entry(root,width=70,textvariable=video_link)
    root.linktext.grid(row=1, column=1, padx=5, pady=5)

    brows = Label(root,text="Select Path:", font= "arial 14 ",bg="#D9BD1D")
    brows.grid(row=2,column=0,padx=5,pady=5)

    root.browstext= Entry(root,width=50,textvariable=path)
    root.browstext.grid(row=2, column=1, padx=3, pady=3)

    browsbutt= Button(root, text="Browse ",font="arial 12 " ,width=10,bg="#4FF036",command=browse)
    browsbutt.grid(row=2,column=2,padx=3,pady=3)



    downbut= Button(root,text="Download Video", font="arial 12", command="",bg="#4FF036",width=25)
    downbut.grid(row=3,column=1,padx=3, pady=3)
def browse():
    down_dir=filedialog.askdirectory(initialdir="Your dir")

    path.set(down_dir)



root=tk.Tk()
root.geometry('700x150')
root.resizable(0,0)
root.title('YouTube Downloader')
root.config(background="#B2AE94")


video_link = StringVar()
path = StringVar()
wid()
root.mainloop()


