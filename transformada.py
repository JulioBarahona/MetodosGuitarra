# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 17:57:15 2017

@author: Julio
"""
from easygui import *
from variables import *
from functions import *

def transform(acorde):
    #defines the note of the button selected
    nota = tunes[acorde]
    #records audio
    getAudio()
    #filters audio
    filter()
