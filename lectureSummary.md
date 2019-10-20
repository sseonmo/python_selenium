# 파이썬 셀레늄(selenium)

### 인스타 크롤링
- 셀레니움을 써야하는 이유 - 기다리기 위함
- libs에 넣는 모듈화( 공통기능 )
    > 디렉토리는 반드시 python package 로 생성
- 모듈 import
    > form libs.<modele> import <함수명>  
- 셀레니움 설치
- 크롬 드리이버 설치(현재 사용하는 크롬 버전에 맞게 다운로드)
- 데이터 호출하기 때는 sleep으로 잠시 기다려주기

### facebook id, pw 입력 후 로그인 버튼 누르기
- find_element_by class, id, xpath
- send_keys
- click

### 정규식

### 네이버카페 크롤
1. 로그인
- time.sleep(20)을 걸고 수동으로 해야
1. 원하는 카페로 이동
3. 검색어 검색하기
4. 결과뽑기