from selenium import webdriver
wd = webdriver.Firefox()

wd.get('https://google.com')
wd.quit()
