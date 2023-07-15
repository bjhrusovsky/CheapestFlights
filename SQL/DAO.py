import sys
import models.flight as Flight
from SQL.my_connector import mydb
sys.path.append("/SQL/my_connector.py")

class DAO:
    __getAllWebsites = "SELECT * FROM WEBSITES;"
    __getAllTravelIntervals = "SELECT * FROM SEARCHINTERVALS;"
    __GetAllAirportsTo = "SELECT * FROM AirportsTo;"
    __GetAllAirportsFrom = "SELECT * FROM AirportsFrom;"
    __InsertFlightInfo = 'INSERT INTO FlIGHTS (airportNameGoing, airportNameReturning, price, flightGoingTime, flightReturnTime,' \
                         ' flightDurationGoing, flightDurationReturning, link, numberOfStopsGoing, numberOfStopsReturning)' \
                         ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    def __init__(self):
        self.cursor = mydb.cursor()
        self.myDatabase = mydb

    def executeQuery(self, query: str) -> list:
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def insertQuery(self, query: str, params):
        self.cursor.execute(query, params)
        return self.myDatabase.commit()

    def getAllWebsiteLinks(self) -> list[str]:
        myWebsites = self.executeQuery(self.__getAllWebsites)
        return myWebsites

    def getAllTravelIntervals(self) -> list[str]:
        myTravelIntervals = self.executeQuery(self.__getAllTravelIntervals)
        return myTravelIntervals

    def getAllAirports(self):
        AirportsTo = self.executeQuery(self.__GetAllAirportsTo)
        AirportsFrom = self.executeQuery(self.__GetAllAirportsFrom)
        AllAirports = []
        for airport in AirportsFrom:
            flightFrom = airport[0] + "-"
            for fromPort in AirportsTo:
                flightDirection = flightFrom + fromPort[0]
                AllAirports.append(flightDirection)
        return AllAirports

    def storeValidFlight(self, flightInfo: Flight.Flight):
        airportNameGoing = flightInfo.airportNameGoing
        airportNameReturning = flightInfo.airportNameReturning
        price = flightInfo.price
        flightGoingTime = flightInfo.flightGoingTime
        flightReturnTime = flightInfo.flightReturnTime
        flightDurationGoing = flightInfo.flightDurationGoing
        flightDurationReturning = flightInfo.flightDurationReturning
        link = flightInfo.link
        numberOfStopsGoing = flightInfo.numOfStopsGoing
        numberOfStopsReturning = flightInfo.numOfStopsReturning
        insertQuery = (airportNameGoing, airportNameReturning, price, flightGoingTime,
                                                flightReturnTime,flightDurationGoing, flightDurationReturning,
                                                link, numberOfStopsGoing, numberOfStopsReturning)
        self.insertQuery(self.__InsertFlightInfo, insertQuery)

