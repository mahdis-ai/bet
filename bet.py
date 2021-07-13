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
def login(driver,user_name,pass_word,surname):
    driver.get("link of website")
    time.sleep(5)
    block = driver.find_element(By.XPATH,"//a[@href='#deny']").click()
    login_form=driver.find_element_by_id('curLoginForm').click()
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='auth_id_email']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='auth-form-password']")))
    username.clear()
#username_of_any_acount
    username.send_keys(user_name)
    password.clear()
#password_of_that_acount
    password.send_keys(pass_word)
    login_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='auth-button auth-button--block auth-button--slide-up-hover auth-button--theme-secondary']"))).click()
    time.sleep(3)
    try:
        surname= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='input_surname']")))
        surname.send_keys("business")
        confirm = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='block-window__btn']"))).click()
    except Exception:
        pass
   
    time.sleep(5)
    current_currency=driver.find_element(By.XPATH,"//div[@class='top-b__account']").click()
    other_currency=driver.find_elements_by_xpath("//div[@class='user-balance-list__item']")
    other_currency[1].click()
    print("logged in successfully")






def bet_on_game(driver,match_link,even_type,price):
    try:
        match_link=driver.get(match_link)
    except Exception:
        print("can not find match")
        return -1
    time.sleep(5)

    time.sleep(5)
    try:
        quarter_number=driver.find_element(By.XPATH, "//li[@class='o-tablo-info-list__item']").text
    except Exception:
        print("game is not underway")
    try:
        menu=driver.find_element(By.XPATH,"//div[@class='multiselect s-scoreboard-nav-multiselect']").click()
    except Exception:
        print("can not find the menu")
        return -1
    bet_quarter=driver.find_elements_by_xpath("//span[@class='multiselect__option']")
    flag=False

    for quarter in bet_quarter:
        if(quarter_number=="Half time"):
            time.sleep(300)
            bet_quarter=driver.find_elements_by_xpath("//li[@class='multiselect__element']")
        if(quarter_number==quarter.text):
            quarter.click()
            time.sleep(5)

    search=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class='scoreboard-nav__search-input']")))
    search.send_keys('Total Even')
    while(True):
        i=0
        if(even_type=="yes"):
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
            time.sleep(60)
            if(i>=2):
                print("bet can not be done")
                return -1
                
   
    if(flag==False):
        bet_price= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class='c-spinner__input bet_sum_input']")))
        bet_price.send_keys(price)
        time.sleep(5)
        try:
            place_bet=WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='c-btn c-btn--size-l c-btn--block c-btn--gradient c-btn--gradient-accent u-upcase']"))).click()
        except Exception:
            print("can not find ")
        ok=WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='c-btn c-btn--size-m c-btn--block c-btn--gradient c-btn--gradient-accent u-upcase']"))).click()
        print("betting has been done")
        return 1
    else:
        print("failed")
        return-1
def betting():
    driver = webdriver.Chrome('C:/Users/user/pyprojects/lib/chromedriver.exe')
    login(driver,"300244749","MyDream0","business")
    #bet_on_game(driver,'link of match',"yes/no",integer price number)


def check_result(user_name,pass_word,surname):
    driver = webdriver.Chrome('C:/Users/user/pyprojects/lib/chromedriver.exe')
    driver.get('https://1xbet-648374.top/registration/?tag=d_49778m_97c_101')
    time.sleep(5)
    block = driver.find_element(By.XPATH,"//a[@href='#deny']").click()
    login=driver.find_element_by_id('curLoginForm').click()
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='auth_id_email']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='auth-form-password']")))
    username.clear()
#username_of_any_acount
    username.send_keys(user_name)
    password.clear()
#password_of_that_acount
    password.send_keys(pass_word)
    login = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='auth-button auth-button--block auth-button--slide-up-hover auth-button--theme-secondary']"))).click()
    time.sleep(3)
    try:
        surname= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='input_surname']")))
        surname.send_keys(surname)
        confirm = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='block-window__btn']"))).click()
        time.sleep(5)
    except Exception:
        pass
    try:
        current_currency=driver.find_element(By.XPATH,"//div[@class='top-b__account']").click()
    except Exception:
        print("can not find currency section")
        return -1
    other_currency=driver.find_elements_by_xpath("//div[@class='user-balance-list__item']")
    other_currency[1].click()
    time.sleep(3)
    my_account=driver.find_element_by_xpath("//a[@title='My account']").click()
    bet_history=driver.find_element_by_xpath("//a[@href='/office/history/']").click()
    time.sleep(5)
    date=driver.find_element_by_xpath("//span[@class='apm-filters__date']").click()
    prev_month=driver.find_element_by_xpath("//span[@class='prev']").click()
    day=driver.find_elements_by_xpath("//span[@class='cell day']")[5].click() 
    show=WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='apm-filters__btn_alt show_history']"))).click()
    time.sleep(5)
    bet_detail=driver.find_element_by_xpath("//div[@class='apm-panel-head__info']").text
    bet_status=re.findall(r'.*Bet slip status?\s+(Win|Loss|Unsettled).*',bet_detail)[0]
    print(bet_status)
    return 1


