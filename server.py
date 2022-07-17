from asyncio.windows_events import NULL
import csv
from multiprocessing.dummy import Array
import time
from pynput import keyboard
import os
import subprocess
import numpy as np
from datetime import datetime, timedelta
import regex as re

def main(obsLocation, outputLocation):
    directory_path = os.getcwd()
    print("Current Directory: " + directory_path)

    # to be changed when gui is set or file handling is better
    filename = "timestamps.csv"
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        timestamp_dict = list(reader)



    timestamp_dict[0]["Timestamp_Absolute"] = 0
    currenttime = 0
    for x in range(len(timestamp_dict)-1):
        timestamp_dict[x+1]["Timestamp_Absolute"] = float(timestamp_dict[x+1]["Timestamp"]) - float(timestamp_dict[x]["Timestamp"])
        
        timestamp_absolutex = timedelta(
            seconds=timestamp_dict[x]["Timestamp_Absolute"],
        )
        timestamp_absolutex1 = timedelta(
            seconds=timestamp_dict[x+1]["Timestamp_Absolute"],
        )

        currenttime = timestamp_dict[x]["Timestamp_Absolute"]+currenttime

        currenttimedelta = timedelta(
            seconds=currenttime
        )
        print(currenttimedelta)

        if (timestamp_dict[x]["Status"] == "False") or (timestamp_dict[x]["Status"] == "Start_Recording"):
            subprocess.call('ffmpeg -i "' + obsLocation + r'\footage.mp4" -ss ' + str(currenttimedelta) + ' -t ' + str(timestamp_absolutex1) + ' -avoid_negative_ts make_zero -vf format=pix_fmts=yuv420p "' + outputLocation + str(x) + '.mp4"')
        elif (timestamp_dict[x]["Status"] == "True"):
            subprocess.call('ffmpeg -i "' + obsLocation + r'\footage.mp4" -ss ' + str(currenttimedelta) + ' -t ' + str(timestamp_absolutex1) + ' -avoid_negative_ts make_zero -vf format=pix_fmts=yuv420p "' + outputLocation + '\deleted\output' + str(x) + '.mp4"')

    for i in range(len(timestamp_dict)):
        print(str(i) + ': ' + str(timestamp_dict[i]))
        

    #for x in range(len(timestamp_dict)):
    #   
