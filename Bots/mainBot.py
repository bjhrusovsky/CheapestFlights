from Utils.service import Service
import Utils.BotUtils as BotUtils
import Bots.KayakBot as KayakBot
def runKayakBot(flightPath: str, DepartureDate: str, ReturnDate: str, link: str):
    websiteLink = BotUtils.BuildKayakLink(flightPath, DepartureDate, ReturnDate, link)
    print(KayakBot.runKayakBot(websiteLink))

# def runExpediaBot(link: str):
#     print(link)

def runBot():
    myService = Service()
    ListOfWebsites = myService.getAllWebsites()
    ListOfFlightPaths = myService.getAllAirportFlightPaths()
    ListOfTravelIntervals = [[1, 10, '2024-01-01', '2024-01-03']]
    for website in ListOfWebsites:
        link = website[0]
        for flightPath in ListOfFlightPaths:
            for travelInterval in ListOfTravelIntervals:
                DepartureDate = travelInterval[2]
                ReturnDate = travelInterval[3]
                # try:
                eval("run" + website[1].lower().capitalize() + "Bot(flightPath, DepartureDate, ReturnDate, link)")
                # except Exception as e:
                #     print(e)


if __name__ == "__main__":
    runBot()
