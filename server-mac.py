#!/usr/bin/env python
 
# Simple Servidor de Datos
# Crea un servidor web para
# controlar la presentacion desde el iPhone
# @author Camilo Castro
# @date   17/07/2014
 
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir,sep,system
 
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        cmd = """
        osascript -e 'tell application "System Events" to key code {0}' 
        """
        
        # Querty Keyboard 
        up = cmd.format(126)
        down = cmd.format(125)
        left = cmd.format(123)
        right = cmd.format(124)
        space = cmd.format(49)
        
        try:
 
        	# Enviamos el comando de teclado segun url
            if(self.path.endswith('/up')):
            	print "Sending Up"
            	system(up)
 
            if(self.path.endswith('/down')):
            	print "Sending Down"
            	system(down)
 
            if(self.path.endswith('/left')):
            	print "Sending Left"
            	system(left)
 
            if(self.path.endswith('/right')):
            	print "Sending Right"
            	system(right)
 
            if(self.path.endswith('/space')):
            	print "Sending Space"
            	system(space)
 
            # Mostramos el html del teclado
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
                
            html = open(curdir + sep + 'keys.html')
                
            self.wfile.write(html.read())
            html.close()
            
        except IOError:
            self.send_error('404','404 Not Found')
    
    def do_POST(self):
        pass
 
def main():
    serverPort = 8080
    try:
        server = HTTPServer(('',serverPort),MyHandler)
        print 'Comenzando a servir los datos localhost:{}'.format(serverPort)
        server.serve_forever()
    except KeyboardInterrupt:
        print 'Apagando servidor'
        server.socket.close()
        
if __name__ == '__main__':
    main()