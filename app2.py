from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
import time
import subprocess

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
chrome_args = [
    chrome_path,
    '--remote-debugging-port=9222',
    '--user-data-dir=C:\\chromeCookie',
    # '--headless',  # 헤드리스 모드로 실행
    '--disable-gpu',  # GPU 사용 안 함
    # '--no-sandbox'  # 샌드박스 사용 안 함
]
subprocess.Popen(chrome_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
options.headless = False

# 웹드라이버 설정
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 원하는 URL로 접속
url = 'https://ggtour.or.kr/camping/main.web'
driver.get(url)
driver.refresh()
parent_window_handle = driver.current_window_handle
time.sleep(2)

# popup - 로그인 or 로그아웃
element = driver.find_element(By.ID, 'cookie_check')
if element.text == '로그인':
    link = driver.find_element(By.LINK_TEXT, '로그인')
    link.click()
    time.sleep(2)

    button = driver.find_element(By.XPATH, '//button[text()="로그인"]')
    button.click()
    time.sleep(3)

    window_handles = driver.window_handles
    main_window_handle = driver.current_window_handle
    for handle in window_handles:
        if handle != main_window_handle:
            driver.switch_to.window(handle)
            break

    popup_title = driver.title
    print(f'팝업 창 제목: {popup_title}')

    link = driver.find_element(By.LINK_TEXT, '네이버 로그인')
    link.click()
    time.sleep(2)

    alert = Alert(driver)
    alert.accept()

    driver.switch_to.window(parent_window_handle)

    title = driver.title
    print(f'창 제목: {title}')

link = driver.find_element(By.LINK_TEXT, '예약하기')
link.click()
time.sleep(2)

# tab -  평화누리캠핑장 예약하기
window_handles = driver.window_handles
main_window_handle = driver.current_window_handle
for handle in window_handles:
    if handle != main_window_handle:
        driver.switch_to.window(handle)
        break
# print(f'텝 창 제목: {driver.titles}')

# id가 'calendar_27'인 td 요소 찾기
calendar_td = driver.find_element(By.ID, 'calendar_29')
links = calendar_td.find_elements(By.TAG_NAME, 'a')
for link in links:
    onclick_value = link.get_attribute('onclick')
    messages = link.text.replace('\r\n', ' ').replace('\n', ' ').split(' ')
    print(f"{messages[1]} : {messages[0]}")
    # print(onclick_value.replace('javascript:f_SelectDateZone( ', '').replace('  );',''))

driver.close()
driver.switch_to.window(parent_window_handle)
driver.close()
# 크롤링 작업을 마친 후 웹드라이버 종료
driver.quit()