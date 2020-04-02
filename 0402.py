import time
from selenium.webdriver import Chrome

chromeDriver = 'C:\\temp\\chromedriver.exe'

driver = Chrome(chromeDriver)

driver.get('https://login.11st.co.kr/auth/front/login.tmall')

time.sleep(3)

input_login = driver.find_element_by_id("loginName")
input_login.send_keys('leedolove1')

input_pw = driver.find_element_by_id("passWord")
input_pw.send_keys('jstju9776')

btn = driver.find_element_by_class_name("htn_Atype")

time.sleep(3)

btn.click()

time.sleep(3)


driver.quit()