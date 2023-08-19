from typing import List
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import csv
from progress import printProgressBar

def runSelenium(rows: List[str], output_path: str):
  chrome_service = Service()
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
  driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

  driver.get('https://teht.hometax.go.kr/websquare/websquare.html?w2xPath=/ui/ab/a/a/UTEABAAA13.xml')

  with open(output_path, 'w', newline='', encoding='euc-kr') as output:
    writer = csv.writer(output)
    writer.writerow(['사업자번호', '과세여부', '조회일'])

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
