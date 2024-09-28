import os
from datetime import datetime
import pandas as pd

def add():
    print("Registra Di Seguito Gli Articoli:\n")
    articolo = input("Inserisci l'articolo: \n")
    quantita = input("Inserisci la quantità: \n")
    value = input("Inserisci il valore: \n")


    lista = os.listdir()
    if "Scorte.csv" not in lista:
        with open("Scorte.csv", 'w') as x:
            x.write("Articolo,Quantita,ValUnit" + "\n")
            x.write(articolo+","+quantita+","+value+"\n")
    else:
        with open("Scorte.csv", 'a') as x:
            x.write(articolo+","+quantita+","+value+"\n")

def read():
    lista = os.listdir()
    if "Scorte.csv" in lista:
        df = pd.read_csv("Scorte.csv")
        print(df)
    else:
        print("Nessun File")