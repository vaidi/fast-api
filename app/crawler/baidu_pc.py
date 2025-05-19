import urllib.request
import urllib.parse





















url ="http://www.baidu.com"
down_url ="https://www.douyin.com/e7b0917c-aa80-4dba-851f-18b0c42a5021"
urllib.request.urlretrieve(down_url,"aa.mp4")

name = urllib.parse.quote("你好")
print(name)
request = urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})

data ={
    "wd": "nihao",
    "sex":"男"
}
enData = urllib.parse.urlencode(data).encode("utf8")
print(enData)


resp = urllib.request.urlopen(url)
#<class 'http.client.HTTPResponse'>
print(f"url:{resp.geturl()}")
print(type(resp))
content = resp.read().decode("utf-8")
print(content)