from Repo.InchiriereRepo import InchiriereRepo
from Domain.Inchiriere import Inchiriere

class InchiriereFileRepository(InchiriereRepo):
    def __init__(self, fisier, clientRepo, filmRepo):
        super().__init__(clientRepo, filmRepo)
        self.__fisier=fisier
        self.citesteFisier()

    def inchiriere(self, inchiriere):
        super().inchiriere(inchiriere)
        self.scrieFisier()

    def returnare(self, inchiriere):
        super().returnare(inchiriere)
        self.scrieFisier()

    def citesteFisier(self):
        f=open(self.__fisier, "r")
        line=f.readline().strip('\n')
        while line != '':
            list=line.split(' ')
            id=int(list[0])
            idClient=list[1]
            idFilm=list[2]
            inchiriere=Inchiriere(id, idClient, idFilm)
            line=f.readline().strip('\n')
            super().adauga(inchiriere)

    def scrieFisier(self):
        f=open(self.__fisier, "w")
        inchirieri=super().getLista()
        for inchiriere in inchirieri:
            id=inchiriere.getID()
            idClient=inchiriere.getClientID()
            idFilm=inchiriere.getFilmID()
            line=str(id) + ' ' + str(idClient) + ' ' + str(idFilm) + '\n'
            f.write(line)
        f.close()