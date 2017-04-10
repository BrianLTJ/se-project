'''

Author: Tingjun Li
Function:
Functional tests

'''

from selenium import webdriver
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):
    def test_index_visit(self):
        self.browser = webdriver.PhantomJS()

        # 首页标题
        self.browser.get(self.live_server_url)

        assert '大学图书管理系统' in self.browser.title

        self.browser.quit()
