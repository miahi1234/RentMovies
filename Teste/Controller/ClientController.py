from unittest import TestCase

class TestClientController(TestCase):
    def setUp(self):
        from Controller.ClientController import ClientController
        from Repo.ClientFileRepository import ClientFileRepo
        self.repository=ClientFileRepo('C:/Users/user/Documents/python-ap/ro/ubb/lab9-11/Teste/Controller/clienti.txt')
        self.controller=ClientController(self.repository)

    def teste(self):
        clienti=self.controller.getLista()
        self.assertTrue(len(clienti)==10)
        self.controller.adauga(12, 'nou', 'nou')
        try:
            self.controller.sterge(20)
        except KeyError as ke:
            print(ke)
        try:
            self.controller.adauga(12, 'b', 'c')
        except KeyError as ke:
            print(ke)
        self.assertTrue(self.controller.cautaNume('nou')==self.controller.getLista()[10])
        self.assertTrue(len(clienti)==11)
        self.controller.modifica(12, 'vechi', 'nou')
        clientNume=self.controller.getLista()[10].getNume()
        self.assertTrue(self.controller.cautaPreume('nou')==self.controller.getLista()[10])
        self.assertTrue(clientNume=='vechi')
        self.controller.sterge(12)
        self.assertTrue(len(self.controller.getLista())==10)
        clientiSort=self.controller.sortNume()
        self.assertTrue(len(clientiSort)==10)
        clientiSort=self.controller.sortNrInchirieri()
        self.assertTrue(len(clientiSort)==10)
        clientiSort=self.controller.procente30()
        self.assertTrue(len(clientiSort)==3)
        self.repository.scrieFisier()