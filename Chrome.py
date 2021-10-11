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
import pandas as pd
import os


print(sys.argv[1])

df = pd.DataFrame(pd.read_excel(sys.argv[1]))
totalkeywords = len(df)
current_path=(os.path.abspath(sys.argv[1]))
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")

#获取当前目录所有的图片，保存在对应变量中
existFile = []
for filename in os.listdir(father_path):
    if filename.endswith('.png'):
        existFile.append(filename.strip('.png').rstrip(string.digits).replace('_', ' ').rstrip())

# print(existFile)
chrome_option = webdriver.ChromeOptions()
# chrome_option.add_argument('--headless')
chrome_option.add_argument('--disable-gpu')
chrome_option.add_argument('--ignore-certificate-errors')
chrome_option.add_argument('log-level=3')
chrome_option.add_argument('--disable-images')
chrome_option.add_argument('--start-maximized')
driver = webdriver.Chrome(chrome_options=chrome_option)
driver.get('https://www.amazon.com/?currency=USD&language=en_US')
time.sleep(10)
driver.find_element_by_xpath('//*[@id="nav-packard-glow-loc-icon"]').click()
time.sleep(15)
driver.find_element_by_xpath('//*[@id="GLUXZipUpdateInput"]').send_keys('10001')
time.sleep(5)
driver.find_element_by_xpath('//*[@id="GLUXZipUpdate"]/span/input').click()
time.sleep(5)
driver.get('https://www.amazon.com/')
# print('Amazon ZIPCode: '+ driver.find_element_by_xpath('//*[@id="glow-ingress-line2"]').text)

#读取ASIN csv 文件

num = 0
times = 1
for indexs in df.index:
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M')
    row = (df.loc[indexs].values)     
    lineToStr = row[0]
    lineToStr=lineToStr.strip().rstrip('\\xa0')
    if lineToStr in existFile:
        totalkeywords = totalkeywords - 1
    else:
        lineToList = lineToStr.split(' ')
        linkStr='s?k='
        picPath = ''
        for i in range(len(lineToList)):
            linkStr= linkStr + lineToList[i] + '+'
            picPath = picPath + lineToList[i] +'_'
        linkStr= linkStr[:-1]
        picPath = picPath[:-1].replace('/','-')
        # s?k=workout+turf   linkStr format.
        linkfront = 'https://www.amazon.com/'
        driver.maximize_window()
        driver.get('https://www.amazon.com/' + linkStr)
        if "No results for " in driver.page_source:
            count = 0
        else:
            count = driver.find_element_by_xpath('//*[@id="search"]/span/div/span/h1/div/div[1]/div/div/span[1]').text
            count = count.split(' ')[-3].replace(',','')
        print('\n Now time is : ' + nowTime )
        # print(picPath + '_' + count + '.png')
        print('This is : ' + str(times) + ' Picture'+ '\n')
        totalkeywords = totalkeywords - 1
        print("Total key words: " + str(totalkeywords))
        jsCode = "var q=document.documentElement.scrollTop=450"
        driver.execute_script(jsCode)
        driver.save_screenshot(father_path + '\\'+ picPath + '_' + str(count) + '.png')
        time.sleep(1)
        times = times + 1
        num = num + 1
        # if num > 500:
        #     driver.quit()
        #     num = 0
        #     print('Now will sleep 10 sec, and restart the brower')
        #     time.sleep(10)
        #     driver = webdriver.Chrome(chrome_options=chrome_option)
        #     driver.get('https://www.amazon.com/?currency=USD&language=en_US')
        #     driver.find_element_by_xpath('//*[@id="nav-packard-glow-loc-icon"]').click()
        #     time.sleep(15)
        #     driver.find_element_by_xpath('//*[@id="GLUXZipUpdateInput"]').send_keys('10001')
        #     time.sleep(5)
        #     driver.find_element_by_xpath('//*[@id="GLUXZipUpdate"]/span/input').click()
        #     time.sleep(5)
        #     driver.get('https://www.amazon.com/')
        #     # print('Amazon ZIPCode: '+ driver.find_element_by_xpath('//*[@id="glow-ingress-line2"]').text)
        #     driver.execute_script("document.body.style.zoom='0.9'")

driver.quit()


