
from characters.guerrier import Guerrier
from characters.archer import Archer
from characters.thomas_le_méchant import Thomas_le_méchant
from characters.magicien import Magicien
from game.naration import *
import random 
import os
C = '\033[H\033[J'
class Game:
    def __init__(self):
        self.nom = None
        self.perso = None
        self.ennemy = None
        self.magicien = Magicien()
        
        
    def player_name(self):
        # One method for the character name
        partie1()
        self.nom= input("What is your name?\n>>>\033[96m").upper()
        print(f"\033[97mWelcome! \033[96m{self.nom}\033[97m,it's time to take charge!\n")

    def character_choice(self):
        # method that will define self.perso used for the rest of the game
        print("\033[97m[\033[93mWarrior\033[97m] | [\033[32mARCHER\033[97m] | [\033[35mMAGICIAN\033[97m]\n")
        self.perso = input("Choose an adventurer among these three characters\n>>>\033[96m" ).lower()
        if self.perso == "warrior":
            self.perso = Guerrier()
            return self.perso
        elif self.perso == "archer":
            self.perso = Archer()
            return self.perso
        elif self.perso == "magician":
            self.perso = self.magicien
            return self.perso
        else:
            print("\033[31mSorry, I don't know that adventurer, pick again!")
            time.sleep(1.)
            print(C)
            self.character_choice()
            
    def ennemy_choice(self):
        #only one foe here but with a random instead it work !
        self.ennemy = Thomas_le_méchant()
        print("=============================================================================")
        print("\033[31mDIABLO\033[97m, IS APPROACHING YOU, BRINGING HIS MINIONS\n - TWO CHOICES AVAILABLE TO YOU--")
        print("Unless you play magos")
        print("=============================================================================")
        return self.ennemy

    def ennemy_vs_player(self):
        #battle loop, define start en end of the battle + action choices
        self.character_choice()
        partie2()
        self.ennemy_choice()
        while self.perso.vie > 0 and self.ennemy.vie > 0:
            print("[Attack: A , Flee: F]")
            if self.perso == self.magicien: #add magician's skill
                print("Heal youself: S")
            action = input("").lower()
            os.system('clear')
            print("========================================================")
            if action == "a":
                self.fight_action()
                self.fight_action_ennemy()
                print(f"{self.nom} | respectfully attack | {self.ennemy.name}")
                print("========================================================")
                print(f"[your health is: \033[31m{self.perso.vie} \033[97mHp]")
                print(f"[your shield is:\033[93m{self.perso.défense}\033[97mpoints]\n") 
                print(f"[\033[31m{self.ennemy.name} \033[97mhealth is:\033[31m{self.ennemy.vie}\033[97mHp\033]97mpoints]")
                print(f"[Diablo's defense is to {self.ennemy.défense} points]\n")

            if action == "s":
                self.magicien.se_soigner()
            if action == "f":
                self.flee()
                
        partie3()
        print("The fight is over, you learned well!!\ngood job")

    def fight_action(self):
        #based on character's stats, a method for calculating damage and life
        if self.ennemy.défense > 0:
            if self.ennemy.défense < self.perso.attaque:
                self.ennemy.vie -= (self.perso.attaque - self.ennemy.défense)
                self.ennemy.défense = 0
            else:
                self.ennemy.défense -= self.perso.attaque
        else:
            if self.ennemy.défense == 0:
                self.ennemy.vie -= self.perso.attaque
                if self.ennemy.vie <= 0:
                    self.ennemy.vie = 0
            else:
                self.ennemy.vie -= (self.perso.attaque - self.ennemy.défense)
        return(self.ennemy.vie)

    def fight_action_ennemy(self):
        #same than fight-action but counter attack from the foe
        if self.perso.défense > 0:
            if self.perso.défense < self.ennemy.attaque:
                self.perso.vie -= (self.ennemy.attaque - self.perso.défense)
                self.perso.défense = 0
            else:
                self.perso.défense -= self.ennemy.attaque
        else:
            if self.perso.défense == 0:
                self.perso.vie -= self.ennemy.attaque
                if self.perso.vie <= 0:
                    self.perso.vie = 0
            else:
                self.perso.vie -= (self.ennemy.attaque - self.perso.défense)
        return(self.perso.vie)

    def flee(self):
        #based on agility stat, modifying the randint modify the chance
        if random.randint(0, 100) in range(0, self.perso.agilité):
            print("Ah you're running away, I'm waiting for your email with your git-hub link !?")
            self.perso.vie = 0
        else:
            print("Stay here, you didn't commit!!")
            self.fight_action_ennemy()


