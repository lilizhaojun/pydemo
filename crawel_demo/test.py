
import requests
import re

url = 'https://www.baidu.com'

response = requests.get(url)
response.encoding = 'utf-8'

html = response.text
#print(html)

content = re.findall(r'<title>(.*?)</title>',html)[0]
print(content)