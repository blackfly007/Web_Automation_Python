from selenium import webdriver

browser=webdriver.Chrome('D:\chromedriver.exe')
browser.get('https:\\www.facebook.com')

user_id="digantadas.d26@gmail.com"
password="mypassion26@"

ep=browser.find_element_by_id("email")
ep.send_keys(user_id)

pp=browser.find_element_by_id("pass")
pp.send_keys(password)

login=browser.find_element_by_id("u_0_b")
login.click()



k='//*[@id="home_birthdays"]/div/div/div/div/a/div/div/span/span[2]'
n=browser.find_element_by_xpath(k).get_attribute('textContent')
num=n[0]
num=int(num)


message= "Happy Birthday!!! Many Many happy returns of the day. :)"
browser.get('https://www.facebook.com/events/birthdays/')


bday_list=browser.find_elements_by_xpath('//*[@class="enter_submit uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea inlineReplyTextArea mentionsTextarea textInput" ]')


c=0
for i in (bday_list):
    element_id=str(i.get_attribute('id'))
    XPATH= '//*[@id ="' + element_id + '"]'
    post=browser.find_element_by_xpath(XPATH)
    post.send_keys(message)
    #time.sleep(1)
    post.send_keys(keys.RETURN)
    c=c+1
    if(c>0):  
        break

