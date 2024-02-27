class Repo:
    def __init__(self):
        self.__repo=[]

    def getLista(self):
        return self.__repo

    def adauga(self, entitate):
        if self.cautaID(entitate.getID()) is False:
            self.getLista().append(entitate)
        else:
            raise KeyError('Exista deja')

    def sterge(self, id):
        if self.cautaID(id) is True:
            for entitate in self.getLista():
                if entitate.getID()==id:
                    self.getLista().remove(entitate)
        else:
            raise KeyError('Nu exista')

    def modifica(self, entitateNoua):
        for i in range (len(self.__repo)):
            if self.__repo[i].getID()==entitateNoua.getID():
                nr=int(float(self.__repo[i].getNrInchirieri()))
                entitateNoua.setNrInchirieri(nr)
                self.__repo[i]=entitateNoua

    def cautaID(self, id):
        for entitate in self.getLista():
            if entitate.getID()==id:
                return True
        return False

    def index(self, id):
        for entitate in self.getLista():
            if entitate.getID()==id:
                return entitate