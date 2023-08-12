import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()

# Chrome 웹드라이버 생성
browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화
url = 'https://finance.naver.com/sise/sise_market_sum.naver?&page=' # url + str(idx)용 

# 1. 웹페이지 이동 
browser.get(url)

time.sleep(1)

# 2. 조회항목 초기화(체크되어있는 항목 체크 해제)
checkboxes = browser.find_elements(By.NAME, 'fieldIds')
for checkbox in checkboxes:
    if checkbox.is_selected(): # 체크된 상태라면?
        checkbox.click() #클릭(체크해제)

# 3. 조회 항목 설정(원하는 항목)
items_to_select = ['PER', 'ROE', 'PBR', '유보율']
for checkbox in checkboxes:
    parent = checkbox.find_element(By.XPATH, '..') # 부모 element 찾기
    label = parent.find_element(By.TAG_NAME, 'label') # (label은 TAG_NAME), 부모의 자식 element 접근가능
   # print(label.text)
    if label.text in items_to_select: # 선택항목과 일치한다면?
        checkbox.click() # 체크

time.sleep(1)

# 4. 적용하기 클릭
btn_apply = browser.find_element(By.XPATH, '//a[@href="javascript:fieldSubmit()"]') # a태그로 찾겠다
btn_apply.click()



# 5. 데이터 추출
for idx in range(1,43): 
    # 사전 작업: 페이지 이동
    browser.get(url + str(idx)) # http://naver.com ...&page=2
    df = pd.read_html(browser.page_source)[1]
    # len(df)

    # df.head(10) # 결측치 제거전(noNamed)

    df.dropna(axis='index',how='all',inplace= True)
    #how='any' 이면 1개라도 결측치잇으면 지워라, #inplace는 실제 데이터에 반영시킴
    # 결측치 제거한후! 
    # df.head(10)

    # Column 기준 모든 data == null일때 삭제 
    df.dropna(axis='columns', how='all', inplace=True)
    df.head(10)

    if len(df) == 0: # 더 이상 가져올 데이터가 없다면?
        break

    # 6. 파일 저장하기
    # 첫 페이지만 Header(종목명/현재가/....)넣고 2p부터는 랭크만 뜨게끔
    import os

    f_name = 'kospi.csv'
    if os.path.exists(f_name): # 파일이 있다면? 헤더 제외 
        df.to_csv(f_name, encoding='utf-8-sig', index= False, mode='a', header=False)
    else: # 최초의 파일이 없다면? 헤더포함, append도 자동적으로 됨
        df.to_csv(f_name, encoding='utf-8-sig', index= False)
    print(f'{idx}페이지 완료')
browser.quit() # 브라우저 종료  