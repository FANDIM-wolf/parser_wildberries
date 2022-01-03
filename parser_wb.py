#selenium version
from selenium import webdriver
import time
import csv 

list_of_urls = ["https://www.wildberries.ru/catalog/39213396/detail.aspx?targetUrl=GP" , "https://www.wildberries.ru/catalog/11701167/detail.aspx?targetUrl=GP" ]

for el_of_list in list_of_urls:
    url = el_of_list
    driver = webdriver.Chrome(executable_path="D:\\parser\\chromedriver.exe")

    try:
        driver.get(url=url)
        time.sleep(5)
    
        #elem = driver.find_element_by_xpath('//h1[@itemprop="name"]')
        elem_title = driver.find_element_by_xpath("//meta[@itemprop='name']")
        elem_price = driver.find_element_by_xpath("//meta[@itemprop='price']")
        elem_rating = driver.find_element_by_xpath("//meta[@itemprop='ratingValue']")
        elem_author = driver.find_elements_by_xpath("//*[@class = 'product-params__table']/tbody/tr[1]/td")
        print(len(elem_author))
        for elem in elem_author :
            print(elem.text)
            author = elem.text
            title = elem_title.get_attribute("content")
            price = elem_price.get_attribute("content")
            rating = elem_rating.get_attribute("content")
            print(title,price,rating,author)
            with open("Data_from_wb.csv" , 'a', newline='') as csvfile :
                writer = csv.writer(csvfile, delimiter=";")
        
                writer.writerow([title , rating , author , price])
            
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
       


