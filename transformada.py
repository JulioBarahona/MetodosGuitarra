# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 17:57:15 2017

@author: Julio
"""
from easygui import *
from variables import *
from functions import *

def Proyecton():
    #GUI principal
    msgbox(welcome,appTitle)
    flag = True
    while(flag):
        button = buttonbox (instructionsTuner, appTitle, guitarStrings)
        if (button == "Salir"):
            flag = False
        else:
            transform(button)
    msgbox(goodbye, appTitle)

def transform(string):
    msgbox(recordingInstructions,string)
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
        msgbox(pitchtoohigh + " " + str(pitch) + " Hz", appTitle)
        transform(string)
    # if the pitch is too low it will tell
    elif(pitch+5 < tune):
        msgbox(pitchtoolow + " " + str(pitch) + " Hz", appTitle)
        transform(string)
    #it the pitch isnt too high or too low then its ready to go
    else:
        msgbox(pitchIsGood, appTitle)