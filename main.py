import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException

urls = ['https://www.meijer.com/shopping/product/boston-warehouse-figural-mug-burger-18oz/2660220593.html',
        'https://www.meijer.com/shopping/product/lindt-lindor-assorted-chocolate-candy-truffles-chocolates-with-smooth-melting-truffle-center-15-2-oz-bag/954201519.html']

print("Starting...")


driver = uc.Chrome()

for url in urls:

    try:
        driver.get(url)
        driver.implicitly_wait(15)
        sale_price = driver.find_element(by=By.CSS_SELECTOR, value="span.product-info__sale-price>span").text
        print("The item is on sale for: " + sale_price)

        item_name = "name"
        item_regular_price = 1

    except NoSuchElementException as e:
        print("The item is not on sale.\n Error Message: " + e)
    except WebDriverException as e:
        print("A webdriver error has occurred. This can be caused by being unable to connect to the website.\n Error Message: " + e)


driver.close()
time.sleep(1)
