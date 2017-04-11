'''

Author: Tingjun Li
Function:
Functional tests

'''

from selenium import webdriver
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.PhantomJS()

    def test_index_visit(self):


        # 首页标题
        self.browser.get(self.live_server_url)

        assert '大学图书管理系统' in self.browser.title

    def tearDown(self):
        self.browser.quit()


class AddBookTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.PhantomJS()

    def test_add_book(self):
        self.browser.get(self.live_server_url+'/api/book/book/add')
        jsontest = self.browser.find_element_by_tag_name('pre').text
        # self.assertIn('\"book_id\": \"12345\"', jsontest)
        # self.assertIn('\"result\": \"ok\"', jsontest)
        self.assertIn('\"message\": \"Not a valid request.\"', jsontest)
        self.assertIn('\"result\": \"error\"', jsontest)

    # def test_get_book_detail(self):


    def tearDown(self):
        self.browser.quit()



