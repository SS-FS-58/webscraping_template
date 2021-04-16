from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

import os
import xlrd

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
prefs = {"download.default_directory": r'{0}\pdfs'.format(
    os.getcwd()), "plugins.always_open_pdf_externally": True}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(
    ChromeDriverManager().install(), options=options)

loc = ("links.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

for i in range(1, sheet.nrows):
    print(sheet.cell_value(i, 1))
    try:
        prefs = {"download.default_directory": r'{0}\{1}'.format(
            os.getcwd(), sheet.cell_value(i, 0)), "plugins.always_open_pdf_externally": True}
        options.add_experimental_option("prefs", prefs)
        driver.get(sheet.cell_value(i, 1))
        elements = driver.find_elements_by_css_selector('a[href$=".pdf"]')
        for i in range(len(elements)):
            print(elements[i].text)
            if elements[i].text != '':
                elements[i].click()
    except:
        pass
    # 'https://ahca.myflorida.com/medicaid/Prescribed_Drug/drug_criteria.shtml')

# pdf download.
    # driver.find_element_by_xpath(
    #     '//*[@id="ColumnContent"]/div[1]/p[1]/a').click()

print('ok')
