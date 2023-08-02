import Utils.BotUtils as BotUtils
import API.GoogleSheetsAPI as sheetsAPI


def exportData():
    """
    Write our data to our google sheets, then send out the emails.
    :return: no return value
    """
    sheetsAPI.writeToGoogleSheets()
    sheetsAPI.sendEmails()

def runBot():
    """
    Execute our program. Here we gather our flight data. Store the flights in db. Then utilize
    flight data to export to our google sheets.
    :return:
    """
    listOfValidFlights = BotUtils.getValidFlights()
    BotUtils.storeValidFLights(listOfValidFlights)
    exportData()

if __name__ == "__main__":
    runBot()


