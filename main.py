#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time
import csv
from progress import printProgressBar

def main():
  chrome_service = Service()
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
  driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

  driver.get('https://teht.hometax.go.kr/websquare/websquare.html?w2xPath=/ui/ab/a/a/UTEABAAA13.xml')

  working_dir = os.getcwd()
  input_path = os.path.join(working_dir, '사업자번호.csv')
  output_path = os.path.join(working_dir, 'output.csv')

  if os.path.exists(output_path):
    os.remove(output_path)

  with open(output_path, 'w', newline='', encoding='euc-kr') as output:
    writer = csv.writer(output)
    writer.writerow(['사업자번호', '과세여부', '조회일'])

    with open(input_path, encoding='euc-kr') as input:
      next(input)
      reader = csv.reader(input)

      rows = [row[0] for row in reader]
      totalCount = len(rows)

      printProgressBar(0, totalCount, prefix='진행상태:', suffix = '완료', length=50)

      for i, business_key in enumerate(rows):
        driver.find_element(By.ID, 'bsno').send_keys(business_key)
        driver.find_element(By.ID, 'trigger5').click()

        time.sleep(1)
        table_body = driver.find_element(By.ID, 'grid2_body_tbody')
        tmp = table_body.text.split(" ")
        writer.writerow([tmp[0], " ".join(tmp[1:-1]), tmp[-1]])
        printProgressBar(i + 1, totalCount, prefix='진행상태:', suffix = '완료', length=50)


if __name__ == '__main__':
  try:
    main()
  except Exception as e:
    working_dir = os.getcwd()
    error_log_path = os.path.join(working_dir, 'error.log')
    with open(error_log_path, 'w') as error_log:
      error_log.write(str(e))
      exit(1)