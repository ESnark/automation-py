#!/usr/bin/env python
# coding: utf-8

import os
import csv
from progress import printProgressBar
from websquare import runSelenium
from open_api import runApiRequest

def main():
  API_URL='https://api.odcloud.kr/api/nts-businessman/v1/status'
  API_QUERIES = { 'returnType': 'JSON', 'serviceKey': '' }

  working_dir = os.getcwd()
  input_path = os.path.join(working_dir, '사업자번호.csv')
  output_path = os.path.join(working_dir, 'output.csv')
  key_path = os.path.join(working_dir, 'key')

  input_file = open(input_path, encoding='euc-kr')
  next(input_file)
  reader = csv.reader(input_file)
  rows = [row[0] for row in reader]
  input_file.close()


  if os.path.exists(output_path):
    os.remove(output_path)

  if os.path.exists(key_path):
    key_file = open(key_path, 'r')
    key = key_file.readline().strip()
    key_file.close()
    runApiRequest(rows, key, output_path)
  else:
    runSelenium(rows, output_path)

if __name__ == '__main__':
  try:
    main()
  except Exception as e:
    working_dir = os.getcwd()
    error_log_path = os.path.join(working_dir, 'error.log')

    if os.path.exists(error_log_path):
      os.remove(error_log_path)

    with open(error_log_path, 'w') as error_log:
      error_log.write(str(e))
      exit(1)