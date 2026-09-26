import mysql.connector
import os
from Display_UserInfo_And_Modifie import ClientInfo

#=====Setup de la lisaison vers la BD=====

#Testé avec ces 2 données :
#INSERT INTO `PERSONNE` (`ID_TIERS`, `NOM`, `PRENOM`, `DATE_NAISSANCE`, `EMAIL`, `SEXE_`, `PERSONNEL`, `FOURNISSEUR`) VALUES
#(1,	'Pag',	'Robert',	'1990-06-26',	'RobertPag@unamur.be',	'Homme',	1,	NULL),
#(2,	'Pag',	'Roberta',	'1991-06-26',	'RoberatPag@unamur.be',	'Femme',	1,	NULL);

    # Établir la connexion à la base de données
connection = mysql.connector.connect(
    host="localhost",
    port=3300,
    user="mysqlUser",
    password="mysqlPassword",
    database="physique"
)
#cursorClient = connection.cursor()


#=====Code principal=====
BDisON=True
while (BDisON): 
    os.system("cls")
    print("======================== Bienvenue chez LePhare ========================")
    print("| 1. Inscription")
    print("| 2. Connexion")
    print("| 3. Quitter")
    choice1=int(input("|\n| entrez 1 pour s inscire ,2 pour se connecter ou 3 pour sortir \n"))

    if (choice1==1):
         print("Si vous voulez inscrire un nouveau client ou un nouveau fournisseur, appuyez sur 1. Sinon, appuyez sur 2")
        choice2= int(input("|\n| entrez 1 pour s inscire ,2 pour supprimer \n"))
        if (choice2==1):
            execute = _FontDescription
            print("| 1. Ajout d'un Fournisseur")
            print("| 2. Ajout d'un membre de personnel")
            choice3= int(input("|\n| entrez 1 pour Fournisseur ,2 pour memebre du personnel \n"))
            if choice3==1:
                print("veuillez saisir le nom, prénom, date_naissance,email,sexe,nom de l'etablissement")
                Nom=input("Nom")
                Prenom=input("prenom")
                Date_n=input("Date de Naissance")
                Email=input("Email")
                Sexe=input("sexe")
                Etablissement=input("Nom De L'etabllissement du fournisseur")
                
                execute = AjouteFournisseur([Nom,Prenom,Date_n,Email,Sexe,Etablissement],connection)
            else: 
                Nom=input("Nom")
                Prenom=input("Prenom")
                Date_n=input("Date_Naissance")
                Email=input("Email")
                Sexe=input("Nom")
                Num_sec=input("Nom")
                Entreprise=input("Nom Entreprise")
                Num_ENTREPRISE=input("Num Entreprise")
                responsable=input("Nom Responsable")
                execute = AjoutPersonnel([Nom,Prenom,Date_n,Email,Sexe,Num_sec,Entreprise,Num_ENTREPRISE,responsable])
        else:
            execute = _FontDescription

    if (choice1==2):
        userConnected=True
         #Juste pour la demo , je demande juste l id
        chosenUser=input("Quel est votre id ?")

        while(userConnected):
            os.system("cls")
           
            
            #query = "SELECT * FROM PERSONNE WHERE ID_TIERS = %s;"%chosenUser
            #cursorClient.execute(query)
            #CLIENT = cursorClient.fetchall()

            print("=======================Bienvenue sur votre page perso=======================")
            print("| 1. Consulter ses données et les modifier")
            print("| 2. Effacer les données du compte")
            print("| 3. Passer une reservation") 
            print("| 4. Rapport Annuel+Mensuel")             #Seulement si c est le responsable
            print("| 5. Voir les personnes sous contrats")   #Seulement si c est le responsable
            print("| 6. Se deconnecter")
            choiceConnected=int(input("|\n|Veuillez choisir le nombre correspondant au choix voulu \n"))

            if (choiceConnected==1):
                ClientInfo(chosenUser,connection)
                #ClientInfo(Client_id,connection)
            if (choiceConnected==2):
                print("-")
            if (choiceConnected==3):
                print("-")
            if (choiceConnected==4):
                print("-")
            if (choiceConnected==5):
                print("-")
            if (choiceConnected==6):
                userConnected=False

    if (choice1>=3):
        BDisON=False

        #Appel de la fonction pour consulter les info client et les modifier
    Client_id=1
    


connection.close()


