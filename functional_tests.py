from selenium import webdriver
import unittest

# Function Tests
# 1) Check that we've got Django(v.1.11) installed and that it's ready for us to work with.
# - How to confirm : Spin up Django's dev server(local) and actually see it serving up a web page by using selenium.


class NewVisitorTest(unittest.TestCase):

    # Before
    def setUp(self):
        # Define the browser that we will proceed to test
        self.browser = webdriver.Firefox()
        # TODO : static url of hp
        # Action : Go to the home page
        self.browser.get('http://localhost:8000')

    # After
    def tearDown(self):
        # Close the browser
        self.browser.quit()

    def test_title_of_home_page(self):
        # Should browser title is To-Do.
        expected = 'To-do'
        # Old
        # assert 'To-Do' in self.browser.title, "Browser title was " + browser.title
        self.assertIn(expected, self.browser.title)

    def test_user_can_start_a_list_and_retreive_it_later(self):

        # Should be invited to enter a new to-do item.

        # Action : When user types and enter, Should page be updated and to-do list also be updated.

        # Should be invited to enter a new to-do item.

        # Should remember the user's to-do list (e.g, unique url for each users)

        # Action : User re-visit that url

        # Should the to-do list is still there.
        pass


if __name__ == '__main__':
    # launche the test runner, which will automatically find test classes and methods and run them.
    unittest.main()


