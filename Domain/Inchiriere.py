class Inchiriere:
    def __init__(self, id, clientID, filmID):
        self.__id=id
        self.__clientID=clientID
        self.__filmID=filmID

    def getID(self):
        return self.__id

    def getClientID(self):
        return self.__clientID

    def getFilmID(self):
        return self.__filmID

    def setID(self, idNou):
        self.__id=idNou

    def setClientID(self, idNou):
        self.__clientID=idNou

    def setFilmID(self, idNou):
        self.__filmID=idNou

    def __str__(self):
        return 'Inchiriere: ' + str(self.getID()) + ' ' + str(self.getClientID()) + ' ' + str(self.getFilmID())