import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


DIREC = os.path.dirname(__file__)

CHROMEDRIVER = webdriver.Chrome(executable_path=ChromeDriverManager().install())

DOWNLOAD_FILE = fr'C:\Users\{os.getlogin()}\Downloads\WATCHLIST.csv'
FINAL_REPORT = fr'Output'

LOGIN = 'wdamasceno58@gmail.com'
PWD = r'willian.21'
URL = 'https://www.imdb.com/'
FAV_URL = "https://www.imdb.com/user/ur152557731/watchlist?ref_=nv_usr_wl"

COLS = {'Title': 'Original Title', 
        'Year': 'Movie Year'}

COLS2 = ['Portuguese Title', 'Original Title', 
         'Movie Year', 'URL Image', 
         'Directors' , 'Actors']


def CreateFolder(folder):
        if not os.path.isdir(folder):
                os.mkdir(folder)

CreateFolder(FINAL_REPORT)