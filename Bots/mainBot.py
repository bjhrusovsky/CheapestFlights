import Utils.BotUtils as BotUtils
import API.GoogleSheetsAPI as sheetsAPI
import API.sendEmail as Email
import datetime
def runBot():
    listOfValidFlights = BotUtils.getValidFlights()
    BotUtils.storeValidFLights(listOfValidFlights)

if __name__ == "__main__":
    file = open(r'C:\Users\16169\PycharmProjects\CheapestFlights\Resources\test.txt', 'a')

    file.write(f'{datetime.datetime.now()} - The script ran\n')
    # runBot()
    # sheetsAPI.writeToGoogleSheets()
    # Email.emailUser()
