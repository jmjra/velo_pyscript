import pandas as pd
import js
from pyodide.ffi import create_proxy
# from pyodide.http import open_url
import utils as ut


# DONNEES = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQBmY_1b2XT94E60Ma_PcEVQcuonGk6r9DR-oXNB2KhrmoQtoJRfkjuqzN-w1XR8HXN0j3h_JLYyqUm/pub?gid=0&single=true&output=csv"
flag = 0


def traitement_donnees(event):

    global flag
    # global df

    do = Element('donnees')
    do.clear()
    if flag == 0:
        do.element.innerHTML = f"""Nombre de sorties : {len(df['mètres'])}</br>
        kilométrage estimé : {len(df['mètres'])*80} km"""
        flag = 1
    else:
        #do.write("<img src='images/cumul_velo.png' />")
        do.element.innerHTML = f"<img src='images/cumul_velo.png' />"
        #display("<img src='images/cumul_velo.png' />", target="donnees')
        flag = 0

def fn_cumul(event):
    _temp = "Passage par cumul"
    # js.alert(_temp)
    ut.affiche(message, df.shape)
    ut.affiche(donnees, df.tail(10).to_html())
    
def fn_semaine(event):
    _temp = "Passage par semaine"
    # js.alert(_temp)
    ut.affiche(message, _temp)

def fn_mois(event):
    _temp = "Passage par mois"
    # js.alert(_temp)
    ut.affiche(message, _temp)


click_bt_visu = create_proxy(traitement_donnees)
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


info = f"""
Visualisation des donn&eacute;es Strava
<br />
Principe :
<br />
    - récup des données google sheet,<br />
    - traitement avec pandas,<br />
    - visualisation avec matplotlib.
"""

# chargement des données

df = ut.recup_donnees()

# affiche(donnees, message)
ut.affiche(donnees, info)




