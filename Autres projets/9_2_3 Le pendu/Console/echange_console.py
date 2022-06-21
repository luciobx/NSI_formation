# By Luc VINCENT 
# 2022.01.20
# Programme echange_console
# 1.0
# luc.vincent@ac-bordeaux.fr
# module de pendu_console.py



import string # pour disposer de string.ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def question(message):
    '''
    Afficher le message dans la console et renvoie le premier caractère en majuscule
    entré au clavier
    '''
    pass
    # ensemble des lettres de l'alphabet
    alphabet = set(string.ascii_uppercase)
    
    while True:
        user_choice = input(message).upper()
        if len(user_choice) > 0 and user_choice[0] in alphabet:
            return user_choice[0]
        else:
            affiche('CARACTERE NON VALIDE')
    
def affiche(message, val=''):
    '''
    Affiche le message suivi de la valeur si elle est précisée
    '''
    pass

    print(message, val)

if __name__ == "__main__":
    affiche('entrée', question("ENTRER UN CARACTERE : "))