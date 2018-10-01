#coding=utf-8

import requests
import re

url = 'https://bbs.ichunqiu.com/portal.php'

headers={
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

r = requests.get(url=url,headers=headers)
print r.status_code
# print r.content

bbs_news = re.findall('class="ui_colorG" style="color: #555555;">(.*?)</a></h3>',r.content)
# print bbs_news

for news in bbs_news:
	print news