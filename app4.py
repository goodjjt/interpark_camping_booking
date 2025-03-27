from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# webdriver_manager 통해 driver 설정
options = Options()
options.headless = True
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# 네이버 접속
driver.get("https://www.naver.com")

# 검색 창 찾아서 hello world 입력
search_input = driver.find_element(By.CLASS_NAME,"search_input")
search_input.click()
search_input.send_keys("hello world")

# 검색 버튼 클릭
btn_search = driver.find_element(By.CLASS_NAME,"btn_search")
btn_search.click()

time.sleep(3)