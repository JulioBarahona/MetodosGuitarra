# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 17:34:58 2017

@author: Julio
PyAudio example: Record a few seconds of audio and save to a WAVE file.
"""
from pylab import *
import scipy.io.wavfile as wav
import pyaudio
import wave

#Con esta funcion se obtiene el audio del mic,
#basado en https://stackoverflow.com/questions/35344649/reading-input-sound-signal-using-python
def getAudio():

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 3
    WAVE_OUTPUT_FILENAME = "output.wav"
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)    
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)    
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

# con esta funcion se limpia el ruido, tomado del ejemplo dado por aristondo
def filter():
    srate, data = wav.read("output.wav")

    N = len(data)
    X = fft(data)
    X_mag = abs(X) * 2.0 / N

    freq = fftfreq(N, 1.0 / srate)
    plot(freq, X_mag)

    figure(2)
    X = where(abs(freq) < 1000, X, 0)
    X_mag = abs(X) * 2.0 / N
    plot(freq, X_mag)

    X = where((abs(X) * 2.0 / N) > 5, X, 0)
    X_mag = abs(X) * 2.0 / N
    freq = fftfreq(N, 1.0 / srate)
    plot(freq, X_mag)

    # agarra solo la parte imaginaria de los datos
    data2 = real(ifft(X))
    data2 = data2.astype(int16)
    wav.write("output_filtered.wav", srate, data2)

    plot(data2)


def getTunes():
    # convierte el archivo en una lista para poder ser analizado
    srate, data = wav.read("output_filtered.wav")

    # convierte los datos en una lista de datos obtenisods
    n = len(data)
    x = fft(data)

    # convierte los datos en valores absolutos
    x_mag = abs(x) * 2.0 / n

    # se obtiene la transformada de fourier rapida de los datos
    freq = fftfreq(n, 1.0 / srate)

    # se separa en partes iguales la marcacion del numero para poder saber cuales fueron de primero
    datoPorNumero = np.split(data, 8)

    # se prepara una lista para almacenar los datos de la transformada
    nList = []
    xList = []

    # lsita de magnitdes
    x_magList = []

    # lista de frecuencias
    freqList = []

    for i in range(8):
        nList.append(len(datoPorNumero[i]))
        xList.append(fft(datoPorNumero[i]))
        x_magList.append(abs(xList[i]) * 2.0 / nList[i])
        freqList.append(fftfreq(nList[i], 1.0 / srate))

    numeroDeTelefono = ""

    for i in range(8):

        for j in range(len(x_magList[i])):
            if (x_magList[i][j] > 25):
                if (freqList[i][j] > 0):
                    if (freqList[i][j] < 1000):
                        inferior = freqList[i][j]
                    if (freqList[i][j] > 1000):
                        superior = freqList[i][j]
                        numeroDeTelefono = numeroDeTelefono + str(frecuencia(inferior, superior))

    print("El numero ingresado fue: " + numeroDeTelefono)
