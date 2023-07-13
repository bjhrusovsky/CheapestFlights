import my_connector as mc

class DAO:
    __getAllWebsites = "SELECT * FROM WEBSITES;"
    def __init__(self):
        self.cursor = mc.mycursor

    def executeReadQuery(self, query: str) -> list:
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def getAllWebsiteLinks(self) -> list:
        myWebsites = self.executeReadQuery(self.__getAllWebsites)
        links = []
        for data in myWebsites:
            links.append(data[0])
        return links
