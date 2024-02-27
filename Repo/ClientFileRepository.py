from Repo.ClientRepository import ClientRepo
from Domain.Client import Client

class ClientFileRepo(ClientRepo):
    def __init__(self, fisier):
        super().__init__()
        self.__fisier=fisier
        self.citesteFisier()

    def adauga(self, client):
        super().adauga(client)
        self.scrieFisier()

    def sterge(self, id):
        super().sterge(id)
        self.scrieFisier()

    def modifica(self, client):
        super().modifica(client)
        self.scrieFisier()

    def citesteFisier(self):
        f=open(self.__fisier, "r")
        line=f.readline().strip('\n')
        while line != '':
            list=line.split(' ')
            id=int(list[0])
            nume=list[1]
            prenume=list[2]
            nrInchirieri=list[3]
            client = Client(id, nume, prenume, nrInchirieri)
            line=f.readline().strip('\n')
            super().adauga(client)

    def scrieFisier(self):
        f=open(self.__fisier, "w")
        clienti=super().getLista()
        for client in clienti:
            id=client.getID()
            nume=client.getNume()
            prenume=client.getPrenume()
            nrInchirieri=client.getNrInchirieri()
            line=str(id) + ' ' + nume + ' ' + prenume + ' ' + str(nrInchirieri) + '\n'
            f.write(line)
        f.close()