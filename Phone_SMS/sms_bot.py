from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


url = 'https://app.vonage.com/messages'
user_id = "albertfairconeture"
password = "@Kako1337"
phone_number = "(862)258-4243"
message = "Hi, How are you?\n"


options = Options()
options.accept_untrusted_certs = True
options.assume_untrusted_cert_issuer = True
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
options.add_argument("--disable-notifications")
options.add_argument("--disable-gpu")
options.add_argument("--disable-ipv6")
driver = webdriver.Chrome(
    ChromeDriverManager().install(), options=options)
print('Sucessfully the webdriver runned.')


def init():
    # driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(url)
    print('get url')
    # return driver


def login():
    # insert user id
    time.sleep(1)
    # driver.find_element(By.ID, 'userid').send_keys(user_id)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.ID, 'userid'))).send_keys(user_id)
    print('Inserted user id correctly.')
    # insert password
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'password').send_keys(Keys.RETURN)
    time.sleep(1)
    print('Sucessfully Logged In.')


def gotosms():
    time.sleep(15)
    driver.get("https://app.vonage.com/messages")
    try:
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div[4]/div/div[3]/button[1]'))).click()
    except:
        pass

    print('okay sms')


def newmessage():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[1]/div/div[4]/div/div[2]/div[3]/div[1]/div[1]/div/div/button'))).click()
    print('New Message!')
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="filterElement"]'))).send_keys(phone_number)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div/div[1]/div[1]/div/div[3]/button'))).click()
    message_tag = WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div/div[4]/div/div[2]/div[3]/div[1]/div[4]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div/p')))
    driver.execute_script(
        "arguments[0].textContent = arguments[1];", message_tag, message)
    message_tag.send_keys(Keys.RETURN)
    # /html/body/div[1]/div/div[4]/div/div[2]/div[3]/div[1]/div[4]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div/p
    print('new message!')


def main():
    init()
    login()
    gotosms()
    newmessage()


if __name__ == "__main__":
    main()
