import os

DIREC = os.path.dirname(__file__)

CHROMEDRIVER = DIREC + r"\chromedriver.exe"

DOWNLOAD_FILE = fr'C:\Users\{os.getlogin()}\Downloads\WATCHLIST.csv'
FINAL_REPORT = fr'Output'

LOGIN = 'contato@fasters.com.br'
PWD = '10203040'
URL = 'https://www.imdb.com/'

COLS = {'Title': 'Original Title', 
        'Year': 'Movie Year'}

COLS2 = ['Portuguese Title', 'Original Title', 
         'Movie Year', 'URL Image', 
         'Directors' , 'Actors']



def CreateFolder(folder,replace=False):
        if not os.path.isdir(folder):
                os.mkdir(folder)

CreateFolder(FINAL_REPORT)