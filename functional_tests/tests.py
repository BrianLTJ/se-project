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




