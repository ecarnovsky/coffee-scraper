import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from sale_item import SaleItem
from email_service import EmailService

def main():

    urls = get_urls_from_file("src/urls/new_urls.txt")
    sale_items = []
    driver = uc.Chrome()


    print("Application starting...")


    for url in urls:

        try:
            driver.get(url)
            driver.implicitly_wait(8)
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


    if len(sale_items) > 0:
        try: 
            email_service = EmailService()
            email_service.send_email(sale_items)
        except Exception as e:
            print("An error has occurred while trying to send an email. " + str(e))

        # UPDATE URL FILES 

    print("Application ending...")

    driver.close()
    time.sleep(1)


def get_urls_from_file(path):

    urls = []

    new_urls_file = open(path, 'r')

    while True:

        url = new_urls_file.readline()

        if not url:
            break
        else:
            urls.append(url)


    if len(urls) == 0:
        exit()

    return urls


main()