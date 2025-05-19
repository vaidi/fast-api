
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class GetTouTiaoData(object):


    def __init__(self):

        self.options =  Options()
        self.options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        self.driver = webdriver.Chrome(options=self.options)


    def get_first_html(self):
        base_url = "https://www.toutiao.com/"
        self.driver.get(base_url)
        print(self.driver.page_source)
        time.sleep(100)



    def login(self):
       self.get_first_html()



    def get_content(self):
        # global list
        base_url = "https://www.toutiao.com/"
        options = Options()
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.toutiao.com/")
        # 等待内容加载

        soup = BeautifulSoup(driver.page_source, 'lxml')
        print(soup.prettify())
        # 继续你的解析...
        divs = soup.find_all("div", class_="feed-card-article-l")
        articles = []  # ✅ 推荐变量名
        for tile in divs:
            # 提取标题和相对链接
            title_tag = tile.find('a', class_='title')
            image_src = None
            img = tile.find('img')
            if img is not None:
                image_src = img.get('src')
            print(f"图片地址{image_src}")

            if title_tag:
                title = title_tag.get_text(strip=True)
                relative_url = title_tag['href']  # 获取href属性
                full_url = urljoin(base_url, relative_url)  # 拼接完整URL
                # 提取来源
                source = tile.find('div', class_='feed-card-footer-cmp-author').get_text(strip=True)

                # 提取时间
                time_content = tile.find('div', class_='feed-card-footer-time-cmp').get_text(strip=True)

                driver.get(full_url)
                content_soup = BeautifulSoup(driver.page_source, 'lxml')

                result_with_original_format = '\n'.join(
                    ["<p>" + p.text + "</p><br>" for p in content_soup.find_all('p')])

                # print(content_soup.prettify())

                # print(f"标题: {title}")
                # print(f"链接: {full_url}")  # 打印完整URL
                # print(f"来源: {source}")
                # print(f"时间: {time_content}")
                # print(f"文章: {result_with_original_format}")
                articles.append([title, image_src, result_with_original_format])
            print("-" * 50)
        return articles

if __name__ == "__main__":
    toutiao = GetTouTiaoData()
    toutiao.login()