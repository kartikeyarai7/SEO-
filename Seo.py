from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

for i in range (0,5):         #Any number of times
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://Google.com')
    driver.maximize_window()
    
    time.sleep(5)
    
    search = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')   #Searching 
    search.send_keys("Butyl tubes")
    search.send_keys(Keys.RETURN)
    
    time.sleep(3)
    
    maxride = driver.find_element_by_xpath('//*[@id="rso"]/div[5]/div/div[1]/a/h3')  #Maxride clicked, Only this is variable due to page rank dynamics. Everything else will remain same
    maxride.click()
    
    time.sleep(7)
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  #Scroll Down
    
    time.sleep(3)
    
    products = driver.find_element_by_xpath('//*[@id="menu-item-4264"]/a') #Click on products
    products.click()
    
    time.sleep(5)
    
    products_new = driver.find_element_by_xpath('//*[@id="menu-item-4264"]/a')  #Hover over products
    
    hover = ActionChains(driver).move_to_element(products_new)
    hover.perform()
    
    time.sleep(2)
    
    butyl_tube = driver.find_element_by_xpath('//*[@id="menu-item-3572"]/a')  #Butyl Tubes
    butyl_tube.click()
    
    time.sleep(3)
    
    check_size = driver.find_element_by_xpath('//*[@id="page-content"]/main/div/article/div/div[3]/div[2]/div/div/div    [8]/div[1]/i')  #Click on sizes
    time.sleep(11)
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  #Scroll Down
    
    contact_us = driver.find_element_by_xpath('//*[@id="menu-item-3451"]/a')   #Click contact us
    contact_us.click()
    
    time.sleep(8)
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  #Scroll down
    
    driver.close()  #Exit
    time.sleep(3)   #Wait and repeat :)
    