#coding=utf-8
# threading & Queue

import threading
import time
import requests
import sys

def fun1():
	time_start = time.time()
	r = requests.get(url='http://www.baidu.com')
	times = time.time()-time_start
	# print 'Hello %s:%s'%(key,time.ctime())
	# print 'Status:%s---%s---%s'%(r.status_code,times,time,time.strftime('%H:%W:%S'))
	sys.stdout.write('Status:%s---%s---%s\n'%(r.status_code,times,time.strftime('%H:%M:%S')))


def main():
	threads = []
	# keys = ['zhangsan','lisi','wangmazi']

	threads_count = 10

	for i in range(threads_count):
		t = threading.Thread(target=fun1,args=())
		threads.append(t)

	for i in range(threads_count):
		threads[i].start()

	for i in range(threads_count):
		threads[i].join()

if __name__ == '__main__':
	main()