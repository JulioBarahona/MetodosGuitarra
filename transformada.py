# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 17:57:15 2017

@author: Julio
"""
from easygui import *
from variables import *

def transform(acorde):
    if(acorde == "E1"):
        msgbox("E1",appTitle)
    elif(acorde == "A"):
        msgbox("A", appTitle)
    elif(acorde == "D"):
        msgbox("D", appTitle)
    elif(acorde == "G"):
        msgbox("G", appTitle)
    elif(acorde == "B"):
        msgbox("B", appTitle)
    elif(acorde == "E2"):
        msgbox("E2", appTitle)
    else:
        print("rekt")
