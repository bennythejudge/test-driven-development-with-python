from selenium import webdriver

# browser = webdriver.Firefox()
browser = webdriver.Firefox(capabilities={"marionette":False})
browser.get('http://localhost:8000')

# browser.get('https://google.com')

assert 'Django' in browser.title
