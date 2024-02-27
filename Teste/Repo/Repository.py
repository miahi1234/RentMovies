from unittest import TestCase

from Domain.Entitate import Entitate


class testRepo(TestCase):
    def setUp(self):
        from Repo.Repository import Repo
        self.repo=Repo()

    def teste(self):
        entitate=Entitate(1, 0)
        self.repo.adauga(entitate)
        self.assertTrue(len(self.repo.getLista())==1)
        entitate=Entitate(1, 0)
        self.repo.modifica(entitate)
        self.assertTrue(self.repo.cautaID(1)==True)
        self.assertTrue(self.repo.index(1)==entitate)
        self.assertTrue(len(self.repo.getLista())==1)
        self.repo.sterge(1)
        self.assertTrue(len(self.repo.getLista())==0)
        self.assertTrue(self.repo.cautaID(1)==False)
        try:
            self.repo.sterge(1)
        except KeyError as error:
            print(error)
        try:
            self.repo.adauga(entitate)
            self.repo.adauga(entitate)
        except KeyError as error:
            print(error)