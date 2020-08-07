from selenium import webdriver

browser=webdriver.Chrome('D:\\chromedriver.exe')
browser.get('https:\\www.facebook.com')

user_id="digantadas.d26@gmail.com"
password="mypassion26@"

ep=browser.find_element_by_id("email")
ep.send_keys(user_id)

pp=browser.find_element_by_id("pass")
pp.send_keys(password)

login=browser.find_element_by_id("u_0_b")
login.click()

#browser.quit()