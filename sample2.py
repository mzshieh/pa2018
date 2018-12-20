from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def getDriver(is_hide):
    option = webdriver.ChromeOptions()
    if is_hide:
        option.add_argument('headless')
    driver = webdriver.Chrome(options=option)
    return driver

driver = getDriver(False)

driver.get('http://twtraffic.tra.gov.tw/twrail/TW_Quicksearch.aspx')
# 起站選新竹
element = driver.find_element_by_css_selector('#lbf_1025')
element.click()

# 訖站選台中區域 太原車站
region = driver.find_element_by_css_selector('#ToCity')
for _ in range(6): region.send_keys(Keys.UP)

station = driver.find_element_by_css_selector('#ToStation')
for _ in range(2): station.send_keys(Keys.UP)

# 標準寫法實在是太長了，改成 too_long
too_long = driver.find_element_by_css_selector

# 點擊查詢
query_button = too_long('#searchbtn')
query_button.click()

# 取得首班車資訊並印出
first_train = too_long('#tablecontent > table:nth-child(3) > tbody > tr:nth-child(2)')
data = first_train.text.split()
print(*data)

# 等個五秒

sleep(25)

# 一定要記得關瀏覽器
driver.close()



































