#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:ke_day.py
# @Time    :2020/7/15 21:08
# @Author  :Harry

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com") #访问页面

#找到输入框，输入内容
driver.find_element_by_id('kw').send_keys("chromewebdriver")
#找到【百度一下】按钮，点击搜索
driver.find_element_by_id('su').click()

driver.quit() #关闭退出浏览器

