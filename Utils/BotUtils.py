
def buildWebsiteLink(flightPath: str, DepartureDate: str, ReturnDate: str, link: str) -> str:
    link.replace("LOCATION", flightPath)
    link.replace("DATETO", DepartureDate)
    link.replace("DATEFROM", ReturnDate)
    return link


def BuildKayakLink(flightPath: str, DepartureDate: str, ReturnDate: str, link):
    return buildWebsiteLink(flightPath, DepartureDate, ReturnDate, link)