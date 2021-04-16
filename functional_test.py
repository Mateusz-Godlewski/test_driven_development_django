from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

chromedriver_path = r"C:\Users\godle\Documents\chrome_driver_development\chromedriver.exe"


#
class NewVisitorTest(unittest.TestCase):


    def setUp(self):
        # user enters a website
        self.browser = webdriver.Chrome(executable_path=chromedriver_path)


    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        self.browser.get("http://localhost:8000")
        # user notices title
        self.assertIn("To-Do",  self.browser.title)

        # user notices header
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("To-Do", header_text)

        # user is invited to add a to-do item
        inputbox = self.browser.find_element_by_id("id_new_item")
        self.assertEqual(
            inputbox.get_attribute("placeholder"),
            "Enter s to-do item"
        )

        # user writes "Buy feathers"
        inputbox.send_keys("Buy feathers")

        # after hitting enter user's item shows up on top and the user is invited to add another item
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertTrue(
            any(row.text == "Buy feathers" for row in rows)
        )

        # user is notified that URL is being updated after every entry to let them save it and access it later on
        self.fail("Finish the test")
        # specific URL can be accessed whenever and wherever.



if __name__ == "__main__":
    unittest.main()
