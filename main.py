from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('1000x500')
root.resizable(0,0)
root.title("youtube video downloader")
Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()

##enter link
link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 80)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 160)

#function to download video
def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.get_audio_only()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 220)

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 220)

root.mainloop()
