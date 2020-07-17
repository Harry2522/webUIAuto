#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:jd_search_goods.py
# @Time    :2020/7/16 20:35
# @Author  :Harry
'''
case:实现京东商品搜索的业务流程
1、打开京东首页；
2、找到搜索框，输入关键词
3、点击搜索按钮
4、品牌选择-ThinkPad
5、屏幕尺寸选择——15.6英寸
6、选择结果中的产品——选择第三款产品
7、进入商品详情页面
8、获取商品价格
9、加入购物车
'''
import time
from selenium import webdriver

#打开浏览器
driver = webdriver.Chrome()
driver.maximize_window()

#访问首页
url = "http://www.jd.com"
driver.get(url=url)
time.sleep(2)
#首页操作
driver.find_element_by_id('key').send_keys("笔记本")
driver.find_element_by_class_name('button').click()
time.sleep(3)
#列表页操作
driver.find_element_by_xpath('//li[@id="brand-11518"]/a/img').click()
time.sleep(2)
driver.find_element_by_xpath('//div[@id="J_selector"]/div[4]/div/div[2]/div[1]/ul/li[5]/a').click()
time.sleep(2)
ch = driver.current_window_handle
print(ch)
#进入详情页面
driver.find_element_by_xpath('//div[@id="J_goodsList"]/ul/li[3]/div/div[1]/a/img').click()
time.sleep(2)
#详情页操作
# cwh = driver.current_window_handle
# print("handles",cwh)
#windows窗口切换
handles = driver.window_handles
driver.switch_to.window(window_name=handles[-1])

print("当前页面的地址",driver.current_url)
price = driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[3]/div/div[1]/div[2]/span[1]/span[2]').text
print("商品价格：",price)

driver.find_element_by_css_selector('#InitCartUrl').click() #加入购物车
time.sleep(3)
#退出浏览器
driver.quit()