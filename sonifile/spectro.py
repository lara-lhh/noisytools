# spectro.py

from audio_utils import cargar_audio
import numpy as np
import sounddevice as sd
from time import sleep
from rich.console import Console
from rich.live import Live

console = Console()
BLOCK_SIZE = 1024
NUM_BARRAS = 64

def obtener_espectro(bloque):
    ventana = np.hanning(len(bloque))
    bloque = bloque * ventana
    espectro = np.fft.rfft(bloque)
    magnitudes = np.abs(espectro)
    return magnitudes[:NUM_BARRAS]

def dibujar_espectro(magnitudes):
    max_magnitud = np.max(magnitudes) or 1
    niveles = (magnitudes / max_magnitud * 8).astype(int)
    filas = []
    for nivel in range(8, 0, -1):
        fila = ""
        for barra in niveles:
            fila += "▇" if barra >= nivel else " "
        filas.append(fila)
    return "\n".join(filas)

def espectro(path):
    datos_audio, samplerate = cargar_audio(path)
    console.print(f"\n Archivo: [bold green]{path}[/bold green]")
    console.print(f" Reproduciendo {len(datos_audio) / samplerate:.2f} segundos de ruido\n")
    sd.play(datos_audio, samplerate=samplerate)

    with Live(console=console, refresh_per_second=20) as live:
        for i in range(0, len(datos_audio) - BLOCK_SIZE, BLOCK_SIZE):
            bloque = datos_audio[i:i + BLOCK_SIZE]
            visual = dibujar_espectro(obtener_espectro(bloque))
            live.update(f"[bold cyan]Espectro[/bold cyan]\n{visual}")
            sleep(0.03)

    sd.wait()
    

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        console.print("[yellow]Uso:[/yellow] python spectro.py archivo")
    else:
        espectro(sys.argv[1])

