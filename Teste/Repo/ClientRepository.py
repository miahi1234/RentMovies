from unittest import TestCase
from Domain.Client import Client

class testClientRepository(TestCase):
    def setUp(self):
        from Repo.ClientRepository import ClientRepo
        self.repo=ClientRepo()

    def teste(self):
        client=Client(1, 'bogdan', 'ana', 3)
        self.repo.adauga(client)
        self.assertTrue(self.repo.cautaNume('bogdan')==client)
        self.assertTrue(self.repo.cautaPrenume('ana')==client)