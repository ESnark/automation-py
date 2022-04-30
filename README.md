사업자번호로 과세여부를 조회하는 간단한 파이썬 프로그램입니다. 홈택스 서비스를 사용합니다.

[selenium](https://pypi.org/project/selenium/), [webdriver-manager](https://pypi.org/project/webdriver-manager/)를 활용하여 만들어졌습니다.

# 사용방법
> 모든 입출력 csv 파일은 euc-kr로 인코딩됩니다.

`main.exe`과 같은 위치에 **사업자번호.csv** 파일을 놓고 main.exe 파일을 실행시킵니다.

사업자번호 조회 결과는 동일한 경로의 **output.csv** 파일로 생성됩니다.


**사업자번호.csv 예시**
```csv
사업자번호,과세여부,조회일
000-00-00000,,
000-00-00000,,
000-00-00000,,
```

# Build (Windows)
1. `.venv\Scripts\activate.bat`
2. pyinstaller --onefile main.py
