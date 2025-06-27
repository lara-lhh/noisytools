# ruido.py

from audio_utils import cargar_audio
import numpy as np
import sounddevice as sd
from time import sleep
from rich.console import Console
from rich.progress import track

console = Console()
BLOCK_SIZE = 1024

def reproducir_ruido(path):
    datos_audio, samplerate = cargar_audio(path)
    console.print(f"\n Archivo: [bold green]{path}[/bold green]")
    console.print(f" Reproduciendo {len(datos_audio) / samplerate:.2f} segundos de ruido\n")
    sd.play(datos_audio, samplerate=samplerate)

    for i in track(range(0, len(datos_audio), BLOCK_SIZE), description="Visualizando..."):
        bloque = datos_audio[i:i + BLOCK_SIZE]
        nivel = int(np.mean(np.abs(bloque)) * 50)
        console.print("▇" * nivel)
        sleep(0.03)

    sd.wait()
    
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        console.print("[yellow]Uso:[/yellow] python ruido.py archivo")
    else:
        reproducir_ruido(sys.argv[1])

