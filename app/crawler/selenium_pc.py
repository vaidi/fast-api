

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# path ="chromedriver.exe"
# base_url = "https://www.toutiao.com/"
# service = Service(path)
# driver = webdriver.Chrome(service=service)
# driver.get(base_url)
# print(driver.page_source)

import  time


# input = driver.find_element(By.ID, "kw")
# input.send_keys("周杰伦")
# time.sleep(5)
# button = driver.find_element(By.ID, "su")
# button.click()
# time.sleep(5)
# js_button = "document.documentElement.scrollTop =100000"
# driver.execute_script(js_button)




# driver.get(base_url)




if __name__ == '__main__':
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    import time

    # 配置 Chrome 选项
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # 禁用自动化控制标志
    chrome_options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")  # 设置真实 User-Agent
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])  # 隐藏自动化测试提示

    # 启动浏览器
    path = "chromedriver.exe"
    service = Service(path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    # 在原有代码基础上添加以下代码（放在 driver.get 之前）
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        });
        """
    })
    # 访问页面
    base_url = "https://www.toutiao.com/"
    driver.get(base_url)
    input("请手动完成验证后按回车继续...")  # 阻塞程序，手动操作
    print(driver.page_source)  # 检查是否成功获取内容
    # login_button = driver.find_element(By.CLASS_NAME,"login-button")
    # print("=== 登录按钮信息 ===")
    # print(f"标签名: {login_button.tag_name}")  # 应该是 's'
    # print(f"文本内容: {login_button.text}")  # 应该是 '立即登录'
    # print(f"class 属性: {login_button.get_attribute('class')}")  # 应该是 'login-button'
    # print(f"rel 属性: {login_button.get_attribute('rel')}")  # 应该是 'nofollow'
    # print(f"完整 outerHTML:\n{login_button.get_attribute('outerHTML')}")  # 打印完整 HTML
 #   login_button.click()
    time.sleep(10)
    print("你好")
    driver.get(base_url)
    print(driver.page_source)





    print("登录按钮点击成功！")

    time.sleep(5)  # 等待页面加载


    driver.quit()