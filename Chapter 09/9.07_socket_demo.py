"""
Code illustration: 7.08
    Socket Programming Demo
Tkinter GUI Application Development Blueprints
"""

import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print( 'Failed to create socket')
    sys.exit()
print ('Socket Created')
host = 'effbot.org'
port = 80
try:
    ip = socket.gethostbyname( host )

except socket.gaierror:
    print('Could not resolve Hostname')
    sys.exit()

#Connect to remote server
s.connect((ip , port))
print ('Socket Connected to ', host, ' on ip ', ip)
#Send some data to remote server
message = "GET / HTTP/1.1 \r\nHost:" + host + "\r\n\r\nAccept: text/html\r\n\r\n"
try :
    #send the message
    s.sendall(message.encode('utf-8'))
except socket.error:
    print('Send failed')
    sys.exit()

print('Message send successfully')
#Now receive data
received_message = s.recv(4098)
print (received_message )
