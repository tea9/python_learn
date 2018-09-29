#coding=utf-8
# socket
# client.py

from socket import *
from time import ctime
from subprocess import Popen,PIPE

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
		data = tcpClient.recv(BUFSIZE)
		if not data:
			break
		tcpClient.send('[%s] %s'%(ctime(),data))

tcpClient.close()
tcpServer.close()