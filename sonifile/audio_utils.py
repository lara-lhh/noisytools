# audio_utils.py

import numpy as np

def cargar_audio(path, samplerate_default=44100):
    with open(path, 'rb') as f:
        datos = np.frombuffer(f.read(), dtype=np.int8)
    datos_audio = datos.astype(np.float32) / 128.0
    samplerate = samplerate_default
    return datos_audio, samplerate

