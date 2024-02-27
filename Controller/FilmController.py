from Domain.Film import Film

class FilmController:
    def __init__(self, repo):
        self.__repo=repo

    def getLista(self):
        return self.__repo.getLista()

    def adauga(self, id, titlu, descriere, gen):
        film=Film(id, titlu, descriere, gen, 0)
        self.__repo.adauga(film)

    def sterge(self, id):
        if self.__repo.cautaID(id) is True:
            self.__repo.sterge(id)
        else:
            raise KeyError('Nu există vreun film cu acest ID!')

    def modifica(self, id, titlu, descriere, gen):
        film=Film(id, titlu, descriere, gen, 0)
        self.__repo.modifica(film)

    def cautaTitlu(self, titlu):
        return self.__repo.cautaTitlu(titlu)

    def cautaDescriere(self, descriere):
        return self.__repo.cautaDescriere(descriere)

    def cautaGen(self, gen):
        return self.__repo.cautaGen(gen)

    def sortFilme(self):
        filme=self.getLista()
        filme.sort(reverse=True, key=lambda x:x.getNrInchirieri())
        return filme