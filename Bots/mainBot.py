import Utils.BotUtils as BotUtils
import API.GoogleSheetsAPI as sheetsAPI

def exportData():
    sheetsAPI.writeToGoogleSheets()
    sheetsAPI.sendEmails()

def runBot():
    listOfValidFlights = BotUtils.getValidFlights()
    BotUtils.storeValidFLights(listOfValidFlights)
    exportData()

if __name__ == "__main__":
    runBot()


