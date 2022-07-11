# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================
@Time : 2022/7/6 21:21
@Author : 阿牛
@Site : zeng
@File : base_page.py
@Software: PyCharm
============================
"""


class BasePage(object):

    def __init__(self, driver):
        driver.maximize_window()
        driver.implicitly_wait(5)
        self.driver = driver

    def open_url(self, url):
        """
        浏览器打开url
        :param url:
        :return:
        """
        self.driver.get(url)

    def find_element(self, *locator):
        """
        定位页面元素
        :param locator:
        :return: 定位到的页面元素
        """
        return self.driver.find_element(*locator)

    def click(self, *locator):
        """
        点击页面元素
        :param locator:
        :return:
        """
        self.find_element(*locator).click()

    def input(self, *locator, content):
        """
        输入内容
        :param locator:
        :param content:
        :return:
        """
        self.find_element(*locator).clear()
        self.find_element(*locator).send_keys(content)

    def quit(self):
        self.driver.quit()
