from unittest import TestCase
from Domain.Inchiriere import Inchiriere
from Domain.Client import Client
from Domain.Film import Film
from Teste.Domain.unittestClient import TestClient


class testInchiriereRepo(TestCase):
    def setUp(self):
        from Repo.InchiriereRepo import InchiriereRepo
        from Repo.ClientRepository import ClientRepo
        from Repo.FilmRepository import FilmRepo
        self.clientRepo=ClientRepo()
        self.filmRepo=FilmRepo()
        self.repo=InchiriereRepo(self.clientRepo, self.filmRepo)

    def teste(self):
        film=Film(1, 'a', 'b', 'c', 0)
        self.filmRepo.adauga(film)
        client=Client(1, 'd', 'e', 0)
        self.clientRepo.adauga(client)
        inchiriere=Inchiriere(1, 1, 1)
        self.repo.inchiriere(inchiriere)
        self.assertTrue(len(self.repo.getLista())==1)
        self.repo.returnare(inchiriere)
        self.assertTrue(len(self.repo.getLista())==0)