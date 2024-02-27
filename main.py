from Controller.ClientController import ClientController
from Controller.FilmController import FilmController
from Controller.InchiriereController import InchiriereController
from Repo.ClientFileRepository import ClientFileRepo
from Repo.FilmFileRepository import FilmFileRepo
from Repo.InchiriereFileRepository import InchiriereFileRepository
from UI.UI import UI

clientRepo=ClientFileRepo('clienti.txt')
filmRepo=FilmFileRepo('filme.txt')
inchiriereRepo=InchiriereFileRepository('inchirieri.txt', clientRepo, filmRepo)

filmController=FilmController(filmRepo)
clientController=ClientController(clientRepo)
inchiriereController=InchiriereController(inchiriereRepo)

ui=UI(clientController, filmController, inchiriereController)

ui.program()