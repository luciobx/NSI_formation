# By Luc VINCENT 
# 2022.01.20
# Programme mot
# 1.0
# luc.vincent@ac-bordeaux.fr
# module de pendu_console.py

import random

from vocabulaire import open_json

def valid_word(words):
    '''
    renvoie un mot "valide" pris au hasard dans la liste words
    words : list[str]
    a_word : str un mot valide en majuscule
    '''
    pass

if __name__ == "__main__":
    # test initial
    some_words = ['aback', 'abaft', 'abandoned', 'ill-fated', 'abashed', 'mess up', 'aberrant']
    print(valid_word(some_words))
    
#     # test complet
#     fichier_json = "words.json"
#     some_words = open_json(fichier_json)        
#   print(valid_word(some_words)) # 15 lettres max dans les mots "words.json" 