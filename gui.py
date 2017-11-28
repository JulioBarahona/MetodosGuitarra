# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 17:45:39 2017

@author: Julio
"""
from functions import *
from easygui import *
from variables import *
from transformada import *

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
    msgbox(goodbye,appTitle)

Proyecton()