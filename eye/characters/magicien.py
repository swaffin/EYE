"""PROJECT RPG DONJONS ET DRAGONS"""

from characters.personnage import Personnage

class Magicien(Personnage):

    def __init__(self):
        super().__init__(600, 20, 50, 25)
        self.mana = 200

    def se_soigner(self):
        self.mana -= 50
        self.vie += 100
        print(f"You still have \033[95m{self.mana} of Mana and your life goes back{self.vie} points")
        if self.mana == 0:
            print("\033[31mYou can no longer heal yourself")
         
        
        
