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
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 1
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

# con esta funcion se limpia el ruido, tomado del ejemplo dado por aristodon
def filter():
    srate, data = wav.read("output.wav")

    N = len(data)
    X = fft(data)
    X_mag = abs(X) * 2.0 / N

    freq = fftfreq(N, 1.0 / srate)
    plot(freq, X_mag)

    #limpia que tengan una intensidad menor a 350
    X = where((abs(X) * 2.0 / N) > 350, X, 0)
    X_mag = abs(X) * 2.0 / N
    freq = fftfreq(N, 1.0 / srate)
    plot(freq, X_mag)

    # agarra solo la parte imaginaria de los datos
    data2 = real(ifft(X))
    data2 = data2.astype(int16)
    wav.write("output_filtered.wav", srate, data2)