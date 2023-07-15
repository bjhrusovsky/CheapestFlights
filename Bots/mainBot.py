import Utils.BotUtils as BotUtils

def runBot():
    listOfValidFlights = BotUtils.getValidFlights()
    BotUtils.storeValidFLights(listOfValidFlights)

if __name__ == "__main__":
    runBot()
