import soundfile as sf
import os
import numpy as np

data, samplerate = sf.read('audio.wav')
n = len(data)/4
result = [data[i * round(n):(i + 1) * round(n)] for i in range((len(data) + round(n) - 1) // round(n) )] 
for i in range(4):
    print(len(result[i]))
    sf.write(f'audio{i}.wav',result[i],samplerate)