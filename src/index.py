import pandas as pd
import js
from pyodide.ffi import create_proxy
from pyodide.http import open_url
import utils as ut


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

def fn_cumul(event):
    _temp = "Passage par cumul"
    # js.alert(_temp)
    ut.aff(message, _temp)
    
def fn_semaine(event):
    _temp = "Passage par semaine"
    # js.alert(_temp)
    ut.aff(message, _temp)

def fn_mois(event):
    _temp = "Passage par mois"
    # js.alert(_temp)
    ut.aff(message, _temp)


click_bt_visu = create_proxy(recup_donnees)
e = js.document.getElementById("bt_visu")
e.addEventListener("click", click_bt_visu)

click_bt_cumul = create_proxy(fn_cumul)
e = js.document.getElementById("cumul")
e.addEventListener("click", click_bt_cumul)

click_bt_semaine = create_proxy(fn_semaine)
e = js.document.getElementById("semaine")
e.addEventListener("click", click_bt_semaine)

click_bt_mois = create_proxy(fn_mois)
e = js.document.getElementById("mois")
e.addEventListener("click", click_bt_mois)

donnees = Element('donnees')
cumul = Element("cumul")
semaine = Element("semaine")
message = Element("message")
mois = Element("mois")


info = """
Visualisation des donn&eacute;es Strava
<br />
Principe :
<br />
    - récup des données google sheet,<br />
    - traitement avec pandas,<br />
    - visualisation avec matplotlib.
"""

# affiche(donnees, message)
ut.aff(donnees, info)




