# By Luc VINCENT 
# 2022.01.20
# Programme pendu_console
# 1.0
# luc.vincent@ac-bordeaux.fr


from vocabulaire import open_json
from mot import valid_word
from echange_console import question, affiche

import string


def pendu(mot):
    '''
    joue le jeu du pendu
    '''
    pass

    # ensemble des lettres valides
    word_letters = set(mot)
    # ensemble des lettres de l'alphabet
    alphabet = set(string.ascii_uppercase)
    # ensemble des lettres utilisées
    used_letters = set()
    # On initialise le ctr de vie 
    lives = len(mot)
    
    # On joue tant qu'il reste des vies ou des lettres à trouver
    
    while len(word_letters) > 0 and lives> 0:
        # Afficher les lettres utilisees
        affiche("Il vous reste ", lives)
        affiche(" vies et vous avez utilisé les lettres :", ' '.join(used_letters))
        
        # afficher le mot partiellement deviné
        partial_word = [letter if letter in used_letters else '-' for letter in mot]
        # transformer en str
        partial_word = ' '.join(partial_word)
        affiche('le mot est :', partial_word)
    
        # interroger le joueur
        user_letter = question("ENTRER UN CARACTERE : ")
        # cas possibles
        # la lettre n'est pas dans l'alphabet
        # la lettre a déjà été trouvée
        # la lettre est encore dans les lettres à trouver alphabet - guessed_letter 
        # et elle est ou pas dans le mot
        if user_letter in (alphabet - used_letters):
            # on l'ajoute dans les lettres utilisées
            used_letters.add(user_letter)
            if user_letter in word_letters:
                # elle est dans le mot alors on l'enlève
                word_letters.remove(user_letter)
            else:
                # elle n'est pas dans le mot
                affiche('CARACTERE ABSENT')
                lives = lives - 1
        elif user_letter in used_letters:
            #la lettre a déjà été trouvée
            affiche('Vous avez déjà utilisé ce caractère, essayer à nouveau')
        else:
            # Ce cas ne doit pas se produire 
            affiche('CARACTERE NON COMFORME')
    if lives > 0:
        affiche('GAGNE, , LE MOT ETAIT BIEN : ', mot)
    else:
        affiche('PERDU, LE MOT ETAIT : ', mot)
    

if __name__ == '__main__':
    # On pourra générer un génrateur de test
    # ou un test unitaire
#     the_word = 'ABANDONNED'
#     pendu(the_word)
    
    
    # test final
    fichier_json = "words.json"
    some_words = open_json(fichier_json)
    the_word = valid_word(some_words).upper()
    print(the_word) # pour debug
    pendu(the_word)
    
    
    
    
    
