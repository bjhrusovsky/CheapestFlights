# CheapestFlights WebScraper
Web scraper to find the cheapest flights. This runs utilizing the selenium library
along with jproperties. Using the webdriver we open the browser grab our desired data
and push it into a database to be analyzed along with the link to the flight in 
the event that we wish to go actually purchase that flight.

*YOU WILL NEED TO SETUP YOUR OWN DATABASE* We utilized mySQL in order to store
and schema our desired data. This will allow you to analyze your pulled data from
the query search in order to find your information.

First thing you will need to do is set up your 'app-config.properties' file.
This will be the settings connecting you do your database. Here's an example:
#Database creds no quotes necessary.
host= str                 (This will most likely be 'localhost')
user=root                   (most likely 'root')
password=superDevloper2k   (or some cool password like that)
port=3306
database=cheapflights

If you wish to modify your flight preferences. Make sure to modify the file:
rules-config.properties
