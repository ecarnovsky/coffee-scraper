import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from sale_item import SaleItem

urls = []
sale_items = []


print("Application starting...")


new_urls_file = open('new_urls.txt', 'r')

while True:

    url = new_urls_file.readline()

    if not url:
        break
    else:
        urls.append(url)


if len(urls) == 0:
    exit()




driver = uc.Chrome()

for url in urls:

    try:
        driver.get(url)
        driver.implicitly_wait(15)
        sale_price = driver.find_element(by=By.CSS_SELECTOR, value="span.product-info__sale-price>span").text
        print("The item is on sale for: " + sale_price)

        name = "name"
        original_price = 1
        sale_item = SaleItem(name, sale_price, original_price, url)
        sale_items.append(sale_item)

    except NoSuchElementException as e:
        print("Could not locate sale price element. Most likely the item is not on sale. \n" + str(e))
    except WebDriverException as e:
        print("A webdriver error has occurred. This can be caused by being unable to connect to the website.\n" + str(e))


print("Application ending...")

driver.close()
time.sleep(1)
