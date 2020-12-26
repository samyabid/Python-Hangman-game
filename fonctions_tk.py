# -*- coding: utf-8 -*-
"""
03/12/2019
VERNOUX Thomas ABID CHAREF Samy
Projet CS DEV TP2 pendu
Ce script contient les fonctions.
"""

from random import randint
from Tkinter import Tk,Label,Button,Entry,Canvas,PhotoImage
from Tkinter import *
import tkMessageBox
import tkFileDialog


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
        
        self.fenetre = Tk()
        self.image = None

    # Cette méthode permet de saisir un mot, elle le stocke dans self.mot
    # Cette méthode ne prend pas de paramètres en entrée, elle ne reourne rien 
    def choisir_mot(self):
        mon_fichier=open(self.nom_fichier,'r')
        mots = mon_fichier.read()
        mon_fichier.close()
        MOTS = mots.split("\n")
        i = randint(0,len(MOTS)-1)
        self.mot = MOTS[i]
        self.saisir_lettre()

    # Cette methode crée deux listes
    # Cette méthode ne prend pas de paramètres en entrée, elle ne reourne rien 
    def creer_listes(self):
        for car in self.mot:
            self.MOT += car
        for car in self.mot:
            self.MOT_ += "_"
        self.MOT_[0] = self.MOT[0]

    # Cette methode permet un affichage conforme aux attentes du jeux
    # Cette méthode ne prend pas de paramètres en entrée, elle ne reourne rien 
    def afficher_mot(self):
        chaine = ""
        for car in self.MOT_:
            chaine += car
        mot = Label(self.fenetre,text = chaine)
        mot.pack()

    # Cette méthode permet à l'utilisateur de saisir une lettre, elle est stockée dans self.lettre_saisie
    # Si la lettre a déjà été saisie, on recommence.
    # Cette méthode ne prend pas de paramètres en entrée, elle ne reourne rien 
    def saisir_lettre(self):
        
        
        print ("la lettre a ete saisie")
    
    # actualise l'image en fonction du nombre de vies restantes
    # Cette méthode ne prend pas de paramètres en entrée, elle ne reourne rien 
#    def actualiser_image(self):
#        if self.compteur == 8:
#            self.image = PhotoImage(file = "bonhomme8.gif")
#            photo.create_image(0,0,anchor="nw",image=dessin)
#            
#         if self.compteur == 7:
#            self.image = PhotoImage(file = "bonhomme7.gif")
#            photo.create_image(0,0,anchor="nw",image=dessin)
#            
#         if self.compteur == 6:
#            self.image = PhotoImage(file = "bonhomme6.gif")
#            photo.create_image(0,0,anchor="nw",image=dessin)
#            
#         if self.compteur == 5:
#            self.image = PhotoImage(file = "bonhomme5.gif")
#            photo.create_image(0,0,anchor="nw",image=dessin)
#            
#         if self.compteur == 4:
#            self.image = PhotoImage(file = "bonhomme4.gif")
#            photo.create_image(0,0,anchor="nw",image=dessin)
#            
#         if self.compteur == 3:
#            self.image = PhotoImage(file = "bonhomme3.gif")
#            photo.create_image(0,0,anchor="nw",image=dessin)
#            
#         if self.compteur == 2:
#            self.image = PhotoImage(file = "bonhomme2.gif")
#            photo.create_image(0,0,anchor="nw",image=dessin)
#            
#         if self.compteur == 1:
#            self.image = PhotoImage(file = "bonhomme1.gif")
#            photo.create_image(0,0,anchor="nw",image=dessin)
#            
#         if self.compteur == 0:
#            self.image = PhotoImage(file = "bonhomme0.gif")
#            photo.create_image(0,0,anchor="nw",image=dessin)
        
       
        
        
        
            
    # Trouve les positions de la lettre self.lettre_saisie dans self.MOT et les ajoutes dans la liste: self.positions_lettre
    # Cette méthode ne prend pas de paramètres en entrée, elle ne reourne rien 
    def trouver_positions_lettre(self):
        self.positions_lettre = []
        for i in range (0,len(self.MOT)):
            if self.lettre_saisie == self.MOT[i]:
                self.positions_lettre.append(i)
                
    # Modifie la liste self.MOT_, les emplacements d'indice compris dans self.positions_lettre sont modifiés
    # Cette méthode ne prend pas de paramètres en entrée, elle ne reourne rien 
    def modification_lettre(self):
        for i in self.positions_lettre:
            self.MOT_[i] = self.MOT[i]

    # Verifie si la lettre est dans le mot et agit en consequence
    # Cette méthode ne prend pas de paramètres en entrée, elle ne reourne rien 
    def verification_et_modifications(self):
        if (self.lettre_saisie in self.MOT):
            self.trouver_positions_lettre()
            self.modification_lettre()
        else:
            self.compt -= 1

    # Cette méthode réunis les méthodes précédentes pour faire un tour de jeu
    # Cette méthode ne prend pas de paramètres en entrée, elle ne reourne rien 
    def tour_de_jeu(self):
       
        
        print("Il vous reste : " , self.compt , "chance(s)")
        self.verification_et_modifications()
        #self.afficher_mot()

    # Actions éfféctuées en cas de victoire
    def victoire(self):
        self.afficher_mot()
        print ("vous avez gagné")

    # Actions éfféctuées en cas de défaite
    def defaite(self):
        print ("Vous avez perdu")
        print ("Le mot était : ",self.mot)

    # Méthode qui renvoi une valeur booléenne en fonction de l'état de la partie (est ce qu'on veut continuer)
    # Cette méthode ne prend pas de paramètres en entrée, elle ne reourne rien 
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
    # Cette méthode ne prend pas de paramètres en entrée, elle ne reourne rien 
    def jouer(self):

        self.choisir_mot()
        self.creer_listes()
        
        # Initialisation de la fenetre
        #fenetre = Tk()
        self.fenetre.geometry("500x500")        

        # Texte de bienvenue
        titre = Label(self.fenetre,text = "Bienvenue dans le monde du pendu")
        titre.pack()
        
        # Boutton quitter
        bouton_quitter=Button(self.fenetre, text="Fermer", command=self.fenetre.destroy)
        bouton_quitter.pack()
        
        # On affiche le mot
        mot = Label(self.fenetre,text = self.MOT_)
        mot.pack()
        
        # On place l'image
        photo = Canvas(self.fenetre,width=300, height=300, bg='bisque')
        dessin = PhotoImage(file = "bonhomme1.gif")
        photo.create_image(0,0,anchor="nw",image=dessin)
        photo.pack(padx=10, pady=10)
    
        # Zone de saisie du texte        
        value = StringVar()
        value.set("texte par défaut")
        entree = Entry(self.fenetre, textvariable="string", width=30)
        entree.pack()
        self.lettre_saisie = entree.get()
        
         # Boutton valider
        bouton_quitter=Button(self.fenetre, text="valider", onclick=self.saisir_lettre())
        bouton_quitter.pack()
        
        

        
        while self.condition():
            self.tour_de_jeu()
       



        self.fenetre.mainloop()









# Cette fonction met en oeuvre la classe pendu afin de faire une ou plusieurs parties.
# Cette fonction ne prend pas de paramètres en entrée, elle ne reourne rien 
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

# Cette fonction fait appel a la classe précédente pour jouer 
def jouer_au_pendu_dans_une_belle_fenetre():
    A = pendu()
    A.jouer()












        


















