import os
import sys
from datetime import datetime

def generar_ruta_salida(ruta_orig, carpeta_destino, incluir_fecha, incluir_sufijo):
    """
    Construye la ruta final del PDF basándose en las opciones seleccionadas.
    Implementa un contador incremental si el archivo ya existe.
    """
    nombre_base = os.path.splitext(os.path.basename(ruta_orig))[0]
    
    if incluir_fecha:
        nombre_base += "_" + datetime.now().strftime("%Y%m%d_%H%M")
    if incluir_sufijo:
        nombre_base += "_CONVERTIDO"
    
    ruta_final = os.path.join(carpeta_destino, f"{nombre_base}.pdf")
    
    # Prevenir sobreescritura
    contador = 1
    while os.path.exists(ruta_final):
        ruta_final = os.path.join(carpeta_destino, f"{nombre_base}_{contador}.pdf")
        contador += 1
        
    return ruta_final

def abrir_carpeta_explorador(ruta):
    """Abre la carpeta de destino en el explorador de archivos según el OS."""
    if sys.platform == "win32":
        os.startfile(ruta)
    elif sys.platform == "darwin": # macOS
        import subprocess
        subprocess.Popen(["open", ruta])
    else: # linux
        import subprocess
        subprocess.Popen(["xdg-open", ruta])