# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 17:45:39 2017

@author: Julio
"""
from transformada import *
from functions import *

msgbox(welcome,appTitle)

flag = True
while(flag):
    button = buttonbox ("Escoja la cuerda", appTitle, guitarStrings)
    if (button == "Salir"):
        flag = False
    else:
        transform(button)

msgbox(goodbye,appTitle)