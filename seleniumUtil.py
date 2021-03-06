from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
import os
import platform
# worker: python test.py


# https://github.com/heroku/heroku-buildpack-google-chrome
# https://github.com/heroku/heroku-buildpack-chromedriver
# https://github.com/waggl/heroku-buildpack-system-fonts.git

# CHROMEDRIVER_PATH = /app/.chromedriver/bin/chromedriver
# GOOGLE_CHROME_BIN = /app/.apt/usr/bin/google-chrome

def get_chrome_win():
    opt = webdriver.ChromeOptions()
    opt.add_argument('--headless')
    opt.add_argument('--disable-gpu')
    opt.add_argument('--window-size=1366x768')
    # opt.add_argument("blink-settings=imagesEnabled=false")
    opt.add_argument(
        "user-agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'")
    driver = webdriver.Chrome(options=opt)
    return driver

def get_chrome_linux():
    if(platform.system().lower() == 'windows'):
        return get_chrome_win()

    CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', '/app/.chromedriver/bin/chromedriver')
    GOOGLE_CHROME_BIN = os.environ.get('GOOGLE_CHROME_BIN', '/app/.apt/usr/bin/google-chrome')

    #CHROMEDRIVER_PATH = "chromedriver"
    #GOOGLE_CHROME_BIN = "headless-chromium"

    options = Options()
    options.binary_location = GOOGLE_CHROME_BIN
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1366x768')
    options.headless = True

    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)
    
    return driver


# driver = get_chrome()

def gethtml(url):
    driver = get_chrome_linux()
    driver.get(url)
    html = driver.page_source
    driver.quit()
    return html

def getpng(url):
    driver = get_chrome_linux()
    driver.get(url)
    png = driver.get_screenshot_as_png()
    driver.quit()
    return png
