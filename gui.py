import tkinter as tk
from tkinter import filedialog
import os
from PIL import ImageTk, Image
from pynput import keyboard





#Note to Jeffery, Insert Intelligable Comment Later
obsLocation = os.path.expanduser("~") + "\Videos"
outputLocation = os.path.expanduser("~") + "\Videos"

start_recording_hk = "<ctrl>+<alt>+r"
create_timestamp_hk = "<ctrl>+<alt>+h"



#Directory for the program and it's assets
curDir = str(os.path.dirname(os.path.abspath(__file__)))
assDir = curDir + "/UI assets"



def entChange(ent, newText=""):
    ent.config(state="normal")
    ent.delete(0, tk.END)
    ent.insert(0, newText)
    ent.config(state="readonly")
'''
2
# don't know what this does - stole it from internet
def for_canonical(f):
    return lambda k: f(l.canonical(k))

# defines hotkeys and the functions that are called when they're triggered
hotkey = keyboard.HotKey(
    keyboard.HotKey.parse(create_timestamp_hk),
    create_timestamp)
hotkey = keyboard.HotKey(
    keyboard.HotKey.parse(start_recording_hk),
    set_starttime)

# hotkey function
with keyboard.GlobalHotKeys({
        create_timestamp_hk: create_timestamp,
        start_recording_hk: set_starttime}) as l:
    l.join()


'''
'''
def onPress(key):
    print(key)
    print(key=="'1'")

def onRelease(key):
    print(key, "released")
    return False
'''

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


# #Functions for setting keybinds, two instead of one because cannot parse variables through tkinter buttons it seems
# def startKeybindListen():
#     global start_recording_hk
#     entChange(ent_startKeybind)
#     with keyboard.Listener(
#             on_press=onPress,
#             on_release=onRelease    ) as listener:
#         listener.join()
    
    


def settingsWindow():
        
    #Creating the tkinter window and setting some shit
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

    window.mainloop()                           #Stops code from progressing until either the 'start' button is pressed or the start keybind is used

    return obsLocation, outputLocation, start_recording_hk, create_timestamp_hk

settingsWindow()
#window.wm_attributes("-topmost", 1)