#selenium version
from selenium import webdriver
import time

url = "https://www.instagram.com/"
driver = webdriver.Chrome(executable_path="D:\\parser\\chromedriver.exe")

try:
    driver.get(url=url)
    time.sleep(5)
    driver.get_screenshot_as_file("sasdsagagsheqerfagaggdfasfa.png")
    
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
