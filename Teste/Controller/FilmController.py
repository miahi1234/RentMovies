from unittest import TestCase

class TestFilmController(TestCase):
    def setUp(self):
        from Controller.FilmController import FilmController
        from Repo.FilmFileRepository import FilmFileRepo
        self.repository=FilmFileRepo('C:/Users/user/Documents/python-ap/ro/ubb/lab9-11/Teste/Controller/filme.txt')
        self.controller=FilmController(self.repository)

    def teste(self):
        filme = self.controller.getLista()
        self.assertTrue(len(filme) == 10)
        self.controller.adauga(12, 'nou', 'nou', 'brumi')
        try:
            self.controller.sterge(20)
        except KeyError as ke:
            print(ke)
        try:
            self.controller.adauga(12, 'b', 'c', 'ursu')
        except KeyError as ke:
            print(ke)
        self.assertTrue(self.controller.cautaTitlu('nou') == self.controller.getLista()[10])
        self.controller.modifica(12, 'vechi', 'nou', 'ursu')
        self.assertTrue(self.controller.cautaDescriere('nou') == self.controller.getLista()[10])
        self.assertTrue(self.controller.cautaGen('ursu') == self.controller.getLista()[10])
        filmTitlu = self.controller.getLista()[10].getTitlu()
        self.assertTrue(filmTitlu == 'vechi')
        self.controller.sterge(12)
        self.assertTrue(len(self.controller.getLista()) == 10)
        filmeSort=self.controller.sortFilme()
        self.assertTrue(len(filmeSort)==10)
        self.repository.scrieFisier()