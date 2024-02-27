from unittest import TestCase
from Teste.Domain.unittestEntitate import TestEntitate

class TestClient(TestCase):
    def setUp(self):
        from Domain.Client import Client
        self.client=Client(1, 'Ioan', 'Ionel-Ionut', 3)

    def testGetteri(self):
        self.assertTrue(self.client.getID()==1)
        self.assertTrue(self.client.getNume()=='Ioan')
        self.assertTrue(self.client.getPrenume()=='Ionel-Ionut')
        self.assertTrue(self.client.getNrInchirieri()==3)

    def testSetteri(self):
        self.client.setID(2)
        self.client.setNume('Bogdan')
        self.client.setPrenume('Bogdi')
        self.client.setNrInchirieri(2)
        self.assertTrue(self.client.getID()==2)
        self.assertTrue(self.client.getNume()=='Bogdan')
        self.assertTrue(self.client.getPrenume()=='Bogdi')
        self.assertTrue(self.client.getNrInchirieri()==2)

    def testSTR(self):
        self.assertTrue(self.client.__str__()=='Client: 1 Ioan Ionel-Ionut 3')