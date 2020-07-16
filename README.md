# Web自动化
2020-0715
---
## 自动化基础
### 自动化介绍
    - 模拟人工、
    - 提升效率
    - 脚本复用、
    - 减少重复工作
  -  相对手工而言：使用工具或代码
  - 验证功能业务满足需求
  - 本质上提升测试效率
  - 适用于回归测试
### 自动化的适用范围
    - 项目需求稳定：UI界面变化不频繁
    - 周期长：半年左右
    - 代码能力较强：Python、Java
###自动化的工具
    - QTP ：基于B/S 、C/S
    - Selenium 
    - RF 
    -AutoIT      
### 自动化框架
    - 编程语言 + 工具 + 测试框架
    - Python + Selenium + unittest/Pytest
    - Java + Selenium + Junit/TestNG
    - 持续集成 Jenkin 、Git、Maven

##Selenium自动化基础
### Selenium介绍
    - 针对QTP的 Mercury
    - Senenium1.0 -> 3.0
    - webdriver :驱动浏览器 Chrome 、Firefox、Safria
###Selenium自动化环境搭建
    - 浏览器：Chrome；
    -Webdriver：[下载]（http://npm.taobao.org/mirrors/chromedriver/）
        - 注意：浏览器与webdriver版本对应
        - webdriver需配置在系统环境变量里
    -开发语言环境：python/java环境
    -开发工具：Pycharm/ Eclipse
### 第一个Selenium自动化脚本
```
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com") #访问页面

```
### Selenium基础操作
    - 定位：ID、Name、Class_Name
    -操作:click()、send_keys()、quit()

---



