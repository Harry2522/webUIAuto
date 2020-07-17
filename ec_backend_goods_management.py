#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:ec_backend_goods_management.py
# @Time    :2020/7/17 10:30
# @Author  :Harry
'''
case: 后台添加商品
1、登录后台
2、添加商品
'''

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
url="http://192.168.1.241/hdshop/admin/index.php"
driver.get(url=url)
time.sleep(2)
#登录
driver.find_element(By.NAME,'username').send_keys("admin")
driver.find_element(By.NAME,'password').send_keys("hdxy2018")
driver.find_element(By.CLASS_NAME,'btn-a').click()
time.sleep(2)

#添加商品
driver.switch_to.frame('menu-frame')

driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[1]').click()
time.sleep(3)
driver.find_element(By.LINK_TEXT,'添加新商品').click()
time.sleep(2)
driver.switch_to.parent_frame()  #退出frame

driver.switch_to.frame('main-frame') #进入main-frame
driver.find_element(By.NAME,'goods_name').send_keys("李宁牌-运动鞋")
time.sleep(2)

#日期控件操作
js = "document.getElementById('promote_start_date').removeAttribute('readonly')"
driver.execute_script(js) #删除readonly属性
driver.find_element(By.ID,'promote_start_date').clear()
time.sleep(1)
driver.find_element(By.ID,'promote_start_date').send_keys("2030-01-01")
time.sleep(5)
driver.switch_to.default_content() #



driver.quit()


