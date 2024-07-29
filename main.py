#Code by Arnab Sarkar;
import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        YTLink = link.get()
        YTObject = YouTube(YTLink)
        title.configure(text=YTObject.title)
        Video = YTObject.streams.get_highest_resolution()
        title.configure(text=YTObject.title)
        FinishLabel.configure(text="")
        Video.download()
        FinishLabel.configure(text="Arnab has helped you download the file. Download completed!")
    except:
        FinishLabel.configure(text="Download Failed!")

#System settings for Dark Mode and Light Mode:-
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#App frame size width height, etc:-
app = customtkinter.CTk()
app.geometry("800x400")
app.title("Arnab's YouTube Downloader")

#Adding UI elements:-
title = customtkinter.CTkLabel(app, text="Paste the youtube link here!")
title.pack(padx=10, pady=10)

#Link input:-
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=360, height=45, textvariable=url_var)
link.pack()

#Finished Downloading:-
FinishLabel = customtkinter.CTkLabel(app, text="")
FinishLabel.pack()

#Download Button:-
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)


#Running app ipn loop to prevent closing automatically:-
app.mainloop()