from selenium import webdriver
from selenium.webdriver.chrome.options import Options


"""
@return: webdriver of chrome. This will allow web scraping amongst specific websites using the
        .get() function.
"""
def seleniumConfig() -> webdriver.Chrome:
    chrome_options = Options()
    chrome_options.add_argument("detach")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome(chrome_options)
    return driver

def getDriver() -> webdriver.Chrome:
    return seleniumConfig()
