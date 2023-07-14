from Utils.selenium_config import getDriver
import src.FlightRules as flightRules
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#   Grab the link we want to arrive on.
location = "LAX - TYO"
DepartDate = '2024-01-22'
ReturnDate = '2024-01-26'
driver = getDriver()
driver.get(f'https://www.kayak.com/flights/{location}/{DepartDate}/{ReturnDate}?sort=price_a')


#   Set the delay that we will wait for
#   after we want to grab the list of flights 'nrc6' then find the information from each flight available.
delay = 10
WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'nrc6')))
flightCards = driver.find_elements(by="xpath", value=".//div[@class='nrc6']")

#   Here we iterate through each of our flight options.
#   From there we grab our price, departure time (with full length of flight)
#   as well the arrival date (with full length of flight)
flightsGathered = []
for flight in flightCards:
    tempDict = {
        "price" : int(flight.find_element(by="xpath", value=".//div[@class='f8F1-price-text']").text[1:]),
        "goingDepartureTimeOfFlight" : flight.find_elements(by="xpath", value=".//div[@class='vmXl vmXl-mod-variant-large']")[0],
        "returnDepartureTimeOfFLight": flight.find_elements(by="xpath", value=".//div[@class='vmXl vmXl-mod-variant-large']")[1],
        "isNonStopGoing" : flight.find_elements(by="xpath", value=".//span[@class='JWEO-stops-text']")[0].text,
        "isNonStopReturn" : flight.find_elements(by="xpath", value=".//span[@class='JWEO-stops-text']")[1].text
    }
    if not flightRules.isUnderPriceLimit((tempDict["price"])):
        break
    if flightRules.passesAllFlightPreferences(tempDict["price"],
                                              tempDict["isNonStopGoing"],
                                              tempDict["isNonStopReturn"],
                                              tempDict["goingDepartureTimeOfFlight"],
                                              tempDict["returnDepartureTimeOfFLight"]): flightsGathered.append(tempDict)
