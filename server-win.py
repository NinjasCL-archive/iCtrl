#!/usr/bin/env python
# 
# iCtrl
# Sends keystrokes to presentations
# @author Camilo Castro
# @date   26/07/2014
 
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir,sep
import win32api
import win32com.client
 
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        
        shell = win32com.client.Dispatch("WScript.Shell")
 
        try:
 
            # Send the Keystrokes
            if(self.path.endswith('/up')):
            	print "Sending Up"
            	shell.SendKeys("{UP}")
 
            if(self.path.endswith('/down')):
            	print "Sending Down"
            	shell.SendKeys("{DOWN}")
 
            if(self.path.endswith('/left')):
            	print "Sending Left"
            	shell.SendKeys("{LEFT}")
 
            if(self.path.endswith('/right')):
            	print "Sending Right"
            	shell.SendKeys("{RIGHT}")
 
            if(self.path.endswith('/space')):
            	print "Sending Space"
            	shell.SendKeys(" ")
 
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