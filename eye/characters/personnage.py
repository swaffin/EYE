"""class mère project rpg"""

class Personnage:
    
    def __init__(self, vie, attaque, défense, agilité):
        self.vie = vie
        self.attaque = attaque
        self.défense = défense
        self.agilité = agilité
       
    def __repr__(self):
        return super().__repr__()