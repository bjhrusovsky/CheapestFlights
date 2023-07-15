import sys
sys.path.append("/SQL/my_connector.py")
from SQL.my_connector import mycursor



class DAO:
    __getAllWebsites = "SELECT * FROM WEBSITES;"
    __getAllTravelIntervals = "SELECT * FROM SEARCHINTERVALS;"
    __GetAllAirportsTo = "SELECT * FROM AirportsTo;"
    __GetAllAirportsFrom = "SELECT * FROM AirportsFrom;"
    def __init__(self):
        self.cursor = mycursor

    def executeReadQuery(self, query: str) -> list:
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def getAllWebsiteLinks(self) -> list[str]:
        myWebsites = self.executeReadQuery(self.__getAllWebsites)
        return myWebsites
    def getAllTravelIntervals(self) -> list[str]:
        myTravelIntervals = self.executeReadQuery(self.__getAllTravelIntervals)
        return myTravelIntervals
    def getAllAirports(self):
        AirportsTo = self.executeReadQuery(self.__GetAllAirportsTo)
        AirportsFrom = self.executeReadQuery(self.__GetAllAirportsFrom)
        AllAirports = []
        for airport in AirportsFrom:
            flightFrom = airport[0] + "-"
            for fromPort in AirportsTo:
                flightDirection = flightFrom + fromPort[0]
                AllAirports.append(flightDirection)
        return AllAirports

