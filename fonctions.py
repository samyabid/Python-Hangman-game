"""
03/12/2019
VERNOUX Thomas ABID CHAREF Samy
Projet CS DEV TP2 pendu
Ce script contient les fonctions.
"""

from random import randint


# Définition de la classe pendu. 
class pendu:
    def __init__(self):
        self.nom_fichier = "mots.txt"
        self.mot = []
        self.MOT = []
        self.MOT_ = []
        self.lettre_saisie = ""
        self.positions_lettre = []
        self.compt = 8
        self.LETTRES_DEJA_SAISIES = []

    # Cette méthode permet de saisir un mot, elle le stocke dans self.mot
    def choisir_mot(self):
        mon_fichier=open(self.nom_fichier,'r')
        mots = mon_fichier.read()
        mon_fichier.close()
        MOTS = mots.split("\n")
        i = randint(0,len(MOTS)-1)
        self.mot = MOTS[i]

    # Cette methode crée deux listes
    def creer_listes(self):
        for car in self.mot:
            self.MOT += car
        for car in self.mot:
            self.MOT_ += "_"
        self.MOT_[0] = self.MOT[0]

    # Cette methode permet un affichage conforme aux attentes du jeux
    def afficher_mot(self):
        chaine = ""
        for car in self.MOT_:
            chaine += car
        print(chaine)

    # Cette méthode permet à l'utilisateur de saisir une lettre, elle est stockée dans self.lettre_saisie
    # Si la lettre a déjà été saisie, on recommence.
    def saisir_lettre(self):
        self.lettre_saisie = str(input("Saisissez une lettre MAJUSCULE :   "))
        while self.lettre_saisie in self.LETTRES_DEJA_SAISIES:
            self.lettre_saisie = str(input("Vous avez déjà choisi cette lettre, saisissez autre lettre MAJUSCULE :   "))
        self.LETTRES_DEJA_SAISIES.append(self.lettre_saisie)
            
    # Trouve les positions de la lettre self.lettre_saisie dans self.MOT et les ajoutes dans la liste: self.positions_lettre
    def trouver_positions_lettre(self):
        self.positions_lettre = []
        for i in range (0,len(self.MOT)):
            if self.lettre_saisie == self.MOT[i]:
                self.positions_lettre.append(i)
                
    # Modifie la liste self.MOT_, les emplacements d'indice compris dans self.positions_lettre sont modifiés
    def modification_lettre(self):
        for i in self.positions_lettre:
            self.MOT_[i] = self.MOT[i]

    # Verifie si la lettre est dans le mot et agit en consequence
    def verification_et_modifications(self):
        if (self.lettre_saisie in self.MOT):
            self.trouver_positions_lettre()
            self.modification_lettre()
        else:
            self.compt -= 1

    # Cette méthode réunis les méthodes précédentes pour faire un tour de jeu
    def tour_de_jeu(self):
        print("Il vous reste : " , self.compt , "chance(s)")
        self.saisir_lettre()
        self.verification_et_modifications()
        self.afficher_mot()

    # Actions éfféctuées en cas de victoire
    def victoire(self):
        self.afficher_mot()
        print ("vous avez gagné")

    # Actions éfféctuées en cas de défaite
    def defaite(self):
        print ("Vous avez perdu")
        print ("Le mot était : ",self.mot)

    # Méthode qui renvoi une valeur booléenne en fonction de l'état de la partie (est ce qu'on veut continuer)
    def condition(self):
        if self.compt > 0:
            if self.MOT != self.MOT_:
                return True
        if self.MOT == self.MOT_:
            self.victoire()
            return False
        if self.compt == 0:
            self.defaite()
            return False

    # Méthode qui réunit les méthodes précédentes afin de jouer
    def jouer(self):
        self.choisir_mot()
        self.creer_listes()
        self.afficher_mot()

        while self.condition():
            self.tour_de_jeu()
        print ("FIN DE LA PARTIE")
    
# Cette fonction met en oeuvre la classe pendu afin de faire une ou plusieurs parties.
def jouer_plusieurs_fois_au_pendu():
    meilleur_score = 0
    print ("Bienvenue dans l'univers du pendu")
    on_continue = True
    while on_continue:
        A = pendu()
        A.jouer()
        if A.compt > meilleur_score or meilleur_score == 0:
            meilleur_score = A.compt
        print ("Meilleur score :  ",meilleur_score)
        print ("Pourquoi pas ne pas refaire une partie ?")
        print ("Pour rejouer saisissez 'je suis accro au pendu'")
        entree = str(input())
        if entree == "je suis accro au pendu":
            on_continue = True
            print ()
            print ("NOUVELLE PARTIE")
            print ()
        else:
            on_continue = False
            print ("FIN DU PROGRAMME")
































