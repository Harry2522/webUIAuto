#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:jd_bottom.py
# @Time    :2020/7/17 14:13
# @Author  :Harry
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
url = "http://www.jd.com"
driver.get(url=url)
time.sleep(2)
js="window.scrollTo(100,900)"
driver.execute_script(js)
time.sleep(3)
driver.find_element(By.XPATH, '//div[@id="J_coupon"]/div[2]/div/div/div[1]/a/div[1]/div[2]/div[1]/span').click()
time.sleep(2)


driver.quit()