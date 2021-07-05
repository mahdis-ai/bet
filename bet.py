from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

driver = webdriver.Chrome('C:/Users/user/pyprojects/lib/chromedriver.exe')
driver.get('https://1xbet-648374.top/registration/?tag=d_49778m_97c_101')
import time
even="yes"
time.sleep(5)
block = driver.find_element(By.XPATH,"//a[@href='#deny']").click()
login=driver.find_element_by_id('curLoginForm').click()
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='auth_id_email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='auth-form-password']")))
username.clear()
#username_of_any_acount
username.send_keys("300244749")
password.clear()
#password_of_that_acount
password.send_keys("MyDream0")
login = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='auth-button auth-button--block auth-button--slide-up-hover auth-button--theme-secondary']"))).click()
time.sleep(3)
#surname= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='input_surname']")))
#surname.send_keys("business")
#confirm = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='block-window__btn']"))).click()
time.sleep(5)
current_currency=driver.find_element(By.XPATH,"//div[@class='top-b__account']").click()
other_currency=driver.find_elements_by_xpath("//div[@class='user-balance-list__item']")
other_currency[1].click()


time.sleep(5)
match=driver.get('https://eyyvjvpnq.top/live/Basketball/215291-FIBA-U19-World-Championship/311936772-Iran-U19-Serbia-U19/')
time.sleep(5)

time.sleep(5)
quarter=driver.find_element(By.XPATH, "//div[@class='c-tablo__text']").text
quarter_number=quarter.split()[0]
menu=driver.find_element(By.XPATH,"//div[@class='multiselect s-scoreboard-nav-multiselect']").click()
bet_quarter=driver.find_element_by_xpath("//span[@class='multiselect__option']").click()
time.sleep(5)
search=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class='scoreboard-nav__search-input']")))
search.send_keys('Total Even')
if(even=="yes"):
    driver.find_element(By.XPATH, "//span[@data-type='182']").click()
else:
    driver.find_element(By.XPATH, "//span[@data-type='183']").click()
bet_price= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class='c-spinner__input bet_sum_input']")))
bet_price.send_keys(5000)
time.sleep(5)
place_bet=WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='c-btn c-btn--size-l c-btn--block c-btn--gradient c-btn--gradient-accent u-upcase']"))).click()
bet_number=driver.find_element(By.XPATH, "//div[class='c-coupon-modal__title']").text
ok=WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='c-btn c-btn--size-m c-btn--block c-btn--gradient c-btn--gradient-accent u-upcase']"))).click()
