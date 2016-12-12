from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(LiveServerTestCase):
  def setUp(self):
    self.browser = webdriver.Firefox(capabilities={"marionette":False})
    self.browser.implicitly_wait(3)

  def tearDown(self):
    self.browser.quit()

  def check_list_table_contains_row_text(self,row_text):
    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    self.assertIn(row_text, [row.text for row in rows])

  def test_can_start_a_list_and_retrieve_it_later(self):
    # the user opens the new to-do web app URL in his broweser
    self.browser.get(self.live_server_url)

    # She notices the page title and header mention to-do lists
    self.assertIn('To-Do', self.browser.title)
    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('To-Do', header_text)

    # She is invited to enter a to-do item straight away
    inputbox = self.browser.find_element_by_id('id_new_item')
    self.assertEqual(
        inputbox.get_attribute('placeholder'),
        'Enter a to-do item'
    )

    # She types "Buy peacock feathers" into a text box (Edith's hobby        
    # is tying fly-fishing lures)
    inputbox.send_keys('Buy peacock feathers')

    # When she hits enter, the page updates, and now the page lists
    # "1: Buy peacock feathers" as an item in a to-do list table
    inputbox.send_keys(Keys.ENTER)

    self.check_list_table_contains_row_text('1: Buy peacock feathers')

    # There is still a text box inviting her to add another item. She
    # enters "Use peacock feathers to make a fly" (Edith is very
    # methodical)
    inputbox = self.browser.find_element_by_id('id_new_item')
    inputbox.send_keys('Use peacock feathers to make a fly')
    inputbox.send_keys(Keys.ENTER)

    # The page updates again, and now shows both items on her list
    self.check_list_table_contains_row_text('1: Buy peacock feathers')
    self.check_list_table_contains_row_text('2: Use peacock feathers to make a fly')


    self.fail("COMPLETE THE TEST CODING")



    # Edith wonders whether the site will remember her list. Then she sees
    # that the site has generated a unique URL for her -- there is some
    # explanatory text to that effect.


    # the page also contains a unique URL generated which allows this user to retrieve
    # his list
    # this is explained in the page with some static text

    # the user checks that URL and checks that it contains his to-do list so far