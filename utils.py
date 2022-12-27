#import js
import pandas as pd
from pyodide.http import open_url

# affichage sur un id

def affiche(id, data):
    #id.write(data)
    #display(data, target=id)
    id.element.innerHTML = data

# récupération des donnees sur googlesheets

def recup_donnees():

    DONNEES = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQBmY_1b2XT94E60Ma_PcEVQcuonGk6r9DR-oXNB2KhrmoQtoJRfkjuqzN-w1XR8HXN0j3h_JLYyqUm/pub?gid=0&single=true&output=csv"
    _data = open_url(DONNEES)

    df = pd.read_csv(_data)
    df = df.drop(columns=['commentaire'])
    df = df[1:-2]

    return df

    
