# audioflux.py

import sys
from ruido import reproducir_ruido
from spectro import espectro
from rich.console import Console

console = Console()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        console.print("[yellow]Uso:[/yellow] python audioflux.py archivo [-s]")
        sys.exit(1)

    archivo = sys.argv[1]
    modo_spectro = "-s" in sys.argv

    if modo_spectro:
        espectro(archivo)
    else:
        reproducir_ruido(archivo)

