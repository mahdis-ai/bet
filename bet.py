from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import re
import time
driver = webdriver.Chrome('C:/Users/user/pyprojects/lib/chromedriver.exe')
driver.get('https://1xbet-648374.top/registration/?tag=d_49778m_97c_101')

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
time.sleep(3)
my_account=driver.find_element_by_xpath("//a[@title='My account']").click()
bet_history=driver.find_element_by_xpath("//a[@href='/office/history/']").click()
#account_change=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class='multiselect__input']")))
#account_change.clear()
#account_change.send_keys("Other currencies (IRR)")
time.sleep(5)
date=driver.find_element_by_xpath("//span[@class='apm-filters__date']").click()
prev_month=driver.find_element_by_xpath("//span[@class='prev']").click()
day=driver.find_elements_by_xpath("//span[@class='cell day']")[5].click()
show=WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='apm-filters__btn_alt show_history']"))).click()
time.sleep(5)
#bet_detail=WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='apm-panel-head__expand']"))).click()
bet_detail=driver.find_element_by_xpath("//div[@class='apm-panel-head__info']").text
bet_status=re.findall(r'.*Bet slip status?\s+(Win|Loss|Unsettled).*',bet_detail)[0]
print(bet_status)
#bet_result=re.findall(r'<p class="apm-panel-head__text">(.*)</p>',bet_status)
#print(bet_result)





time.sleep(5)
match=driver.get('https://tvevyiehz.top/live/Basketball/950511-Argentina-TNA/312446236-Racing-de-Chivilcoy-Estudiantes-Olavarria/')
time.sleep(5)

time.sleep(5)
quarter_number=driver.find_element(By.XPATH, "//li[@class='o-tablo-info-list__item']").text
print(quarter_number)
menu=driver.find_element(By.XPATH,"//div[@class='multiselect s-scoreboard-nav-multiselect']").click()
bet_quarter=driver.find_elements_by_xpath("//span[@class='multiselect__option']")
flag=False

for quarter in bet_quarter:
    print(quarter.text)
    if(quarter_number=="Half time"):
        time.sleep(300)
        bet_quarter=driver.find_elements_by_xpath("//li[@class='multiselect__element']")
    if(quarter_number==quarter):
        quarter.click()
        time.sleep(5)

search=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class='scoreboard-nav__search-input']")))
search.send_keys('Total Even')
while(True):
    i=0
    if(even=="yes"):
        try:
            even_yes=driver.find_element(By.XPATH, "//span[@data-type='182']")
            if(even_yes!=None):
                even_yes.click()
                break
            else:
                print("bet can not be done , end of quarter")

        except Exception:
            flag=True
            i+=1
            print("Error")
    
 
    else:
        try:
            even_no=driver.find_element(By.XPATH, "//span[@data-type='183']")
            if(even_no!=None):
                even_no.click()
                break
            else:
                print("bet can not be done , end of quarter")
        except Exception:
            flag=True
            i+=1
            print("Error")
        if(flag==False):
            break
        else:
            if(i>=2):
                print("bet can not be done")
                break
            time.sleep(60)
   


bet_price= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class='c-spinner__input bet_sum_input']")))
bet_price.send_keys(5000)
time.sleep(5)
#place_bet=WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='c-btn c-btn--size-l c-btn--block c-btn--gradient c-btn--gradient-accent u-upcase']"))).click()
ok=WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='c-btn c-btn--size-m c-btn--block c-btn--gradient c-btn--gradient-accent u-upcase']"))).click()

def check_result(user,pass,surname):
    driver = webdriver.Chrome('C:/Users/user/pyprojects/lib/chromedriver.exe')
    driver.get('https://1xbet-648374.top/registration/?tag=d_49778m_97c_101')
    time.sleep(5)
    block = driver.find_element(By.XPATH,"//a[@href='#deny']").click()
    login=driver.find_element_by_id('curLoginForm').click()
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='auth_id_email']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='auth-form-password']")))
    username.clear()
#username_of_any_acount
    username.send_keys(user)
    password.clear()
#password_of_that_acount
    password.send_keys(pass)
    login = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='auth-button auth-button--block auth-button--slide-up-hover auth-button--theme-secondary']"))).click()
    time.sleep(3)
#surname= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='input_surname']")))
#surname.send_keys(surname)
#confirm = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='block-window__btn']"))).click()
    time.sleep(5)
    current_currency=driver.find_element(By.XPATH,"//div[@class='top-b__account']").click()
    other_currency=driver.find_elements_by_xpath("//div[@class='user-balance-list__item']")
    other_currency[1].click()
    time.sleep(3)
    my_account=driver.find_element_by_xpath("//a[@title='My account']").click()
    bet_history=driver.find_element_by_xpath("//a[@href='/office/history/']").click()
#account_change=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class='multiselect__input']")))
#account_change.clear()
#account_change.send_keys("Other currencies (IRR)")
    time.sleep(5)
    date=driver.find_element_by_xpath("//span[@class='apm-filters__date']").click()
    prev_month=driver.find_element_by_xpath("//span[@class='prev']").click()
    day=driver.find_elements_by_xpath("//span[@class='cell day']")[5].click()
    show=WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='apm-filters__btn_alt show_history']"))).click()
    time.sleep(5)
#bet_detail=WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='apm-panel-head__expand']"))).click()
    bet_detail=driver.find_element_by_xpath("//div[@class='apm-panel-head__info']").text
    bet_status=re.findall(r'.*Bet slip status?\s+(Win|Loss|Unsettled).*',bet_detail)[0]
    return bet_status



