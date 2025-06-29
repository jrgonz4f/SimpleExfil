import http.server
import socketserver
import cgi
import os
from datetime import datetime

PORT = 8000
UPLOAD_DIR = "./uploads"

# Crear carpeta si no existe
os.makedirs(UPLOAD_DIR, exist_ok=True)

class UploadHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.get('Content-Type'))
        
        if ctype == 'multipart/form-data':
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            pdict['CONTENT-LENGTH'] = int(self.headers.get('Content-length'))
            
            form = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ={'REQUEST_METHOD': 'POST'}, keep_blank_values=True)
            
            if 'file' in form:
                file_item = form['file']
                
                filename = os.path.basename(file_item.filename)
                
                if not filename:
                    filename = f"upload_{datetime.now().strftime('%Y%m%d%H%M%S')}"
                
                filepath = os.path.join(UPLOAD_DIR, filename)
                
                with open(filepath, 'wb') as f:
                    f.write(file_item.file.read())
                
                self.send_response(200)
                self.end_headers()
                self.wfile.write(f"File '{filename}' uploaded successfully.\n".encode())
                return
        
        self.send_response(400)
        self.end_headers()
        self.wfile.write(b"Invalid upload.\n")

# Iniciar el servidor
with socketserver.TCPServer(("", PORT), UploadHandler) as httpd:
    print(f"[*] Server listening on port {PORT}...")
    httpd.serve_forever()

