from unittest import TestCase

class TestEntitate(TestCase):
    def setUp(self):
        from Domain.Entitate import Entitate
        self.entitate=Entitate(1, 0)

    def testGetteri(self):
        self.assertTrue(self.entitate.getID()==1)
        self.assertTrue(self.entitate.getNrInchirieri()==0)

    def testSetteri(self):
        self.entitate.setID(2)
        self.assertTrue(self.entitate.getID()==2)
        self.entitate.setNrInchirieri(1)
        self.assertTrue(self.entitate.getNrInchirieri()==1)

    def testSTR(self):
        self.assertTrue(self.entitate.__str__()=='ID: 1 0')