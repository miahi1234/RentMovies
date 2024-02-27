from unittest import TestCase

from Domain.Film import Film


class TestFilmRepo(TestCase):
    def setUp(self):
        from Repo.FilmRepository import FilmRepo
        self.repo=FilmRepo()

    def teste(self):
        film=Film(1, 'titlu', 'descriere', 'gen', 2)
        self.repo.adauga(film)
        self.assertTrue(self.repo.cautaTitlu('titlu')==film)
        self.assertTrue(self.repo.cautaDescriere('descriere')==film)
        self.assertTrue(self.repo.cautaGen('gen')==film)