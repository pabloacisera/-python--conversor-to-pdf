[Setup]
AppName=Conversor PDF Universal
AppVersion=1.0
DefaultDirName={autopf}\ConversorPDF
DefaultGroupName=Conversor PDF
OutputDir=Output
OutputBaseFilename=Instalador_ConversorPDF
SetupIconFile=gui\assets\logo.ico
Compression=lzma
SolidCompression=yes

[Files]
; Toma todo lo que generó PyInstaller en la máquina virtual
Source: "dist\ConversorPDF\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
; Crea el acceso directo en el menú inicio y escritorio
Name: "{group}\Conversor PDF"; Filename: "{app}\ConversorPDF.exe"
Name: "{autodesktop}\Conversor PDF"; Filename: "{app}\ConversorPDF.exe"; IconFilename: "{app}\gui\assets\logo.ico"