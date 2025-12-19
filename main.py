"""
Punto de entrada de la aplicación Conversor Universal a PDF.
Asegúrese de tener instaladas las dependencias:
pip install customtkinter fpdf python-docx
"""

from gui.app_ui import ConversorApp

def main():
    app = ConversorApp()
    app.run()

if __name__ == "__main__":
    main()