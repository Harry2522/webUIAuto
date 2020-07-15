#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:first.py
# @Time    :2020/7/15 14:09
# @Author  :Harry
'''
webdriver 控制浏览器
'''
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window() #窗口最大化
# driver.set_window_size(600,400) #设置窗口大小

driver.get("http://www.baidu.com") #打开浏览器并访问百度
time.sleep(2)
driver.refresh()  #刷新页面
time.sleep(2)

driver.get("http://www.taobao.com")
time.sleep(2)

driver.get("http://www.jd.com")
time.sleep(2)
driver.back() #回退
time.sleep(2)
driver.forward()#前进

time.sleep(3) #等待3s
# driver.close() #关闭浏览器
driver.quit() #退出浏览器


