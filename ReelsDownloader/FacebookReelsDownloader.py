import http.server
import socketserver
import threading
import webbrowser
import pyautogui
import pyperclip

import time
from urllib.parse import parse_qs

PORT = 8015
processing = False
urls_queue = []

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

    def do_POST(self):
        global processing, urls_queue
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        parsed_data = parse_qs(post_data)
        
        urls = [url.strip() for url in parsed_data.get('urls', [''])[0].split('\n') if url.strip()]
        urls_queue = urls
        print(urls_queue)
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Processing started...')
        
        if not processing:
            processing = True
            threading.Thread(target=process_downloads).start()

def process_downloads():
    global processing, urls_queue
    time.sleep(2)  # Wait for browser to focus
    
    try:
        for url in urls_queue:
            pyperclip.copy(url)
            # Open new tab
            pyautogui.hotkey('ctrl', 't')
            time.sleep(1)
            
            # Navigate to fsave.io
            pyautogui.write('https://fsave.io')
            pyautogui.press('enter')
            time.sleep(3)
            
            # Press Tab 2 times
            for _ in range(2):
                pyautogui.press('tab')
                time.sleep(0.5)
            
            # Enter URL
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            time.sleep(8)
            
            # Press Tab 2 times
            for _ in range(2):
                pyautogui.press('tab')
                time.sleep(0.5)

            time.sleep(1)
            
            # Start download
            pyautogui.press('enter')
            time.sleep(7)
            
            # Close tab
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(3)
            
    finally:
        processing = False
        urls_queue = []

def start_server():
    with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}")
        httpd.serve_forever()

if __name__ == '__main__':
    # Start HTTP server
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    
    # Open browser
    webbrowser.open(f'http://localhost:{PORT}')
    
    # Keep main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nServer stopped")