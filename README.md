# 🔄 Conversor Universal a PDF

Aplicación de escritorio **multiplataforma** desarrollada en **Python** que permite convertir archivos de texto plano (`.txt`) y documentos de Microsoft Word (`.doc` y `.docx`) a **PDF** de forma simple, rápida y confiable.

La aplicación cuenta con una **interfaz gráfica moderna** basada en **CustomTkinter** y un sistema de **automatización de builds** para Windows y Linux mediante **GitHub Actions**.

![Versión](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Plataformas](https://img.shields.io/badge/platform-Linux%20%7C%20Windows-lightgrey.svg)

---

## ✨ Características

* **Soporte multiformato**: Conversión de archivos `.txt`, `.doc` y `.docx` a PDF
* **Interfaz moderna**: GUI oscura, limpia e intuitiva
* **Procesamiento por lotes**: Conversión de múltiples archivos en una sola ejecución
* **Opciones configurables**:

  * Agregar marca de tiempo al nombre del archivo
  * Agregar sufijo automático `_CONVERTIDO`
  * Apertura automática de la carpeta de destino
* **Multiplataforma**:

  * Ejecutable `.exe` para **Windows**
  * Paquete `.deb` para **Linux (Debian/Ubuntu)**
* **Build automático** con GitHub Actions

---

## 🖥️ Capturas

*(Podés agregar screenshots de la aplicación en esta sección)*

---

## 📦 Descarga

Los binarios listos para usar están disponibles en la sección **Releases** del repositorio:

* **Windows**: `ConversorPDF.exe`
* **Linux**: `conversor-pdf.deb`

👉 No es necesario tener Python instalado para usar los binarios.

---

## 🚀 Instalación

### 🐧 Linux (Debian / Ubuntu)

Descargá el archivo `.deb` desde **Releases** y ejecutá:

```bash
sudo apt install ./conversor-pdf.deb
```

Esto creará un acceso directo en el menú de aplicaciones como **Conversor PDF**.

---

### 🪟 Windows

1. Descargá `ConversorPDF.exe` desde **Releases**
2. Ejecutá el instalador
3. Seguí el asistente

Se creará un acceso directo en el escritorio y en el menú Inicio.

---

## 🧱 Estructura del proyecto

```text
.
├── core/                  # Lógica de conversión (FPDF, python-docx)
├── gui/                   # Interfaz gráfica (CustomTkinter)
│   └── assets/            # Iconos e imágenes
│       └── logo.ico
├── utils/                 # Utilidades y helpers
├── main.py                # Punto de entrada de la aplicación
├── requirements.txt       # Dependencias del proyecto
├── installer_script.iss   # Script de Inno Setup (Windows)
└── .github/workflows/
    ├── windows_build.yml  # Build automático para Windows
    └── linux_build.yml    # Build automático para Linux
```

---

## 💻 Desarrollo local

### Requisitos

* Python **3.10+**

### Clonar repositorio

```bash
git clone https://github.com/pabloacisera/python-conversor-to-pdf.git
cd python-conversor-to-pdf
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Ejecutar la aplicación

```bash
python main.py
```

---

## 🧪 Build manual

### Windows (PyInstaller)

```bash
pyinstaller --noconfirm --onedir --windowed \
  --add-data "core;core" \
  --add-data "gui;gui" \
  --add-data "utils;utils" \
  --icon gui/assets/logo.ico \
  --name ConversorPDF main.py
```

### Linux

```bash
pyinstaller --noconfirm --onedir \
  --add-data "core:core" \
  --add-data "gui:gui" \
  --add-data "utils:utils" \
  --name conversor-pdf main.py
```

---

## ⚙️ Automatización (CI/CD)

El proyecto utiliza **GitHub Actions** para automatizar la generación de binarios:

### Windows

* Compila el ejecutable con **PyInstaller**
* Genera instalador usando **Inno Setup**
* Publica el `.exe` como artefacto

### Linux

* Compila el binario con **PyInstaller**
* Empaqueta como `.deb`
* Publica el paquete como artefacto

Los workflows se ejecutan automáticamente en cada **push a la rama `main`**.

---

## 🛠️ Tecnologías utilizadas

* **Python 3.10**
* **CustomTkinter**
* **FPDF**
* **python-docx**
* **PyInstaller**
* **Inno Setup** (Windows)
* **GitHub Actions**

---

## 📄 Licencia

Este proyecto se distribuye bajo la **Licencia MIT**.

---

## 👤 Autor

Desarrollado por **pabloacisera**

---

## ⭐ Contribuciones

* ⭐ Stars son bienvenidas
* 🐞 Issues para reportar errores
* 🤝 Pull Requests abiertos

Este proyecto está pensado para seguir creciendo y mejorar con el feedback de la comunidad.
