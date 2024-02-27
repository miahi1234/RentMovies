from unittest import TestCase

class testInchiriere(TestCase):
    def setUp(self):
        from Domain.Inchiriere import Inchiriere
        self.inchiriere=Inchiriere(1, 2, 3)

    def testGetteri(self):
        self.assertTrue(self.inchiriere.getID()==1)
        self.assertTrue(self.inchiriere.getClientID()==2)
        self.assertTrue(self.inchiriere.getFilmID()==3)

    def testSetteri(self):
        self.inchiriere.setID(4)
        self.inchiriere.setFilmID(5)
        self.inchiriere.setClientID(6)
        self.assertTrue(self.inchiriere.getID()==4)
        self.assertTrue(self.inchiriere.getFilmID()==5)
        self.assertTrue(self.inchiriere.getClientID()==6)

    def testSTR(self):
        self.assertTrue(self.inchiriere.__str__()=='Inchiriere: 1 2 3')