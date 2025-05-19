#CRX TO ZIP CTXL+SHIFT+X
# 1,xpath
# 2. beautifulsoup


import  urllib.request
import urllib.parse

url = "http://www.baidu.com"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
from lxml import etree
html = etree.HTML(content)
print(html.xpath("//input[@id='su']/@value"))






















tree = etree.parse('xpath.html')

li_list = tree.xpath('//ul')
print(li_list)