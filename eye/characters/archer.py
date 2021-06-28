"""PROJECT RPG DONJONS ET DRAGONS"""
from characters.personnage import Personnage

class Archer(Personnage):

    def __init__(self):
        super().__init__(350, 80, 30, 50)
    