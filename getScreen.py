#-*-coding: utf-8 -*-
# pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
#pip3 install pillow selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert 
from PIL import Image
import time
import csv
import re
import sys
import datetime
import string
import os
nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M')
# chrome_option = webdriver.ChromeOptions()
# # chrome_option.add_argument('--headless')
# chrome_option.add_argument('--disable-gpu')
# chrome_option.add_argument('--ignore-certificate-errors')
# chrome_option.add_argument('--disable-images')
# chrome_option.add_argument('--start-maximized')

# driver = webdriver.Chrome(chrome_options=chrome_option)
# firefox_option = webdriver.FirefoxOptions()
# Fdriver = webdriver.Firefox(firefox_options=firefox_option)
# # ?currency=USD&language=en_US
# driver.get('https://www.amazon.com/?currency=USD&language=en_US')
# driver.find_element_by_xpath('//*[@id="nav-packard-glow-loc-icon"]').click()
# time.sleep(5)
# driver.find_element_by_xpath('//*[@id="GLUXZipUpdateInput"]').send_keys('10001')
# time.sleep(5)
# driver.find_element_by_xpath('//*[@id="GLUXZipUpdate"]/span/input').click()
# time.sleep(5)
# driver.get('https://www.amazon.com/')
# print('Amazon ZIPCode:'+ driver.find_element_by_xpath('//*[@id="glow-ingress-line2"]').text)

# Fdriver.get('https://www.amazon.com/?currency=USD&language=en_US')
# Fdriver.find_element_by_xpath('//*[@id="nav-packard-glow-loc-icon"]').click()
# time.sleep(5)
# Fdriver.find_element_by_xpath('//*[@id="GLUXZipUpdateInput"]').send_keys('10001')
# time.sleep(5)
# Fdriver.find_element_by_xpath('//*[@id="GLUXZipUpdate"]/span/input').click()
# time.sleep(5)
# Fdriver.get('https://www.amazon.com/')
# print('Amazon ZIPCode:'+ driver.find_element_by_xpath('//*[@id="glow-ingress-line2"]').text)

#获取当前目录所有的图片，保存在对应变量中
existFile = []
for filename in os.listdir('.'):
    if filename.endswith('.png'):
        existFile.append(filename.strip('.png').rstrip(string.digits).replace('_', ' ').rstrip())
print(existFile)


#获取当前目录下面所有的CSV文件
CSVFile=[]
for filename in os.listdir('.'):
    if filename.endswith('.csv'):
        CSVFile.append(filename)


# 判断有多个CSV文件
for i in range(len(CSVFile)):
    if (i % 2) == 0:
        nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M')
        print(nowTime)
        #chrome
        print(CSVFile[i],'chrome')
        time.sleep(30)
    if (i % 2) != 0:
        #firefox
        nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M')
        print(nowTime)
        print(CSVFile[i], 'firefox')
        time.sleep(30)

        

# # 读取ASIN csv 文件
# num = 0
# times = 1
# with open(sys.argv[1],'r') as f:
#     reader = csv.reader(f)
#     for row in reader:       
#         lineToStr = row[0]
#         if lineToStr in existFile:
#             print ('this pic has been finished')
#             print(lineToStr)
#         else:
#             lineToList = lineToStr.split(' ')
#             linkStr='s?k='
#             picPath = ''
#             for i in range(len(lineToList)):
#                 linkStr= linkStr + lineToList[i] + '+'
#                 picPath = picPath + lineToList[i] +'_'
#             linkStr= linkStr[:-1]
#             picPath = picPath[:-1].replace('/','-')
#             # s?k=workout+turf   linkStr format.
#             linkfront = 'https://www.amazon.com/'
#             driver.maximize_window()
#             driver.get('https://www.amazon.com/' + linkStr)
#             count = driver.find_element_by_xpath('//*[@id="search"]/span/div/span/h1/div/div[1]/div/div/span[1]').text
#             count = count.split(' ')[-3].replace(',','')
#             print('Now time is : ' + nowTime )
#             print(picPath + '_' + count + '.png')
#             print('This is : ' + str(times) + ' Picture'+ '\n')
#             jsCode = "var q=document.documentElement.scrollTop=100"
#             driver.execute_script(jsCode)
#             driver.save_screenshot(picPath + '_' + count + '.png')
#             time.sleep(1)
#             times = times + 1
#             num = num + 1
#             if num > 500:
#                 driver.quit()
#                 num = 0
#                 print('Now will sleep 10 sec, and restart the brower')
#                 time.sleep(10)
#                 driver = webdriver.Chrome(chrome_options=chrome_option)
#                 driver.get('http://amazon.com/?currency=USD&language=en_US')
#                 time.sleep(5)
#                 driver.execute_script("document.body.style.zoom='0.9'")


