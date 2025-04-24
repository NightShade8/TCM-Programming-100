#SOCKETS - Sockets can be used to connect two nodes together.  
# This File is inteded to be used on a kali linux machine (for ethical hacking purposed only)
# The NC command is commented out to avoid giving errors, in order to run the code, uncomment the command and run it in a terminal
import socket

HOST = '127.0.0.1'
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #af_inet is ipv4, sock stream is a port
s.connect((HOST,PORT))



#nc -nvlp 7777