import pandas as pd
import yfinance as yf
import os # # 파일경로 지정하기. os.path 사용
from datetime import date, datetime # datetime 모듈내 date, datetime
import matplotlib.pyplot as plt

def read_stocks_from_CSV(file=""):
    file = "input.csv" if not file else file # if not file: file = "input.csv" else: file = file

    # file = "input.csv"
    # file_path = os.path.join("Data", "Input",f"{file}.csv") # "Data/Input/input"
    # file_path
    # # 상대경로는 기피한다. 무조건 절대경로를 사용하기 => os.path.abspath
    # abs_file_path = os.path.abspath("Data/Input/input") # 절대경로로 변경!
    # abs_file_path
    file_path = os.path.abspath(os.path.join("Data", "Input",f"{file}")) # 축약
    print(file_path)

    ## csv파일에 ticker/symbol값이 정의 되어 있는데,
    ## 미국주식에는 ticker/symbol값이 string
    ## 한국주식에는 symbol값이 숫자  
    
    #runtime 에러 방지
    try:
        return pd.read_csv(file_path, dtype=object)# string으로 강제변형(dtype=object)
    except FileNotFoundError:
        print(f"{file} 파일이 없습니다.")
        return None
    except pd.errors.EmptyDataError:
        print(f"{file} 파일에 데이터가 없습니다.")
        return None


read_stocks_from_CSV()



def yf_download_rev(ticker="", start="", end=""):
    """
    yf.download() 메소드에서 start date의 default날짜만 올해 1월 1일로 변경.
    나머지는 모두 동일
    """
    this_year = date.today().year
    Jan_1st_this_year = datetime(year=this_year, month=1, day=1).date()
    
    start = str(Jan_1st_this_year) if not start else start
    end = str(date.today()) if not end else end

    return yf.download(ticker, start, end)


yf_download_rev("AAPL", start="2015-09-06", end="2018-11-02")


# 이제 stock이란 dataframe을 yf_download_rev에 던진다
# 그리고 나서 dictionary 
# stock_dic = {
# "Apple": ~~ Apple의 통계자료(DataFrame),
# "삼성전자": 삼성전자의 통계자료(DataFrame)
# }

stocks = read_stocks_from_CSV()
stocks

for key, value in zip(stocks["종목명"], stocks["Ticker"]):
    print(key, value)

## dictionary making! -> dictionary comprehension
stock_dict = {key: yf_download_rev(ticker=value,start="",end="") 
              for key, value in zip(stocks["종목명"],stocks["Ticker"])}

type(stock_dict)


# stock_dict["삼성전자"]
stock_dict["Apple"]

def make_output_CSV_file(stock_dict):
    # Apple.csv, Naver.csv...
    for name, statics in stock_dict.items():
        file_path = os.path.join("Data","Output", f"{name}.csv")
        statics.to_csv(file_path)

make_output_CSV_file(stock_dict)

def get_stock_history_from_yahoo(file="", start="", end=""):
 """
    개요:
        - /Data/Input/폴더 안에 종목들이 정의가 된 csv 파일을 읽어 들일거에요. 
        - 그리고 각 종목들의 통계 자료를 /Data/Output 폴더 안에 ~~.csv파일로 저장할거에요
    인수:
        (1)file: 종목이 정의가 된 csv파일 이름(string), default는 input.csv
        (2)start: 통계 자료가 시작이 되는 날(포함), yyyy-mm-dd(string), default는 yyyy-01-01(올해의 1월 1일)
        (3)end: 통계 자료의 마지막 날(안 포함),yyyy-mm-dd(string), default는 today
    반환값:
        dictionary 형태에요, key는 종목명, value는 종목의 통계자료(DataFrame)
    stock_dict = {
        "Apple" : Apple 통계자료(DataFrame),
        "삼성전자" : 삼성전자의 통계자료(DataFrame)
    }
 """
 stocks = read_stocks_from_CSV(file=file)
 stock_dict = {key: yf_download_rev(ticker=value, start=start , end=end)
                for key, value in zip(stocks["종목명"],stocks["Ticker"])}
 make_output_CSV_file(stock_dict)
 
 return stock_dict


# stock_dict = get_stock_history_from_yahoo()

stock_dict = get_stock_history_from_yahoo()
stock_dict["코스피"]

stock_dict = get_stock_history_from_yahoo(file="index.csv", start="2020-01-01")
for key, value in stock_dict.items():
    # plt.figure(figsize=(15,5))
    # plt.figure()
    plt.plot(value["Close"], label=key)
    plt.legend()
plt.show() 