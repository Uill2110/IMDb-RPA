import os

DIREC = os.path.dirname(__file__)

CHROMEDRIVER = DIREC + r"\chromedriver.exe"

DOWNLOAD_FILE = fr'C:\Users\{os.getlogin()}\Downloads\WATCHLIST.csv'
FINAL_REPORT = fr'C:\Users\{os.getlogin()}\Documents\filmes.xlsx'

LOGIN = 'contato@fasters.com.br'
PWD = '10203040'
URL = 'https://www.imdb.com/'

COLS = {'Title': 'Original Title', 
        'Year': 'Movie Year'}

COLS2 = ['Portuguese Title', 'Original Title', 'Movie Year', 'URL Image', 'Directors' , 'Actors']