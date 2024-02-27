class UI:
    def __init__(self, clientController, filmController, inchiriereController):
        self.__clientController=clientController
        self.__filmController=filmController
        self.__inchiriereController=inchiriereController

    def menu(self):
        meniu='1. Acțiuni filme\n'
        meniu+='2. Acțiuni clienți\n'
        meniu+='3. Acțiuni închirieri'
        return meniu

    def program(self):
        meniu=self.menu()
        while True:
            print(meniu)
            try:
                comanda=int(input('Introduceți comanda: '))
                if comanda == 1:
                    self.uiActiuniFilme()
                elif comanda == 2:
                    self.uiActiuniClienti()
                elif comanda == 3:
                    self.uiActiuniInchirieri()
            except KeyError as ke:
                print(ke)
            except ValueError as error:
                print(error)

    def uiActiuniFilme(self):
        print('1. Adaugă film')
        print('2. Șterge film')
        print('3. Modifică film')
        print('4. Listă de filme')
        print('5. Caută film')
        comanda = int(input('Introduceți comanda: '))
        if comanda == 1:
            self.uiAdaugaFilm()
        elif comanda == 2:
            self.uiStergeFilm()
        elif comanda == 3:
            self.uiModificaFilm()
        elif comanda == 4:
            self.uiArataFilme()
        elif comanda == 5:
            self.cautaFilm()

    def uiActiuniClienti(self):
        print('1. Adaugă client')
        print('2. Șterge client')
        print('3. Modifică client')
        print('4. Listă de clienți')
        print('5. Caută client')
        comanda = int(input('Introduceți comanda: '))
        if comanda == 1:
            self.uiAdaugaClient()
        elif comanda == 2:
            self.uiStergeClient()
        elif comanda == 3:
            self.uiModificaClient()
        elif comanda == 4:
            self.uiArataClienti()
        elif comanda == 5:
            self.cautaClient()

    def uiAdaugaFilm(self):
        id=int(input('id: '))
        titlu=input('titlu: ')
        descriere=input('descriere: ')
        gen=input('gen: ')
        self.__filmController.adauga(id, titlu, descriere, gen)

    def uiAdaugaClient(self):
        id=int(input('id: '))
        nume=input('nume: ')
        prenume=input('prenume: ')
        self.__clientController.adauga(id, nume, prenume)

    def uiStergeFilm(self):
        id=int(input('id: '))
        self.__filmController.sterge(id)

    def uiStergeClient(self):
        id=int(input('id: '))
        self.__clientController.sterge(id)

    def uiModificaFilm(self):
        id=int(input('id: '))
        titlu=input('titlu: ')
        descriere=input('descriere: ')
        gen=input('gen: ')
        self.__filmController.modifica(id, titlu, descriere, gen)

    def uiModificaClient(self):
        id=int(input('id: '))
        nume=input('nume: ')
        prenume=input('prenume: ')
        self.__clientController.modifica(id, nume, prenume)

    def uiArataFilme(self):
        filme=self.__filmController.getLista()
        if len(filme)==0:
            print('Nu există filme!')
        else:
            for film in filme:
                print(film)

    def uiArataClienti(self):
        clienti=self.__clientController.getLista()
        if len(clienti)==0:
            print('Nu există clienți')
        else:
            for client in clienti:
                print(client)

    def cautaFilm(self):
        print('1. Caută după titlu')
        print('2. Caută dupa descriere')
        print('3. Caută după gen')
        comanda=int(input('comanda: '))
        if comanda == 1:
            titlu=input('titlu: ')
            print(self.__filmController.cautaTitlu(titlu))
        elif comanda == 2:
            descriere=input('descriere: ')
            print(self.__filmController.cautaDescriere(descriere))
        elif comanda == 3:
            gen = input('gen: ')
            print(self.__filmController.cautaGen(gen))

    def cautaClient(self):
        print('1. Caută după nume')
        print('2. Caută dupa prenume')
        comanda = int(input('comanda: '))
        if comanda == 1:
            nume=input('nume: ')
            print(self.__clientController.cautaNume(nume))
        elif comanda == 2:
            prenume=input('prenume: ')
            print(self.__clientController.cautaPrenume(prenume))

    def uiActiuniInchirieri(self):
        print('1. Închiriere')
        print('2. Returnare')
        print('3. Rapoarte')
        comanda=int(input('Introduceți comanda: '))
        if comanda == 1:
            self.uiInchiriere()
        elif comanda == 2:
             self.uiReturnare()
        elif comanda == 3:
             self.uiRapoarte()

    def uiInchiriere(self):
        id = int(input('id: '))
        idClient = int(input('id client: '))
        idFilm = int(input('id film: '))
        self.__inchiriereController.inchiriere(id, idClient, idFilm)

    def uiReturnare(self):
        id = int(input('id: '))
        self.__inchiriereController.returnare(id)

    def uiRapoarte(self):
        print('1. Clienți ordonați după nume')
        print('2. Clienți ordonați dupa numărul de filme închiriate')
        print('3. Cele mai închiriate filme')
        print('4. Primii 30% cliențî după numărul de filme închiriate')
        print('5. Închirieri')
        comanda = int(input('comanda: '))
        if comanda == 1:
            self.clientiNume()
        elif comanda == 2:
            self.topClienti()
        elif comanda == 3:
            self.topFilme()
        elif comanda == 4:
            self.procente30UI()
        elif comanda == 5:
            self.uiArataInchirieri()

    def clientiNume(self):
        clienti=self.__clientController.sortNume()
        for client in clienti:
            print(client)

    def topClienti(self):
        clienti=self.__clientController.sortNrInchirieri()
        for client in clienti:
            print(client)

    def topFilme(self):
        filme=self.__filmController.sortFilme()
        for film in filme:
            print(film)

    def procente30UI(self):
        clienti=self.__clientController.procente30()
        print(clienti)

    def uiArataInchirieri(self):
        inchirieri=self.__inchiriereController.getLista()
        for inchiriere in inchirieri:
            print(inchiriere)