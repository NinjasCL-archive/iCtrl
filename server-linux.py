#!/usr/bin/env python
# 
# iCtrl
# Sends keystrokes to presentations
# @author Camilo Castro
# @date   26/07/2014
 
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir,sep,system
 
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        cmd = """
        xdotool key {0}
        """
        
        # Querty Keyboard 
        up = cmd.format("Up")
        down = cmd.format("Down")
        left = cmd.format("Left")
        right = cmd.format("Right")
        space = cmd.format("space")
        
        try:
 
        	# Send keystrokes
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
 
            # Show html
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
        print 'Serving at localhost:{}'.format(serverPort)
        server.serve_forever()
    except KeyboardInterrupt:
        print 'Shutting Down'
        server.socket.close()
        
if __name__ == '__main__':
    main()