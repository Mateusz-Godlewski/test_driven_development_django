from selenium import webdriver
import unittest

geckodriver_path = r"C:\Program Files\Mozilla Firefox\geckodriver.exe"


#
class NewVisitorTest(unittest.TestCase):


    def setUp(self):
        # user enters a website
        self.browser = webdriver.Firefox(executable_path=geckodriver_path)


    def test_can_start_a_list_and_retrieve_it_later(self):

        self.browser.get("http://localhost:8000")
        # user notices title
        self.assertIn("To-Do",  self.browser.title)
        self.fail("Finish the test")


        # user is invited to add a to-do item
        # after hitting enter user's item shows up on top and the user is invited to add another item
        # user is notified that URL is being updated after every entry to let them save it and access it later on
        # specific URL can be accessed whenever and wherever.



if __name__ == "__main__":
    unittest.main()
