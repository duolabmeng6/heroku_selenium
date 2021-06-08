from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
import os
import platform
# worker: python test.py


def 浏览器_获取本地chrome():
    opt = webdriver.ChromeOptions()
    opt.add_argument('--headless')
    opt.add_argument('--disable-gpu')
    opt.add_argument('--window-size=1366x768')
    # opt.add_argument("blink-settings=imagesEnabled=false")
    opt.add_argument(
        "user-agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'")
    driver = webdriver.Chrome(options=opt)
    return driver

def testddd():
    if(platform.system().lower() == 'windows'):
        return 浏览器_获取本地chrome()

    CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', '/usr/local/bin/chromedriver')
    GOOGLE_CHROME_BIN = os.environ.get('GOOGLE_CHROME_BIN', '/usr/bin/google-chrome')

    #CHROMEDRIVER_PATH = "chromedriver"
    #GOOGLE_CHROME_BIN = "headless-chromium"

    options = Options()
    options.binary_location = GOOGLE_CHROME_BIN
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1366x768')
    # options.add_argument('--user-data-dir=/tmp/user-data')
    options.add_argument('--hide-scrollbars')
    # options.add_argument('--enable-logging')
    # options.add_argument('--log-level=0')
    options.add_argument('--single-process')
    # options.add_argument('--data-path=/tmp/data-path')
    options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--homedir=/tmp')
    # options.add_argument('--disk-cache-dir=/tmp/cache-dir')
    options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36')

    options.headless = True

    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)
    
    return driver


# driver = 浏览器_获取本地chrome()

def gethtml(url):
    driver = testddd()
    driver.get(url)
    html = driver.page_source
    return html

def getpng(url):
    driver = testddd()
    driver.get(url)

    return driver.get_screenshot_as_png()
