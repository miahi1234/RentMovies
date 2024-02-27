from unittest import TestCase
from Domain.Client import Client

class testFileClient(TestCase):
    def setUp(self):
        from Repo.ClientFileRepository import ClientFileRepo
        self.repoFile=ClientFileRepo('C:/Users/user/Documents/python-ap/ro/ubb/lab9-11/Teste/Repo/clientiREP.txt')

    def teste(self):
        client=Client(2, 'd', 'e', 0)
        self.repoFile.adauga(client)
        self.assertTrue(len(self.repoFile.getLista())==2)
        client1=Client(2, 'g', 'j', 0)
        self.repoFile.modifica(client1)
        nume=self.repoFile.getLista()[1].getNume()
        self.assertTrue(nume=='g')
        self.repoFile.sterge(2)
        self.assertTrue(len(self.repoFile.getLista())==1)
        self.repoFile.scrieFisier()