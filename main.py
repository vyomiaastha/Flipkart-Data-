from selenium import webdriver
from selenium.webdriver.common.by import By
import json

browser = webdriver.Chrome()

products = []

page_num = 1
while page_num:

    url='https://www.flipkart.com/tablets/~apple-ipads/pr?sid=tyy%2Chry&otracker=nmenu_sub_Electronics_0_Apple+iPads&page='+str(page_num)
    #no. of pages changes acc. to the value of i
    browser.get(url)
    elem_list = browser.find_elements(By.CSS_SELECTOR, "._13oc-S") #gives our element and if we print is is console log our element
    
    if elem_list:
        for ele in elem_list:
            items = ele.find_element(By.CSS_SELECTOR, '._4rR01T').text
            price = ele.find_element(By.CSS_SELECTOR, '._1_WHN1').text
            link = ele.find_element(By.CSS_SELECTOR, '._2kHMtA ._1fQZEK').get_attribute('href')
            
            products.append({
                    "Title": items,
                    "Price": price.replace('\u20b9', ''),
                    "Link": link
            })
        page_num += 1

    else:
        page_num = 0
        

with open('flipData_Final.json','w') as j:
    json.dump(products,j, indent = 3)
