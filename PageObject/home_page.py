# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================
@Time : 2022/7/7 20:48
@Author : 阿牛
@Site : zeng
@File : home_page.py
@Software: PyCharm
============================
"""
from .base_page import BasePage
from Util.util import page

home_page = page['Home_Page']
home_elements = home_page['locators']


class HomePage(BasePage):
    """商城主页"""
    url = home_page['url']
    search_locator = (home_elements[0]['type'], home_elements[0]['value'])
    search_button = (home_elements[1]['type'], home_elements[1]['value'])

    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self):
        super().open_url(self.url)

    def input_search(self, text):
        super().input(*self.search_locator, content=text)

    def click_search_button(self):
        super().click(*self.search_button)
