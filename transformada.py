# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 17:57:15 2017

@author: Julio
"""
from easygui import *
from variables import *
from functions import *

def transform(string):
    msgbox(recordingInstructions,appTitle)
    #defines the note of the button selected
    tune = tunes[string]
    #records audio
    getAudio()
    #filters audio
    filter()

    #gets The Tune playing
    pitch = getTunes()

    #if the pitch is too high it will tell and calls the function again
    if (pitch-5 > tune):
        msgbox(pitchtoohigh + " " + str(pitch), appTitle)
        button = buttonbox("Que desea hacer?", appTitle, tunningOptions)
        transform(string)
    # if the pitch is too low it will tell
    elif(pitch+5 < tune):
        msgbox(pitchtoolow + " " + str(pitch), appTitle)
        button = buttonbox("Que desea hacer?", appTitle, tunningOptions)
        transform(string)
    #it the pitch isnt too high or too low then its ready to go
    else:
        msgbox(pitchIsGood, appTitle)