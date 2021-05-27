# tutorial: https://towardsdatascience.com/build-a-youtube-downloader-with-python-8ef2e6915d97
# documentation: https://python-pytube.readthedocs.io/en/latest/index.html

# Importing necessary packages
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog


# Function Widgets() to create necessary tkinter widgets

# todo: Check if link is valid. If not, ask for a valid link

def Widgets():
    link_label = Label(root,
                       text="YouTube URL  :",
                       bg="#E8D579")
    link_label.grid(row=1,
                    column=0,
                    pady=5,
                    padx=5)

    root.linkText = Entry(root,
                          width=55,
                          textvariable=video_url)
    root.linkText.grid(row=1,
                       column=1,
                       pady=5,
                       padx=5,
                       columnspan=2)

    destination_label = Label(root,
                              text="Destination    :",
                              bg="#E8D579")
    destination_label.grid(row=2,
                           column=0,
                           pady=5,
                           padx=5)

    root.destinationText = Entry(root,
                                 width=40,
                                 textvariable=download_Path)
    root.destinationText.grid(row=2,
                              column=1,
                              pady=5,
                              padx=5)

    browse_B = Button(root,
                      text="Browse",
                      command=Browse,
                      width=10,
                      bg="#05E8E0")
    browse_B.grid(row=2,
                  column=2,
                  pady=1,
                  padx=1)

    Download_B = Button(root,
                        text="Download",
                        command=Download,
                        width=20,
                        bg="#05E8E0")
    Download_B.grid(row=3,
                    column=1,
                    pady=3,
                    padx=3)


# Defining function browse() to select a destination folder

def Browse():
    # Directory selection.
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")

    # Displaying the directory Path
    download_Path.set(download_Directory)


# Function Download() that downloads the video
def Download():
    # getting user-input (URL)
    Youtube_URL = video_url.get()

    # select the optimal location for
    # saving file's
    download_Folder = download_Path.get()

    # Creating object of YouTube()
    getVideo = YouTube(Youtube_URL)

    # Getting all the available streams
    videoStream = getVideo.streams.first()

    # Downloading the video
    videoStream.download(download_Folder)

    # Displaying the message
    messagebox.showinfo("Download Successful!",
                        "Saved at\n"
                        + download_Folder)


# Creating object of tk class
root = tk.Tk()

# Setting the window's style
root.geometry("600x120")
root.resizable(False, False)
root.title("YouTube Downloader")
root.config(background="#000000")

# Creating the tkinter Variables
video_url = StringVar()
download_Path = StringVar()

# Calling the Widgets() function
Widgets()

# Defining infinite loop to run
# application
root.mainloop()
