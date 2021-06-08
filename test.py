from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
import os
import platform
# worker: python test.py


# https://github.com/heroku/heroku-buildpack-google-chrome
# https://github.com/heroku/heroku-buildpack-chromedriver
# CHROMEDRIVER_PATH = /app/.chromedriver/bin/chromedriver
# GOOGLE_CHROME_BIN = /app/.apt/usr/bin/google-chrome

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

    CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', '/app/.chromedriver/bin/chromedriver')
    GOOGLE_CHROME_BIN = os.environ.get('GOOGLE_CHROME_BIN', '/app/.apt/usr/bin/google-chrome')

    #CHROMEDRIVER_PATH = "chromedriver"
    #GOOGLE_CHROME_BIN = "headless-chromium"

    options = Options()
    options.binary_location = GOOGLE_CHROME_BIN
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    opt.add_argument('--window-size=1366x768')
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
