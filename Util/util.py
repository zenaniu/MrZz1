# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================
@Time : 2022/7/6 20:42
@Author : 阿牛
@Site : zeng
@File : util.py
@Software: PyCharm
============================
"""
import os
import yaml


def read_yaml():
    base_path = os.path.dirname(os.path.realpath(__file__))
    yaml_path = os.path.join(os.path.dirname(base_path), 'Page_elements')
    page_element = {}
    for fpath, dirname, fname in os.walk(yaml_path):
        for name in fname:
            yaml_file_path = os.path.join(fpath, name)
            if '.yaml' in str(yaml_file_path):
                with open(yaml_file_path, 'r', encoding='utf-8') as f:
                    page = yaml.load(f, Loader=yaml.FullLoader)
                    page_element.update(page)
    return page_element


page = read_yaml()
