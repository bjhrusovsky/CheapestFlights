from datetime import datetime, time
from Utils.OpenJProperties import openFile

configs = openFile("../src/rules-config.properties")

def isUnderPriceLimit(price: int) -> bool:
    return price <= int(configs.get("priceLimit").data)

def isNonStopFlight(flightStops: str) -> bool:
    return flightStops.lower() == configs.get("numOfStops").data

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
    rule1 = isUnderPriceLimit(price)
    rule2 = isNonStopFlight(goingFlightStops)
    rule4 = isWithinTimeRange(goingTimeOfFlight)
    return isUnderPriceLimit(price) and\
           isNonStopFlight(goingFlightStops) and\
           isWithinTimeRange(goingTimeOfFlight)

def passesFlightPreferencesWithoutNonStop(price: int, goingDepartureTimeOfFlight: str, returnDepartureTimeOfFLight: str):
    return isUnderPriceLimit(price) and isWithinTimeRange(goingDepartureTimeOfFlight) and isWithinTimeRange(returnDepartureTimeOfFLight)
