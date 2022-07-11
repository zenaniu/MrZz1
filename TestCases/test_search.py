# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================
@Time : 2022/7/7 21:05
@Author : 阿牛
@Site : zeng
@File : test_search.py
@Software: PyCharm
============================
"""
from PageObject.home_page import HomePage
from selenium import webdriver
import time


class TestSearch(object):

    def test_search_success(self):
        driver = webdriver.Chrome()
        home = HomePage(driver)
        home.open_home_page()
        home.input_search(text='包包')
        home.click_search_button()
        time.sleep(5)
        home.quit()
