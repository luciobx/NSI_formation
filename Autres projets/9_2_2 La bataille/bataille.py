# By Luc VINCENT 
# 2021.11.20
# Programme bataille
# 1.0
# luc.vincent@ac-bordeaux.fr


import c1
import c2
import c3
import c4
import c5

# creer le paquet de carte
paquet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, \
          1, 2, 3, 4, 5, 6, 7, 8, 9, 10, \
          1, 2, 3, 4, 5, 6, 7, 8, 9, 10, \
          1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# creer les mains des joueurs
joueur_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            
joueur_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# # mélanger les cartes
# paquet_mix = c1.melanger(paquet)
# # distribuer les cartes
# c2.distribuer(paquet_mix, joueur_1, joueur_2)
#   
# while True:
#     if c3.fin_plis(joueur_1, joueur_2):
#         break
# # Désigner le vainqueur
# vainqueur = c4.quel_vainqueur(joueur_1, joueur_2)
# # afficher le vainqueur
# c5.afficher(vainqueur)

# Pour jouer 25 parties
for i in range(25):
    # mélanger les cartes
    paquet_mix = c1.melanger(paquet)
    # distribuer les cartes
    c2.distribuer(paquet_mix, joueur_1, joueur_2)
    # jouer
    c3.fin_plis(joueur_1, joueur_2)
    # Désigner le vainqueur
    vainqueur = c4.quel_vainqueur(joueur_1, joueur_2)
    # afficher le vainqueur
    print(f"Partie {i+1} :", end=" ")
    c5.afficher(vainqueur)

if __name__ == "__main__":
    # creer le paquet de carte
    paquet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, \
          1, 2, 3, 4, 5, 6, 7, 8, 9, 10, \
          1, 2, 3, 4, 5, 6, 7, 8, 9, 10, \
          1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # creer les mains des joueurs
    joueur_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            
    joueur_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print("Le paquet mélangé")
    print(paquet_mix)
    c2.distribuer(paquet_mix, joueur_1, joueur_2)
    print("La main du joueur 1")
    print(joueur_1)
    print("La main du joueur 2")
    print(joueur_2)
    print("après la partie")
    c3.fin_plis(joueur_1, joueur_2)
    print("Les cartes du joueur 1")
    print(joueur_1)
    print("Les cartes du joueur 2")
    print(joueur_2)
    vainqueur = c4.quel_vainqueur(joueur_1, joueur_2)
    c5.afficher(vainqueur)
    
