from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item

from lists.views import home_page


# Create your tests here.
class HomePageTest(TestCase):

  def test_root_url_resolves_to_home_page_view(self):
    found = resolve('/')
    self.assertEqual(found.func, home_page)

  def test_home_page_html_content_is_correct(self):
    request = HttpRequest()
    response = home_page(request)
    # print(repr(response.content))
    # self.assertTrue(response.content.startswith(b'<html>'))
    # self.assertIn(b'<title>To-Do lists</title>', response.content)
    # self.assertTrue(response.content.strip().endswith(b'</html>'))
    expected_html = render_to_string('home.html')
    self.assertEqual(response.content.decode(), expected_html)

  def test_home_page_can_save_a_POST_request(self):
    request = HttpRequest()
    request.method = 'POST'
    request.POST['item_text'] = 'A new list item'

    response = home_page(request)

    self.assertEqual(Item.objects.count(), 1)
    new_item = Item.objects.first()
    self.assertEqual(new_item.text, 'A new list item')


  def test_home_page_redirects_after_POST(self):
    request = HttpRequest()
    request.method = 'POST'
    request.POST['item_text'] = 'A new list item'

    response = home_page(request)
    self.assertEqual(response.status_code, 302)
    self.assertEqual(response['location'], '/')

  def test_home_page_only_saves_items_when_necessary(self):
    request = HttpRequest()
    home_page(request)
    self.assertEqual(Item.objects.count(), 0)

  def test_home_page_displays_all_list_items(self):
    Item.objects.create(text='itemey 1')
    Item.objects.create(text='itemey 2')

    request = HttpRequest()
    response = home_page(request)

    self.assertIn('itemey 1', response.content.decode())
    self.assertIn('itemey 2', response.content.decode())


class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first ever item'
        first_item.save()

        second_item = Item()
        second_item.text = 'The second item'
        second_item.save()

        # at this point there should be 2 items
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        # let's retrieve them and check they are what we expect
        saved_item_one = saved_items[0]
        saved_item_two = saved_items[1]
        self.assertEqual(saved_item_one.text, 'The first ever item')
        self.assertEqual(saved_item_two.text, 'The second item')
