from selenium import webdriver

# Function Tests
# 1) Check that we've got Django(v.1.11) installed and that it's ready for us to work with.
# - How to confirm : Spin up Django's dev server(local) and actually see it serving up a web page by using selenium.

browser = webdriver.Firefox()

# Action : Check out its homepage.
browser.get('http://localhost:8000')

# Should browser title is To-Do.
assert 'To-Do' in browser.title

# Should be invited to enter a new to-do item.

# Action : When user types and enter, Should page be updated and to-do list also be updated.

# Should be invited to enter a new to-do item.

# Should remember the user's to-do list (e.g, unique url for each users)

# Action : User re-visit that url

# Should the to-do list is still there.

browser.quit()



