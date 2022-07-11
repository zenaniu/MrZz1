# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================
@Time : 2022/7/6 21:47
@Author : 阿牛
@Site : zeng
@File : test_login.py
@Software: PyCharm
============================
"""
from PageObject.login_page import LoginPage
from selenium import webdriver
import time


class TestLogin(object):

    def test_login_success(self):
        driver = webdriver.Chrome()
        login = LoginPage(driver)
        login.open_login_page()
        login.input_username(username='zenaniu')
        login.input_pwd(pwd='123456')
        login.click_login_button()
        time.sleep(5)
        login.quit()
