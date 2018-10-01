#!/usr/bin/env python
#coding=utf-8
# BeautifulSoup 需要安装其他的包 https://cuiqingcai.com/1319.html
# BeautifulSoup 文档 https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/

import requests
import re
from bs4 import BeautifulSoup


url = 'https://bbs.ichunqiu.com/portal.php'

headers={
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

r = requests.get(url,headers=headers)
soup = BeautifulSoup(r.content,'lxml')

# bbs_news = soup.find_all(name='a',attrs={'class':'ui_colorG'})
# 正则
bbs_news = soup.find_all(name='a',attrs={'href':re.compile('thread-\d*?-1-1.html')})

for news in bbs_news:
	print news.string

# print soup.title
# print soup.title.string


