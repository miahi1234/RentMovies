from unittest import TestCase
from Teste.Domain.unittestEntitate import TestEntitate

class Testfilm(TestCase):
    def setUp(self):
        from Domain.Film import Film
        self.film=Film(1, 'Avatar', 'foarte smek recomand', 'aventura', 3)

    def testGetteri(self):
        self.assertTrue(self.film.getID()==1)
        self.assertTrue(self.film.getTitlu()=='Avatar')
        self.assertTrue(self.film.getDescriere()=='foarte smek recomand')
        self.assertTrue(self.film.getGen()=='aventura')
        self.assertTrue(self.film.getNrInchirieri()==3)

    def testSetteri(self):
        self.film.setID(2)
        self.film.setTitlu('Forrest Gump')
        self.film.setDescriere('misto')
        self.film.setGen('comedie')
        self.film.setNrInchirieri(4)
        self.assertTrue(self.film.getID()==2)
        self.assertTrue(self.film.getTitlu()=='Forrest Gump')
        self.assertTrue(self.film.getDescriere()=='misto')
        self.assertTrue(self.film.getGen()=='comedie')
        self.assertTrue(self.film.getNrInchirieri()==4)

    def testSTR(self):
        self.assertTrue(self.film.__str__()=='Film: 1 Avatar foarte smek recomand aventura 3')