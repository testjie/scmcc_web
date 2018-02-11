# -*- coding:utf-8 -*-
__author__ = 'snake'

import unittest

from config import config
from src.test.common import common
from src.utils.util_xml import XmlUtils
from ddt import data,ddt,file_data,unpack
from src.test.page.page_index import IndexPage


@ddt
class TestCaseSearch(unittest.TestCase):
    global keys
    keys = XmlUtils.read_xml_document(config.DATA_FILE_PATH, "test_search_success")

    # 测试方法执行前执行
    def setUp(self):
        self.browser = common.get_browser()


    # 测试方法执行后执行
    def tearDown(self):
        self.browser.close()


    # 测试搜索成功
    @data(*keys)
    def test_search_success(self, key):
        result_page = IndexPage(browser = self.browser).search(key.get("ky"))
        assert result_page.toindex.text == "百度首页1"


    def test_click_news(self):
        result_page = IndexPage(browser = self.browser).news_link()
        raise Exception("123")




if __name__ == "__main__":
    unittest.main()

