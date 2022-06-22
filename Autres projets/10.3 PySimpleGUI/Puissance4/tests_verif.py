# By Luc VINCENT 
# 2022.06.08
# Puissance4
# Un exemple de test
# 1.0
# luc.vincent@ac-bordeaux.fr
# sys.version '3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)]'

import unittest
from constantes import *

from fonctions_verif import *


class Tests(unittest.TestCase):
    
    def setUp(self):
        """
        initialise la grille pour les tests
        """
        self.grille = [[0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 2, 0, 0, 0],
                       [0, 0, 2, 1, 0, 0, 0],
                       [2, 2, 1, 1, 1, 2, 0],
                       [2, 1, 2, 1, 2, 1, 1]]


  
    def test_diagonale_montante(self):
        """
        Fonction est_remplie
        """
#         self.assertFalse() ou self.assertTrue() 
        self.assertTrue(verif_diagonale_montante(self.grille, 2, 2, 3))


if __name__ == "__main__":
    unittest.main()	
