import os
from fpdf import FPDF

def procesar_txt(ruta_origen, ruta_destino):
    """
    Lee el contenido de un archivo TXT y lo vuelca en un objeto FPDF.
    Maneja errores de codificación comunes usando latin-1 como fallback.
    """
    try:
        with open(ruta_origen, 'r', encoding='utf-8', errors='ignore') as f:
            contenido = f.read()
        
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=11)
        
        nombre_archivo = os.path.basename(ruta_origen)
        pdf.cell(200, 10, txt=f"Archivo: {nombre_archivo}", ln=1, align='C')
        pdf.ln(10)
        
        lineas = contenido.split('\n')
        for linea in lineas[:500]: # Límite preventivo de líneas
            if linea.strip():
                try:
                    linea_cod = linea.encode('latin-1', 'replace').decode('latin-1')
                    pdf.multi_cell(0, 6, txt=linea_cod[:500])
                except:
                    pdf.multi_cell(0, 6, txt=linea[:200])
        
        pdf.output(ruta_destino)
        return True
    except Exception as e:
        print(f"Error en conversión TXT: {e}")
        return False

def procesar_docx(ruta_origen, ruta_destino):
    """
    Utiliza la librería python-docx para extraer párrafos y escribirlos en PDF.
    """
    try:
        from docx import Document
        doc = Document(ruta_origen)
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=11)
        pdf.cell(200, 10, txt=f"DOCX: {os.path.basename(ruta_origen)}", ln=1, align='C')
        pdf.ln(10)
        
        for paragraph in doc.paragraphs:
            texto = paragraph.text.strip()
            if texto:
                try:
                    linea_cod = texto.encode('latin-1', 'replace').decode('latin-1')
                    pdf.multi_cell(0, 6, txt=linea_cod[:500])
                except:
                    pdf.multi_cell(0, 6, txt=texto[:200])
        
        pdf.output(ruta_destino)
        return True
    except Exception as e:
        print(f"Error en conversión DOCX: {e}")
        return False

def procesar_doc_binario(ruta_origen, ruta_destino):
    """
    Extrae texto de archivos .doc antiguos mediante lectura binaria y filtrado.
    Es una solución simplificada para evitar dependencias de sistema (como Word).
    """
    try:
        with open(ruta_origen, 'rb') as f:
            contenido_bin = f.read()
        contenido = contenido_bin.decode('latin-1', errors='ignore')
        contenido = ''.join(c for c in contenido if c.isprintable() or c in '\n\r\t')
        
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=11)
        pdf.cell(200, 10, txt=f"DOC (Extracción): {os.path.basename(ruta_origen)}", ln=1, align='C')
        pdf.ln(10)
        
        lineas = contenido.split('\n')
        for linea in lineas[:300]:
            if linea.strip():
                pdf.multi_cell(0, 6, txt=linea[:200])
        
        pdf.output(ruta_destino)
        return True
    except Exception as e:
        print(f"Error en conversión DOC: {e}")
        return False