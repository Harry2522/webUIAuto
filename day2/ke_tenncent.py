#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:ke_tenncent.py
# @Time    :2020/7/16 21:33
# @Author  :Harry

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://ke.qq.com/"
driver.get(url=url)
time.sleep(2)

#login
driver.find_element(By.XPATH,'//*[@id="js-mod-entry-index"]/a').click()
time.sleep(2)
driver.switch_to.alert
driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div[2]/a[1]').click()
time.sleep(2)
driver.find_element(By.CLASS_NAME,'img_out_focus').click()

time.sleep(13)
# driver.quit()