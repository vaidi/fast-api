import random
import urllib.request
import urllib.parse
import json

#xPa

aa = random.choice([1,23,2,3,2,3,2,3,2,3])
print(aa)
request = urllib.request.Request("http://fanyi.youdao.com/")

handler = urllib.request.HTTPHandler()
opener = urllib.request.build_opener(handler)
res_body = opener.open(request)


headers = {
    'authority': 'm.douban.com',
    'method': 'GET',
    'path': '/rexxar/api/v2/subject/recent_hot/movie?start=20&limit=20&category=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&type=%E5%85%A8%E9%83%A8',
    'scheme': 'https',
    'accept': 'application/json, text/plain, */*',
   # 'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'bid=CGFYzUByd1U; _vwo_uuid_v2=D289BC18B748DBDDAB491F4745D537C11|dc735ad3082ae5abd39b8c60ac622ca1; __utmc=30149280; ll="108288"; ap_v=0,6.0; __utma=30149280.1667997604.1743478304.1746497247.1747038962.3; __utmb=30149280.0.10.1747038962; __utmz=30149280.1747038962.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
    'origin': 'https://movie.douban.com',
    'priority': 'u=1, i',
    'referer': 'https://movie.douban.com/explore?support_type=movie&is_all=false&category=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&type=%E5%85%A8%E9%83%A8',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}
#https://m.douban.com/rexxar/api/v2/subject/recent_hot/movie?start=20&limit=20&category=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&type=%E5%85%A8%E9%83%A8

for i in range(0,20):
    douban_url =  "https://m.douban.com/rexxar/api/v2/subject/recent_hot/movie?"
    params = {
        "start": str(i * 20),
        "limit": "20",
        "category": "豆瓣高分",  # 直接使用中文，稍后编码
        "type": "全部",
    }
    douban_url = douban_url + urllib.parse.urlencode(params)
    print(douban_url)
    request = urllib.request.Request(douban_url, headers=headers)
    resp =   urllib.request.urlopen(request)
    dec_resp =  resp.read().decode('utf8')
    print(json.loads(dec_resp))
    print(resp.read().decode('utf-8'))
    with open("douban.json", 'w', encoding='utf-8') as f:
        f.write(json.dumps(json.loads(dec_resp), ensure_ascii=False, indent=4))  # 字典转字符串再写入





#https://m.douban.com/rexxar/api/v2/subject/recent_hot/movie?start=20&limit=20&category=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&type=%E5%85%A8%E9%83%A8

url_param = "category=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&type=%E5%85%A8%E9%83%A8"

decoded_param = urllib.parse.unquote(url_param)
print(decoded_param)

with open("hello.json","w",encoding="utf-8") as fp:
    fp.write(json.dumps({"aa":"sfd"}))

url="https://fanyi.baidu.com/sug"
data ={
    "kw" :"怎么了"
}
enData  =  urllib.parse.urlencode(data).encode("utf-8")
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
}

req = urllib.request.Request(url,data=enData,headers=headers)
resp = urllib.request.urlopen(req).read().decode('utf-8')
print( json.loads(resp) )