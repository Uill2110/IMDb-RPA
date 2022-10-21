from app.models.selenium.acess_site import getCsvFile
from app.config import *
from app.models.pandas import dataExport

def main():
    imdb = getCsvFile(CHROMEDRIVER, URL , LOGIN, PWD, FAV_URL)
    
    imdb.site()
    
    imdb.login_site()
  
    imdb.download_favs()
    
    df = dataExport(DOWNLOAD_FILE)
    
    df.generate_final_file()
    
    
    
    a=1     
    
    
    
    