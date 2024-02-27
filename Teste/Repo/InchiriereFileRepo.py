from unittest import TestCase
from Domain.Inchiriere import Inchiriere

class TestInchirieriFile(TestCase):
    def setUp(self):
        from Repo.ClientFileRepository import ClientFileRepo
        from Repo.FilmFileRepository import FilmFileRepo
        from Repo.InchiriereFileRepository import InchiriereFileRepository
        self.ClientRepo=ClientFileRepo('C:/Users/user/Documents/python-ap/ro/ubb/lab9-11/Teste/Repo/clienti.txt')
        self.FilmRepo=FilmFileRepo('C:/Users/user/Documents/python-ap/ro/ubb/lab9-11/Teste/Repo/filme.txt')
        self.InchiriereRepo=InchiriereFileRepository('C:/Users/user/Documents/python-ap/ro/ubb/lab9-11/Teste/Repo/inchirieri.txt', self.ClientRepo, self.FilmRepo)

    def teste(self):
        inchiriere=Inchiriere(2, 3, 1)
        self.InchiriereRepo.inchiriere(inchiriere)
        self.assertTrue(len(self.InchiriereRepo.getLista())==2)
        self.InchiriereRepo.returnare(inchiriere)
        self.assertTrue(len(self.InchiriereRepo.getLista())==1)
        self.InchiriereRepo.scrieFisier()