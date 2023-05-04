import pytube
from pytube import YouTube #importing pytube library
from tkinter import *  #importing tkinter for gui


window = Tk()  #creating window and configuring
window.title("ytmp3")
window.geometry("500x500")
window.configure(bg="pink")

#creating needed labels
l1 = Label(window,text="YOUTUBE TO MP3 CONVERTOR",font = ("Arial",20),fg="red",bg="pink")
l1.place(x=100,y=20)
l1a = Label(window,text="URL: ",fg = "red",bg="pink")
l1a.place(x=20,y=70)
l2 = Label(window,text="streams: ",fg = "red",bg="pink")
l2.place(x=20,y=120)
l3 = Label(window,text="enter stream index: ",fg = "red",bg="pink")
l3.place(x=20,y=300)

#creating required entry windows
e1 = Entry(window)
e1.place(x=80,y=70)
e2 = Text(window,height=10,width=40)
e2.place(x=100,y=120)
e3 = Entry(window)
e3.place(x=170,y=300)
e4 = Entry(window)
e4.place(x=120,y=400)

s1 = StringVar()  #variable which stores url

def c1():  #this function downloads video,filters audio and stores it in "vid"
    yt = YouTube(e1.get())

    # streams function to get the different types of ways the video can be streamed(quality)
    # filter - to only filter and get audio
    audio = yt.streams.filter(only_audio=True)

    # enumerate to basically count or give index value to items (as a key)
    vid = list(enumerate(audio))
    for i in vid:
        e2.insert(END, str(i))
        e2.insert(END, "\n")

def c2():  #this function stores the selected type of audio in given destination
    yt = YouTube(e1.get())
    audio = yt.streams.filter(only_audio=True)

    # the item in "audio" stored along with the value entered in "stream"
    audio[stream.get()].download('/Users/jess/Desktop/converted mp3')
    e4.delete(0, END)
    e4.insert(0, "DOWNLOAD SUCCESSFUL !!")

#creating required buttons
b1 = Button(window,text="   ",highlightbackground="red",command=c1)
b1.place(x=300,y=70)
b2 = Button(window,text="   ",highlightbackground="red",command=c2)
b2.place(x=400,y=300)

stream = IntVar()  #stores the chosen option by user
 #binds variable with widget , any change in variable in e3 will update "stream" (so multiple types for one video)
e3.config(textvariable=stream)

window.mainloop()

