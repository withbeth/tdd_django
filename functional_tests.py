from selenium import webdriver

# Function Tests
# 1) Check that we've got Django(v.1.11) installed and that it's ready for us to work with.
# - How to confirm : Spin up Django's dev server(local) and actually see it serving up a web page by using selenium.

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title



