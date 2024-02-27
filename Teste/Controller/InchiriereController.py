from unittest import TestCase

class TestInchirirereController(TestCase):
    def setUp(self):
        from Controller.InchiriereController import InchiriereController
        from Repo.InchiriereFileRepository import InchiriereFileRepository
        from Repo.FilmFileRepository import FilmFileRepo
        from Repo.ClientFileRepository import ClientFileRepo
        self.filmrepo=FilmFileRepo('C:/Users/user/Documents/python-ap/ro/ubb/lab9-11/Teste/Controller/filme.txt')
        self.clientrepo=ClientFileRepo('C:/Users/user/Documents/python-ap/ro/ubb/lab9-11/Teste/Controller/clienti.txt')
        self.repo=InchiriereFileRepository('C:/Users/user/Documents/python-ap/ro/ubb/lab9-11/Teste/Controller/inchirieri.txt', self.clientrepo, self.filmrepo)
        self.controller=InchiriereController(self.repo)

    def teste(self):
        self.assertTrue(len(self.controller.getLista())==14)
        self.controller.inchiriere(15, 2, 10)
        try:
            self.controller.inchiriere(15, 2, 10)
        except KeyError as ke:
            print(ke)
        try:
            self.controller.inchiriere(16, 2, 10)
        except KeyError as ke:
            print(ke)
        try:
            self.controller.returnare(17)
        except KeyError as ke:
            print(ke)
        self.assertTrue(len(self.controller.getLista())==15)
        self.assertTrue(self.controller.cautaIDfilmSIclientID(10, 2)==True)
        self.assertTrue(self.controller.cautaIDfilmSIclientID(2, 10)==False)
        self.controller.returnare(15)
        self.assertTrue(len(self.controller.getLista())==14)
        self.repo.scrieFisier()