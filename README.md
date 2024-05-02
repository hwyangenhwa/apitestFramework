# APITest FrameWork

## 만든 이유
- Requests를 쓰다가 자주 쓰는 명령어를 쉽게 쓰고 싶어서 간단하게 만들어봄

## 설치모듈
- requests (pip3 install requests)

## package
 - requests_func
    - apicheck.py
        - get, post 관련 함수
            - retry_strategy : 재시도 관련 내용 정보 (total= 시도 횟수, backoff_factor= 설정된 횟수만큼 재시도 시 time.sleep을 더 증가시켜함)
            - errorCheck : 에러체크를 하는 decorator로써 에러 파일 정보 및 라인 수 리턴
    - decorator.py
        - Error 관련 모듈 decorator
- example.py : test 관련 함수
  
  ## 사용방법
  - get(url, **kwargs) 호출
  - post(url, **kwargs) 호출
