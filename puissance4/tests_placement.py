#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Mardi 05 Octobre 2021 22:17
"""

from fonctions_placement import *
from constantes import *
import unittest


class Tests(unittest.TestCase):
    
    def setUp(self):
        """
        initialise la grille pour les tests
        """
        self.grille = [[VIDE for i in range(LARGEUR)] for j in range(HAUTEUR)]
       
        # rempli la première colonne
        for i in range(HAUTEUR):
            self.grille[i][0] = JAUNE
        # place 2 jetons dans colonne 3
        self.grille[5][3] = JAUNE
        self.grille[4][3] = JAUNE

  
    def test_remplie(self):
        """
        Fonction est_remplie
        """
        self.assertTrue(est_remplie(self.grille, 0))
        self.assertFalse(est_remplie(self.grille, 1))
        
    


if __name__ == "__main__":
    unittest.main()	
