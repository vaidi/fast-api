import requests
from bs4 import BeautifulSoup

class GetBossData(object):
    domain = "https://www.zhipin.com"
    base_url = "https://www.zhipin.com/c101280600/?query="
    position =""
    prox_ip ="58.220.95.30"
    prox_port ="10174"

    def __init__(self,position):
        self.position = position

    def get_url_html(self,url,cookie):
        ip_url = self.prox_ip+":" +str(self.prox_port)
        proxies = {"http": ip_url, "https": ip_url}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'cookie': cookie
        }
        request = requests.get(url,headers=headers,proxies=proxies,timeout=5)
        html = False
        if request.status_code == 200:
            html = request.content
        return html

    def get_cookie(self,page):
        if page < 4:
            cookie_val = 'lastCity=101280600; __zp_seo_uuid__=d59649f5-bc8a-4263-b4e1-d5fb1526ebbe; __c=1592469667; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1592469673; __l=l=%2Fwww.zhipin.com%2Fshenzhen%2F&r=https%3A%2F%2Fwww.google.com%2F&friend_source=0&friend_source=0; toUrl=https%3A%2F%2Fwww.zhipin.com%2F%2Fjob_detail%2F3f35305467e161991nJ429i4GA%7E%7E.html; __a=43955211.1592469667..1592469667.39.1.39.39; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1592530438; __zp_stoken__=7f3aaPCVBFktLe0xkP21%2BJSFCLWILSwx7NEw4bVJkRx8pdBE3JGNmWjVwdx5PXC8rHmN%2BJB0hX1UvTz5VPyMmOhIVHBglVzoxJQIdLQtKR3ZFBFIeazwOByVndHwXBAN%2FXFo7W2BffFxtXSU%3D; __zp_sseed__=Ykg0aQ3ow1dZqyi9KmeVnWrqZXcZ32a4psiagwqme3M=; __zp_sname__=93bf4835; __zp_sts__=1592530479301'
        elif page < 7:
            cookie_val = 'lastCity=101280600; __zp_seo_uuid__=d59649f5-bc8a-4263-b4e1-d5fb1526ebbe; __c=1592469667; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1592469673; __l=l=%2Fwww.zhipin.com%2Fshenzhen%2F&r=https%3A%2F%2Fwww.google.com%2F&friend_source=0&friend_source=0; toUrl=https%3A%2F%2Fwww.zhipin.com%2F%2Fjob_detail%2F3f35305467e161991nJ429i4GA%7E%7E.html; __a=43955211.1592469667..1592469667.39.1.39.39; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1592530438; __zp_stoken__=7f3aaPCVBFktLe0xkP21%2BJSFCLWILSwx7NEw4bVJkRx8pdBE3JGNmWjVwdx5PXC8rHmN%2BJB0hX1UvTz5VPyMmOhIVHBglVzoxJQIdLQtKR3ZFBFIeazwOByVndHwXBAN%2FXFo7W2BffFxtXSU%3D; __zp_sseed__=Ykg0aQ3ow1dZqyi9KmeVnWrqZXcZ32a4psiagwqme3M=; __zp_sname__=93bf4835; __zp_sts__=1592530514188'
        elif page < 10:
            cookie_val = 'lastCity=101280600; __zp_seo_uuid__=d59649f5-bc8a-4263-b4e1-d5fb1526ebbe; __c=1592469667; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1592469673; __l=l=%2Fwww.zhipin.com%2Fshenzhen%2F&r=https%3A%2F%2Fwww.google.com%2F&friend_source=0&friend_source=0; toUrl=https%3A%2F%2Fwww.zhipin.com%2F%2Fjob_detail%2F3f35305467e161991nJ429i4GA%7E%7E.html; __a=43955211.1592469667..1592469667.40.1.40.40; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1592530479; __zp_stoken__=7f3aaPCVBFktLCT4uVVV%2BJSFCLWIVPWZyNUk4bVJkR25XXHVeZWNmWjVwd286Sm83HmN%2BJB0hX1UvBiBVRyt9IWQOcRtWSk83fAsfJAtKR3ZFBE5efUl%2FByVndHwXRQN%2FXFo7W2BffFxtXSU%3D; __zp_sseed__=Ykg0aQ3ow1dZqyi9KmeVnd/9vyiSRHrJFoMai+azsb8=; __zp_sname__=93bf4835; __zp_sts__=1592530496863'
        else:
            cookie_val = 'lastCity=101280600; __zp_seo_uuid__=d59649f5-bc8a-4263-b4e1-d5fb1526ebbe; __c=1592469667; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1592469673; __l=l=%2Fwww.zhipin.com%2Fshenzhen%2F&r=https%3A%2F%2Fwww.google.com%2F&friend_source=0&friend_source=0; toUrl=https%3A%2F%2Fwww.zhipin.com%2F%2Fjob_detail%2F3f35305467e161991nJ429i4GA%7E%7E.html; __a=43955211.1592469667..1592469667.41.1.41.41; __zp_stoken__=7f3aaPCVBFktLc1t4VTp%2BJSFCLWJscnlxSgw4bVJkRw9tLB4pb2NmWjVwdwwgc2l7HmN%2BJB0hX1UvGFZVTH0OdhQQfwxfOyoieW8cOgtKR3ZFBAJYRFMcByVndHwXTwN%2FXFo7W2BffFxtXSU%3D; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1592530497; __zp_sseed__=Ykg0aQ3ow1dZqyi9KmeVnSZKsrhFUU/CYntJcRoFki4=; __zp_sname__=93bf4835; __zp_sts__=1592530514188'
        return cookie_val

    def run(self):
        page_list = range(1,11)
        dict_file = open("job.mod","a",encoding="utf-8")
        dict_file.seek(0)
        dict_file.truncate()
        dict_file.write('| 岗位 | 区域 | 薪资 | 年限信息 | 公司名称 | 公司信息 | 链接 |')
        dict_file.write('\n| --- | --- | --- | --- | --- | --- | --- |')
        for page in page_list:
            print("开始爬取第"+str(page)+"页数据")
            base_url = self.base_url+str(self.position)+"&page="+str(page)+"&ka=page-"+str(page)
            cookie = self.get_cookie(page)
            html = self.get_url_html(base_url,cookie)
            soup = BeautifulSoup(html, 'html.parser')
            # 招聘职位列表
            job_list = soup.select('.job-list ul li')
            for job_li in job_list:
                # 单条职位信息
                url = self.domain + job_li.select('.job-title a')[0].attrs['href']
                title = job_li.select('.job-title a')[0].get_text()
                area = job_li.select('.job-title .job-area')[0].get_text()
                salary = job_li.select('.job-limit .red')[0].get_text()
                year = job_li.select('.job-limit p')[0].get_text()
                company = job_li.select('.info-company h3')[0].get_text()
                industry = job_li.select('.info-company p')[0].get_text()
                info = {
                    'title': title,
                    'area': area,
                    'salary': salary,
                    'year': year,
                    'company': company,
                    'industry': industry,
                    'url': url
                }
                print(info)
                # 写入职位信息
                info_demo = '\n| %s | %s | %s | %s | %s | %s | %s |'
                dict_file.write(info_demo % (title, area, salary, year, company, industry, url))
        dict_file.close()

if __name__ == '__main__':
    job_name = input("请输入关键字：").strip()
    if job_name == '':
        print('关键字为空，请重新调试')
        exit(0)

    gl = GetBossData(job_name)
    gl.run()






