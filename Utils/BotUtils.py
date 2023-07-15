
def buildWebsiteLink(flightPath: str, DepartureDate: str, ReturnDate: str, link: str) -> str:
    link = link.replace("LOCATION", flightPath)
    link = link.replace("DATETO", DepartureDate)
    link = link.replace("DATEFROM", ReturnDate)
    return link


def BuildKayakLink(flightPath: str, DepartureDate: str, ReturnDate: str, link):
    return buildWebsiteLink(flightPath, DepartureDate, ReturnDate, link)
