from Domain.Inchiriere import Inchiriere

class InchiriereController:
    def __init__(self, inchiriereRepo):
        self.__inchiriereRepo=inchiriereRepo

    def getLista(self):
        return self.__inchiriereRepo.getLista()

    def inchiriere(self, id, clientID, filmID):
        if self.__inchiriereRepo.cautaID(id) is False:
            if self.cautaIDfilmSIclientID(filmID, clientID) is False:
                inchiriere=Inchiriere(id, clientID, filmID)
                self.__inchiriereRepo.inchiriere(inchiriere)
            else:
                raise KeyError('Clientul a închiriat deja acest film!')
        else:
            raise KeyError('Există deja o închiriere cu acest id!')

    def returnare(self, id):
        if self.__inchiriereRepo.cautaID(id) is True:
            inchiriere=self.__inchiriereRepo.index(id)
            self.__inchiriereRepo.returnare(inchiriere)
        else:
            raise KeyError('Nu există vreo închiriere cu acest ID!')

    def cautaIDfilmSIclientID(self, filmID, clientID):
        for inchiriere in self.__inchiriereRepo.getLista():
            if inchiriere.getFilmID()==filmID and inchiriere.getClientID()==clientID:
                return True
        return False