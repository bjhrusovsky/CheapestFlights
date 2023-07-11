from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
path = 'Resources/chromedriver.exe'

driver = webdriver.Chrome(path)

driver.get('https://www.expedia.com/')
