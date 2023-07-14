from datetime import datetime, time
from Utils.OpenJProperties import openFile

configs = openFile("../src/rules-config.properties")

def isUnderPriceLimit(price: int) -> bool:
    return price <= int(configs.get("priceLimit").data)

def isNonStopFlight(flightStops: str) -> bool:
    return flightStops.lower() == configs.get("numOfStops").data

def isWithinTimeRange(timeOfFlight: str) -> bool:
    timeOfFlight = datetime.strptime(timeOfFlight, '%I:%M %p').time()
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

def passesFlightPreferencesWithoutNonStop(price: int, goingDepartureTimeOfFlight: str, returnDepartureTimeOfFLight: str):
    return isUnderPriceLimit(price) and isWithinTimeRange(goingDepartureTimeOfFlight) and isWithinTimeRange(returnDepartureTimeOfFLight)
