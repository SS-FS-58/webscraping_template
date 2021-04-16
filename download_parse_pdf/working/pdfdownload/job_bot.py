from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import glob
import os
import shutil
import re
import time
import threading
from datetime import date
from datetime import datetime
# import keyboard
import random
import sys

source_path = os.getcwd()
user_id = "foxy4k"
password = "6f0bb268"
message = """
Hi XXXXXXX, 

We are interested in working with you.
If you are interested, please reply back to support@foxy4k.me or text +1-604-774-4983 to obtain more information. 

Best Regards
"""

max_messages_per_day = 100
min_time_gap = 60
max_time_gap = 360

today_count = 0
today = ''

sent_ids = []
sent_names = []
options = Options()
options.accept_untrusted_certs = True
options.assume_untrusted_cert_issuer = True
# options.add_argument(f'user-agent={userAgent}')
options.add_argument("window-size=1920,1080")
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
options.add_argument(f'user-agent={user_agent}')
# options.add_argument("headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-session-crashed-bubble")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--disable-dev-shm-using")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-ipv6")
m_driver = webdriver.Chrome(
    ChromeDriverManager().install(), options=options)
print('Sucessfully the webdriver runned.')


def init_bot():
    m_driver.implicitly_wait(5)
    # m_driver.maximize_window()
    m_driver.get("https://www.sexyjobs.com/login")
    # insert user id
    WebDriverWait(m_driver, 10).until(EC.presence_of_element_located(
        (By.ID, 'email'))).clear()
    m_driver.find_element(By.ID, 'email').send_keys(user_id)
    # insert password
    m_driver.find_element(By.ID, 'password').clear()
    m_driver.find_element(By.ID, 'password').send_keys(password)
    m_driver.find_element(By.ID, 'password').send_keys(Keys.RETURN)

    # try:
    #     WebDriverWait(m_driver, 30).until(EC.presence_of_element_located(
    #         (By.ID, 'password'))).send_keys(password)
    # except:
    #     WebDriverWait(m_driver, 30).until(EC.element_to_be_clickable(
    #         (By.ID, 'cookies-accept'))).click()
    #     time.sleep(2)
    #     WebDriverWait(m_driver, 30).until(EC.presence_of_element_located(
    #         (By.ID, 'password'))).send_keys(password)

    # click login
    time.sleep(1)
    try:
        error_txt = m_driver.find_element(
            By.XPATH, '//*[@id="about_pbr"]/label').text
        label_txt = 'Jobseekers log in with your email address, Employers log in with your username'
        if error_txt == label_txt:
            time.sleep(random.randint(min_time_gap, max_time_gap))
            print('Someone logged in already with your account!')
            init_bot()
    except:
        pass
    # WebDriverWait(m_driver, 30).until(EC.element_to_be_clickable(
    #     (By.ID, 'register'))).click()
    # m_driver.find_element(By.ID, 'register').click()
    print('Sucessfully Logged In.')
    time.sleep(1)


def set_bot():
    time.sleep(3)
    try:
        m_driver.find_element(
            By.XPATH, '//*[@id="talent-links"]/li[7]/a').click()
    except:
        time.sleep(1)
        print('Log in faile, So let you login again.')
        time.sleep(random.randint(min_time_gap, max_time_gap))
        init_bot()
        set_bot()

    # WebDriverWait(m_driver, 30).until(EC.element_to_be_clickable(
    #     (By.XPATH, '//*[@id="talent-links"]/li[7]/a'))).click()

    # m_driver.find_element(By.XPATH, '//*[@id="talent-links"]/li[7]/a').click()
    time.sleep(3)
    # if EC.element_to_be_clickable(By.ID, 'cookies-accept'):
    #     WebDriverWait(m_driver, 30).until(EC.element_to_be_clickable(
    #         (By.ID, 'cookies-accept'))).click()

    m_driver.find_element(
        By.XPATH, '//*[@id="savedsearches"]/tbody/tr[2]/td[1]/a').click()
    time.sleep(1)
    m_driver.find_element(
        By.XPATH, '//*[@id="page-1"]/div[1]/div/p[1]/span[1]').click()


def send_message(today_count):
    time.sleep(3)

    WebDriverWait(m_driver, 30).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="send-message-link"]'))).click()
    # m_driver.find_element(By.XPATH, '//*[@id="send-message-link"]').click()

    id = m_driver.find_element(By.XPATH, '//*[@id="pb_talent"]/div/span').text
    print('new id started', id)
    if id not in sent_ids:
        try:
            print('new id started')
            m_driver.find_element(
                By.XPATH, '//*[@id="show-all-activity"]').click()
            time.sleep(2)

            print('Clicked activity')
            last_message = m_driver.find_element(
                By.XPATH, '//*[@id="talent-details"]/tbody/tr[4]/td[2]').text
            # last_message = m_driver.find_element(By.XPATH, '//*[@id="talent-details"]/tbody/tr[1]/td[2]').text
            print('Clicked Talent details', last_message)

            name = m_driver.find_element(
                By.XPATH, '//*[@id="stagename"]/span').text
            print('Get name:', name)

            if "No messages" in last_message:

                sent_message = message.replace("XXXXXXX", name, 1)
                # //*[@id="send-message-link"]
                time.sleep(5)
                # WebDriverWait(m_driver, 30).until(EC.presence_of_element_located(
                #     (By.ID, 'reply_message'))).send_keys(sent_message)
                # print('sent_message typed')
                # time.sleep(5)
                # WebDriverWait(m_driver, 30).until(EC.element_to_be_clickable(
                #     (By.ID, 'register'))).click()
                m_driver.find_element(
                    By.ID, 'reply_message').send_keys(sent_message)
                print('---  inserted msg to msg box! ----')
                m_driver.find_element(
                    By.ID, 'reply_message').send_keys(Keys.RETURN)
                print('---  sent a msg to  ----')
                time.sleep(5)
                print("---Ok----sent message:", sent_message)
                # keyboard.write("\n")
                sent_ids.append(id)
                print('Append ids lists new ', id)
                today_count += 1
                print('++++   Currently number of messages: ', today_count)
                # Switch the control to the Alert window
                obj = m_driver.switch_to.alert

                # Retrieve the message on the Alert window
                msg = obj.text
                print("Alert shows following message: " + msg)
                if "Daily Usage Limit Reached" in msg:
                    print('Limit Reached so next day I can send it again sorry.')
                    return max_messages_per_day
                time.sleep(2)

                # use the accept() method to accept the alert
                obj.accept()

                print(" Clicked on the OK Button in the Alert Window")

                WebDriverWait(m_driver, 30).until(EC.element_to_be_clickable(
                    (By.ID, 'ft_next'))).click()
                time.sleep(random.randint(min_time_gap, max_time_gap))
            else:
                print('Already sent messages.Next')
                WebDriverWait(m_driver, 30).until(EC.element_to_be_clickable(
                    (By.ID, 'ft_next'))).click()
                print('Clicked next!')
            time.sleep(3)
        except:
            print("Oops!", sys.exc_info()[0], "occurred.")
            print('3 sec!')
            time.sleep(3)
    else:
        WebDriverWait(m_driver, 20).until(EC.presence_of_element_located(
            (By.ID, 'ft_next'))).click()
        time.sleep(3)
    return today_count


init_bot()
set_bot()
while True:

    if today != date.today():
        today = date.today()
        today_count = 0
        print('new day is ', today)
    if today_count < max_messages_per_day:
        now = datetime.now()
        print("now =", now)
        today_count = send_message(today_count)
        # time.sleep(random.randint(min_time_gap, max_time_gap))
    else:
        print("I will come back tommorrow again, Bye now.")
        time.sleep(1800)
        # m_driver.close()
        # m_driver.quit()


print("ok")
