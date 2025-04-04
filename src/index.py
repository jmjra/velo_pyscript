from pyscript import display
import pandas as pd
import matplotlib.pyplot as plt
import js
from pyodide.ffi import create_proxy
# from pyodide.http import open_url
import utils as ut



# DONNEES = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQBmY_1b2XT94E60Ma_PcEVQcuonGk6r9DR-oXNB2KhrmoQtoJRfkjuqzN-w1XR8HXN0j3h_JLYyqUm/pub?gid=0&single=true&output=csv"
global flag
flag = 0


def traitement_donnees(event):

    global flag

    do = js.document.getElementById("donnees")
    #do = Element('donnees')
    #do.clear()
    do.innerHTML = ""
    if flag%2:
        #do.element.innerHTML = f"""Nombre de sorties : {len(df['mètres'])}</br>
        #kilométrage estimé : {len(df['mètres'])*80} km"""
    
        #do.element.innerHTML = info
        do.innerHTML = info
        flag += 1
        
    else:
        #do.write("<img src='images/cumul_velo.png' />")
        do.innerHTML = f"<img src='images/cumul_velo.png' />"
        #do.innerHTML = f"<img src='https://docs.google.com/spreadsheets/d/e/2PACX-1vTzRuweEgvJ_ZdOKO_HwD008mGmfIWQlWPaAJWHOpJbG43j07iuLrwdFnGy102V17rnC3JO0flQCxew/pubchart?oid=12&format=interactive' />"
        #display("<img src='images/cumul_velo.png' />", target="donnees")
        flag += 1

        

def fn_cumul(event):
    _temp = "Cumul des sorties de l'année"

    donnees.innerHTML = ""    
    ut.affiche(message, f"nombre de sorties = {df.shape[0]}")

    fig, ax = plt.subplots(figsize=(5,5))

    #ax.set_xticks(rotation = 30)
    ax.tick_params(axis='x', labelrotation = 45)
    
    ax = plt.plot(df['nb jours'], df['cum'], 'o--', color='teal')
    
    display(fig, target="donnees")
    #ut.affiche(donnees, fig)



    
def fn_semaine(event):
    _temp = "Passage par semaine"

    donnees.innerHTML = ""

    _x = df['sem'].to_list()
    _y = df['mètres']/1000

    fig, ax = plt.subplots(figsize=(4,4))
    ax.set_xlim(0,53)
    ax = plt.plot(_x,_y, 'o--', color='green' )
    #ax = plt.stem(_x,_y)
    ut.affiche(message, _temp)

    display(fig, target="donnees")
    #ut.affiche(donnees, fig)


def fn_mois(event):
    _temp = "Cumul mois"
    #donnees.clear()
    donnees.innerHTML = ""
    ut.affiche(message, _temp)
    df_mois = df.groupby('mois')['mètres'].sum()/1000
    _x = df_mois.index.to_list()
    fig, ax = plt.subplots(figsize=(5,5))
    ax.set_xlim(0,13)
    ax = plt.bar(_x,df_mois, width=0.8, align="center")

    #ut.affiche(donnees, df_mois[2])
    display(fig, target="donnees")
    #ut.affiche(donnees, fig)

def fn_tableau(event):
    _temp = "Détail des sorties"
    #donnees.clear()
    donnees.innerHTML = ""
    ut.affiche(message, _temp)
    ut.affiche(donnees, df.tail(20).to_html())

    



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

click_bt_tableau = create_proxy(fn_tableau)
e = js.document.getElementById("bt_tableau")
e.addEventListener("click", click_bt_tableau)




#donnees = Element('donnees')
donnees =js.document.getElementById("donnees")
#cumul = Element("cumul")
cumul = js.document.getElementById("cumul")
#semaine = Element("semaine")
semaine = js.document.getElementById("semaine")
#message = Element("message")
message = js.document.getElementById("message")
#mois = Element("mois")
mois = js.document.getElementById("mois")



# chargement des données

df = ut.recup_donnees()
df['date'] = pd.to_datetime(df['date'], format="%d/%m/%Y" )
df['jour'] = df.date.dt.day
df['mois'] = df.date.dt.month
df['sem'] = df.date.dt.isocalendar().week
df['mètres'] = df['mètres'].apply(lambda x: ''.join(x.split()))
df['mètres'] = df['mètres'].apply(lambda x : str(x).replace(",","."))
df['mètres'] = df['mètres'].astype('float')
df['cum'] = df['mètres'].cumsum()/1000
bilan_cat = df.groupby('vélo')['mètres'].sum()/1000

info = f"""
Visualisation des donn&eacute;es Strava
<br />
Total 2025 :
<br />
    - Cumul = {round(df['cum'].to_list()[-1],2)} km,<br />
    """
#    - Type de vélo : <br />
#        # pelso : {bilan_cat['pelso']:0.2f} km <br />
#        # wilierT : {bilan_cat['wilierT']:0.2f} km </br>
#        # giantRevolt : {bilan_cat['giantRevolt']:0.2f} km 
        


# affiche(donnees, message)
ut.affiche(donnees, info)




