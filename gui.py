# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 17:45:39 2017

@author: Julio
"""
from transformada import *
from input import *

msgbox("Afinador de guitarra usando transformada de Fourier: \n    Julio Barahona \n    Jorgue Suchite  \n    Kevin Muñoz \n    Fernando Hernandez",
      appTitle )

flag = True
while(flag):
    button = buttonbox ("Escoja la cuerda", appTitle, guitarStrings)
    if (button ==  "E1"):
        transform(button)
    if (button == "Salir"):
        flag = False

msgbox("Gracias por usar el afinador de guitarras",appTitle )