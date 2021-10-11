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
driver.find_element_by_xpath('//*[@id="GLUXZipUpdateInput"]').send_keys('95113')
time.sleep(5)
driver.find_element_by_xpath('//*[@id="GLUXZipUpdate"]/span/input').click()
time.sleep(5)
driver.get('https://www.amazon.com/')
print('Amazon ZIPCode: '+ driver.find_element_by_xpath('//*[@id="glow-ingress-line2"]').text)

#读取ASIN csv 文件

def iselementisexist(elemnet):
        flag=True
        try:
            driver.find_element_by_xpath(elemnet)
            return flag
        except:
            flag = False
            return flag

final_result = {}

num = 0
times = 1
nowTime= ''
for indexs in df.index:
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M')
    row = (df.loc[indexs].values)     
    lineToStr = row[0]
    lineToStr=lineToStr.strip().rstrip('\\xa0')
    driver.get('https://www.amazon.com/dp/'+ lineToStr)
    time.sleep(3)
    print('time is :', times)
    times = times + 1

    if (lineToStr not in final_result):
        final_result[lineToStr] = {}

    if(iselementisexist('//*[@id="acrCustomerReviewText"]')):
        print('\n',lineToStr)
        if(iselementisexist('//*[@id="priceblock_saleprice"]')):
            price = driver.find_element_by_xpath('//*[@id="priceblock_saleprice"]').text
        elif(iselementisexist('//*[@id="priceblock_ourprice"]')):
            price = driver.find_element_by_xpath('//*[@id="priceblock_ourprice"]').text
        elif(iselementisexist('//*[@id="priceblock_dealprice"]')):
            price = driver.find_element_by_xpath('//*[@id="priceblock_dealprice"]').text
        else:
            price = 0

        ratingScore = driver.find_element_by_xpath('//*[@id="reviewsMedley"]/div/div[1]/div[2]/div[1]/div/div[2]/div/span/span').text
        ratingScore = ratingScore.split(' ')[0]

        rating = driver.find_element_by_xpath('//*[@id="acrCustomerReviewText"]').text
        rating = rating.split(' ')[0].replace(',','')

        final_result[lineToStr]['price'] = price
        final_result[lineToStr]['rating'] = rating
        final_result[lineToStr]['score'] = ratingScore

pf = pd.DataFrame(final_result)
pf = pd.DataFrame(pf.values.T,index=pf.columns,columns=pf.index)
files = str(nowTime)+'-asin.xlsx'
file_path= pd.ExcelWriter(files)
pf.to_excel(file_path,encoding='utf-8',index=True)
file_path.save()

driver.quit()
