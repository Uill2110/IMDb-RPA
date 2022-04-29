from app.config import *
import pandas as pd
from app.models.requests import get_film_data

class dataExport:
    def __init__(self, csv):
        self.csv = csv
        self.df2 = None
        self.dataframe = pd.read_csv(csv)
        self.movie_url = []
       
    def get_url(self):
        self.df2 = self.dataframe.reset_index()
        for index, row in self.df2.iterrows():
            self.movie_url.append(row[7])

        return self.movie_url
    
    def generate_final_file(self):
        
        fav_movies_url = self.get_url()
        img = []
        actors = []
        title = []
        
        for movie_url in fav_movies_url:
            movie_data   = get_film_data(movie_url)
            img.append(movie_data[0])
            title.append(movie_data[1])
            actors.append(movie_data[2])
            
        self.dataframe['Portuguese Title'] = title
        self.dataframe['Actors'] = actors
        self.dataframe['URL Image']  = img 
    
        
        pd.DataFrame((self.dataframe.rename(columns=COLS)), columns=COLS2).to_excel(FINAL_REPORT)
        