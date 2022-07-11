# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================
@Time : 2022/7/6 21:41
@Author : 阿牛
@Site : zeng
@File : login_page.py
@Software: PyCharm
============================
"""
from .base_page import BasePage
from Util.util import page

# 获取yaml文件中元素定位
login_page = page['LoginPage']
login_elements = login_page['locators']


class LoginPage(BasePage):
    """登录页"""
    url = login_page['url']
    username_locator = [login_elements[0]['type'], login_elements[0]['value']]
    pwd_locator = [login_elements[1]['type'], login_elements[1]['value']]
    login_button = [login_elements[2]['type'], login_elements[2]['value']]

    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        super().open_url(self.url)

    def input_username(self, username):
        super().input(*self.username_locator, content=username)

    def input_pwd(self, pwd):
        super().input(*self.pwd_locator, content=pwd)

    def click_login_button(self):
        super().click(*self.login_button)
