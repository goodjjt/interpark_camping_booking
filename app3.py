from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

options = Options()
options.add_argument('--headless=new')   # headless 모드를 명시적으로 추가
options.add_argument('--disable-gpu')  # GPU 사용 비활성화 (일부 환경에서 필요할 수 있음)
options.add_argument('--no-sandbox')  # 보안 관련 문제를 피하기 위해 추가

# 웹드라이버 설정
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 원하는 URL로 접속
url = 'https://yeyak.seoul.go.kr/web/reservation/selectReservView.do?rsv_svc_id=S250201130906229632&code=T500&dCode=T502&sch_order=1&sch_choose_list=&sch_type=&sch_text=%EB%82%9C%EC%A7%80%203%EC%9B%94&sch_recpt_begin_dt=&sch_recpt_end_dt=&sch_use_begin_dt=&sch_use_end_dt=&svc_prior=N&sch_reqst_value='
driver.get(url)
time.sleep(1)

title = driver.title
html_content = driver.page_source
soup = BeautifulSoup(html_content, 'html.parser')

specific_id = soup.find(id='cal_20250329')
print(specific_id.get('title'))

driver.quit()
