#coding=utf-8

import requests
import re

url = 'https://bbs.ichunqiu.com/portal.php'

r = requests.get(url=url)
print r.status_code