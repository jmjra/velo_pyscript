import pandas as pd
import js
from pyodide.ffi import create_proxy
from pyodide.http import open_url


# DONNEES = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQBmY_1b2XT94E60Ma_PcEVQcuonGk6r9DR-oXNB2KhrmoQtoJRfkjuqzN-w1XR8HXN0j3h_JLYyqUm/pub?gid=0&single=true&output=csv"

def recup_donnees(event):
    # dico = {"nom":['ADNET','Brunel'], "prenom":['jm','pascale']}
    DONNEES = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQBmY_1b2XT94E60Ma_PcEVQcuonGk6r9DR-oXNB2KhrmoQtoJRfkjuqzN-w1XR8HXN0j3h_JLYyqUm/pub?gid=0&single=true&output=csv"
    _data = open_url(DONNEES)

    df = pd.read_csv(_data)
    df = df.drop(columns=['commentaire'])
    df = df[1:-2]

    do = Element('donnees')
    do.clear()
    # do.write(f"Nombre de sorties : {len(df['mètres'])}")
    do.write("<img src='images/cumul_velo.png' />")

def affiche(id, data):
    id.write(data)

click_proxy = create_proxy(recup_donnees)
e = js.document.getElementById("bt_1")
e.addEventListener("click", click_proxy)


donnees = Element('donnees')

message = """
Visualisation des donn&eacute;es Strava
<br />
Principe :
<br />
    - récup des donnes google sheet,<br />
    - traitement avec pandas,<br />
    - visualisation avec matplotlib.
"""

affiche(donnees, message)





