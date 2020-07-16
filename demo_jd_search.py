#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:demo_jd_search.py
# @Time    :2020/7/16 13:45
# @Author  :Harry
'''
case: 京东搜索
1、访问京东首页；
2、首页搜索"华为手机"
3、输出当前地址；
4、重新搜索“小米”

'''
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

#访问京东首页
url = "http://www.jd.com"
driver.get(url=url)
time.sleep(2)
print("当前窗口句柄-1：",driver.current_window_handle)
#首页搜索-华为手机
driver.find_element(By.ID,'key').send_keys("华为")
driver.find_element(By.XPATH, '//button[@class="button"]').click()
print("当前窗口句柄-2：",driver.current_window_handle)
time.sleep(1)
print(driver.current_url) #打印当前页面地址
time.sleep(2)

#找到第二个产品 //
driver.find_element(By.XPATH,'//div[@id="J_goodsList"]/ul/li[6]/div/div[1]/a/img').click()
time.sleep(2)
#进入商品详情页
handles = driver.window_handles
driver.switch_to.window(handles[-1])

print(driver.current_url)
#获取商品价格
price = driver.find_element(By.XPATH,'//span[@class="p-price"]/span[2]').text
print("价格",price)

#加入购物车
# driver.find_element(By.ID,'InitCartUrl').click()
#返回列表重新搜索
driver.switch_to.window(handles[0])

#重新搜索-小米
driver.find_element_by_id('key').clear()
driver.find_element_by_id('key').send_keys("小米")
driver.find_element_by_css_selector('div[class="form"] button').click()
time.sleep(2)
print(driver.title)
print("当前窗口句柄-3：",driver.current_window_handle)
driver.find_element(By.XPATH,'//div[@id="J_goodsList"]/ul/li[3]/div/div[1]/a/img').click()

#切换窗口
handles = driver.window_handles
driver.switch_to.window(handles[-1])
print(driver.title)

time.sleep(5)
driver.quit()
