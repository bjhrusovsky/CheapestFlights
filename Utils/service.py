import sys
from SQL.DAO import DAO
sys.path.append("/SQL/DAO")


class Service:
    __instance = None

    def __init__(self):
        self.DAO = DAO()

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def getAllWebsites(self) -> list[str]:
        return self.DAO.getAllWebsiteLinks()

    def getAllAirportFlightPaths(self):
        return self.DAO.getAllAirports()

    def getAllTravelIntervals(self):
        return self.DAO.getAllTravelIntervals()

    def storeValidFlight(self, flightInfo):
        return self.DAO.storeValidFlight(flightInfo)
