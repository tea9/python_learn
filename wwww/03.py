#coding=utf-8
# 爬虫1.0 爬ichunqiu课程名称

import requests
import json

url_start = 'https://www.ichunqiu.com/courses/ajaxCourses'

def lesson():
	headers = {
		'Host': 'www.ichunqiu.com',
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:62.0) Gecko/20100101 Firefox/62.0',
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Accept-Encoding': 'gzip, deflate',
		'Referer': 'https://www.ichunqiu.com/courses',
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'X-Requested-With': 'XMLHttpRequest',
	}
	
	r = requests.post(url=url,headers=headers,data=payload)
	data = json.loads(r.text)
	name_long = len(data['course']['result'])

	for i in range(name_long):
		print data['course']['result'][i]['courseName']

if __name__ == '__main__':
	url = url_start
	for i in range(1,3):
	# 	url = url_start+str(i)
		payload = {"pageIndex":i}
		lesson()
		print "----"
