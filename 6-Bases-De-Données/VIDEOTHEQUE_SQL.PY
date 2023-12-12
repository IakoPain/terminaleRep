#https://www.w3schools.com/python/python_mysql_getstarted.asp
import mysql.connector
from mysql.connector import FieldType


def connectBD():
    db = mysql.connector.connect(user='root', password='',
                                  host='127.0.0.1',
                                  database='videotheque')
    return db

#effectue une requete et affiche les résulats
def selectRequete(requete):
    print(requete)
    db=connectBD()
    cur = db.cursor()
    cur.execute(requete)
    enregistrements=cur.fetchall()
    #affiche le nom des champs
    for champs in cur.description:
        print("{0:30}".format(champs[0]),end='')
    print()
    #affiche les enregistrements
    for lignes in enregistrements:
        for valeurs in lignes:
            print("{0:30}".format(str(valeurs)),end='')
        print()
    cur.close()
    db.close()

#effectue une insertion de données
def insertData(requete):
    print(requete)
    db=connectBD()
    cur = db.cursor()
    cur.execute(requete)
    db.commit()
    print(cur.rowcount, "Enregistrement  inséré.")
    cur.close()
    db.close()


#demande le genre du film et retourne une chaine de caractère correspondant au genre
def choixGenre():
    print("Quel genre voulez-vous ?")
    print("1 Science-fiction ")
    print("2 Comedie")
    print("3 Policier")
    print("4 Aventure")
    numeroGenre=input("Votre choix de film ?")
    genre=""
    # A Compléter

#fonction requete Affichage de tous les films par ordre décroissant de durée
def afficheFilmsDesc():
    requete=""
    # A Compléter

#fonction requete Affichage des les films par genre
def afficheFilmsGenre():
    # A Compléter
    genre=""

#fonction requete Liste tous les films d’une durée supérieur à une valeur
def afficheFilmsDuree():
    valeur=input("durée minimale du film ?")
    # A Compléter

#fonction requete Comptabilise tous les films
def comptabiliseFilms():
    # A Compléter
    requete=""

#fonction d'insertion de film
def ajouterFilms():
    titre=input("Votre titre de film ?")
    duree=int(input("La duree du film ?"))
    genre=choixGenre()
    # A Compléter


menu='0'
while menu!='q':
    print("------------------------------------------------------------")
    print("1 Afficher tous les films par ordre décroissant de durée")
    print("2 Afficher les films par genre")
    print("3 Lister tous les films d’une durée supérieur à une valeur")
    print("4 Comptabiliser tous les films")
    print("5 Ajouter un film")
    print("q : Quitter")
    print("------------------------------------------------------------")
    menu=input("Votre choix ?")
    # A Compléter


