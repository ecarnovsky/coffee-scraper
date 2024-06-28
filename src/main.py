import os
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from sale_item import SaleItem
from email_service import EmailService
import subprocess
from pyvirtualdisplay import Display



def main():



    NEW_URLS_PATH = "src/urls/new_urls.txt"
    OLD_URLS_PATH = "src/urls/old_urls.txt"

    if(os.getenv("GITHUB_ACTIONS") == True):
        display = Display(visible=0, size=(800, 800))  
        display.start()

    urls = get_urls_from_file(NEW_URLS_PATH)
    sale_items = []
    driver = uc.Chrome()


    print("Application starting...")


    for url in urls:

        try:
            driver.get(url)
            driver.implicitly_wait(8)
            sale_price = driver.find_element(by=By.CSS_SELECTOR, value="span.product-info__sale-price>span").text
            print("The item is on sale for: " + sale_price)

            name = driver.find_element(by=By.CSS_SELECTOR, value="h1.product-info__title").text
            original_price =  driver.find_element(by=By.CSS_SELECTOR, value="span.product-info__regular-price > span.product-info__regular-price").text
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




        with open(OLD_URLS_PATH, 'a') as file:
            for sale_item in sale_items:
                file.write(sale_item.url)



        new_urls = urls

        for sale_item in sale_items:
            new_urls = list(filter(lambda url : url != sale_item.url, new_urls))

 
        with open(NEW_URLS_PATH, 'w') as file:
            for url in new_urls:
                file.write(url)

        if(os.getenv("GITHUB_ACTIONS") == True):
            result = subprocess.run(['bash', './bot-push.sh'], capture_output=True, text=True)
            if(result.stderr):
                print(result.stderr)

            



    print("Application ending...")


    driver.quit()
    try:
        time.sleep(0.1)
    except OSError:
        pass




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
