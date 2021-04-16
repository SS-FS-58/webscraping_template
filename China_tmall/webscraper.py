from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv


url = 'https://list.tmall.com/search_product.htm?spm=a221t.1710963.cat.2.242a1135x57Fco&cat=50025174&q=%e7%89%9b%e4%bb%94%e8%a3%a4'

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
    # //*[@id = "J_ItemList"]/div[1]
    datas = []
    try:
        result_list = driver.find_elements_by_xpath(
            '*//div[@class="product  "]')

        # datas = []
        for i in range(len(result_list)):
            print('Select result: ', i)
            current_ele = result_list[i]

            print('get product image:')
            copyright = WebDriverWait(current_ele, 20).until(
                EC.visibility_of_element_located((By.XPATH, './/div/div[@class="productImg-wrap"]/a/img')))
            driver.execute_script(
                "return arguments[0].scrollIntoView(true);", copyright)
            current_image = current_ele.find_element_by_xpath(
                './/div/div[@class="productImg-wrap"]/a/img').get_attribute('src').replace('\n', ' ').replace('\t', ' ')
            print(current_image)

            print('get url:')
            current_url = current_ele.find_element_by_xpath(
                './/div/div[@class="productImg-wrap"]/a').get_attribute('href').replace('\n', ' ').replace('\t', ' ')
            print(current_url)

            print('get title:')
            current_title = current_ele.find_element_by_xpath(
                './/div/p[@class="productTitle"]/a').get_attribute("title").replace('\n', ' ').replace('\t', ' ')
            print(current_title)
            print('get price')
            c_price = current_ele.find_element_by_xpath(
                './/div/p[@class="productPrice"]/em').get_attribute("title").replace('\n', ' ').replace('\t', ' ')
            print(c_price)
            print('get shop name')
            c_shop = current_ele.find_element_by_xpath(
                './/div/div[@class="productShop"]/a').text.replace('\n', ' ').replace('\t', ' ')
            print(c_shop)
            datas.append([current_image, current_url,
                          current_title, c_price, c_shop])
        # print(result_list)
        driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[8]/div/b[1]/a[3]').click()
        time.sleep(5)
    except:
        pass
    with open('result.csv', 'w', newline='', encoding='utf-8-sig') as file:
        fieldnames = ['product', 'url', 'title', 'price', 'shop']
        writer = csv.writer(file)
        writer.writerow(fieldnames)
        for data in datas:
            writer.writerow(data)
            print(data)


def main():
    init()
    get_list()


if __name__ == "__main__":
    main()
