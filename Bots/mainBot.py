import Utils.BotUtils as BotUtils
import API.GoogleSheetsAPI as sheetsAPI
def runBot():
    listOfValidFlights = BotUtils.getValidFlights()
    BotUtils.storeValidFLights(listOfValidFlights)

if __name__ == "__main__":
    runBot()
    sheetsAPI.writeToGoogleSheets()
