from datetime import datetime
from Utils.OpenJProperties import openFile

configs = openFile("../src/rules-config.properties")

def isUnderPriceLimit(price: int) -> bool:
    return price <= int(configs.get("priceLimit").data)

def isNonStopFlight(flightStops: str) -> bool:
    numOfFlightStops = {
        "nonstop": 0,
        "1 stop": 1,
        "2 stops": 2,
        "3 stops": 3
    }
    return numOfFlightStops[flightStops.lower()] <= int(configs.get("numOfStops").data)

def isWithinTimeRange(timeOfFlight: str) -> bool:
    if timeOfFlight[-2] in '-+':
        timeOfFlight = timeOfFlight[:-2]
    timeOfFlight = timeOfFlight.split("–")
    startTimeOfFlight = timeOfFlight[0]
    timeOfFlight = datetime.strptime(startTimeOfFlight, '%I:%M %p').time()  #'YYYY:MM:DD'
    departRangeStart = datetime.strptime(configs.get("departRangeStart").data, '%I:%M %p').time()
    departRangeEnd = datetime.strptime(configs.get("departRangeEnd").data, '%I:%M %p').time()
    return departRangeStart <= timeOfFlight <= departRangeEnd

def passesAllFlightPreferences(price: int, goingFlightStops: str, returnFlightStops: str,
                            goingTimeOfFlight: str, returnTimeOfFLight: str) -> bool:
    return isUnderPriceLimit(price) and\
           isNonStopFlight(goingFlightStops) and\
           isNonStopFlight(returnFlightStops) and\
           isWithinTimeRange(goingTimeOfFlight) and\
           isWithinTimeRange(returnTimeOfFLight)

def passesFlightPreferencesForGoingFlight(price: int, goingFlightStops: str,
                            goingTimeOfFlight: str) -> bool:
    return isUnderPriceLimit(price) and\
           isNonStopFlight(goingFlightStops) and\
           isWithinTimeRange(goingTimeOfFlight)

def passesFlightPreferencesWithoutNonStop(price: int, goingDepartureTimeOfFlight: str, returnDepartureTimeOfFLight: str):
    return isUnderPriceLimit(price) and isWithinTimeRange(goingDepartureTimeOfFlight) and isWithinTimeRange(returnDepartureTimeOfFLight)
