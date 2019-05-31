import os
import sys
import random
import operator # Pour trier la liste


# Liste des citations
def citations():

    citations = [
        "Un jour, Bebert a dit : Je suis le maître du monde. Après deux semaines de torture pédagogique, Bebert admit qu'il s'était trompé.",
        "Spartacus était un esclave. Bebert est un stagiaire. La différence est simple : l'esclave est un être humain, le stagiaire non.",
        "Un jour Bebert a dit : nous avons des droits et des devoirs. Narlan l'a corrigé disant : toi, tu as surtout des devoirs !",
        "Il est dit qu'on trouve des oeufs de stagiaires dans les marécages. Mais qui pond les oeufs ?",
        "Le premier qui découvrit un stagiaire dans son champ était un paysan mésopotamien. C'est ainsi que naquît le mythe de la Goule.",
        "Lovecraft était un écrivain inspiré par l'horreur cosmique, elle même inspiré par son stagiaire personnel.",
        "Il est dit que l'enfer est le lieu où les méchants signent pour l'éternité des conventions de stages.",
        "Un jour, Narlan a eu une idée. Il a retiré le cerveau de Bebert et l'a branché à une machine. Ainsi est né l'assistant Bebert.",
        "L'assistant Bebert est né lorsque Bebert à fait une grosse bêtise.",
        "Dans certains pays, les stagiaires n'ont pas le droit de faire des études, de formations, ni aucune activités pouvant les amener à faire un stage.",
        "On pense qu'un stagiaire peut devenir humain s'il obtient un emploi... mais attention, il devient alors un esclave, pas plus !",
        "Dans l'Empire Babylonien, les criminels ayant commis les pires atrocités étaient condamnés à effectuer un stage de deux mois.",
        "Le corps humain est constitué à 60 pourcent d'eau. Celui du stagiaire est constitué à 95 pourcent de morves.",
        "Narlan n'a jamais aimé les escaliers.",
        "Bebert mesure 1 mètre 64. Il pèse 57 kilos, parle 4 langues et a un BTS gestion administrative... d'après son CV.",
    ]

    return random.choice(citations)


# Fonctions d'initialisation de l'assistant
def démarrage():

    try:
        file = open("sauvegarde_convois.txt", "r")
        file.close ()

    except:
        file = open("sauvegarde_convois.txt", "w+")
        file.write("Maryyyyyy 1 1\n")
        file.close()

def chargement():

    try:
        liste_pseudos = []
        liste_tdc = []
        liste_besoins = []
        file = open("sauvegarde_convois.txt", "r")
        list_of_lines = []

        for line in file :
            temp = line.split()
            temp[1] = int(temp[1])
            temp[2] = int(temp[2])
            list_of_lines.append(temp)

        list_of_lines = triage_depuis_lignes(list_of_lines)

        for line in list_of_lines:
            liste_pseudos.append(str(line[0]))
            liste_tdc.append(int(line[1]))
            liste_besoins.append(int(line[2]))
            
        return liste_pseudos, liste_tdc, liste_besoins
        
    except:
        print("Erreur ! Echec de chargement de la sauvegarde !")
        print("Vérifiez qu'il ne se trouve aucune lettre dans les espaces consacré au TDC et aux besoins.")
        print("Si un membre ne reçois pas de convois, il faut indiquer un zéro dans son espace besoins.")
        print("Si vous décidez de supprimer la sauvegarde, une nouvelle sera créé au prochain lancement.")
        input("Appuyez sur entrer pour quitter le programme...")
        sys.exit()

def triage_depuis_lignes(list_of_lines):

    return sorted(list_of_lines, key=operator.itemgetter(1), reverse = True)


# Fonctions des calculs
def calcul_production_besoin_jours_totale(liste_tdc, liste_besoins):

    production_totale = 0
    for tdc in liste_tdc:
        production_totale += tdc * 48

    besoin_total = 0
    for besoin in liste_besoins:
        besoin_total += besoin

    return production_totale, besoin_total, besoin_total / production_totale

def livraisons(liste_pseudos, liste_tdc, liste_besoins, besoin_total, jours_avant_satisfation):

    liste_livraisons = []

    cpt = 0

    for pseudo in liste_pseudos:
        liste_livraisons.append(int((liste_besoins[cpt] / jours_avant_satisfation) - liste_tdc[cpt] * 48))
        cpt += 1
    
    return liste_livraisons


# Menu
def menu(liste_pseudos, liste_tdc, liste_besoins, liste_livraisons, production_totale, jours_avant_satisfation):

    choix = "rien"
    is_choice_right = False
    cpt = 0

    while is_choice_right == False:

        os.system("cls")
        print("\033[44m{}\033[0m".format(citations()))
        print("")
        print("\033[91m{:<20}{:<20}{:<20}{:<20}\033[00m".format("PSEUDO", "TDC", "BESOINS", "BALANCE"))
        print("")
        for pseudo in liste_pseudos:
            print("\033[93m{:<20}\033[00m{:<20}{:<20}{:<20}".format(pseudo, liste_tdc[cpt], liste_besoins[cpt], liste_livraisons[cpt]))
            cpt = cpt + 1
        cpt = 0

        production_totale = 0
        for tdc in liste_tdc:
            production_totale += tdc * 48

        print("")
        print("- Production totale par jour :", production_totale, "Matériaux")
        print("- Il faudrait en théorie \033[41m{}\033[00m jours pour satisfaire les besoins de tout le monde.".format(int(jours_avant_satisfation)))

        print("")
        print("")

        print("\033[92m[1]\033[00m Affichage simplifié")
        print("\033[92m[2]\033[00m Supprimer un membre")
        print("\033[92m[3]\033[00m Ajouter un membre")
        print("\033[92m[4]\033[00m Modifier un membre")
        print("")
        print("\033[92m[8]\033[00m Sauvegarder !")
        print("\033[92m[9]\033[00m Quitter sans sauvegarder")
        print("Choix : ", end = " ")
        choix = input()

        if choix == "1" or choix == "9" or choix == "2" or choix == "3" or choix == "4" or choix == "8":
            is_choice_right = True

    return choix

def affichage_simplifié(liste_pseudos, liste_livraisons):

    os.system("cls")
    cpt = 0
    for membre in liste_pseudos:
        print("{:.<20} {:<20}".format(membre, liste_livraisons[cpt]))
        cpt += 1
    input("\nAppuyez sur entrer...")


# Traitement listes (supréssion, ajout, sauvegarde...)
def sup_membre(liste_pseudos, liste_tdc, liste_besoins, liste_livraisons):

    os.system("cls")
    cpt = 1
    for membre in liste_pseudos:
        print("[" + str(cpt) + "] " + membre)
        cpt = cpt + 1
    print("Suprimer : ", end = "")
    supp = input()
    try:
        supp = int(supp)
        liste_pseudos.pop(supp - 1)
        liste_tdc.pop(supp - 1)
        liste_besoins.pop(supp - 1)
        liste_livraisons.pop(supp - 1)
    except:
        os.system("cls")
        print("Erreur ! Pas de correspondace !")
        print("")
        input("Appuyez sur entrer...")

    return liste_pseudos, liste_tdc, liste_besoins, liste_livraisons

def ajout_membre(liste_pseudos, liste_tdc, liste_besoins):

    while True:
        os.system("cls")
        line = ""

        print("\033[42mRemplir 'x' pour annuler...\033[00m")
        print("")
        print("Pseudo, TDC, besoins : ", end = "")
        line = input()

        line = line.split()

        if "x" in line:
            return liste_pseudos, liste_tdc, liste_besoins
        if "X" in line:
            return liste_pseudos, liste_tdc, liste_besoins

        try:
            liste_tdc.append(int(line[1]))
            liste_besoins.append(int(line[2]))
            liste_pseudos.append(line[0])
            return liste_pseudos, liste_tdc, liste_besoins

        except:
            os.system("cls")
            print("\033[41mErreur ! Le TDC et les besoins doivent être des nombres !\033[0m")
            print("")
            input("Appuyez sur entrer...")
    
def triage_depuis_listes(liste_pseudos, liste_tdc, liste_besoins):

    list_of_lines = []
    cpt = 0

    for pseudo in liste_pseudos:
        list_of_lines.append([liste_pseudos[cpt], liste_tdc[cpt], liste_besoins[cpt]])
        cpt += 1
    
    cpt = 0
    list_of_lines = sorted(list_of_lines, key=operator.itemgetter(1), reverse = True)

    liste_pseudos = []
    liste_tdc = []
    liste_besoins = []

    for line in list_of_lines:
        liste_pseudos.append(str(line[0]))
        liste_tdc.append(int(line[1]))
        liste_besoins.append(int(line[2]))
    
    return liste_pseudos, liste_tdc, liste_besoins

def modification(liste_pseudos, liste_tdc, liste_besoins, liste_livraisons):
    
    ok = False
    os.system("cls")
    cpt = 0

    print("     {:<20}{:<20}{:<20}{:<20}".format("PSEUDO", "TDC", "BESOINS", "BALANCE"))
    print("")
    for pseudo in liste_pseudos:
        print("{} {:<20}{:<20}{:<20}{:<20}".format("["+ str(cpt+1) +"]", pseudo, liste_tdc[cpt], liste_besoins[cpt], liste_livraisons[cpt]))
        cpt = cpt + 1
    print("")
    print("Modifier : ", end = "")
    cpt = input()
    os.system("cls")

    try :
        cpt = int(cpt)
        cpt = cpt - 1
        print("\033[42mRemplir 'x' pour ne pas modifier...\033[00m")
        print("")
        print("\033[93mPseudo  \033[00m:", liste_pseudos[cpt])
        print("\033[93mTDC     \033[00m: ", end = "")
        ok = True
        
    except:
        os.system("cls")
        print("Erreur ! Le numéro indiqué ne correspond à aucun nom.")
        print("")
        input("Appuyez sur entrer...")        
        

    if ok == True:

        try:
            temp = input()
            temp = temp.replace(" ", "")

            if temp == "x" or temp == "X":
                temp = liste_tdc[cpt]
            else:
                temp = int(temp)
                liste_tdc[cpt] = temp
        
        except:
            os.system("cls")
            print("Erreur ! Entrez un nombre ou 'x' pour ne rien changer !")
            print("")
            input("Appuyez sur entrer...")        
            return liste_pseudos, liste_tdc, liste_besoins

        print("\033[93mBesoins \033[00m: ", end = "")
        
        try:
            temp = input()
            temp = temp.replace(" ", "")

            if temp == "x" or temp == "X":
                temp = liste_besoins[cpt]
            else:
                temp = int(temp)
                liste_besoins[cpt] = temp
        
        except:
            os.system("cls")
            print("Non retenu ! Entrez un nombre ou 'x' pour ne rien changer ! La valeur du TDC indiqué précédement est mémorisé.")
            print("")
            input("Appuyez sur entrer...")        
            return liste_pseudos, liste_tdc, liste_besoins

    return liste_pseudos, liste_tdc, liste_besoins


# Déclaration des listes et variables
liste_pseudos = []
liste_tdc = []
liste_besoins = []
liste_livraisons = []
besoin_total = 0
production_totale = 0
jours_avant_satisfation = 0
choix = "rien"


# Innitialisation
démarrage()
liste_pseudos, liste_tdc, liste_besoins = chargement()
production_totale, besoin_total, jours_avant_satisfation = calcul_production_besoin_jours_totale(liste_tdc, liste_besoins)
liste_livraisons = livraisons(liste_pseudos, liste_tdc, liste_besoins, besoin_total, jours_avant_satisfation)


# Boucle principale
while True:

    choix = menu(liste_pseudos, liste_tdc, liste_besoins, liste_livraisons, production_totale, jours_avant_satisfation)

    if choix == "1":

        affichage_simplifié(liste_pseudos, liste_livraisons)
    
    if choix == "2":

        liste_pseudos, liste_tdc, liste_besoins, liste_livraisons = sup_membre(liste_pseudos, liste_tdc, liste_besoins, liste_livraisons)
        liste_pseudos, liste_tdc, liste_besoins = triage_depuis_listes(liste_pseudos, liste_tdc, liste_besoins)
        production_totale, besoin_total, jours_avant_satisfation = calcul_production_besoin_jours_totale(liste_tdc, liste_besoins)
        liste_livraisons = livraisons(liste_pseudos, liste_tdc, liste_besoins, besoin_total, jours_avant_satisfation)

    if choix == "3":

        liste_pseudos, liste_tdc, liste_besoins = ajout_membre(liste_pseudos, liste_tdc, liste_besoins)
        liste_pseudos, liste_tdc, liste_besoins = triage_depuis_listes(liste_pseudos, liste_tdc, liste_besoins)
        production_totale, besoin_total, jours_avant_satisfation = calcul_production_besoin_jours_totale(liste_tdc, liste_besoins)
        liste_livraisons = livraisons(liste_pseudos, liste_tdc, liste_besoins, besoin_total, jours_avant_satisfation)

    if choix == "4":

        liste_pseudos, liste_tdc, liste_besoins = modification(liste_pseudos, liste_tdc, liste_besoins, liste_besoins)
        liste_pseudos, liste_tdc, liste_besoins = triage_depuis_listes(liste_pseudos, liste_tdc, liste_besoins)
        production_totale, besoin_total, jours_avant_satisfation = calcul_production_besoin_jours_totale(liste_tdc, liste_besoins)
        liste_livraisons = livraisons(liste_pseudos, liste_tdc, liste_besoins, besoin_total, jours_avant_satisfation)


    # Sauvegarde
    if choix == "8":

        os.system("cls")
        cpt = 0
        file = open("sauvegarde_convois.txt", "w")
        for pseudo in liste_pseudos:
            file.write(liste_pseudos[cpt] + " " + str(liste_tdc[cpt]) + " " + str(liste_besoins[cpt]) + "\n")
            cpt = cpt + 1
        file.close()

        print("\033[42mSauvegarde réussi !\033[0m")
        print("")
        input("Appuyez sur entrer...")
    
    if choix == "9":

        sys.exit()
        