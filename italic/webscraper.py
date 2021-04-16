from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv


url = 'https://www.eventiesagre.it/Eventi_Sagre/elenco.html'

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
options.add_argument("--disable-gpu")
options.add_argument("--disable-ipv6")
driver = webdriver.Chrome(
    ChromeDriverManager().install(), options=options)
print('Sucessfully the webdriver runned.')


def init():
    driver.get(url)
    print('get url')


def get_list():
    print('Call get List function!')
    datas = []
    try:
        result_list = driver.find_elements_by_xpath(
            '//*[@id="contenuto"]/div[1]/div[@class="risultatoEvento"]')

        # datas = []

        for i in range(len(result_list)):
            print('Select result: ', i)
            current_ele = result_list[i]

            print('get title:')
            current_title = current_ele.find_element_by_xpath(
                './/a/div[2]/div/h3[1]').text.replace('\n', ' ').replace('\t', ' ')
            print(current_title)
            try:
                print('get event type')
                current_property = current_ele.find_element_by_xpath(
                    './/a/div[2]/div/h3[2]').text.replace('\n', ' ').replace('\t', ' ')
                print(current_property)
            except:
                current_property = ''
                print(current_property)
            c_date = current_ele.find_element_by_xpath(
                './/a/div[2]/div/div[1]').text.replace('\n', ' ').replace('\t', ' ')
            print(c_date)
            c_description = current_ele.find_element_by_xpath(
                './/a/div[2]/div').text.replace('\n', ' ').replace('\t', ' ')
            print(c_description)
            datas.append([current_title, current_property,
                          c_date, c_description])

        print(result_list)
    except:
        pass
    with open('result.csv', 'w', newline='') as file:
        # fieldnames = ['title', 'information', 'price', 'primary']
        writer = csv.writer(file)
        # writer.writerow(['title', 'information', 'price', 'primary'])
        for data in datas:
            writer.writerow(data)


def main():
    init()
    get_list()


if __name__ == "__main__":
    main()
