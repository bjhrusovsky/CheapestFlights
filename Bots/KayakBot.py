import time
import models.flight as Flight
from Utils.selenium_config import getDriver
import src.FlightRules as flightRules
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#   Grab the link we want to arrive on.
# location = "LAX - TYO"
# DepartDate = '2024-01-22'
# ReturnDate = '2024-01-26'
def runKayakBot(link: str, DepartureDate: str, ReturnDate: str):
    driver = getDriver()
    driver.get(link)

    #   Set the delay that we will wait for. In this case the progress bar. 
    delay = 10
    WebDriverWait(driver, delay).until(EC.text_to_be_present_in_element((By.ID, "hiddenAlertContainer"), 'Results ready'))

    flightCards = driver.find_elements(by="xpath", value=".//div[@class='nrc6']")

    #   Here we iterate through each of our flight options.
    #   From there we grab our price, departure time (with full length of flight)
    #   as well the arrival date (with full length of flight)
    flightsGathered = []
    for flight in flightCards:
        try:
            currentFlight = Flight.Flight()
            currentFlight.price = (int((flight.find_element(by="xpath", value=".//div[@class='f8F1-price-text']").text[1:]).replace(',', '')))
            currentFlight.flightGoingTime = flight.find_elements(by="xpath", value=".//div[@class='vmXl vmXl-mod-variant-large']")[0].text
            currentFlight.flightReturnTime = flight.find_elements(by="xpath", value=".//div[@class='vmXl vmXl-mod-variant-large']")[1].text
            currentFlight.numOfStopsGoing = flight.find_elements(by="xpath", value=".//span[@class='JWEO-stops-text']")[0].text
            currentFlight.numOfStopsReturning = flight.find_elements(by="xpath", value=".//span[@class='JWEO-stops-text']")[1].text
            currentFlight.link = flight.find_element(by="xpath", value=".//a[@role='link']").get_attribute('href')
            currentFlight.flightDurationGoing = flight.find_elements(by="xpath", value=".//div[@class='vmXl vmXl-mod-variant-default']")[1].text
            currentFlight.flightDurationReturning = flight.find_elements(by="xpath", value=".//div[@class='vmXl vmXl-mod-variant-default']")[3].text
            currentFlight.airportNameGoing = flight.find_elements(by="xpath", value=".//span[@class='EFvI-ap-info']")[0].text \
                                             + "-" + flight.find_elements(by="xpath", value=".//span[@class='EFvI-ap-info']")[1].text
            currentFlight.airportNameReturning = flight.find_elements(by="xpath", value=".//span[@class='EFvI-ap-info']")[2].text\
                                                 + "-" + flight.find_elements(by="xpath", value=".//span[@class='EFvI-ap-info']")[3].text
            currentFlight.flightReturnDate = ReturnDate
            currentFlight.flightGoingDate = DepartureDate
        except Exception as e:
            continue
        if not flightRules.isUnderPriceLimit(currentFlight.price):
            break
        if flightRules.passesFlightPreferencesForGoingFlight(currentFlight.price,
                                                  currentFlight.numOfStopsGoing,
                                              currentFlight.flightGoingTime): flightsGathered.append(currentFlight)
    time.sleep(5)
    return flightsGathered
