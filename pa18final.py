from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import UnexpectedAlertPresentException
from time import sleep
from getpass import getpass
from urllib.parse import quote

def getDriver(is_hide):
    option = webdriver.ChromeOptions()
    if is_hide:
        option.add_argument('headless')
    driver = webdriver.Chrome(options=option)
    return driver

def getE3Text(driver, student_id, passwd, ith):
    driver.get('https://e3.nctu.edu.tw')
    driver.find_element_by_css_selector('#txtAccount').send_keys(student_id)    
    driver.find_element_by_css_selector('#txtPwd').send_keys(passwd)
    driver.find_element_by_css_selector('#btnLoginIn').click()
    ele_id_prefix = '#ctl00_ContentPlaceHolder1_rptNewList_ctl%02d' % ith
    text = ''
    text += driver.find_element_by_css_selector(ele_id_prefix + '_lbCourseNa').text
    text += driver.find_element_by_css_selector(ele_id_prefix + '_lnkMore').text
    text += driver.find_element_by_css_selector(ele_id_prefix + '_lbContent').text
    return text

def speak(driver, text):
    driver.get("https://translate.google.com.tw/?hl=zh-TW&tab=wT&authuser=0#view=home&op=translate&sl=auto&tl=zh-CN&text=" + quote(text))
    elem = None
    while not elem:
        elem = driver.find_element_by_css_selector('div.src-tts.left-positioned.ttsbutton')
    elem.click()
    while elem.get_attribute('aria-pressed') != 'false':
        sleep(0.1)

if __name__ == '__main__':
    driver = getDriver(True)
    try:
        sid = input('Student ID: ')
        passwd = getpass()
        text = getE3Text(driver, sid, passwd, 0)
        print(text)
        speak(driver, text)
    except UnexpectedAlertPresentException:
        print('Login failed')
    driver.close()
