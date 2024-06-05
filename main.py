from selenium.webdriver.support import expected_conditions as EC
import time
import undetected_chromedriver as uc

print("Starting...")


driver = uc.Chrome()
driver.get('https://www.meijer.com/shopping/product/boston-warehouse-figural-mug-burger-18oz/2660220593.html')
driver.implicitly_wait(15)
driver.close()
time.sleep(1)