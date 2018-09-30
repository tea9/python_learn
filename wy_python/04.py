#coding=utf-8
# 多线程

import thread
import time
from subprocess import Popen,PIPE

def fun1():
	print 'Hello Word! %s'%time.ctime()

def main():
	thread.start_new_thread(fun1,())
	thread.start_new_thread(fun1,())
	time.sleep(2)

def ping_check(ip):
	check = Popen(['/bin/bash','-c','ping -c 2 '+ip],stdin=PIPE,stdout=PIPE)
	data = check.stdout.read()
	if 'ttl' in data:
		print 'UP'

def main1():
	for i in range(1,255):
		ip = '106.42.25.'+str(i)
		thread.start_new_thread(ping_check, (ip,))
		time.sleep(0.1)

if __name__ == '__main__':
	main1()
