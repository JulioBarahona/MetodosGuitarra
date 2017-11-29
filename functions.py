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
    srateFilt, dataFilt = wav.read("output_filtered.wav")

    NFilt = len(dataFilt)
    X = fft(dataFilt)

    freq = fftfreq(NFilt, 1.0 / srateFilt)
    freq1 = where(freq > 10, freq, 0)

    X1 = where((abs(X) * 2.0 / NFilt) > 0, X, 0)
    X1 = where((abs(X1) * 2.0 / NFilt) < 40, X, 0)

    Xmag = abs(X1) * 2.0 / NFilt

    import operator
    index, value = max(enumerate(Xmag), key=operator.itemgetter(1))
    Value_1 = freq1[index]
    Xmag[index] = 0

    index1, value1 = max(enumerate(Xmag), key=operator.itemgetter(1))
    Value_2 = freq1[index1]
    Xmag[index1] = 0

    index2, value2 = max(enumerate(Xmag), key=operator.itemgetter(1))
    Value_3 = freq1[index2]

    freq_values = [Value_1, Value_2, Value_3]

    index9, value9 = max(enumerate(freq_values), key=operator.itemgetter(1))

    HF = value9
    freq_values[index9] = 0

    index9, value9 = max(enumerate(freq_values), key=operator.itemgetter(1))
    LF = value9

    tunePlayed = HF
    return tunePlayed
