import customtkinter as ctk
from tkinter import filedialog, messagebox
import os

# Importaciones de módulos internos
from core.converter import procesar_txt, procesar_docx, procesar_doc_binario
from utils.helpers import generar_ruta_salida, abrir_carpeta_explorador

class ConversorApp:
    def __init__(self):
        self.ventana = ctk.CTk()
        self.ventana.title("📄 Conversor Universal a PDF")
        self.ventana.geometry("850x850")
        self.ventana.minsize(800, 750)
        
        self.archivos_seleccionados = []
        self.tipo_conversion = ""
        
        # Ruta por defecto inicial
        documentos = os.path.join(os.path.expanduser("~"), "Documents")
        self.carpeta_destino = documentos if os.path.exists(documentos) else os.getcwd()
        
        self.crear_interfaz()

    def crear_interfaz(self):
        """Crea la estructura principal de la UI con scroll"""
        self.marco_principal = ctk.CTkScrollableFrame(self.ventana, fg_color="transparent")
        self.marco_principal.pack(fill="both", expand=True, padx=20, pady=20)

        # Título Principal
        ctk.CTkLabel(
            self.marco_principal, 
            text="🔄 CONVERSOR UNIVERSAL A PDF", 
            font=("Segoe UI", 28, "bold"), 
            text_color="#4CC9F0"
        ).pack(pady=(10, 30))

        # Renderizado de Secciones
        self._interfaz_paso_1()
        self._interfaz_paso_2()
        self._interfaz_paso_3()
        self._interfaz_lista_archivos()
        self._interfaz_acciones_finales()
        self._interfaz_barra_estado()

    # --- Secciones con Estética Unificada ---

    def _interfaz_paso_1(self):
        """Sección de selección de formato de origen"""
        # Contenedor del título (Gris con bordes redondeados)
        marco_instruccion = ctk.CTkFrame(self.marco_principal, corner_radius=10)
        marco_instruccion.pack(fill="x", pady=(0, 10))
        ctk.CTkLabel(marco_instruccion, text="PASO 1: Selecciona el formato de origen", 
                     font=("Segoe UI", 15, "bold"), text_color="#B0B0B0").pack(pady=12)

        # Contenedor de botones (Transparente para que luzcan alineados)
        marco_botones = ctk.CTkFrame(self.marco_principal, fg_color="transparent")
        marco_botones.pack(fill="x", pady=(0, 20))
        marco_botones.grid_columnconfigure((0, 1, 2), weight=1)

        botones = [
            ("📝 TXT a PDF", "#4361EE", self.seleccionar_txt),
            ("📘 DOCX a PDF", "#7209B7", self.seleccionar_docx),
            ("📗 DOC a PDF", "#F72585", self.seleccionar_doc)
        ]

        for i, (texto, color, comando) in enumerate(botones):
            btn = ctk.CTkButton(marco_botones, text=texto, command=comando, height=50,
                                font=("Segoe UI", 14, "bold"), fg_color=color, hover_color="#2D2D2D")
            btn.grid(row=0, column=i, padx=5, sticky="ew")

    def _interfaz_paso_2(self):
        """Sección de ajustes adicionales con estética unificada"""
        # Título unificado
        marco_instruccion = ctk.CTkFrame(self.marco_principal, corner_radius=10)
        marco_instruccion.pack(fill="x", pady=(0, 10))
        ctk.CTkLabel(marco_instruccion, text="PASO 2: Ajustes adicionales", 
                     font=("Segoe UI", 15, "bold"), text_color="#4CC9F0").pack(pady=12)

        # Contenedor de Checkboxes
        marco_checks = ctk.CTkFrame(self.marco_principal)
        marco_checks.pack(fill="x", pady=(0, 20))

        self.var_fecha = ctk.BooleanVar(value=False)
        self.var_marcar = ctk.BooleanVar(value=True)
        self.var_abrir = ctk.BooleanVar(value=False)

        contenedor_interno = ctk.CTkFrame(marco_checks, fg_color="transparent")
        contenedor_interno.pack(fill="x", padx=30, pady=15)

        ctk.CTkCheckBox(contenedor_interno, text="Fecha en nombre", variable=self.var_fecha).pack(side="left", expand=True)
        ctk.CTkCheckBox(contenedor_interno, text="Sufijo '_CONVERTIDO'", variable=self.var_marcar).pack(side="left", expand=True)
        ctk.CTkCheckBox(contenedor_interno, text="Abrir al finalizar", variable=self.var_abrir).pack(side="left", expand=True)

    def _interfaz_paso_3(self):
        """Sección de destino con estética unificada"""
        # Título unificado
        marco_instruccion = ctk.CTkFrame(self.marco_principal, corner_radius=10)
        marco_instruccion.pack(fill="x", pady=(0, 10))
        ctk.CTkLabel(marco_instruccion, text="PASO 3: Ubicación de salida", 
                     font=("Segoe UI", 15, "bold"), text_color="#4CC9F0").pack(pady=12)

        # Contenedor de Entrada y Botón
        marco_input = ctk.CTkFrame(self.marco_principal)
        marco_input.pack(fill="x", pady=(0, 20))
        
        contenedor_interno = ctk.CTkFrame(marco_input, fg_color="transparent")
        contenedor_interno.pack(fill="x", padx=15, pady=15)

        self.entry_destino = ctk.CTkEntry(contenedor_interno, height=45, font=("Segoe UI", 12))
        self.entry_destino.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.entry_destino.insert(0, self.carpeta_destino)

        ctk.CTkButton(contenedor_interno, text="📁 Explorar", command=self.seleccionar_destino, 
                      width=140, height=45, fg_color="#3A0CA3", font=("Segoe UI", 12, "bold")).pack(side="right")

    def _interfaz_lista_archivos(self):
        """Visualización de la cola de procesamiento"""
        marco = ctk.CTkFrame(self.marco_principal)
        marco.pack(fill="both", expand=True, pady=(0, 20))
        
        self.texto_archivos = ctk.CTkTextbox(marco, height=180, font=("Consolas", 12), border_width=1)
        self.texto_archivos.pack(fill="both", expand=True, padx=15, pady=15)
        self.texto_archivos.configure(state="disabled")

    def _interfaz_acciones_finales(self):
        """Botones de ejecución"""
        marco = ctk.CTkFrame(self.marco_principal, fg_color="transparent")
        marco.pack(fill="x", pady=(0, 10))
        
        self.boton_convertir = ctk.CTkButton(
            marco, 
            text="🚀 INICIAR CONVERSIÓN", 
            command=self.iniciar,
            height=60, 
            font=("Segoe UI", 18, "bold"), 
            fg_color="#4CAF50", 
            hover_color="#388E3C",
            text_color="white", 
            state="disabled"
        )
        self.boton_convertir.pack(side="left", expand=True, fill="x", padx=(0, 10))
        
        ctk.CTkButton(
            marco, text="🗑️ LIMPIAR", command=self.limpiar, 
            height=60, width=150, fg_color="#FF9800", hover_color="#E68A00", text_color="white",
            font=("Segoe UI", 14, "bold")
        ).pack(side="right")

    def _interfaz_barra_estado(self):
        """Progreso y mensajes de sistema"""
        self.barra_progreso = ctk.CTkProgressBar(self.marco_principal, height=15)
        self.barra_progreso.set(0)
        
        self.label_estado = ctk.CTkLabel(
            self.marco_principal, 
            text="Esperando selección de archivos...", 
            font=("Segoe UI", 12, "italic"),
            text_color="#9E9E9E"
        )
        self.label_estado.pack(pady=10)

    # --- Lógica de Procesamiento ---

    def seleccionar_txt(self): self._cargar_archivos("txt", "*.txt", "Archivos de texto")
    def seleccionar_docx(self): self._cargar_archivos("docx", "*.docx", "Documentos Word")
    def seleccionar_doc(self): self._cargar_archivos("doc", "*.doc", "Word antiguo")

    def _cargar_archivos(self, tipo, ext, desc):
        archivos = filedialog.askopenfilenames(title=f"Cargar {tipo}", filetypes=[(desc, ext)])
        if archivos:
            self.archivos_seleccionados = list(archivos)
            self.tipo_conversion = tipo
            self.actualizar_lista()
            self.boton_convertir.configure(state="normal")
            self.label_estado.configure(text=f"✅ {len(archivos)} archivos listos para procesar", text_color="#4CAF50")

    def seleccionar_destino(self):
        c = filedialog.askdirectory()
        if c:
            self.carpeta_destino = c
            self.entry_destino.delete(0, "end")
            self.entry_destino.insert(0, c)

    def iniciar(self):
        """Ejecuta la conversión y corrige el mensaje de estado al terminar"""
        if not self.archivos_seleccionados: return
        
        total = len(self.archivos_seleccionados)
        self.barra_progreso.pack(fill="x", pady=5)
        self.boton_convertir.configure(state="disabled")
        exitosos = 0
        
        for i, ruta in enumerate(self.archivos_seleccionados):
            # Actualización visual de progreso
            self.label_estado.configure(text=f"Procesando {i+1}/{total}: {os.path.basename(ruta)[:30]}...")
            self.ventana.update()
            
            destino = generar_ruta_salida(ruta, self.carpeta_destino, self.var_fecha.get(), self.var_marcar.get())
            
            res = False
            if self.tipo_conversion == "txt": res = procesar_txt(ruta, destino)
            elif self.tipo_conversion == "docx": res = procesar_docx(ruta, destino)
            elif self.tipo_conversion == "doc": res = procesar_doc_binario(ruta, destino)
            
            if res: exitosos += 1
            self.barra_progreso.set((i + 1) / total)

        # --- SOLUCIÓN PUNTO 2: Limpieza de mensaje al finalizar ---
        self.label_estado.configure(text="✨ Conversión finalizada con éxito.", text_color="#4CAF50")
        messagebox.showinfo("Proceso Completado", f"Se han convertido {exitosos} de {total} archivos.")
        
        if self.var_abrir.get(): 
            abrir_carpeta_explorador(self.carpeta_destino)
            
        self.limpiar()
        self.barra_progreso.pack_forget()

    def actualizar_lista(self):
        self.texto_archivos.configure(state="normal")
        self.texto_archivos.delete("1.0", "end")
        for i, f in enumerate(self.archivos_seleccionados, 1):
            self.texto_archivos.insert("end", f"{i:2d}. {os.path.basename(f)}\n")
        self.texto_archivos.configure(state="disabled")

    def limpiar(self):
        self.archivos_seleccionados = []
        self.tipo_conversion = ""
        self.actualizar_lista()
        self.boton_convertir.configure(state="disabled")
        self.label_estado.configure(text="Esperando selección de archivos...", text_color="#9E9E9E")

    def run(self): 
        self.ventana.mainloop()