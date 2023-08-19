import json
from typing import List
import requests
import time
import csv
from progress import printProgressBar

def runApiRequest(rows: List[str], key: str, output_path: str):
  API_URL=f'https://api.odcloud.kr/api/nts-businessman/v1/status?serviceKey={key}'

  output_file = open(output_path, 'w', newline='', encoding='euc-kr')
  writer = csv.writer(output_file)
  writer.writerow(['사업자번호', '납세자 상태', '과세유형','직전과세유형'])

  start_idx = 0
  totalCount = len(rows)

  printProgressBar(0, totalCount, prefix='진행상태:', suffix = '완료', length=50)
  while (start_idx < totalCount):
    end_idx = totalCount if totalCount < start_idx + 100 else start_idx + 100
    data = { 'b_no': list(map(lambda b_no: b_no.replace('-', ''), rows[start_idx:end_idx]))  }

    res = requests.post(API_URL, data=json.dumps(data), headers={ 'Content-Type': 'application/json' })
    res.raise_for_status()

    for i, b_status in enumerate(res.json()['data']):
      writer.writerow([rows[start_idx + i], b_status['b_stt'], b_status['tax_type'], b_status['rbf_tax_type']])

    start_idx = end_idx

    printProgressBar(end_idx, totalCount, prefix='진행상태:', suffix = '완료', length=50)
    time.sleep(1)

