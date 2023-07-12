from Utils.selenium_config import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#   Grab the link we want to arrive on.
location = "LAX - TYO"
DepartDate = '2024-01-22'
ReturnDate = '2024-01-26'
driver.get(f'https://www.kayak.com/flights/{location}/{DepartDate}/{ReturnDate}?sort=price_a')


#   Set the delay that we will wait for
#   after we want to grab the list of flights 'nrc6' then find the information from each flight available.
delay = 10
WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'nrc6')))
flightCards = driver.find_elements(by="xpath", value=".//div[@class='nrc6']")

#   Here we iterate through each of our flight options.
#   From there we grab our price, departure time (with full length of flight)
#   as well the arrival date (with full length of flight)
for flight in flightCards:
    price = flight.find_element(by="xpath", value=".//div[@class='f8F1-price-text']").text
    departure = flight.find_elements(by="xpath", value=".//div[@class='vmXl vmXl-mod-variant-large']")
    print(departure[0].text)
    print("Second: " + departure[1].text)
