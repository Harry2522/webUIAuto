#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:demo_baidu_search.py
# @Time    :2020/7/15 15:42
# @Author  :Harry
'''
百度搜索
1、打开网页
2、找到输入框，输入关键词
3、点击【百度一下】按钮搜索
'''

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(1)
#1、打开网页
driver.get("http://www.baidu.com")

# 2、找到输入框，输入关键词
# driver.find_element_by_id('kw').send_keys("python")
driver.find_element_by_name('wd').send_keys("Selenium")

# driver.find_element_by_tag_name("input").send_keys("")

time.sleep(2)
# 3、点击【百度一下】按钮搜索
# driver.find_element_by_id('su').click()
driver.find_element_by_class_name('s_btn').click()
time.sleep(2)
#4、点击搜索结果
driver.find_element_by_partial_link_text('Selenium(WEB自动化工具)').click()
time.sleep(2)



time.sleep(2)
driver.quit()
