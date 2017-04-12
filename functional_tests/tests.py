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
        # Add book
        self.browser.get(self.live_server_url+'/admin/book/add')
        testadd=[["isbn","9787505715660"],["title","小王子"],["edition","13014"],["pubhouse","中国友谊出版公司"],["pubtime","12342253"],["summary","小王子驾到！大家好，我是小王子，生活在B612星球，别看我是王子出生，我要做的事也不少，有时给花浇水，有时我还得耐心地把火山口通一通。实在闷得发慌的时候，为了找些事做"],["context","序言：法兰西玫瑰\n小王子\n圣埃克苏佩里年表\n"],["clc","239/6"],["price", "11.4"]]
        # get input list
        # inplist = []
        for data in testadd:
            # inplist.append(self.browser.find_element_by_id(data[0]))
            # inplist[len(inplist)-1].send_keys(data[1])
            inp = self.browser.find_element_by_id(data[0])
            inp.send_keys(data[1])
        
        submitbtn=self.browser.find_element_by_id('btn-save')
        submitbtn.click()

        # Get Book
        self.browser.get(self.live_server_url+'/book/detail/1')
        self.browser.implicitly_wait(5)
        readbookinfo=self.browser.find_element_by_tag_name('body').text
        for data in testadd:
            self.assertIn(data[1],readbookinfo)
     
        # self.browser.get(self.live_server_url+'/api/book/book/add')
        # jsontest = self.browser.find_element_by_tag_name('pre').text
        # self.assertIn('\"book_id\": \"12345\"', jsontest)
        # self.assertIn('\"result\": \"ok\"', jsontest)
        # self.assertIn('\"message\": \"Not a valid request.\"', jsontest)
        # self.assertIn('\"result\": \"error\"', jsontest)

    # def test_get_book_detail(self):


    def tearDown(self):
        self.browser.quit()



