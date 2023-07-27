from __future__ import print_function
import smtplib

from Utils.service import Service
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import API.getGoogleAPICredentials as CREDS
from Utils.OpenJProperties import openFile

import Resources.passwordEncryption as Encrypt
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1X5jnb-A97bQxlZYVP_79ViK6VrdprD9ov7x5NobHWJU'


def writeToGoogleSheets():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = CREDS.initCredentials(SCOPES)

    try:
        service = build('sheets', 'v4', credentials=creds)
        # Call the Sheets API
        sheet = service.spreadsheets()

        myService = Service()
        listOfFlights = myService.getAllFlights()
        lengthOfList = len(listOfFlights) + 1
        range = f'FlightData!A2:L{lengthOfList}'

        results = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
                                                 range=range,
                                                 valueInputOption="USER_ENTERED",
                                                 body={
                                                     "values": listOfFlights
                                                 }).execute()

    except HttpError as err:
        print(err)

def sendEmails():
    creds = CREDS.initCredentials(SCOPES)

    configs = openFile("api-config.properties")
    '''
    Change these to your credentials and name
    '''
    privateKey, publicKey = Encrypt.loadKeys()
    encryptedPassword = open("../Resources/encrypted.password", "rb").read()
    pw = Encrypt.decrypt(encryptedPassword, privateKey)


    # Set your email credentials and load them in here.
    your_name = configs.get("name").data
    your_email = configs.get("email").data
    your_password = pw

    # If you are using something other than gmail
    # then change the 'smtp.gmail.com' and 465 in the line below
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(your_email, your_password)

    #prepare our data from sheets and gather the emails to send to.
    service = build('sheets', 'v4', credentials=creds)
    range = 'EmailData!A1:B3'
    result = service.spreadsheets().values().batchGet(
        spreadsheetId=SPREADSHEET_ID, ranges=range).execute()
    ranges = result.get('valueRanges', [])
    emails = []
    names = []
    if ranges:
        for item in ranges[0]["values"]:
            emails.append(item[0])
            names.append(item[1])
    else:
        print("We have no email data.")
    emails = ', '.join(emails)
    names = ', '.join(names)

    # Gather our data.
    name = names
    email = emails
    subject = 'Flight Data'
    message = configs.get("linkdata").data
    full_email = ("From: {0} <{1}>\n"
                  "To: {2} <{3}>\n"
                  "Subject: {4}\n\n"
                  "{5}"
                  .format(your_name, your_email, name, email, subject, message))

    try:
        server.sendmail(your_email, [email], full_email)
        print('Email to {} successfully sent!\n\n'.format(email))
    except Exception as e:
        print('Email to {} could not be sent :( because {}\n\n'.format(email, str(e)))

    # Close the smtp server
    server.close()
