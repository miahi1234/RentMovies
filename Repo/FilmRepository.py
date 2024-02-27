from Repo.Repository import Repo

class FilmRepo(Repo):
    def __init__(self):
        super().__init__()

    def cautaTitlu(self, titlu):
        for film in self.getLista():
            if film.getTitlu()==titlu:
                return film

    def cautaDescriere(self, descriere):
        for film in self.getLista():
            if film.getDescriere()==descriere:
                return film

    def cautaGen(self, gen):
        for film in self.getLista():
            if film.getGen()==gen:
                return film