import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


DIREC = os.path.dirname(__file__)

CHROMEDRIVER = webdriver.Chrome(executable_path=ChromeDriverManager().install())

DOWNLOAD_FILE = fr'C:\Users\{os.getlogin()}\Downloads\WATCHLIST.csv'
FINAL_REPORT = fr'Output'

LOGIN = 'yemapen969@ilusale.com'
PWD = r'12345678'
URL = 'https://www.imdb.com/'
FAV_URL = "https://www.imdb.com/user/ur157959375/watchlist?ref_=nv_usr_wl"

COLS = {'Title': 'Original Title', 
        'Year': 'Movie Year'}

COLS2 = ['Portuguese Title', 'Original Title', 
         'Movie Year', 'URL Image', 
         'Directors' , 'Actors']


def CreateFolder(folder):
        if not os.path.isdir(folder):
                os.mkdir(folder)

CreateFolder(FINAL_REPORT)