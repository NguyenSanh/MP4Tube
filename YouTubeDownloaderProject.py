# Preconditons: Install moviepy and pytube to your local system.

# Import tkinter framework to create GUI elements in Python
# Import moviepy and pytube
# Import shutil (not external, already built into the  Python Standard Library)
from tkinter import *
from tkinter import filedialog
from tkinter.tix import IMAGETEXT
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil 

# Functions
def select_pathLocation():
    # Allows user to ask directory and select download path in explorer
    path = filedialog.askdirectory()
    # Changes path_label to the display specified path 
    path_label.config(text=path)

def download_file():
    # Fetch user path
    fetch_link = link_field.get()

    # Fetch selected path location
    user_path = path_label.cget('text')
    screen.title('Download commencing')

    # Download
    mp4_video = YouTube(fetch_link).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4_video)
    video_clip.close()

    # Move te file into a specified directory
    shutil.move(mp4_video, user_path)
    screen.title('Your download is complete! Paste another video link to download.')


# Create instance of Tk class, initialize toplevel window for application
screen = Tk()  
title = screen.title('YouTube to MP4')
# Initialize the app's canvas
canvas = Canvas(screen, width = 600, height = 600)
canvas.pack()

# Set image for logo
image_logo = PhotoImage(file = 'logo.png')
image_logo = image_logo.subsample(5, 5)

# Display 'image_logo' in canvas with exact coordinates 
canvas.create_image(250, 80, anchor = 'center', image = image_logo)


# Link Field
link_field = Entry(screen, width = 50)  # Create field to insert our link
link_label = Label(screen, text = 'Paste Link to YouTube Video', font = ('Verdana', 17)) # Create label as a description
# Add these widgets  for link to canvas
canvas.create_window(250, 170, window = link_label)
canvas.create_window(250, 220, window = link_field)


# Choose a Path Destination For Saving File
path_label = Label(screen, text='Choose Location', font = ('Verdana', 17))
select_btn = Button(screen, text='Select Download Location', command = select_pathLocation)
# Add widgets to canvas
canvas.create_window(250, 280, window = path_label)
canvas.create_window(250, 330, window = select_btn)


# Button (download)
# Button need a command to link an action from the download_file() function
download_btn = Button(screen, text = 'Download File', command = download_file)
# Add download button widget to canvas
canvas.create_window(250, 390, window = download_btn)



screen.mainloop()
