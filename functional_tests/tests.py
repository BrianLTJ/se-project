'''

Author: Tingjun Li
Function:
Functional tests

'''

from selenium import webdriver
from django.test import LiveServerTestCase


browser = webdriver.PhantomJS()

# 首页标题
browser.get('http://localhost:8000')

assert '大学图书管理系统' in browser.title



browser.quit()
