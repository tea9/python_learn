import re

# 第一种
pattern = re.compile('hello')
match = pattern.match('hello world');
print(match.group())

# 第二种
word = re.findall('hello','hello word!')
print(word)

# 匹配h和一个任意字符
word = 'http://www.ichunqiu.com python_1.1'
key = re.findall('h.',word)
print(key)

# \ 转义字符 匹配所有点
key = re.findall('\.',word)
print(key)

# 匹配小数点一位
key = re.findall('\d.\d',word)
print(key)

# 匹配所有非数字
key = re.findall('\D',word)
print(key)

# 匹配空字符
key = re.findall('\s',word)
print(key)

# 匹配非空字符
key = re.findall('\S',word)
print(key)

