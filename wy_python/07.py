#coding=utf-8
# socket
# server.py

from socket import *

HOST = ''
PORT = 2333
BUFSIZE = 1024

ADDR = (HOST,PORT)

tcpServer = socket(AF_INET,SOCK_STREAM)
tcpServer.bind(ADDR)
tcpServer.listen(5)

while True:
	print 'waiting for connection...'
	tcpClient,addr = tcpServer.accept()
	print '..connected form:'addr
	while True:
		data = tcpClientrecy(BUFSIZE)
		if not data:
			break
		tcpClient.send('[%s] %s'%(ctime(),data))

tcpClient.close()
tcpServer.close()
		
