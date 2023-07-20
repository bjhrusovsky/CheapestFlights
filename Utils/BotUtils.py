from Utils.service import Service
import sys, os
from datetime import datetime, timedelta
from itertools import product
import Bots.KayakBot as KayakBot

def buildWebsiteLink(flightPath: str, DepartureDate: str, ReturnDate: str, link: str) -> str:
    link = link.replace("LOCATION", flightPath)
    link = link.replace("DATETO", DepartureDate)
    link = link.replace("DATEFROM", ReturnDate)
    return link

def BuildKayakLink(flightPath: str, DepartureDate: str, ReturnDate: str, link):
    return buildWebsiteLink(flightPath, DepartureDate, ReturnDate, link)

def runKayakBot(flightPath: str, DepartureDate: str, ReturnDate: str, link: str):
    websiteLink = BuildKayakLink(flightPath, DepartureDate, ReturnDate, link)
    return KayakBot.runKayakBot(websiteLink, DepartureDate, ReturnDate)

def getValidFlights():
    myService = Service()
    listOfWebsites = myService.getAllWebsites()
    listOfFlightPaths = myService.getAllAirportFlightPaths()
    listOfTravelIntervals = myService.getAllTravelIntervals()
    listOfValidFlights = []
    for website, flightpath, travelInterval in product(listOfWebsites, listOfFlightPaths, listOfTravelIntervals):
        link = website[0]
        startDate = travelInterval[2]
        endDate = travelInterval[3]
        startEndDateGap = endDate - startDate
        while startEndDateGap.days >= travelInterval[1]:
            flightPathParam = flightpath
            try:
                currentReturnDate = (startDate + timedelta(days=travelInterval[1])).strftime('%Y-%m-%d')
                startDatestr = startDate.strftime('%Y-%m-%d')

                validFlights = eval(
                    "run" + website[1].lower().capitalize() + "Bot(flightPathParam, startDatestr, currentReturnDate, link)")
                startDate = (startDate + timedelta(days=1))
                startEndDateGap = endDate - startDate
                listOfValidFlights.append(validFlights)
            except Exception as e:
                print("Something went wrong within getValidFlights function.\n")
                print(e)
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print("\nError Type:")
                print(exc_type)
                print("\nFileName:")
                print(fname)
                print("\nLine Number:")
                print(exc_tb.tb_lineno)  # Error handling
                sys.exit()
    return listOfValidFlights

def storeValidFLights(ListOfValidFlights: list):
    myService = Service()
    myService.clearOldFlightData()
    for flightList in ListOfValidFlights:
        for flight in flightList:
            myService.storeValidFlight(flight)