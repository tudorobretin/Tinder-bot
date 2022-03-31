from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

USER = os.environ['user']
USER2 = os.environ['user2']
KEY = os.environ['password']
KEY2 = os.environ['password2']
option = webdriver.ChromeOptions()
# option.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(executable_path="C:\\Users\\MAXMEDIA\\Desktop\\Python downloads\\Chromedriver\\chromedriver.exe", options=option)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
URL = "https://tinder.com/"
driver.get(URL)

time.sleep(1)

driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button').click() #accepts cookies
time.sleep(1)
driver.set_window_size(2000, 1140)
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()  #clicks on login
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/div[2]/button').click()                         #clicks on facebook sign in
time.sleep(1)
window1 = driver.current_window_handle
windows = driver.window_handles

driver.switch_to.window(windows[1])
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, '._9xo5 button').click() #accepts facebook cookies

email = driver.find_element(By.XPATH, '//*[@id="email"]')
email.send_keys(USER2)

password = driver.find_element(By.XPATH, '//*[@id="pass"]')
password.send_keys(KEY2)

driver.find_element(By.XPATH, '//*[@id="loginbutton"]').click()
time.sleep(4)

driver.switch_to.window(windows[0])
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[1]').click() #accepts location
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[2]').click() # enables not notification
time.sleep(4)
while True:
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/button[2]').click()
        print('"Add Tinder to your Home Screen" appeared')
    except:
        try:
            driver.find_element(By.XPATH, '/html/body/div[2]/div/div/button[2]').click()

        except:
            try:
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[3]/button').click()
            except:
                try:
                    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[4]/button').click()
                except:
                    try:
                        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[1]/button').click()

                    except:


                        bar = driver.find_element(By.CLASS_NAME, "Isolate")
                        # print(bar.tag_name)
                        # print(bar.text)
                        # print(bar.id)
                        all = bar.find_elements(By.TAG_NAME, "button")
                        #print(all)
                        like = all[3]
                        like.click()
                        # for item in all:
                        #     print(item.text)

                        #driver.find_element(By.CLASS_NAME, "Bgc($c-like-green)").click()

                        # buttons = driver.find_element(By.CLASS_NAME, 'Isolate').find_element(By.TAG_NAME, "div").find_elements(By.TAG_NAME, "div")
                        # buttons[4].click()
                        # print(buttons)

                        #driver.find_element(By.XPATH, "//div[@class='Isolate']/div[1]/div[4]").click()


