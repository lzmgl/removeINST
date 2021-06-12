import soundfile as sf
import os
import numpy as np

data, samplerate = sf.read('audio.wav')
quat = len(data)/4
y = data[:round(quat)]
sf.write('audio_cut.wav',y,samplerate)