from unittest import TestCase
from Domain.Film import Film

class testFileFilm(TestCase):
    def setUp(self):
        from Repo.FilmFileRepository import FilmFileRepo
        self.repoFile=FilmFileRepo('C:/Users/user/Documents/python-ap/ro/ubb/lab9-11/Teste/Repo/filmeREP.txt')

    def teste(self):
        film=Film(2, 'd', 'e', 'f', 0)
        self.repoFile.adauga(film)
        self.assertTrue(len(self.repoFile.getLista())==2)
        film1=Film(2, 'g', 'j', 'f', 0)
        self.repoFile.modifica(film1)
        titlu=self.repoFile.getLista()[1].getTitlu()
        self.assertTrue(titlu=='g')
        self.repoFile.sterge(2)
        self.assertTrue(len(self.repoFile.getLista())==1)
        self.repoFile.scrieFisier()