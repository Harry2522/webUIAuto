#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:demo_taobao_search.py
# @Time    :2020/7/16 10:15
# @Author  :Harry
'''
case：淘宝商品搜索
methods: 使用xpath进行定位
'''
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
#访问
url = "https://www.taobao.com/"
driver.get(url=url)
time.sleep(2)
#业务操作
#xpath 搜索
# driver.find_element_by_xpath('//input[@id="q"]').send_keys("凉拖鞋")
# time.sleep(2)
# # driver.find_element_by_xpath('//button[@class="btn-search tb-bg"]').click()
# driver.find_element_by_xpath('//form[@id="J_TSearchForm"]/div[1]/button').click()
# time.sleep(2)
# driver.back()
# time.sleep(2)
#css selector 搜索
# driver.find_element_by_css_selector('.search-combobox-input').send_keys("辣条")
# time.sleep(2)
# driver.find_element_by_css_selector('div[class="search-button"]>button').click()
#
# driver.back()
txt = driver.find_element_by_css_selector('div[class="search-hots-fline"] a:nth-child(3)').text
print(txt)

txt1 = driver.find_element_by_css_selector('div[class="search-hots-fline"] :nth-of-type(1)').text
print(txt1)

href = driver.find_element_by_css_selector('div[class="search-hots-fline"] :nth-of-type(1)').get_attribute('href')
print(href)

print(driver.current_url)

#退出
time.sleep(2)
driver.quit()