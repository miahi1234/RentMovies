from Repo.Repository import Repo

class InchiriereRepo(Repo):
    def __init__(self, clientRepo, filmRepo):
        super().__init__()
        self.__clientRepo=clientRepo
        self.__filmRepo=filmRepo

    def inchiriere(self, inchiriere):
        super().adauga(inchiriere)
        filmID=int(inchiriere.getFilmID())
        film=self.__filmRepo.index(filmID)
        clientID=int(inchiriere.getClientID())
        client=self.__clientRepo.index(clientID)
        nr=int(film.getNrInchirieri())+1
        film.setNrInchirieri(nr)
        nr=int(client.getNrInchirieri())+1
        client.setNrInchirieri(nr)

    def returnare(self, inchiriere):
        super().sterge(inchiriere.getID())
        filmID=int(inchiriere.getFilmID())
        film=self.__filmRepo.index(filmID)
        clientID=int(inchiriere.getClientID())
        client=self.__clientRepo.index(clientID)
        nr=int(film.getNrInchirieri())-1
        film.setNrInchirieri(nr)
        nr=int(client.getNrInchirieri())-1
        client.setNrInchirieri(nr)