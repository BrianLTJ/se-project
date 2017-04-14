'''

Author: Tingjun Li
Function:
Functional tests

'''
import time
from selenium import webdriver
from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class AddBookTest(StaticLiveServerTestCase):
    testadd = [["isbn", "9787505715660"], ["title", "小王子"], ["author", "（法）圣埃克苏佩里"], ["translator", "胡雨苏"],["edition", "13014"], ["pubhouse", "中国友谊出版公司"], ["pubtime", "12342253"],["summary", "小王子驾到！大家好，我是小王子，生活在B612星球，别看我是王子出生，我要做的事也不少，有时给花浇水，有时我还得耐心地把火山口通一通。实在闷得发慌的时候，为了找些事做"],["context", "序言：法兰西玫瑰 小王子 圣埃克苏佩里年表"], ["clc", "239/6"], ["price", "11.4"]]
    catelist1 = ["aaa","bbb","ccc","252fd","测试分类1","计算机","金融","医学","电子"]
    catelist2 = ["fff","ggg","jjj","afw","g2rg2"]
    taglist =["BHpmw","MNIoT","va0crc","ZnkNH1xTD","pGyleT","lAD9","s6yAXa","GrvlN","typM","T96Ol","z1gg","TWqmR5"]

    def setUp(self):
        self.browser = webdriver.PhantomJS()
        # self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()


    def test_add_book(self):
        # Add book
        self.browser.get(self.live_server_url+'/admin/book/add')

        # get input list
        for data in AddBookTest.testadd:
            inp = self.browser.find_element_by_id(data[0])
            inp.send_keys(data[1])

        # Add cate
        new_cate_input = self.browser.find_element_by_id("input-newcate")
        new_cate_add_btn = self.browser.find_element_by_id("btn-addnewcate")
        for item in AddBookTest.catelist1:
            new_cate_input.send_keys(item)
            new_cate_add_btn.click()
            time.sleep(0.3)

        # Test cate in list
        catelist = self.browser.find_elements_by_tag_name("option")
        catelisttext = []
        for i in catelist:
            catelisttext.append(i.text)

        for item in AddBookTest.catelist1:
            self.assertTrue(item in catelisttext)

        # Add tag
        new_tag_input = self.browser.find_element_by_id("input-newtag")
        new_tag_add_btn = self.browser.find_element_by_id("btn-addnewtag")
        for item in AddBookTest.taglist:
            new_tag_input.send_keys(item)
            new_tag_add_btn.click()
            time.sleep(0.3)

        submitbtn = self.browser.find_element_by_id('btn-save')
        submitbtn.click()
        time.sleep(2)

        # book detail
        self.browser.get(self.live_server_url+'/book/detail/1')
        time.sleep(1)

        # Test Book info
        readbookinfo = self.browser.find_element_by_id('book-info').text
        for data in AddBookTest.testadd:
            self.assertIn(data[1], readbookinfo)

        # test cates
        cates=self.browser.find_elements_by_class_name('cate-item')
        catelisttext=[]
        for i in cates:
            catelisttext.append(i.text)

        for item in AddBookTest.catelist1:
            self.assertTrue(item in catelisttext)

        # test tags
        tags = self.browser.find_elements_by_class_name('tag-item')
        taglisttext = []
        for i in tags:
            taglisttext.append(i.text)

        for item in AddBookTest.taglist:
            self.assertTrue(item in taglisttext)

