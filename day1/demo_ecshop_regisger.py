#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:demo_ecshop_regisger.py
# @Time    :2020/7/16 17:25
# @Author  :Harry

'''
case : 用户注册
Select 下拉菜单
'''

from selenium import  webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver =webdriver.Chrome()
driver.maximize_window()
url = "http://192.168.1.241/hdshop/user.php?act=register"
driver.get(url=url)
time.sleep(2)

#定位下拉菜单
ele = driver.find_element(By.TAG_NAME,'select')
sel = Select(ele)
sel.select_by_visible_text("我最喜爱的电影？")
time.sleep(3)


driver.quit()
