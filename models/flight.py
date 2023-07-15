class Flight:
    def __init__(self):
        self._airportNameGoing = None
        self._airportNameReturning = None
        self._price = None
        self._flightGoingTime = None
        self._flightReturnTime = None
        self._flightDurationGoing = None
        self._flightDurationReturning = None
        self._link = None
        self._numOfStopsGoing = None
        self._numOfStopsReturning = None

    @property
    def airportNameGoing(self):
        return self._airportNameGoing

    @airportNameGoing.setter
    def airportNameGoing(self, airportNameGoing):
        self._airportNameGoing = airportNameGoing

    @property
    def airportNameReturning(self):
        return self._airportNameReturning

    @airportNameReturning.setter
    def airportNameReturning(self, airportNameReturning):
        self._airportNameReturning = airportNameReturning

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def flightGoingTime(self):
        return self._flightGoingTime

    @flightGoingTime.setter
    def flightGoingTime(self, flightGoingTime):
        self._flightGoingTime = flightGoingTime

    @property
    def flightReturnTime(self):
        return self._flightReturnTime

    @flightReturnTime.setter
    def flightReturnTime(self, flightReturnTime):
        self._flightReturnTime = flightReturnTime

    @property
    def flightDurationGoing(self):
        return self._flightDurationGoing

    @flightDurationGoing.setter
    def flightDurationGoing(self, flightDurationGoing):
        self._flightDurationGoing = flightDurationGoing

    @property
    def flightDurationReturning(self):
        return self._flightDurationReturning

    @flightDurationReturning.setter
    def flightDurationReturning(self, flightDurationReturning):
        self._flightDurationReturning = flightDurationReturning

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, link):
        self._link = link

    @property
    def numOfStopsGoing(self):
        return self._numOfStopsGoing

    @numOfStopsGoing.setter
    def numOfStopsGoing(self, numOfStopsGoing):
        self._numOfStopsGoing = numOfStopsGoing

    @property
    def numOfStopsReturning(self):
        return self._numOfStopsReturning

    @numOfStopsReturning.setter
    def numOfStopsReturning(self, numOfStopsReturning):
        self._numOfStopsReturning = numOfStopsReturning


