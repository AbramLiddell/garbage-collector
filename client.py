from asyncio.windows_events import NULL
import csv
import time
import os
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image  
from pynput import keyboard
import server

global timestatus
global writer
global starttime
global csvfile
global start_recording_hk
global create_timestamp_hk

timestatus = True
starttime = 0



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Note to Jeffery, Insert Intelligable Comment Later
obsLocation = os.path.expanduser("~") + "\Videos"
outputLocation = os.path.expanduser("~") + "\Videos"

start_recording_hk = "<ctrl>+<alt>+r"
create_timestamp_hk = "<ctrl>+<alt>+h"



#Directory for the program and it's assets
curDir = str(os.path.dirname(os.path.abspath(__file__)))
assDir = curDir + "/UI assets"

# creates the timestamp with time.time() python module
def create_timestamp():
    global timestatus
    global writer

    try:
        currenttime = time.time()
        print('Record status: ' + str(timestatus) + ", Time: " + str(currenttime) + ".")
        writer.writerow({'Timestamp': currenttime, 'Status': timestatus})

        if timestatus == True:
            timestatus = False
        elif timestatus == False:
            timestatus = True
    except:
        print("An error occured. Please try starting recording before creating timestamps. You Dumbass")

# writes stop line in .csv file and closes file for program cease protocol
def on_exit():
    global writer
    global csvfile
    currenttime = time.time()
    writer.writerow({'Timestamp': currenttime, 'Status': 'Stopped_Recording'})
    csvfile.close()
    print("CSV file closed.")

# sets a line indicating start of recording - to be taken over later by a button instead of a hotkey
def set_starttime():
    global starttime
    global writer
    global csvfile
    if starttime != 0:
        on_exit()
    else:
        csvfile = open('timestamps.csv', 'w', newline='')
        fieldnames = ['Timestamp', 'Status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        starttime = time.time()
        writer.writeheader()
        writer.writerow({'Timestamp': starttime, 'Status': 'Start_Recording'})
        print('Started recording at', starttime)

    
# don't know what this does - stole it from internet
def for_canonical(f):
    return lambda k: f(l.canonical(k))



def entChange(ent, newText=""):
    ent.config(state="normal")
    ent.delete(0, tk.END)
    ent.insert(0, newText)
    ent.config(state="readonly")


#Functions for browsing directories, two instead of one because cannot parse variables through tkinter buttons it seems
def obsLocationBrowse(): #Basically copied from https://stackoverflow.com/questions/43516019/python-tkinter-browse-folder-button 
    global obsLocation
    fileName = filedialog.askdirectory()
    obsLocation = fileName
    entChange(ent_obsLocation, fileName)

def outputLocationBrowse(): #Basically copied from https://stackoverflow.com/questions/43516019/python-tkinter-browse-folder-button 
    global outputLocation
    fileName = filedialog.askdirectory()
    obsLocation = fileName
    entChange(ent_outputLocation, fileName)    

''''
#Functions for setting keybinds, two instead of one because cannot parse variables through tkinter buttons it seems
def startKeybindListen():
    global start_recording_hk
    entChange(ent_startKeybind)
    with keyboard.Listener(
            on_press=onPress,
            on_release=onRelease    ) as listener:
        listener.join()
'''
    
def killSettings():
    tk.destroy(window)

def settingsWindow():
        
    #Creating the tkinter window and setting some shit
    global window
    window = tk.Tk()                            #Basically learnt tkinter from https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter while doing this, so alot copied from there
    window.title("Garbage Collector")
    window.iconbitmap(os.getcwd() + r"\assets\logoTiny.ico")



    #loading images
    logoImage = Image.open(os.getcwd() + r"\assets\logo2.png")
    logoDraw = ImageTk.PhotoImage(logoImage)

    #logo being created as a label
    lbl_logo = tk.Label(master=window, image=logoDraw)
    lbl_logo.pack()


    #Frame including everything for user selecting obs output directory
    frm_obsLocation = tk.Frame(master=window, relief=tk.RAISED, width=300)
    frm_obsLocation.pack()
    #Label for directory
    lbl_obsLocation = tk.Label(master=frm_obsLocation, text="Obs Output Directory:")
    lbl_obsLocation.pack(side=tk.LEFT)
    #Entry for directory
    global ent_obsLocation
    ent_obsLocation = tk.Entry(master=frm_obsLocation, width=50)
    ent_obsLocation.pack(side=tk.LEFT)
    ent_obsLocation.insert(0, obsLocation)
    ent_obsLocation.config(state="readonly")
    #Button for browsing directories for obs output location
    btn_obsLocation = tk.Button(master=frm_obsLocation, text="Browse Files", command=obsLocationBrowse)
    btn_obsLocation.pack(side=tk.LEFT)


    #Frame including everything for user selecting final video output directory
    frm_outputLocation = tk.Frame(master=window, relief=tk.RAISED, width=300)
    frm_outputLocation.pack()
    #Label for directory
    lbl_outputLocation = tk.Label(master=frm_outputLocation, text="Edited Video Output Directory:")
    lbl_outputLocation.pack(side=tk.LEFT)
    #Entry for directory
    global ent_outputLocation
    ent_outputLocation = tk.Entry(master=frm_outputLocation, width=50)
    ent_outputLocation.pack(side=tk.LEFT)
    ent_outputLocation.insert(0, obsLocation)
    ent_outputLocation.config(state="readonly")
    #Button for browsing directories for obs output location
    btn_outputLocation = tk.Button(master=frm_outputLocation, text="Browse Files", command=outputLocationBrowse)
    btn_outputLocation.pack(side=tk.LEFT)


    #Label to describe the next section
    lbl_startDescription = tk.Label(master=window, text="This keybind will be used to start and stop the 'recording', this should be set the same as your obs or equivilant start and stop recording keybind")
    lbl_startDescription.pack()
    #Frame including everything for user selecting their keybind to start the program
    frm_startKeybind = tk.Label(master=window)
    frm_startKeybind.pack()
    #Label for keybind
    lbl_startKeybind = tk.Label(master=frm_startKeybind, text="Start/Stop Recording Keybind:")
    lbl_startKeybind.pack(side=tk.LEFT)
    #Entry for keybind
    global ent_startKeybind
    ent_startKeybind = tk.Entry(master=frm_startKeybind, width=20)
    ent_startKeybind.pack(side=tk.LEFT)
    ent_startKeybind.insert(0, start_recording_hk)
    ent_startKeybind.config(state="readonly")

    #Button to listen for keys
    #btn_startKeybind = tk.Button(master=frm_startKeybind, text="Set Keybind", command=startKeybindListen)
    #btn_startKeybind.pack(side=tk.LEFT)


    #Label to describe the next section
    lbl_timestamptDescription = tk.Label(master=window, text="This keybind will be used to place a time stampt where you would like to start/stop recording a clip")
    lbl_timestamptDescription.pack()
    #Frame including everything for user selecting their keybind to start the program
    frm_timestamptKeybind = tk.Label(master=window)
    frm_timestamptKeybind.pack()
    #Label for keybind
    lbl_timestamptKeybind = tk.Label(master=frm_timestamptKeybind, text="Place Timestamp Keybind:")
    lbl_timestamptKeybind.pack(side=tk.LEFT)
    #Entry for keybind
    global ent_timestamptKeybind
    ent_timestamptKeybind = tk.Entry(master=frm_timestamptKeybind, width=20)
    ent_timestamptKeybind.pack(side=tk.LEFT)
    ent_timestamptKeybind.insert(0, create_timestamp_hk)
    ent_timestamptKeybind.config(state="readonly")  

    btn_ready = tk.Button(master=window, text="Ready", command=killSettings)
    
    tk.mainloop()

    return obsLocation, outputLocation, start_recording_hk, create_timestamp_hk


# defines hotkeys and the functions that are called when they're triggered
hotkey = keyboard.HotKey(
    keyboard.HotKey.parse(create_timestamp_hk),
    create_timestamp)
hotkey = keyboard.HotKey(
    keyboard.HotKey.parse(start_recording_hk),
    set_starttime)

settingsWindow()
#window.wm_attributes("-topmost", 1)


# hotkey function
with keyboard.GlobalHotKeys({
        create_timestamp_hk: create_timestamp,
        start_recording_hk: set_starttime}) as l:
    l.join()

#server.main()