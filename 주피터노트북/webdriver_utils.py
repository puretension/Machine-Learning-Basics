# webdriver_utils.py 파일
def get_chrome_driver():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager

    chrome_options = Options()
    chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    chrome_options.add_experimental_option("detach", True)

    # 불필요한 에러 메시지 없애기
    chrome_options.add_experimental_option("excludeSwiches", ["enable-logging"])

    service = Service(executable_path=ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=chrome_options)

