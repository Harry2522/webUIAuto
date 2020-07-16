#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:demo_jd_search.py
# @Time    :2020/7/16 13:45
# @Author  :Harry
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

url = ""
driver.get(url=url)
time.sleep(2)

driver.quit()
