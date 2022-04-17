#!/usr/bin/env python
# coding: utf-8

# In[96]:

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.common.by import By
import pandas as pd


def main():
  # In[97]:


  chrome_service = Service(ChromeDriverManager().install())
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
  driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


  # In[98]:


  driver.get('https://teht.hometax.go.kr/websquare/websquare.html?w2xPath=/ui/ab/a/a/UTEABAAA13.xml')


  # In[99]:


  df = pd.read_csv('사업자번호.csv', encoding='euc-kr')
  df.loc[:, '과세여부'] = df.loc[:, '과세여부'].astype('str')
  df.loc[:, '조회일'] = df.loc[:, '조회일'].astype('str')


  # In[100]:


  import time


  # In[101]:


  for i in range(len(df)):
      time.sleep(5)
      business_key = df.iloc[i]['사업자번호']
      driver.find_element(By.ID, 'bsno').send_keys(business_key)
      driver.find_element(By.ID, 'trigger5').click()
      time.sleep(1)
      table_body = driver.find_element(By.ID, 'grid2_body_tbody')
      tmp = table_body.text.split(" ")
      result = [tmp[0], " ".join(tmp[1:-1]), tmp[-1]]

      df.at[i, '과세여부'] = result[1]
      df.at[i, '조회일'] = result[2]


  # In[102]:


  df.to_csv('output.csv', encoding='euc-kr')

if __name__ == '__main__':
  main()