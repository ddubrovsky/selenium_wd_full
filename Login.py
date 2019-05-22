from selenium import webdriver
wd = webdriver.Firefox()

wd.get('http://localhost/litecart/public_html/admin/login.php')
wd.find_element_by_name('username').send_keys('admin')
wd.find_element_by_name('password').send_keys('admin')
wd.find_element_by_name('login').click()
