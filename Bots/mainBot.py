from Utils.service import Service
import Utils.BotUtils as BotUtils
import Bots.KayakBot as KayakBot
from datetime import datetime, timedelta
def runKayakBot(flightPath: str, DepartureDate: str, ReturnDate: str, link: str):
    websiteLink = BotUtils.BuildKayakLink(flightPath, DepartureDate, ReturnDate, link)
    #print(KayakBot.runKayakBot(websiteLink))
    return websiteLink

# def runExpediaBot(link: str):
#     print(link)

def runBot():
    myService = Service()
    ListOfWebsites = myService.getAllWebsites()
    ListOfFlightPaths = myService.getAllAirportFlightPaths()
    ListOfTravelIntervals = [[1, 10, '2024-01-01', '2024-02-01']]
    for website in ListOfWebsites:
        link = website[0]
        for flightPath in ListOfFlightPaths:
            for travelInterval in ListOfTravelIntervals:
                startDate = travelInterval[2]
                endDate = travelInterval[3]

                startEndDateGap = datetime.strptime(endDate, '%Y-%m-%d').date() - datetime.strptime(startDate, '%Y-%m-%d').date()
                while startEndDateGap.days >= 10:
                    try:
                        currentReturnDate = datetime.strptime(startDate, '%Y-%m-%d').date() + timedelta(days=10)
                        currentReturnDate = currentReturnDate.strftime("%Y-%m-%d")
                        print(eval("run" + website[1].lower().capitalize() + "Bot(flightPath, startDate, currentReturnDate, link)"))
                        startDate = datetime.strptime(startDate, '%Y-%m-%d').date() + timedelta(days=1)
                        startEndDateGap = datetime.strptime(endDate, '%Y-%m-%d').date() -\
                                          datetime.strptime(startDate,'%Y-%m-%d').date()
                    except Exception as e:
                        print(e)




if __name__ == "__main__":
    runBot()
