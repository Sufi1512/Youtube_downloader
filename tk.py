from tkinter import *
from pytube import YouTube
root = Tk()

root.geometry('600x300')

root.resizable(0,0)
root.title("YT Downloader")
Label(root,text="YT Downloader", font='arial 26 bold').pack()
link =StringVar()

Label(root,text="Enter your link here", font= 'arial 15 bold').place(x=180,y=70)
enter= Entry(root,width=70,textvariable=link).place(x=32,y=100)
def download():
    url = YouTube(str(link.get()))
    video=url.streams.get_highest_resolution()
    video.download()
    Label(root, text="Downloaded",font='arial 15').place(x=200,y=120)
Button(root,text="Download", font='arial 15 bold',bg="#D98775",padx=3, command=download).place(x=200 ,y= 150)
root.mainloop()