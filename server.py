import http.server
import socketserver
import os

PORT = 8080  # Используем порт 8080 для локального запуска

class CORSHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Content-Type', 'text/html; charset=utf-8')  # Явно указываем кодировку UTF-8
        super().end_headers()
    
    def do_GET(self):
        # Если запрос идет на корневой URL, используем index.html
        if self.path == '/':
            self.path = '/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

if __name__ == "__main__":
    # Запускаем сервер
    Handler = CORSHTTPRequestHandler
    
    with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
        print(f"Serving at http://0.0.0.0:{PORT}")
        print(f"Access the game at: http://localhost:{PORT}/")
        print(f"Direct link to game: http://localhost:{PORT}/tetris.html")
        print("Press Ctrl+C to stop the server")
        httpd.serve_forever()