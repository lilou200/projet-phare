import mysql.connector
import os

# Fonction qui prend en parametre l id du client et la connection vers la BD, et qui permet de voir ces info ainsi que les modifier si souhaité 
def ClientInfo(id_client,connection):

    inUserInfo=1
    # Creation du curseur pour exécuter des requetes SQL
    cursorClient = connection.cursor()
    while inUserInfo:
        # Executer la requete SQL pour recuperer les elements de la table PERSONNE
        query = "SELECT * FROM PERSONNE WHERE ID_TIERS = %s;"%id_client
        cursorClient.execute(query)

        # Récupérer les resultats de la requete
        CLIENT = cursorClient.fetchall()

        if(len(CLIENT)<=0):
            print("Aucune donnée")
            return
        
        # Affiche les info de l utilisateur
        os.system("cls")
        print("=========================== Bienvenue %s =========================== "%CLIENT[0][2])
        print("| Page personnel :\n|")
        #print("| Nom :%s \t Prenom:%s \t Date de naissance:%s \t email:%s \t sexe:%s ")
        print("| Nom : %s" %CLIENT[0][1])
        print("| Prenom : %s" %CLIENT[0][2])
        print("| Date de naissance : %s" %CLIENT[0][3])
        print("| email : %s" %CLIENT[0][4])
        print("| sexe : %s \n|" %CLIENT[0][5])
        choice = int(input("| Entrez 0 pour sortir , 1 pour modifier les données utilisateur \n| "))

        if (choice ==0) : inUserInfo=0
        else :
            # Demande a l utilisateur quel info veut il modifier 
            changeUserData=1
            collumName=""
            while (changeUserData):
                print("| Quelle donnée voulez vous modifier ? \n| 1. Nom\n| 2. Prenom\n| 3. Date de naissance\n| 4. email\n| 5. sexe\n| 6. Retour")
                choice2=int(input("| "))
                if (choice2 == 1):
                    collumName="NOM"
                if (choice2 == 2):
                    collumName="PRENOM"
                if (choice2 == 3):
                    collumName="DATE_NAISSANCE"
                if (choice2 == 4):
                    collumName="EMAIL"
                if (choice2 == 5):
                    collumName="SEXE_"

                if (choice2 >= 6):
                    changeUserData=0
                else :
                    updatedThing=input("| Entrez la modification de la valeur : ")
                    #query="UPDATE PERSONNE SET %s = '%s' WHERE ID_TIERS=%d ;" %(collumName,updatedThing, id_client) 
                    query = "UPDATE PERSONNE SET {}= '{}' WHERE ID_TIERS = {};".format(collumName,updatedThing, id_client)
                    cursorClient.execute(query)
                    #print(query)     
def AjoutFournisseur(donner,connection):

    inUserInfo=1
    # Creation du curseur pour exécuter des requetes SQL
    cursor = connection.cursor()
    
        # Executer la requete SQL pour recuperer les elements de la table PERSONNE
    query = "INSERT INTO PERSONNE (NOM,PRENOM,DATE_NAISSANCE,EMAIL,SEXE)"
    donner_inserer=(donner[0],donner[1],donner[2],donner[3],donner[4])
    cursor.execute(query,donner_inserer)

    personne_id = cursor.lastrowid

    # Insertion des données dans la table "fournisseur"
    insert_fournisseur_query = "INSERT INTO FOURNISSEUR (ID_TIERS, NOM_ETABLISSEMENT) VALUES (%s, %s)"
    fournisseur_data = (personne_id, donner[5])

    cursor.execute(insert_fournisseur_query, fournisseur_data)

def AjoutPersonnel(donner,connection):

    inUserInfo=1
    # Creation du curseur pour exécuter des requetes SQL
    cursor = connection.cursor()
    
        # Executer la requete SQL pour recuperer les elements de la table PERSONNE
    query = "INSERT INTO PERSONNE (NOM,PRENOM,DATE_NAISSANCE,EMAIL,SEXE)"
    donner_inserer=(donner[0],donner[1],donner[2],donner[3],donner[4])
    cursor.execute(query,donner_inserer)

    personne_id = cursor.lastrowid

    # Insertion des données dans la table "fournisseur"
    
    insert_fournisseur_query = "INSERT INTO personnel (ID_TIERS, NOM_ETABLISSEMENT)"
    fournisseur_data = (personne_id, donner[5])

    cursor.execute(insert_fournisseur_query, fournisseur_data)

    
    # Fermeture du curseur
    #cursorClient.close()
