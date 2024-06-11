#載入 Selenium 相關模組
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime, timedelta



URL = ""

def Conncet_Web_Browers(): #瀏覽器條件設定 

   
        ## 設定Chrome的瀏覽器彈出時遵照的規則
        ## 這串設定是防止瀏覽器上頭顯示「Chrome正受自動控制」
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)


        ##  設定Chrome將禁用某些彈出提示，包括"密碼太弱"提示。
        options.add_argument("--disable-infobars")

        ##  禁用擴展
        options.add_argument("--disable-extensions")

        ##  禁用彈出攔截
        options.add_argument("--disable-popup-blocking")

        ##  禁用通知
        options.add_argument("--disable-notifications")

        ##  禁用密碼儲存提示
        options.add_argument("--disable-save-password-bubble")

        ##  禁用密碼更改提示
        options.add_argument("--disable-password-change")

        ##  關閉自動記住密碼的提示彈窗
        options.add_experimental_option("prefs", {
                                        "profile.password_manager_enabled": False, "credentials_enable_service": False})

   
        # 創建一個 Chrome WebDriver 實例
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(20)  # 设置隐式等待时间
        driver.get(URL)
        driver.maximize_window()
        return driver

def wait_until_noon():#等待直到中午12点
   
    now = datetime.now()
    target_time = now.replace(hour=12, minute=0, second=0, microsecond=0)
    if now.hour >= 12:
        target_time += timedelta(days=1)
    wait_time = (target_time - now).total_seconds()
    print(f"当前时间: {now}, 等待时间: {wait_time} 秒")
    time.sleep(wait_time)


def click_reserve(driver): #點擊訂房
    reserve1 = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div[4]/div/div[3]/div/div[1]/div/div[2]/ul/li[1]/div[1]/div[1]/div[2]/div[2]/div/button")
    reserve1.click()



def FILL_IN(driver):  #填入相關資料
    #輸入名
    button1 = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div/form/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div/input")
    button1.send_keys("")
    #輸入姓
    button2 = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div/form/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div[1]/div[2]/div/div/input")
    button2.send_keys("")
    #輸入手機
    button3 = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div/form/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/div/input")
    button3.send_keys("09")



def pay(driver): #點擊付款
    button = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div/form/div/div[1]/div[6]/button/span/span")
    button.click()


def fifty(driver):
    fifty_50 = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div[2]/form/div/div/div[3]/div[2]/div/div/div[2]/div[1]/div[2]/div/div/div/div/span/span/span")
    # 獲取元素的文本內容
    text_content = fifty_50.text

    # 檢查文本內容中是否包含'50'
    if '50' in text_content:
        print("元素包含'50'")
    else:
        print("元素不包含'50'")

# def creditcard_pay(driver):
#     try:
#         button1 = driver.find_element(By.CSS_SELECTOR,"input[data-testid='textField-input']")
#         button1.send_keys("123456")
#         print("OK1")
#         button2 = driver.find_element(By.CSS_SELECTOR,"input[autocomplete='cc-number']")
#         button2.send_keys("777778888")
#         print("OK2")
#         button3 = driver.find_element(By.CSS_SELECTOR,"select[autocomplete='cc-exp-month']")
#         button3.send_keys("12")
#         print("OK3")
#         button4 = driver.find_element(By.CSS_SELECTOR,"select[autocomplete='cc-exp-year']")
#         button4.send_keys("2036")
#         print("OK4")
#         button5 = driver.find_element(By.CSS_SELECTOR,"input[autocomplete='off']")
#         button5.send_keys("487")
#         print("OK5")


#     except:print("BUG")

# def check(driver):
#     button1 = driver.find_element(By.CSS_SELECTOR,"div[data-testid='checkbox-icon']")
#     button1.click()
#     print("OK123")
#     button2 = driver.find_element(By.CSS_SELECTOR,"button[data-testid='bookingStep2-complete-button']")
#     button2.click()
#     print("OK1234")






driver = Conncet_Web_Browers()
wait_until_noon()
click_reserve(driver)
FILL_IN(driver)
driver.execute_script("window.scrollTo(30, document.body.scrollHeight);")
driver.execute_script("window.scrollTo(400, document.body.scrollHeight);")
pay(driver)
# creditcard_pay(driver)
# check(driver)
time.sleep(10000)