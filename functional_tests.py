from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
  def setUp(self):
    self.browser = webdriver.Firefox(capabilities={"marionette":False})
    self.browser.implicitly_wait(3)

  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self):
    # the user opens the new to-do web app URL in his broweser
    self.browser.get('http://localhost:8000')

    # he notices the title of the application
    self.assertIn('To-Do', self.browser.title)
    self.fail('Finish the test')

    # the user is invited to enter to-do's - a form accepting a text box?

    # the user enters "buy peaches" in the text box

    # the user presses enter and the page is updated, and now there is a list with 
    # an entry "1: buy peaches"

    # there is still a text box to enter more to-do's tasks

    # the user enters: "go hang yourself!"

    # the web page is updated and now shows the above plus "2. go hang youself!"

    # the page also contains a unique URL generated which allows this user to retrieve
    # his list
    # this is explained in the page with some static text

    # the user checks that URL and checks that it contains his to-do list so far

if __name__ == '__main__':
  unittest.main(warnings='ignore')
