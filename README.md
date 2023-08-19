사업자번호로 과세여부를 조회하는 간단한 파이썬 프로그램입니다. 홈택스 서비스를 사용합니다.

[selenium](https://pypi.org/project/selenium/), [webdriver-manager](https://pypi.org/project/webdriver-manager/)를 활용하여 만들어졌습니다.

# 사용방법
> 모든 입출력 csv 파일은 euc-kr로 인코딩됩니다.

`main.exe`와 같은 위치에 **사업자번호.csv** 파일을 놓고 `main.exe` 파일을 실행시킵니다.

사업자번호 조회 결과는 동일한 경로의 **output.csv** 파일로 생성됩니다.


**사업자번호.csv 예시**
```csv
사업자번호,과세여부,조회일
000-00-00000,,
000-00-00000,,
000-00-00000,,
```

## websquare mode (기본모드)
[홈텍스 웹사이트](https://teht.hometax.go.kr/websquare/websquare.html?w2xPath=/ui/ab/a/a/UTEABAAA13.xml)를 브라우저에서 열고 사업자등록번호를 하나씩 조회합니다. 느리지만 사업자등록번호만 준비하면 바로 사용할 수 있습니다.

## OpenAPI mode
공공데이터포털 [오픈 API](https://www.data.go.kr/data/15081808/openapi.do)를 사용해서 100개씩 한번에 사업자 상태를 조회합니다.

`main.exe`와 같은 위치에 `key`라는 이름의 파일을 만들고 API 키를 저장한 다음 `main.exe` 파일을 실행하면 동작하는 모드입니다.

공공데이터포털에 가입하고 API 키를 발급받아야 사용할 수 있습니다.

다음 정보를 조회할 수 있습니다.

- 사업자번호
- 납세자 상태
- 과세유형
- 직전과세유형

# Build (Windows)
1. poetry shell
2. pyinstaller --onefile main.py
