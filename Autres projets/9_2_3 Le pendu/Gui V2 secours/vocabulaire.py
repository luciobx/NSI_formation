# By Luc VINCENT 
# 2022.01.20
# Programme vocabulaire
# 1.0
# luc.vincent@ac-bordeaux.fr
# module de pendu_console.py

import json

def open_json(cible):
    ''' Ouvrir un fichier json
    cible:str le nom du fichier à ouvrir
    rep: list[str] une liste de mots
    '''
    assert type(cible) is str, 'erreur de fichier'
    
    with open(cible) as mon_fichier:
        json_dico = json.load(mon_fichier)
    return json_dico['data'] 
    

if __name__ == "__main__":
    fichier_json = "words.json"
    words = open_json(fichier_json)
    print(words)
    