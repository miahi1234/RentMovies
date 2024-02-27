from Domain.Entitate import Entitate

class Client(Entitate):
    def __init__(self, id, nume, prenume, nrInchirieri):
        super().__init__(id , nrInchirieri)
        self.__nume=nume
        self.__prenume=prenume

    def getNume(self):
        return self.__nume

    def getPrenume(self):
        return self.__prenume

    def setNume(self, numeNou):
        self.__nume=numeNou

    def setPrenume(self, prenumeNou):
        self.__prenume=prenumeNou

    def __str__(self):
        return "Client: " + str(self.getID()) + ' ' + self.getNume() + ' ' + self.getPrenume() + ' ' + str(self.getNrInchirieri())