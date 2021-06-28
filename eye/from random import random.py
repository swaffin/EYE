from random import random
import pyxel
import time, sys
import socket
import itertools
import string
import tkinter as tk
from tkinter import *
import numpy as np
import pygame
import copy
R = '\033[31m'
G = '\033[32m'
W = '\033[97m'
B = '\033[94m'
C = '\033[H\033[J'
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)
SCENE_TITLE = 0
SCENE_PLAY = 1
SCENE_GAMEOVER = 2

STAR_COUNT = 100
STAR_COLOR_HIGH = 12
STAR_COLOR_LOW = 5

PLAYER_WIDTH = 8
PLAYER_HEIGHT = 8
PLAYER_SPEED = 2

BULLET_WIDTH = 2
BULLET_HEIGHT = 8
BULLET_COLOR = 11
BULLET_SPEED = 4

ENEMY_WIDTH = 8
ENEMY_HEIGHT = 8
ENEMY_SPEED = 1.5

BLAST_START_RADIUS = 1
BLAST_END_RADIUS = 8
BLAST_COLOR_IN = 7
BLAST_COLOR_OUT = 10

enemy_list = []
bullet_list = []
blast_list = []




eye = ("""  
            
                                                \033[97m//  \033[96m _______ \033[93m __   __ \033[31m _______  \033[97m//
                                                \033[97m//  \033[96m|       |\033[93m|  | |  |\033[31m|       | \033[97m//
                                                \033[97m//  \033[96m|    ___|\033[93m|  |_|  |\033[31m|    ___| \033[97m//
                                                \033[97m//  \033[96m|   |___ \033[93m|       |\033[31m|   |___  \033[97m// 

                                                \033[97m//  \033[96m|    ___|\033[93m|_     _|\033[31m|    ___| \033[97m//
                                                \033[97m//  \033[96m|   |___ \033[93m |   |   \033[31m|   |___  \033[97m//
                                                \033[97m//  \033[96m|_______|\033[93m |___|   \033[31m|_______| \033[97m//
                              \033[97m//\033[96mm _______  ______    _______  \033[93m_______  \033[31m______    _______  __   __\033[97m     //
                              \033[97m//\033[96mm|        ||    _ |  |       |\033[93m|       |\033[31m|    _ |  |   _   ||  |_|  | \033[97m  //
                              \033[97m//\033[96mm|     _  ||   | ||  |   _   |\033[93m|    ___|\033[31m|   | ||  |  |_|  ||       | \033[97m  //
                              \033[97m//\033[96mm|    |_| ||   |_||_ |  | |  |\033[93m|   | __ \033[31m|   |_||_ |       ||       |  \033[97m // 
                              \033[97m//\033[96mm|     ___||    __  ||  |_|  |\033[93m|   ||  |\033[31m|    __  ||       ||       | \033[97m  //
                              \033[97m//\033[96mm|    |    |   |  | ||       |\033[93m|   |_| |\033[31m|   |  | ||   _   || ||_|| |  \033[97m //
                              \033[97m//\033[96mm| ___|    |___|  |_||_______|\033[93m|_______|\033[31m|___|  |_||__| |__||_|   |_|  \033[97m //""")


acc =   ("""//  \033[32m╔═╗┌─┐┌─┐┌─┐┌─┐┌─┐  ┌─┐┬─┐┌─┐┌┐┌┌┬┐┌─┐┌┬┐  
        //  ╠═╣│  │  ├┤ └─┐└─┐  │ ┬├┬┘├─┤│││ │ ├┤  ││  
        //  ╩ ╩└─┘└─┘└─┘└─┘└─┘  └─┘┴└─┴ ┴┘└┘ ┴ └─┘─┴┘  \033[97m""")


def help():
  choice = input('Enter letter here:\033[93m ').upper()
cif choice == 'I':
    print("\033[H\033[J")
    print("\033[97m")
    print(open('help.txt', 'r', ).read())
    input('Press [\033[32menter\033[97m] when ready to play. ')
    print("\033[H\033[J")

def cm():
    R = '\033[31m'
    G = '\033[32m'
    W = '\033[97m'
    B = '\033[94m'
    C = '\033[H\033[J'
    print(eye)
    q1 = input("""
\033[96m##########################################################################
\033[96m# \033[97mIf you want to play xdroid type: 'droid'                               \033[96m#         \033[93m##############################
\033[96m# \033[97mIf you want to play tic tac in the terminal type: 'cm tic'.            \033[96m#         \033[93m#                            #
\033[96m# \033[97mIf you want to play enter the Wine Sever type: 'pass'                  \033[96m#         \033[93m#    \033[97mIf you need help, type: \033[93m# 
\033[96m# \033[97mif you want to Tkinter tic tac, type: 'tic'                            \033[96m#         \033[93m#             \033[97m'\033[96mhelp\033[97m'         \033[93m#
\033[96m# \033[97mif you want to play Tkinter Mineaweeper, type: 'mine'                  \033[96m#         \033[93m##############################                          
\033[96m# \033[97mif you want to play terminal minesweeper, type: 'cm mine'              \033[96m#         
\033[96m# \033[97mif you want to enter the tkinter testing page, type: 'test'            \033[96m#         
\033[96m# \033[97mif none of these option are up to your liking, type: 'N'               \033[96m#         
\033[96m##########################################################################

\033[97m>>>\033[94m""")

    if q1 == 'droid':
      print("\033[97mHave fun!")
    elif q1 == 'n':
        print("That's too bad")
        time.sleep(1.5)
        sys.exit()
    ##########################################################################################
    elif q1 == 'help':
      help()
      time.sleep(5.)
      print(C)
      cm()

    ##########################################################################################    
    elif q1 == 'dmesg':
      print(open('dmesg.txt', 'r').read())
    ##########################################################################################
    elif q1 == 'test':
        hostname = socket.gethostname()    
        IPAddr = socket.gethostbyname(hostname)
        print('\033[97m',(hostname),'\n',(IPAddr))
        print(C)
        q2 = input("This is an interested place!\n>>>\033[94m")
        if q2 == "yes it is":
            print("okay, okay, okay. Have a fun time, with Tkinter")
            window = tk.Tk()   
            #label = tk.Label(text="Hello world!")
            label = tk.Label(
                text="""Hello, Tkinter
             Testing tkinter witrh multiple quotes""",
                foreground="red",  # Set the text color to white
                background="black"  # Set the background color to black
             )
            label.pack()
            hi = tk.Label(
                text="Hello, Tkinter",
                fg="white",
                bg="black",
                width=80,
                height=7
            )
            hi.pack()
            button = tk.Button(
                text="Close this application, if you want to go back to the game!",
                width=77,
                height=7,
                bg="blue",
                fg="yellow",
            )
            button.pack()
            entry = tk.Entry(fg="yellow", bg="blue", width=50)
            entry.pack()
            label = tk.Label(text="Name")
            entry = tk.Entry()
            name = entry.get()
            name
            'real python'
            print(name)
            entry.delete(0)
            entry.delete(0, tk.END) 
            entry.insert(0, "Python")
            #window.destroy()
            text_box = tk.Text()
            text_box.pack()
            text_box.get("1.0", tk.END) 
            'Hello\nWorld\n'
            text_box.delete("1.0")
            text_box.insert(tk.END, "Less testing")
            text_box.insert(tk.END, "\nMore testing")
            window.mainloop()
    ##########################################################################################
    ###########################################################################################################################################################################################################################################################################
    elif q1 == 'cm mine':

        class bcolours:
          ResetAll     = '\033[0m'
          Default      = "\033[39m"
          Black        = "\033[30m"
          Red          = "\033[31m"
          Green        = "\033[32m"
          Yellow       = "\033[33m"
          Blue         = "\033[34m"
          Magenta      = "\033[35m"
          Cyan         = "\033[36m"
          LightGray    = "\033[37m"
          DarkGray     = "\033[90m"
          LightRed     = "\033[91m"
          LightGreen   = "\033[92m"
          LightYellow  = "\033[93m"
          LightBlue    = "\033[94m"
          LightMagenta = "\033[95m"
          LightCyan    = "\033[96m"
          White        = "\033[97m"
        #Introduction to the game minesweeper.
        print()
        print('\033[93mHi, welcome to my minesweeper game! I hope you enjoy playing it.\033[97m')
        print('================================================================')
        print("\033[32mHave fun!\033[97m")
        print() 
        #Sets up the game.
        def re():
            print('''
        MAIN MENU
        =========
        \033[36m>>>\033[97m For the rules and goals:\ntype '\033[33mI\033[97m'\n
        \033[36m>>>\033[97m To play right now:\ntype '\033[32mP\033[97m'
        ''')
            choice = input('Enter letter here:\033[93m ').upper()
            
            if choice == 'I':
                print("\033[H\033[J")
                #This part of the code will access a different file and print whatever is inside that file, in a print statement.
                print("\033[97m")
                print(open('Instructions.txt.', 'r').read())
                input('Press [\033[32menter\033[97m] when ready to play. ')
                print("\033[H\033[J")
                a = 1
                #prints a loading screen for the player/user with two pretty flowers.
                while a < 10:
                  print('\033[32m!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!            ', "\033[93m", a, "\033[32m", a,'\033[96mGame will be starting in\033[32m', a, "\033[93m", a, "\033[32m", "            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",)       
              
                  print("\n                                  \033[32m!!!!!!!!!!!!!\033[96m              \033[31m***\033[96m10s\033[31m***   \033[32m          !!!!!!!!!!!!!")

                  print("""
              \n\n\033[97m





                              \033[31m,\033[97m'   \033[31m,\033[97m'        \033[31m,\033[97m'                  \033[31m,\033[97m'   \033[31m,\033[97m'          \033[31m,\033[97m'
                          \033[31m,\033[97m'          \033[31m,\033[97m'                     \033[31m,\033[97m'           \033[31m,\033[97m'                                     
                                \033[31m,\033[97m'                                 \033[31m,\033[97m'
                              \033[31m,\033[97m'        \033[31m,\033[97m'                       \033[31m,\033[97m'         \033[31m,\033[97m'
                      \033[35m.,.\033[31m         ,\033[97m'                    \033[35m .,.\033[31m         ,\033[97m'
                    \033[35m.`.`.`.\033[31m   ,\033[97m'\033[31m      ,\033[97m'               \033[35m.`.`.`.\033[31m  ,\033[97m'\033[31m       ,\033[97m'
                    \033[35m.`.`.`.`.\033[31m   ,\033[97m'\033[31m  ,\033[97m'                 \033[35m.`.`.`.`.\033[31m   ,\033[97m'\033[31m  ,\033[97m'
                    \033[35m.`.`.`.`.\033[31m                          \033[35m.`.`.`.`.\033[31m
                    \033[35m.`.`.`.`.\033[31m  ,\033[97m'\033[31m     ,\033[97m'               \033[35m.`.`.`.`.\033[31m  ,\033[97m'\033[31m     ,\033[97m'
                    \033[35m\\`.`.`.\033[31m      ,\033[97m'                   \033[35m\\`.`.`.\033[31m      ,\033[97m'\033[31m
                     \033[35m/\.,.\033[31m   ,\033[97m'\033[31m     ,\033[97m'                  \033[35m/\.,.\033[31m   ,\033[97m'\033[31m     ,\033[97m'
                    \033[32m///                                \033[32m///
                  :::                                :::
                  :::                                :::
                ///                                ///
                :::                                :::
                :::                                :::           
                :::                                :::
               ///                                 ///
             :::                                  :::
             ///                                 ///
             :::                                :::
        \033[92m/   /  /        / /   /  /        / /   /  /        / /   /  /        / /   /  /        / /   /  /        / /   /  /  / / /
        :   :  :        :   /  / :   :  :        :   /  / :   :  :        :   /  / :   :  :        :   /  / :   :  :        : / / :
        /:  /   :     /  :  :  : /:  /   :     /  :  :  : /:  /   :     /  :  :  : /:  /   :     /  :  :  : /:  /   :     / : / : :
         /: : : / /    ::   :  :  :     /  / / /  /: : : / /    ::   :  :  :     /  / / / /: : : / /    ::   :  :  : /  / / / : : : 
        :: / :: :    / :  /  /  / /   :  : : : :: / :: :    / :  /  /  / /   :  : : :  :: / :: :    / :  /  /  / /   :  : : : / / /
        / ::  /  : : :  : :  :  : : : / : : : / ::  /  : : :  : :  :  : : : /   : : : / ::  /  : : :  : :  :  : : : /   : : : : : :
         //  :  / / /  / /  /  / / / :  / / /   //  :  / / /  / /  /  / / / : / / /  //  :  / / /  / /  /  / / / :   / / / / / : ///
        : : : :  : : : :  : : : :  : : : :  : : : :  : :  :  : : :  :  : : :  :  : : :  : : :  : : :  : : :  : : :  : : :  : : : :::
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^""")
                  a += 1
                  
                  print("\033[H\033[J")




            #Player doesn't want to see the rules/instructions and just wants to play the game.    
            elif choice != 'P':
                print("\033[H\033[J")
                re()



            
            print("\033[H\033[J")

            a = 1
            #same thing as line56
            while a < 10:
              print('\033[32m!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!            ', "\033[93m", a, "\033[32m", a,'\033[96mGame will be starting in\033[32m', a, "\033[93m", a, "\033[32m", "            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",)       
              
              print("\n                                  \033[32m!!!!!!!!!!!!!\033[96m              \033[31m***\033[96m10s\033[31m***   \033[32m          !!!!!!!!!!!!!")
              
              
              
              
              print("""
              \n\n\033[97m





                              \033[31m,\033[97m'   \033[31m,\033[97m'        \033[31m,\033[97m'                  \033[31m,\033[97m'   \033[31m,\033[97m'          \033[31m,\033[97m'
                          \033[31m,\033[97m'          \033[31m,\033[97m'                     \033[31m,\033[97m'           \033[31m,\033[97m'                                     
                                \033[31m,\033[97m'                                 \033[31m,\033[97m'
                              \033[31m,\033[97m'        \033[31m,\033[97m'                       \033[31m,\033[97m'         \033[31m,\033[97m'
                      \033[35m.,.\033[31m         ,\033[97m'                    \033[35m .,.\033[31m         ,\033[97m'
                    \033[35m.`.`.`.\033[31m   ,\033[97m'\033[31m      ,\033[97m'               \033[35m.`.`.`.\033[31m  ,\033[97m'\033[31m       ,\033[97m'
                    \033[35m.`.`.`.`.\033[31m   ,\033[97m'\033[31m  ,\033[97m'                 \033[35m.`.`.`.`.\033[31m   ,\033[97m'\033[31m  ,\033[97m'
                    \033[35m.`.`.`.`.\033[31m                          \033[35m.`.`.`.`.\033[31m
                    \033[35m.`.`.`.`.\033[31m  ,\033[97m'\033[31m     ,\033[97m'               \033[35m.`.`.`.`.\033[31m  ,\033[97m'\033[31m     ,\033[97m'
                    \033[35m\\`.`.`.\033[31m      ,\033[97m'                   \033[35m\\`.`.`.\033[31m      ,\033[97m'\033[31m
                     \033[35m/\.,.\033[31m   ,\033[97m'\033[31m     ,\033[97m'                  \033[35m/\.,.\033[31m   ,\033[97m'\033[31m     ,\033[97m'
                    \033[32m///                                \033[32m///
                  :::                                :::
                  :::                                :::
                ///                                ///
                :::                                :::
                :::                                :::           
                :::                                :::
               ///                                 ///
             :::                                  :::
             ///                                 ///
             :::                                :::
        \033[92m/   /  /        / /   /  /        / /   /  /        / /   /  /        / /   /  /        / /   /  /        / /   /  /  / / /
        :   :  :        :   /  / :   :  :        :   /  / :   :  :        :   /  / :   :  :        :   /  / :   :  :        : / / :
        /:  /   :     /  :  :  : /:  /   :     /  :  :  : /:  /   :     /  :  :  : /:  /   :     /  :  :  : /:  /   :     / : / : :
         /: : : / /    ::   :  :  :     /  / / /  /: : : / /    ::   :  :  :     /  / / / /: : : / /    ::   :  :  : /  / / / : : : 
        :: / :: :    / :  /  /  / /   :  : : : :: / :: :    / :  /  /  / /   :  : : :  :: / :: :    / :  /  /  / /   :  : : : / / /
        / ::  /  : : :  : :  :  : : : / : : : / ::  /  : : :  : :  :  : : : /   : : : / ::  /  : : :  : :  :  : : : /   : : : : : :
         //  :  / / /  / /  /  / / / :  / / /   //  :  / / /  / /  /  / / / : / / /  //  :  / / /  / /  /  / / / :   / / / / / : ///
        : : : :  : : : :  : : : :  : : : :  : : : :  : :  :  : : :  :  : : :  :  : : :  : : :  : : :  : : :  : : :  : : :  : : : :::
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
              """)
              a += 1
              
              print("\033[H\033[J")


            


            #Populates the grid. Basically what happens is these zero's don't have any variables right now but when they get put into the grid some of them will get mines on them well others will give you points!
            populator = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
            for n in range (0, 10):
                placeBomb(populator)

            for y in range (0, 9):
                for x in range (0, 9):
                    value = l(y, x, populator)
                    if value == '*':
                        updateValues(y, x, populator)
            #Sets the variable grid to a grid of blank spaces, because nothing is yet known about the grid.
            values = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            #prints the grid so the player can see the grid.
            printBoard(values)
            #Start timer.
            startTime = time.time()
            #This is when the game starts and the player can play.
            play(populator, values, startTime)
        #Gets the value of each box inside the grid, so when the player inputs the cordinates the program will know what they're saying.
        def l(y, x, populator):
            return populator[y][x]
        #Places the miens around the grid to make the game a challenge for the user.
        def placeBomb(populator):
            y = random.randint(0, 8)
            x = random.randint(0, 8)
            #Checks if there's a bomb in the randomly generated location. If not, it puts one there. If there is, it tries a new box to try placing a mine there.
            currentRow = populator[y]
            if not currentRow[x] == '*':
                currentRow[x] = '*'
            else:
                placeBomb(populator)
        #In this loop it adds 1's in around box around the mine (not the whole grid just the box's around the mine)
        def updateValues(yn, x, populator):
            #Prints 1's on the top of the box the mine is in.
            if yn-1 > -1:
                y = populator[yn-1]
                if x-1 > -1:
                    if not y[x-1] == '*':
                        y[x-1] += 1

                if not y[x] == '*':
                    y[x] += 1

                if 9 > x+1:
                    if not y[x+1] == '*':
                        y[x+1] += 1
            #Prints 1's in the box's beside the box that has a mine in it.   
            y = populator[yn]
            if x-1 > -1:
                if not y[x-1] == '*':
                    y[x-1] += 1

            if 9 > x+1:
                if not y[x+1] == '*':
                    y[x+1] += 1
            #Prints 1's in the box's under the box that has mine in it.
            if 9 > yn+1:
                y = populator[yn+1]
                if x-1 > -1:
                    if not y[x-1] == '*':
                        y[x-1] += 1

                if not y[x] == '*':
                    y[x] += 1

                if 9 > x+1:
                    if not y[x+1] == '*':
                        y[x+1] += 1
        #When a zero is found, all the squares around it are opened. Minesweeper does this to save time for the player/user.
        def zeroProcedure(y, x, values, populator):
            #Goes through the row above the box the user has just opened with a 0 in it. Does this till it hits a 1, 2 or mine.
            if y-1 > -1:
                row = values[y-1]
                if x-1 > -1: row[x-1] = l(y-1, x-1, populator)
                row[x] = l(y-1, x, populator)
                if 9 > x+1: row[x+1] = l(y-1, x+1, populator)
            #Goes through the row beside the box the user has just opened with a 0 in it. Does this till it hits a 1, 2 or mine.
            row = values[y]
            if x-1 > -1: row[x-1] = l(y, x-1, populator)
            if 9 > x+1: row[x+1] = l(y, x+1, populator)
            #Goes through the row under the box the user has just opened with a 0 in it. Does this till it hits a 1, 2 or mine.
            if 9 > y+1:
                row = values[y+1]
                if x-1 > -1: row[x-1] = l(y+1, x-1, populator)
                row[x] = l(y+1, x, populator)
                if 9 > x+1: row[x+1] = l(y+1, x+1, populator)
        #Checks known grid for 0s.
        def checkZeros(values, populator, y, x):
            oldGrid = copy.deepcopy(values)
            zeroProcedure(y, x, values, populator)
            if oldGrid == values:
                return 
            while True:
                oldGrid = copy.deepcopy(values)
                for x in range (9):
                    for y in range (9):
                        if l(x, y, values) == 0:
                            zeroProcedure(x, y, values, populator)
                if oldGrid == values:
                    return
        #Places a marker wherever the player thinks there is one (eg. mE4), if a player puts that in it will place a red flag showing that shows that's where th eplayer thinks there is a mine.
        def marker(y, x, values):
            values[y][x] = '\033[31m⚐\033[97m'
            printBoard(values)
        #prints the grid so the player can see the grid.
        def printBoard(populator):
            print("\033[H\033[J")
            print('    \033[96mA   B   C   D   E   F   G   H   I')
            print('  \033[97m╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗')
            for y in range (0, 9):
                print(y,'║',l(y,0,populator),'║',l(y,1,populator),'║',l(y,2,populator),'║',l(y,3,populator),'║',l(y,4,populator),'║',l(y,5,populator),'║',l(y,6,populator),'║',l(y,7,populator),'║',l(y,8,populator),'║')
                if not y == 8:
                    print('  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣')
            print('  ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝')
        #Let's the player choose their cordinates, so they can progress/play the game.
        def choose(populator, values, startTime):
            #Defiens the variables of the cordinates for the player.
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ,'i']
            numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
            #Loops this part of the code in case the program has an invalid entry.
            #This part of the code also prints what the player can do and how to input a flag or open a box.
            while True:
                chosen = input('\033[97m\n  \033[36m>>>\033[97m Choose a box\033[93m █\033[97m (eg. \033[32mE4)\n  \033[36m>>>\033[97m If you want to make a marker to where you think a mine is type (eg. \033[31mmE4\033[97m)\n\n  Type here:\033[32m').lower()
                #Checks/makes sure the box they have entered is a valid box or if it's not.
                print("\033[94m")
                if len(chosen) == 3 and chosen[0] == 'm' and chosen[1] in letters and chosen[2] in numbers:
                    x, y = (ord(chosen[1]))-97, int(chosen[2])
                    marker(y, x, values)
                    play(populator, values, startTime)
                    break
                elif len(chosen) == 2 and chosen[0] in letters and chosen[1] in numbers: return (ord(chosen[0]))-97, int(chosen[1])
                else: choose(populator, values, startTime)    
        #This is basically where the gameplay comes together. By that I mean this is where the user gets to do stuff.
        def play(populator, values, startTime):
            #When the player chooses a box to open, it allows them to do so.
            x, y = choose(populator, values, startTime)
            #Gets the value fo the box the palyer wanted to open, basically checks to see what's in there, whether that be 0, 1, 2 or a mine.
            v = l(y, x, populator)
            #If the player opens a box and hits a mine, it'll end the game.
            if v == '*':
                printBoard(populator)
                print('  \033[31mYou Lose\033[97m!')
                #Gives the player their time it took them to lose.
                print('  \033[33mTime\033[97m:\033[32m ' + str(round(time.time() - startTime)) + '\033[97ms') 
                #Offers the player if they ant to play the game again. 
                playAgain = input('  Play again? (\033[32mY\033[97m/\033[31mN\033[97m): ').lower()
                if playAgain == 'y':
                    print("\033[H\033[J")
                    reset()
                else:
                    #Gives the player a sentimental text sayign bye and their always welcome to come back.
                    print("\n  \033[36mAw that's too bad. Hope you have a wonderful day, come back at any time bye!",(Time2))
                    print((C), (Time_50))
                    quit()
                    
            #Puts that value into the known grid (grid).
            values[y][x] = v
            #Runs checkZeros() if that value is a 0 or else.
            if v == 0:
                checkZeros(values, populator, y, x)
            printBoard(values)
            #Checks to see if you have won.
            squaresLeft = 0
            for x in range (0, 9):
                row = values[x]
                squaresLeft += row.count(' ')
                squaresLeft += row.count('⚐')
            if squaresLeft == 10:
                printBoard(populator)
                print('You win!')
                #Print time it took the player to win the game.
                print('Time: ' + str(round(time.time() - startTime)) + 's')
                #Offers the player the option to play again!
                playAgain = input('Play again? (Y/N): ')
                playAgain = playAgain.lower()
                if playAgain == 'y':
                    print("\033[H\033[J")
                    re()
                #If the player doesn't want tqo playa agin it'll give the same sentimental text.    
                else:
                    print("Aw that's too bad. Hope you have a wonderful day, come back at any time bye!", (Time1_5))
                    quit()
            #Repeats the game if the player wanted to play the game again!!!
            play(populator, values, startTime)
        #restarts the game and gives the grid new values.
        re()




    ##################################################################################################################################

    elif q1 == 'mine':
        FPS = 100
        WINDOWWIDTH = 400
        WINDOWHEIGHT = 300
        BOXSIZE = 20
        GAPSIZE = 3
        FIELDWIDTH = 15
        FIELDHEIGHT = 20
        XMARGIN = int((WINDOWWIDTH-(FIELDWIDTH*(BOXSIZE+GAPSIZE)))/2)
        YMARGIN = XMARGIN
        MINESTOTAL = 60

        # assertions
        assert MINESTOTAL < FIELDHEIGHT*FIELDWIDTH, 'More mines than boxes'
        assert BOXSIZE^2 * (FIELDHEIGHT*FIELDWIDTH) < WINDOWHEIGHT*WINDOWWIDTH, 'Boxes will not fit on screen'
        assert BOXSIZE/2 > 5, 'Bounding errors when drawing rectangle, cannot use half-5 in drawMinesNumbers'

        # assign colors 
        LIGHTGRAY = (225, 225, 225)
        DARKGRAY = (160, 160, 160)
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        BLUE = (0, 0, 255)
        GREEN = (0, 128, 0)

        # set up major colors
        BGCOLOR = WHITE
        FIELDCOLOR = BLACK
        BOXCOLOR_COV = DARKGRAY # covered box color
        BOXCOLOR_REV = LIGHTGRAY # revealed box color
        MINECOLOR = BLACK
        TEXTCOLOR_1 = BLUE
        TEXTCOLOR_2 = RED
        TEXTCOLOR_3 = BLACK
        HILITECOLOR = GREEN
        RESETBGCOLOR = LIGHTGRAY
        MINEMARK_COV = RED

        # set up font 
        FONTTYPE = 'Courier New'
        FONTSIZE = 20

        def main():

            # initialize global variables & pygame module, set caption
            global FPSCLOCK, DISPLAYSURFACE, BASICFONT, RESET_SURF, RESET_RECT, SHOW_SURF, SHOW_RECT
            pygame.init()
            pygame.display.set_caption('Minesweeper')
            FPSCLOCK = pygame.time.Clock()
            DISPLAYSURFACE = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
            BASICFONT = pygame.font.SysFont(FONTTYPE, FONTSIZE)

            # obtain reset & show objects and rects
            RESET_SURF, RESET_RECT = drawButton('RESET', TEXTCOLOR_3, RESETBGCOLOR, WINDOWWIDTH/2, WINDOWHEIGHT-120)
            SHOW_SURF, SHOW_RECT = drawButton('SHOW ALL', TEXTCOLOR_3, RESETBGCOLOR, WINDOWWIDTH/2, WINDOWHEIGHT-95)

            # stores XY of mouse events
            mouse_x = 0
            mouse_y = 0

            # set up data structures and lists
            mineField, zeroListXY, revealedBoxes, markedMines = gameSetup()

            # set background color
            DISPLAYSURFACE.fill(BGCOLOR)

            # main game loop
            while True:

                # check for quit function
                checkForKeyPress()

                # initialize input booleans
                mouseClicked = False
                spacePressed = False

                # draw field
                DISPLAYSURFACE.fill(BGCOLOR)
                pygame.draw.rect(DISPLAYSURFACE, FIELDCOLOR, (XMARGIN-5, YMARGIN-5, (BOXSIZE+GAPSIZE)*FIELDWIDTH+5, (BOXSIZE+GAPSIZE)*FIELDHEIGHT+5))
                drawField()
                drawMinesNumbers(mineField)        

                # event handling loop
                for event in pygame.event.get(): 
                    if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                        terminate()
                    elif event.type == MOUSEMOTION:
                        mouse_x, mouse_y = event.pos
                    elif event.type == MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = event.pos
                        mouseClicked = True
                    elif event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            spacePressed = True
                    elif event.type == KEYUP:
                        if event.key == K_SPACE:
                            spacePressed = False

                # draw covers
                drawCovers(revealedBoxes, markedMines)

                # mine marker tip
                tipFont = pygame.font.SysFont(FONTTYPE, 16) ## not using BASICFONT - too big
                drawText('Tip: Highlight a box and press space (rather than click the mouse)', tipFont, TEXTCOLOR_3, DISPLAYSURFACE, WINDOWWIDTH/2, WINDOWHEIGHT-60)
                drawText('to mark areas that you think contain mines.', tipFont, TEXTCOLOR_3, DISPLAYSURFACE, WINDOWWIDTH/2, WINDOWHEIGHT-40)
                    
                # determine boxes at clicked areas
                box_x, box_y = getBoxAtPixel(mouse_x, mouse_y)

                # mouse not over a box in field
                if (box_x, box_y) == (None, None):

                    # check if reset box is clicked
                    if RESET_RECT.collidepoint(mouse_x, mouse_y):
                        highlightButton(RESET_RECT)
                        if mouseClicked: 
                            mineField, zeroListXY, revealedBoxes, markedMines = gameSetup()

                    # check if show box is clicked
                    if SHOW_RECT.collidepoint(mouse_x, mouse_y):
                        highlightButton(SHOW_RECT)
                        if mouseClicked:
                            revealedBoxes = blankRevealedBoxData(True)

                # mouse currently over box in field
                else:

                    # highlight unrevealed box
                    if not revealedBoxes[box_x][box_y]: 
                        highlightBox(box_x, box_y)

                        # mark mines
                        if spacePressed:
                            markedMines.append([box_x, box_y])
                            
                        # reveal clicked boxes
                        if mouseClicked:
                            revealedBoxes[box_x][box_y] = True

                            # when 0 is revealed, show relevant boxes
                            if mineField[box_x][box_y] == '[0]':
                                showNumbers(revealedBoxes, mineField, box_x, box_y, zeroListXY)

                            # when mine is revealed, show mines
                            if mineField[box_x][box_y] == '[X]':
                                showMines(revealedBoxes, mineField, box_x, box_y)
                                gameOverAnimation(mineField, revealedBoxes, markedMines, 'LOSS')
                                mineField, zeroListXY, revealedBoxes, markedMines = gameSetup()

                # check if player has won 
                if gameWon(revealedBoxes, mineField):
                    gameOverAnimation(mineField, revealedBoxes, markedMines, 'WIN')
                    mineField, zeroListXY, revealedBoxes, markedMines = gameSetup()
                    
                # redraw screen, wait clock tick
                pygame.display.update()
                FPSCLOCK.tick(FPS)
            
        def blankField():

           # creates blank FIELDWIDTH x FIELDHEIGHT data structure

            field = []
            for x in range(FIELDWIDTH):
                field.append([]) 
                for y in range(FIELDHEIGHT):
                    field[x].append('[ ]')
            return field

        def placeMines(field): 

            # places mines in FIELDWIDTH x FIELDHEIGHT data structure
            # requires blank field as input

            mineCount = 0
            xy = [] 
            while mineCount < MINESTOTAL: 
                x = random.randint(0,FIELDWIDTH-1)
                y = random.randint(0,FIELDHEIGHT-1)
                xy.append([x,y]) 
                if xy.count([x,y]) > 1: 
                    xy.remove([x,y]) 
                else: 
                    field[x][y] = '[X]' 
                    mineCount += 1

        def isThereMine(field, x, y): 

            # checks if mine is located at specific box on field

            return field[x][y] == '[X]'  

        def placeNumbers(field): 

            # places numbers in FIELDWIDTH x FIELDHEIGHT data structure
            # requires field with mines as input

            for x in range(FIELDWIDTH):
                for y in range(FIELDHEIGHT):
                    if not isThereMine(field, x, y):
                        count = 0
                        if x != 0: 
                            if isThereMine(field, x-1, y):
                                count += 1
                            if y != 0: 
                                if isThereMine(field, x-1, y-1):
                                    count += 1
                            if y != FIELDHEIGHT-1: 
                                if isThereMine(field, x-1, y+1):
                                    count += 1
                        if x != FIELDWIDTH-1: 
                            if isThereMine(field, x+1, y):
                                count += 1
                            if y != 0: 
                                if isThereMine(field, x+1, y-1):
                                    count += 1
                            if y != FIELDHEIGHT-1: 
                                if isThereMine(field, x+1, y+1):
                                    count += 1
                        if y != 0: 
                            if isThereMine(field, x, y-1):
                                count += 1
                        if y != FIELDHEIGHT-1: 
                            if isThereMine(field, x, y+1):
                                count += 1
                        field[x][y] = '[%s]' %(count)

        def blankRevealedBoxData(val):

            # returns FIELDWIDTH x FIELDHEIGHT data structure different from the field data structure
            # each item in data structure is boolean (val) to show whether box at those fieldwidth & fieldheight coordinates should be revealed

            revealedBoxes = []
            for i in range(FIELDWIDTH):
                revealedBoxes.append([val] * FIELDHEIGHT)
            return revealedBoxes

        def gameSetup():

            # set up mine field data structure, list of all zeros for recursion, and revealed box boolean data structure

            mineField = blankField()
            placeMines(mineField)
            placeNumbers(mineField)
            zeroListXY = []
            markedMines = []
            revealedBoxes = blankRevealedBoxData(False)

            return mineField, zeroListXY, revealedBoxes, markedMines

        def drawField():

            # draws field GUI and reset button

            for box_x in range(FIELDWIDTH):
                for box_y in range(FIELDHEIGHT):
                    left, top = getLeftTopXY(box_x, box_y)
                    pygame.draw.rect(DISPLAYSURFACE, BOXCOLOR_REV, (left, top, BOXSIZE, BOXSIZE))

            DISPLAYSURFACE.blit(RESET_SURF, RESET_RECT)
            DISPLAYSURFACE.blit(SHOW_SURF, SHOW_RECT)

        def drawMinesNumbers(field):
            
            # draws mines and numbers onto GUI
            # field should have mines and numbers

            half = int(BOXSIZE*0.5) 
            quarter = int(BOXSIZE*0.25)
            eighth = int(BOXSIZE*0.125)
            
            for box_x in range(FIELDWIDTH):
                for box_y in range(FIELDHEIGHT):
                    left, top = getLeftTopXY(box_x, box_y)
                    center_x, center_y = getCenterXY(box_x, box_y)
                    if field[box_x][box_y] == '[X]':
                        pygame.draw.circle(DISPLAYSURFACE, MINECOLOR, (left+half, top+half), quarter)
                        pygame.draw.circle(DISPLAYSURFACE, WHITE, (left+half, top+half), eighth)
                        pygame.draw.line(DISPLAYSURFACE, MINECOLOR, (left+eighth, top+half), (left+half+quarter+eighth, top+half))
                        pygame.draw.line(DISPLAYSURFACE, MINECOLOR, (left+half, top+eighth), (left+half, top+half+quarter+eighth))
                        pygame.draw.line(DISPLAYSURFACE, MINECOLOR, (left+quarter, top+quarter), (left+half+quarter, top+half+quarter))
                        pygame.draw.line(DISPLAYSURFACE, MINECOLOR, (left+quarter, top+half+quarter), (left+half+quarter, top+quarter))
                    else: 
                        for i in range(1,9):
                            if field[box_x][box_y] == '[' + str(i) + ']':
                                if i in range(1,3):
                                    textColor = TEXTCOLOR_1
                                else:
                                    textColor = TEXTCOLOR_2
                                drawText(str(i), BASICFONT, textColor, DISPLAYSURFACE, center_x, center_y)

        def showNumbers(revealedBoxes, mineField, box_x, box_y, zeroListXY):

            # modifies revealedBox data strucure if chosen box_x & box_y is [0] 
            # show all boxes using recursion
            
            revealedBoxes[box_x][box_y] = True
            revealAdjacentBoxes(revealedBoxes, box_x, box_y)
            for i,j in getAdjacentBoxesXY(mineField, box_x, box_y):
                if mineField[i][j] == '[0]' and [i,j] not in zeroListXY:
                    zeroListXY.append([i,j])
                    showNumbers(revealedBoxes, mineField, i, j, zeroListXY)

        def showMines(revealedBoxes, mineField, box_x, box_y): 

            # modifies revealedBox data strucure if chosen box_x & box_y is [X] 

            for i in range(FIELDWIDTH):
                for j in range(FIELDHEIGHT):
                    if mineField[i][j] == '[X]':
                        revealedBoxes[i][j] = True
            
        def revealAdjacentBoxes(revealedBoxes, box_x, box_y):

            # modifies revealedBoxes data structure so that all adjacent boxes to (box_x, box_y) are set to True

            if box_x != 0: 
                revealedBoxes[box_x-1][box_y] = True
                if box_y != 0: 
                    revealedBoxes[box_x-1][box_y-1] = True
                if box_y != FIELDHEIGHT-1: 
                    revealedBoxes[box_x-1][box_y+1] = True
            if box_x != FIELDWIDTH-1:
                revealedBoxes[box_x+1][box_y] = True
                if box_y != 0: 
                    revealedBoxes[box_x+1][box_y-1] = True
                if box_y != FIELDHEIGHT-1: 
                    revealedBoxes[box_x+1][box_y+1] = True
            if box_y != 0: 
                revealedBoxes[box_x][box_y-1] = True
            if box_y != FIELDHEIGHT-1: 
                revealedBoxes[box_x][box_y+1] = True

        def getAdjacentBoxesXY(mineField, box_x, box_y):

            # get box XY coordinates for all adjacent boxes to (box_x, box_y)

            adjacentBoxesXY = []

            if box_x != 0:
                adjacentBoxesXY.append([box_x-1,box_y])
                if box_y != 0:
                    adjacentBoxesXY.append([box_x-1,box_y-1])
                if box_y != FIELDHEIGHT-1:
                    adjacentBoxesXY.append([box_x-1,box_y+1])
            if box_x != FIELDWIDTH-1: 
                adjacentBoxesXY.append([box_x+1,box_y])
                if box_y != 0:
                    adjacentBoxesXY.append([box_x+1,box_y-1])
                if box_y != FIELDHEIGHT-1:
                    adjacentBoxesXY.append([box_x+1,box_y+1])
            if box_y != 0:
                adjacentBoxesXY.append([box_x,box_y-1])
            if box_y != FIELDHEIGHT-1:
                adjacentBoxesXY.append([box_x,box_y+1])

            return adjacentBoxesXY
            
        def drawCovers(revealedBoxes, markedMines):

            # uses revealedBox FIELDWIDTH x FIELDHEIGHT data structure to determine whether to draw box covering mine/number
            # draw red cover instead of gray cover over marked mines

            for box_x in range(FIELDWIDTH):
                for box_y in range(FIELDHEIGHT):
                    if not revealedBoxes[box_x][box_y]:
                        left, top = getLeftTopXY(box_x, box_y)
                        if [box_x, box_y] in markedMines:
                            pygame.draw.rect(DISPLAYSURFACE, MINEMARK_COV, (left, top, BOXSIZE, BOXSIZE))
                        else:
                            pygame.draw.rect(DISPLAYSURFACE, BOXCOLOR_COV, (left, top, BOXSIZE, BOXSIZE))

        def drawText(text, font, color, surface, x, y):  

            # function to easily draw text and also return object & rect pair

            textobj = font.render(text, True, color)
            textrect = textobj.get_rect()
            textrect.centerx = x
            textrect.centery = y
            surface.blit(textobj, textrect)

        def drawButton(text, color, bgcolor, center_x, center_y):

            # similar to drawText but text has bg color and returns obj & rect

            butSurf = BASICFONT.render(text, True, color, bgcolor)
            butRect = butSurf.get_rect()
            butRect.centerx = center_x
            butRect.centery = center_y

            return (butSurf, butRect)

        def getLeftTopXY(box_x, box_y):

            # get left & top coordinates for drawing mine boxes

            left = XMARGIN + box_x*(BOXSIZE+GAPSIZE)
            top = YMARGIN + box_y*(BOXSIZE+GAPSIZE)
            return left, top

        def getCenterXY(box_x, box_y):

            # get center coordinates for drawing mine boxes
            
            center_x = XMARGIN + BOXSIZE/2 + box_x*(BOXSIZE+GAPSIZE)
            center_y = YMARGIN + BOXSIZE/2 + box_y*(BOXSIZE+GAPSIZE)
            return center_x, center_y

        def getBoxAtPixel(x, y):

            # gets coordinates of box at mouse coordinates
            
            for box_x in range(FIELDWIDTH):
                for box_y in range(FIELDHEIGHT):
                    left, top = getLeftTopXY(box_x, box_y)
                    boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
                    if boxRect.collidepoint(x, y):
                        return (box_x, box_y)
            return (None, None)

        def highlightBox(box_x, box_y):

            # highlight box when mouse hovers over it
            
            left, top = getLeftTopXY(box_x, box_y)
            pygame.draw.rect(DISPLAYSURFACE, HILITECOLOR, (left, top, BOXSIZE, BOXSIZE), 4)

        def highlightButton(butRect):

            # highlight button when mouse hovers over it

            linewidth = 4
            pygame.draw.rect(DISPLAYSURFACE, HILITECOLOR, (butRect.left-linewidth, butRect.top-linewidth, butRect.width+2*linewidth, butRect.height+2*linewidth), linewidth)

        def gameWon(revealedBoxes, mineField):

            # check if player has revealed all boxes

            notMineCount = 0

            for box_x in range(FIELDWIDTH):
                for box_y in range(FIELDHEIGHT):
                    if revealedBoxes[box_x][box_y] == True:
                        if mineField[box_x][box_y] != '[X]':
                            notMineCount += 1

            if notMineCount >= (FIELDWIDTH*FIELDHEIGHT)-MINESTOTAL:
                return True
            else:
                return False

        def gameOverAnimation(mineField, revealedBoxes, markedMines, result):

            # makes background flash red (loss) or blue (win)

            origSurf = DISPLAYSURFACE.copy()
            flashSurf = pygame.Surface(DISPLAYSURFACE.get_size())
            flashSurf = flashSurf.convert_alpha()
            animationSpeed = 20

            if result == 'WIN':
                r, g, b = BLUE
            else:
                r, g, b = RED
        #This si the animation loop aka blinking red colros or blue whether you win or lose the game, it also shows the green highlights when you hover over a cube etc...
            for i in range(5):
                for start, end, step in ((0, 255, 1), (255, 0, -1)):
                    for alpha in range(start, end, animationSpeed*step): # animation loop
                        checkForKeyPress()
                        flashSurf.fill((r, g, b, alpha))
                        DISPLAYSURFACE.blit(origSurf, (0, 0))
                        DISPLAYSURFACE.blit(flashSurf, (0, 0))
                        pygame.draw.rect(DISPLAYSURFACE, FIELDCOLOR, (XMARGIN-5, YMARGIN-5, (BOXSIZE+GAPSIZE)*FIELDWIDTH+5, (BOXSIZE+GAPSIZE)*FIELDHEIGHT+5))
                        drawField()
                        drawMinesNumbers(mineField)
                        tipFont = pygame.font.SysFont(FONTTYPE, 16) ## not using BASICFONT - too big
                        drawText('Tip: Highlight a box and press space (rather than click the mouse)', tipFont, TEXTCOLOR_3, DISPLAYSURFACE, WINDOWWIDTH/2, WINDOWHEIGHT-60)
                        drawText('to mark areas that you think contain mines.', tipFont, TEXTCOLOR_3, DISPLAYSURFACE, WINDOWWIDTH/2, WINDOWHEIGHT-40)
                        RESET_SURF, RESET_RECT = drawButton('RESET', TEXTCOLOR_3, RESETBGCOLOR, WINDOWWIDTH/2, WINDOWHEIGHT-120)
                        SHOW_SURF, SHOW_RECT = drawButton('SHOW ALL', TEXTCOLOR_3, RESETBGCOLOR, WINDOWWIDTH/2, WINDOWHEIGHT-95)
                        drawCovers(revealedBoxes, markedMines)
                        pygame.display.update()
                        FPSCLOCK.tick(FPS)
        #little side note to whom ever wants to see the source code for this program. go to this https/www.346732.ca/21%21%21%21
        def terminate():

            # simple function to exit game
            
            pygame.quit()
            sys.exit()

        def checkForKeyPress():

            # check if quit or any other key is pressed
            
            if len(pygame.event.get(QUIT)) > 0:
                terminate()
                
            keyUpEvents = pygame.event.get(KEYUP)
            if len(keyUpEvents) == 0:
                return None
            if keyUpEvents[0].key == K_ESCAPE:
                terminate()
            return keyUpEvents[0].key

        # run code
        if __name__ == '__main__':
            main()











    #################################################################################################################################################    
    elif q1 == 'Pass':
        #porting2
        #bin/pyth\By: Andrew Dumais/Bleot_blot\swaffin.
        R = '\033[31m'
        G = '\033[32m'
        W = '\033[97m'
        C = '\033[H\033[J'
        hostname = socket.gethostname()    
        IPAddr = socket.gethostbyname(hostname)
        Port1 = ('Tor port1: 9058')
        Port2 = ('Tor Port2: 9085')
        Port3 = ('Tor port3: 9075')
        Port4 = ('Tor port4: 9056')
        def OK(OK1, OK2, OK3, OK4):
          OK1 = "Tor Port [9058]-Success!"
          OK2 = "Tor Port [9085]-Success!"
          OK3 = "Tor Port [9075]-Success!"
          OK4 = "Tor Port [9056]-Success!"
          return OK
          #Making a copy for realution (program auto re for the APK)
        attempts = 0
        N = '\n'
        Tor = '   Tor Port...'
        OK1 = ("      [9050]-Success! OK1   [9051]-Success! OK2   [9052]-Success! OK3   [9053]-Success! OK4   [9054]-Success! OK5   [9055]-Success! OK6 ")
        OK2 = ("      [9080]-Success! OK10  [9081]-Success! OK11  [9082]-Success! OK12  [9083]-Success! OK13  [9084]-Success! OK14  [9085]-Success! OK15")
        OK3 = ("      [9075]-Success! OK19  [9040]-Success! OK20  [9041]-Success! OK21  [9042]-Success! OK22  [9043]-Success! OK23  [9044]-Success! OK24")
        OK4 = ("      [9056]-Success! OK29  [9091]-Success! OK30  [9092]-Success! OK31  [9093]-Success! OK32  [9094]-Success! OK33  [9095]-Success! OK34")

        Ko1 = ("      [9058]-Failure! Ko1   [9051]-Failure! Ko2   [9052]-Failure! Ko2   [9053]-Failure! Ko3   [9054]-Failure! Ko4   [9055]-Failure! Ko5 ")
        Ko2 = ("      [9085]-Failure! Ko9   [9058]-Failure! Ko1   [9058]-Failure! Ko1   [9058]-Failure! Ko1   [9058]-Failure! Ko1   [9058]-Failure! Ko1 ")
        Ko3 = ("      [9075]-Failure! Ko3   [9058]-Failure! Ko1   [9058]-Failure! Ko1   [9058]-Failure! Ko1   [9058]-Failure! Ko1   [9058]-Failure! Ko1 ")
        Ko4 = ("      [9056]-Failure! Ko4   [9058]-Failure! Ko1   [9058]-Failure! Ko1   [9058]-Failure! Ko1   [9058]-Failure! Ko1   [9058]-Failure! Ko1 ")
        credential = {"john" : "123a", "Jack" : "456b", "p" : "t", "bleot" : "BUGGOMZ457892282", "swaffin" : "457892282xgJp39102upmoqotet"}
        for i in range(1):
          print("""0063 6f70 6c61 7900 0030 0007 5374 6561 0063 6f70 6c61 7900 0030 0007 5374 6561 0063 6f70 6c61 7900 0030 0007 5374 6561 0063 6f70 6c61 7900 0030 0007 5374 6561
        6d49 4400 0e8b bf16 0100 1001 0767 616d 6d49 4400 0e8b bf16 0100 1001 0767 \033[31m616d \033[97m6d49 4400 0e8b bf16 0100 1001 0767 616d 6d49 4400 0e8b bf16 0100 1001 0767 616d 6d49 
        6569 6400 \033[31m4ada \033[97m0300 0000 0000 0270 6c616569 6400 4ada 0300 0000 0000 0270 6c61 6569 6400 4ada 0300 0000 0000 0270 6c61 6569 6400 4ada 0300 0000 0000 0270 6c61 6569 6400  
        7954 696d 6500 4234 \033[32ma95c \033[97m0800 \033[97m3100 \033[97m07537954 696d 6500 4234 a95c 0800 3100 0753 7954 696d 6500 4234 a95c 0800 3100 0753 7954 696d 6500 4234 a95c 0800 3100 0753 7954 696d  
        7465 616d 4944 00f1 2471 1701 0010 01077465 616d 4944 00f1 2471 1701 0010 0107 7465 616d 4944 00f1 2471 1701 \033[31m0010 \033[97m0107 7465 616d 4944 00f1 2471 1701 0010 0107 7465 616d 
        1f00 2f00 10b7 a6f5 1900 2f44 3a5c 0000 1f00 2f00 10b7 a6f5 1900 2f44 3a5c 00001f00 2f00 10b7 a6f5 1900 \033[31m2f44 \033[97m3a5c 00001f00 2f00 10b7 a6f5 1900 2f44 3a5c 00001f00 2f00 1
        0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 \033[31m00000000 \033[97m0000 0000 \033[31m0000 \033[97m0000 0000 0000 00000000 0000 0000 0000 0000 0000 0000 00000000 0000 0
        0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 00000000 0000 0000 0000 0000 0000 0000 00000000 0000 0000 0000 0000 0000 0000 00000000 0000 0
        0000 0074 1a59 5e96 dfd3 488d 6717 33bc 0000 0074 1a59 5e96 dfd3 488d 6717 33bc0000 0074 1a59 5e96 dfd3 488d 6717 33bc0000 0074 1a59 5e96 dfd3 488d 6717 33bc0000 0074 1
        ee28 ba77 2cfb f52f 0e16 4aa3 813e 560c ee28 ba77 2cfb f52f 0e16 4aa3 813e 560cee28 ba77 2cfb f52f 0e16 4aa3 813e 560cee28 ba77 2cfb f52f 0e16 4aa3 813e 560cee28 ba77 2
        68bc 8300 0032 0000 001c 0000 0001 0000 68bc 8300 0032 0000 001c 0000 0001 000068bc 8300 0032 0000 001c 0000 0001 000068bc 8300 0032 0000 001c 0000 0001 000068bc 8300 0
        001c 0000 002d 0000 0000 0000 0031 0000 001c 0000 002d \033[31m0000 \033[97m0000 0000 0031 0000001c 0000 002d 0000 0000 0000 0031 0000001c 0000 002d 0000 0000 0000 0031 \033[31m0000001c \033[97m0000 0
        0011 0000 0002 0000 00fb 0887 \033[31m2410 \033[97m0000 0011 0000 0002 0000 00fb 0887 \033[31m2410 \033[97m00000011 0000 0002 0000 00fb 0887 2410 00000011 0000 0002 0000 00fb 0887 2410 00000011 0000 0
        0000 443a 5c00 0001 002e 00b3 0000 0009 0000 443a 5c00 0001 002e 00b3 0000 00090000 443a 5c00 0001 002e 00b3 \033[31m0000 \033[97m00090000 443a 5c00 0001 002e 00b3 0000 00090000 443a 5
        0000 a072 0000 0031 5350 5330 f125 b7ef 0000 a072 0000 0031 5350 5330 f125 b7ef0000 a072 0000 0031 \033[31m5350 \033[97m5330 f125 b7ef0000 a072 0000 0031 5350 5330 f125 b7ef0000 a072 0
        471a 10a5 f102 608c 9eeb ac31 0000 000a 471a 10a5 f102 608c 9eeb ac31 0000 000a471a 10a5 f102 608c 9eeb ac31 0000 000a471a 10a5 f102 608c 9eeb ac31 0000 000a471a 10a5 f
        0000 0000 1f00 0000 0f00 0000 5500 5300 0000 0000 1f00 \033[32m0000\033[97m 0f00 0000 5500 53000000 0000 1f00 0000 0f00 0000 5500 53000000 0000 1f00 0000 0f00 0000 5500 53000000 0000 1
        4200 2000 4400 7200 6900 7600 6500 2000 4200 2000 4400 7200 6900 7600 \033[32m6500\033[97m 20004200 2000 4400 7200 6900 7600 6500 20004200 2000 4400 7200 6900 7600 6500 20004200 2000 4
        2800 4400 \033[31m3a00 \033[31m2900 0000 \033[97m0000 2500 0000 2800 \033[31m4400 \033[97m3a00 2900 0000 0000 2500 00002800 4400 3a00 2900 0000 0000 2500 00002800 4400 3a00 2900 0000 0000 2500 00002800 4400 3
        0400 0000 001f 0000 000a 0000 0055 \033[31m0053 \033[97m0400 0000 001f 0000 000a 0000 0055 00530400 0000 001f 0000 000a 0000 0055 00530400 0000 001f 0000 000a 0000 0055 00530400 0000 0
        0042 0020 0044 \033[31m0072 \033[97m0069 0076 0065 0000 0042 0020 0044 0072 0069 0076 0065 00000042 0020 0044 0072 0069 0076 0065 00000042 0020 0044 0072 0069 0076 0065 00000042 0020 0
        0000 0000 0035 0000 0031 5350 53a6 6a63 0000 0000 0035 0000 0031 5350 53a6 6a630000 0000 0035 0000 0031 5350 53a6 6a630000 0000 0035 0000 0031 5350 53a6 6a630000 0000 0
        283d 95d2 11b5 d600 c04f d918 d019 0000 283d 95d2 11b5 \033[31md600 \033[97mc04f d918 d019 0000283d 95d2 11b5 d600 c04f d918 d019 0000283d 95d2 11b5 d600 c04f d918 d019 0000283d 95d2 1
        001e 0000 0000 1f00 0000 0400 0000 4400 001e 0000 0000 1f00 0000 0400 0000 4400001e 0000 0000 1f00 0000 0400 0000 4400001e 0000 0000 1f00 0000 0400 0000 4400001e 0000 0
        0063 6f70 6c61 7900 0030 0007 \033[32m5374 \033[97m6561 0063 6f70 6c61 7900 0030 0007 5374 6561 0063 6f70 6c61 7900 0030 0007 5374 6561 0063 6f70 6c61 7900 0030 0007 5374 6561
        6d49 4400 0e8b bf16 0100 1001 0767 616d 6d49 4400 0e8b bf16 0100 1001 0767 616d 6d49 4400 0e8b bf16 0100 1001 0767 616d 6d49 4400 0e8b bf16 0100 1001 0767 616d 6d49 
        6569 6400 4ada 0300 0000 0000 0270 6c616569 6400 4ada 0300 \033[31m0000 0000 \033[97m0270 6c61 6569 6400 4ada 0300 0000 0000 0270 6c61 6569 6400 4ada 0300 0000 0000 0270 6c61 6569 6400  
        7954 696d 6500 4234 a95c 0800 3100 07537954 696d 6500 4234 a95c 0800 \033[32m3100\033[97m 0753 7954 696d 6500 4234 a95c 0800 3100 0753 7954 696d 6500 4234 a95c 0800 3100 0753 7954 696d  
        7465 616d 4944 00f1 2471 1701 0010 01077465 616d 4944 00f1 2471 1701 0010 0107 7465 616d 4944 00f1 2471 1701 0010 0107 7465 616d 4944 00f1 2471 1701 0010 0107 7465 616d 
        1f00 2f00 10b7 a6f5 1900 2f44 3a5c \033[32m0000\033[97m 1f00 2f00 10b7 a6f5 1900 2f44 3a5c 00001f00 2f00 10b7 a6f5 1900 2f44 3a5c 00001f00 2f00 10b7 a6f5 1900 2f44 3a5c 00001f00 2f00 1
        0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 00000000 \033[32m0000 \033[97m0000 0000 0000 0000 0000 00000000 0000 0000 0000 0000 0000 0000 00000000 0000 0
        0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 00000000 0000 0000 0000 0000 0000 0000 00000000 0000 0000 0000 0000 0000 0000 00000000 0000 0
        0000 0074 1a59 5e96 dfd3 488d\033[31m 6717 \033[97m33bc 0000 0074 1a59 5e96 dfd3 488d 6717 33bc0000 0074 1a59 5e96 dfd3 488d 6717 33bc0000 0074 1a59 5e96 dfd3 488d 6717 33bc0000 0074 1
        ee28 ba77 2cfb f52f 0e16 4aa3 813e 560c ee28 ba77 2cfb f52f 0e16 4aa3 813e 560cee28 ba77 2cfb f52f 0e16 4aa3 813e 560cee28 ba77 2cfb f52f 0e16 4aa3 813e 560cee28 ba77 2
        68bc 8300 0032 0000 001c 0000 \033[31m0001 \033[97m0000 68bc 8300 0032 0000 001c 0000 0001 \033[32m000068bc\033[97m 8300 0032 0000 001c 0000 0001 000068bc 8300 0032 0000 001c 0000 0001 \033[31m000068bc \033[97m8300 0
        001c 0000 002d 0000 0000 0000 0031 0000 001c 0000 002d 0000 0000 0000 0031 0000001c 0000 002d 0000 0000 0000 0031 0000001c 0000 002d 0000 0000 0000 0031 0000001c 0000 0
        0011 0000 0002 0000 00fb 0887 2410 0000 0011 0000 0002 0000 00fb 0887 2410 \033[32m00000011\033[97m 0000 0002 0000 00fb 0887 2410 00000011 0000 0002 0000 00fb 0887 2410 00000011 0000 0
        0000 443a 5c00 0001 \033[31m002e \033[97m00b3 0000 0009 0000 443a 5c00 0001 002e 00b3 0000 00090000 443a 5c00 0001 002e 00b3 0000 00090000 443a 5c00 0001 002e 00b3 0000 00090000 443a 5
        0000 a072 0000 0031 5350 5330 f125 b7ef 0000 a072 0000 0031 \033[31m5350 \033[97m5330 f125 b7ef0000 a072 0000 0031 5350 5330 f125 b7ef0000 a072 0000 0031 5350 5330 f125 b7ef0000 a072 0
        471a 10a5 f102 608c 9eeb ac31 0000 000a 471a 10a5 f102 608c 9eeb ac31 0000 000a471a 10a5 f102 608c 9eeb ac31 0000 000a471a 10a5 f102 608c 9eeb ac31 0000 000a471a 10a5 f
        0000 0000 1f00 0000 0f00 0000 5500 \033[32m5300 0\033[97m000 0000 1f00 0000 0f00 0000 5500 53000000 0000 1f00 0000 0f00 0000 5500 53000000 0000 1f00 0000 0f00 0000 5500 53000000 0000 1
        4200 2000 4400 7200 6900 7600 6500 2000 4200 2000 4400 7200 6900 7600 6500 20004200 2000 4400 7200 6900 7600 6500 20004200 2000 4400 7200 6900 7600 6500 20004200 2000 4
        2800 4400 3a00 2900 0000 0000 2500 \033[32m0000 \033[97m2800 4400 3a00 2900 0000 0000 2500 00002800 4400 3a00 2900 0000 0000 2500 00002800 4400 3a00 2900 0000 0000 2500 00002800 4400 3
        0400 0000 001f 0000 000a 0000 0055 0053 0400 0000 001f 0000 \033[32m000a \033[97m0000 0055 00530400 0000 001f 0000 000a 0000 0055 00530400 0000 001f 0000 000a 0000 0055 00530400 0000 0
        0042 0020 0044 0072 0069 0076 0065 0000 0042 0020 0044 0072 0069 0076 0065 00000042 0020 0044 0072 0069 0076 0065 00000042 0020 0044 0072 0069 0076 0065 00000042 0020 0
        0000 0000 0035 0000 0031 5350 53a6 6a63 0000 0000 0035 0000 0031 5350 53a6 6a630000 0000 0035 0000 0031 5350 53a6 6a630000 0000 0035 0000 0031 5350 53a6 6a630000 0000 0
        283d 95d2 11b5 d600 c04f d918 d019 0000 \033[32m283d \033[97m95d2 11b5 d600 c04f d918 d019 0000283d 95d2 11b5 d600 c04f d918 d019 0000283d 95d2 11b5 d600 c04f d918 d019 0000283d 95d2 1
        001e 0000 0000 1f00 0000 0400 0000 4400 001e 0000 0000 1f00 0000 0400 0000 4400001e 0000 0000 1f00 0000 0400 0000 4400001e 0000 0000 1f00 0000 0400 0000 4400001e 0000 0
        0063 6f70 6c61 7900 0030 0007 5374 6561 0063 6f70 6c61 7900 0030 0007 5374 6561 0063 6f70 6c61 7900 0030 0007 5374 6561 0063 6f70 6c61 7900 0030 0007 5374 6561
        6d49 4400 0e8b bf16 0100 1001 0767 616d 6d49 4400 0e8b bf16 0100 1001 0767 616d 6d49 4400 0e8b bf16 \033[32m0100\033[97m 1001 0767 616d 6d49 4400 0e8b bf16 0100 1001 0767 616d 6d49 
        6569 6400 4ada 0300 0000 0000 0270 6c616569 6400 \033[32m4ada\033[97m 0300 0000 0000 0270 6c61 6569 6400 4ada 0300 0000 0000 0270 6c61 6569 6400 4ada 0300 0000 0000 0270 6c61 6569 6400  
        7954 696d 6500 4234 a95c 0800 3100 07537954 696d 6500 4234 a95c 0800 3100 0753 7954 696d 6500 \033[32m4234\033[97m a95c 0800 3100 0753 7954 696d 6500 4234 a95c 0800 3100 0753 7954 696d  
        7465 616d 4944 00f1 2471 1701 0010 01077465 616d 4944 00f1 2471 1701 0010 0107 7465 616d 4944 00f1 2471 1701 0010 0107 7465 616d 4944 00f1 2471 1701 0010 0107 7465 616d 
        1f00 2f00 10b7 a6f5 1900 \033[32m2f44\033[97m 3a5c 0000 1f00 2f00 10b7 a6f5 1900 2f44 3a5c 00001f00 2f00 10b7 a6f5 1900 2f44 3a5c 00001f00 2f00 10b7 a6f5 1900 2f44 3a5c 00001f00 2f00 1
        0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 00000000 0000 0000 0000 0000 0000 0000 00000000 0000 0000 0000 0000 0000 0000 00000000 0000 0
        0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 00000000 0000 0000 0000 0000 0000 0000 00000000 0000 0000 0000 0000 0000 0000 00000000 0000 0
        0000 0074 1a59 5e96 dfd3 488d 6717 33bc 0000 0074 1a59 5e96 dfd3 488d 6717 33bc0000 0074 1a59 5e96 dfd3 488d 6717 33bc0000 0074 1a59 5e96 dfd3 488d 6717 33bc0000 0074 1
        ee28 ba77 2cfb f52f 0e16 4aa3 813e 560c ee28 ba77 2cfb f52f 0e16 4aa3 813e 560cee28 ba77 2cfb f52f 0e16 4aa3 813e 560cee28 ba77 2cfb f52f 0e16 4aa3 813e 560cee28 ba77 2
        68bc 8300 0032 0000 001c 0000 0001 0000 68bc 8300 0032 \033[32m0000\033[97m 001c 0000 0001 000068bc 8300 0032 0000 001c 0000 0001 000068bc 8300 0032 0000 001c 0000 0001 000068bc 8300 0
        001c 0000 002d 0000 0000 0000 0031 0000 001c 0000 002d 0000 0000 0000 0031 0000001c 0000 002d 0000 0000 0000 0031 0000001c 0000 002d 0000 0000 0000 0031 0000001c 0000 0
        0011 0000 0002 0000 00fb 0887 2410 0000 0011 0000 0002 0000 00fb 0887 2410 00000011 0000 0002 0000 00fb 0887 2410 00000011 0000 0002 0000 00fb 0887 2410 00000011 0000 0
        0000 443a 5c00 0001 002e 00b3 0000 0009 0000 443a 5c00 0001 002e 00b3 \033[32m0000\033[97m 00090000 443a 5c00 0001 002e 00b3 0000 00090000 443a 5c00 0001 002e 00b3 0000 00090000 443a 5
        0000 a072 0000 0031 5350 5330 f125 b7ef 0000 a072 0000 0031 5350 5330 f125 b7ef0000 a072 0000 0031 5350 5330 f125 b7ef0000 a072 0000 0031 5350 5330 f125 b7ef0000 a072 0
        471a 10a5 f102 608c 9eeb ac31 0000 000a 471a 10a5 f102 608c 9eeb ac31 0000 000a471a 10a5 f102 608c 9eeb ac31 0000 000a471a 10a5 f102 608c 9eeb ac31 0000 000a471a 10a5 f
        0000 0000 1f00 0000 0f00 0000 5500 5300 0000 0000 1f00 0000 0f00 0000 5500 53000000 0000 1f00 0000 0f00 0000 5500 53000000 0000 1f00 0000 0f00 0000 5500 53000000 0000 1
        4200 2000 4400 7200 6900 7600 6500 2000 4200 2000 4400 7200 6900 7600 6500 20004200 2000 4400 7200 6900 7600 6500 20004200 2000 4400 7200 6900 7600 6500 20004200 2000 4
        2800 4400 3a00 2900 0000 0000 2500 0000 2800 4400 3a00 2900 0000 0000 2500 00002800 4400 3a00 2900 0000 0000 2500 00002800 4400 3a00 2900 0000 0000 2500 00002800 4400 3
        0400 0000 001f 0000 000a 0000 0055 0053 0400 0000 001f 0000 000a 0000 0055 00530400 0000 001f 0000 000a 0000 0055 00530400 0000 001f 0000 000a 0000 0055 00530400 0000 0
        0042 0020 0044 0072 0069 0076 0065 0000 0042 0020 0044 0072 0069 0076 0065 00000042 0020 0044 0072 0069 0076 0065 00000042 0020 0044 0072 0069 0076 0065 00000042 0020 0
        0000 0000 0035 0000 0031 5350 53a6 6a63 0000 0000 0035 0000 0031 5350 53a6 6a630000 0000 0035 0000 0031 5350 53a6 6a630000 0000 0035 0000 0031 5350 53a6 6a630000 0000 0
        283d 95d2 11b5 d600 c04f d918 d019 0000 283d 95d2 11b5 d600 c04f d918 d019 0000283d 95d2 11b5 d600 c04f d918 d019 0000283d 95d2 11b5 d600 c04f d918 d019 0000283d 95d2 1
        001e 0000 0000 1f00 0000 0400 0000 4400 001e 0000 0000 1f00 0000 \033[32m0400\033[97m 0000 4400001e 0000 0000 1f00 0000 0400 0000 4400001e 0000 0000 1f00 0000 0400 0000 4400001e 0000 0
        0063 6f70 6c61 7900 0030 0007 5374 6561 0063 6f70 6c61 7900 0030 0007 5374 6561 0063 6f70 6c61 7900 0030 0007 5374 6561 0063 6f70 6c61 7900 0030 0007 5374 6561
        6d49 4400 0e8b bf16 0100 1001 0767 616d 6d49 4400 0e8b bf16 0100 1001 0767 616d 6d49 4400 0e8b bf16 0100 1001 0767 616d 6d49 4400 0e8b bf16 0100 1001 0767 616d 6d49 
        6569 6400 4ada 0300 0000 0000 0270 6c616569 6400 4ada 0300 0000 0000 0270 6c61 6569 6400 4ada 0300 0000 0000 0270 6c61 6569 6400 4ada 0300 0000 0000 0270 6c61 6569 6400  
        7954 696d 6500 \033[32m4234\033[97m a95c 0800 3100 07537954 696d 6500 4234 a95c 0800 3100 0753 7954 696d 6500 4234 a95c 0800 3100 0753 7954 696d 6500 4234 a95c 0800 3100 0753 7954 696d  
        7465 616d 4944 00f1 2471 1701 0010 01077465 616d 4944 00f1 2471 1701 0010 0107 7465 616d 4944 00f1 2471 1701 0010 0107 7465 616d 4944 00f1 2471 1701 0010 0107 7465 616d 
        1f00 2f00 10b7 a6f5 1900 2f44 3a5c 0000 1f00 2f00 10b7 a6f5 1900 2f44 3a5c 00001f00 2f00 10b7 a6f5 1900 2f44 3a5c 00001f00 2f00 10b7 a6f5 1900 2f44 3a5c 00001f00 2f00 1
        0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 00000000 0000 0000 0000 0000 0000 0000 00000000 0000 0000 0000 0000 0000 0000 00000000 0000 0
        0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 00000000 0000 0000 0000 0000 0000 0000 00000000 0000 0000 0000 0000 0000 0000 00000000 0000 0
        0000 0074 1a59 5e96 dfd3 488d 6717 33bc 0000 0074 1a59 5e96 dfd3 488d 6717 33bc0000 0074 1a59 5e96 dfd3 488d 6717 33bc0000 0074 1a59 5e96 dfd3 488d 6717 33bc0000 0074 1
        ee28 ba77 2cfb f52f 0e16 4aa3 813e 560c ee28 ba77 2cfb f52f 0e16 4aa3 813e 560cee28 ba77 2cfb f52f 0e16 4aa3 813e 560cee28 ba77 2cfb f52f 0e16 4aa3 813e 560cee28 ba77 2
        68bc 8300 0032 0000 001c 0000 0001 \033[32m0000\033[97m 68bc 8300 0032 0000 001c 0000 0001 000068bc 8300 0032 0000 001c 0000 0001 000068bc 8300 0032 0000 001c 0000 0001 000068bc 8300 0
        001c 0000 002d 0000 0000 0000 0031 0000 001c 0000 002d 0000 0000 0000 0031 0000001c 0000 002d 0000 0000 0000 0031 0000001c 0000 002d 0000 0000 0000 0031 0000001c 0000 0
        0011 0000 0002 0000 00fb 0887 2410 0000 0011 0000 0002 0000 00fb 0887 2410 00000011 0000 0002 0000 00fb 0887 2410 00000011 0000 0002 0000 00fb 0887 2410 00000011 0000 0
        0000 443a 5c00 0001 002e 00b3 0000 0009 0000 443a 5c00 0001 002e 00b3 0000 00090000 443a 5c00 0001 002e 00b3 0000 00090000 443a 5c00 0001 002e 00b3 0000 00090000 443a 5
        0000 a072 0000 0031 5350 5330 f125 b7ef 0000 a072 0000 0031 5350 5330 f125 b7ef0000 a072 0000 0031 5350 5330 f125 b7ef0000 a072 0000 0031 5350 5330 f125 b7ef0000 a072 0
        471a 10a5 f102 608c 9eeb ac31 0000 000a 471a 10a5 f102 608c 9eeb ac31 0000 000a471a 10a5 f102 608c 9eeb ac31 0000 000a471a 10a5 f102 608c 9eeb ac31 0000 000a471a 10a5 f
        0000 0000 1f00 0000 0f00 0000 5500 \033[32m5300\033[97m 0000 0000 1f00 0000 0f00 0000 5500 53000000 0000 1f00 0000 0f00 0000 5500 53000000 0000 1f00 0000 0f00 0000 5500 53000000 0000 1
        4200 2000 4400 7200 6900 7600 6500 2000 4200 2000 4400 7200 6900 7600 6500 20004200 2000 4400 7200 6900 7600 6500 20004200 2000 4400 7200 6900 7600 6500 20004200 2000 4
        2800 4400 3a00 2900 0000 0000 2500 0000 2800 4400 3a00 2900 0000 0000 2500 00002800 4400 3a00 2900 0000 0000 2500 00002800 4400 3a00 2900 0000 0000 2500 00002800 4400 3
        0400 0000 001f 0000 000a 0000 0055 0053 0400 0000 001f 0000 000a 0000 0055 00530400 0000 001f 0000 000a 0000 0055 00530400 0000 001f 0000 000a 0000 0055 00530400 0000 0
        0042 0020 0044 0072 0069 0076 0065 0000 0042 0020 0044 0072 0069 0076 0065 00000042 0020 0044 0072 0069 0076 0065 00000042 0020 0044 0072 0069 0076 0065 00000042 0020 0
        0000 0000 0035 0000 0031 5350 53a6 6a63 0000 0000 0035 0000 0031 5350 53a6 \033[32m6a630000\033[97m 0000 0035 0000 0031 5350 53a6 6a630000 0000 0035 0000 0031 5350 53a6 6a630000 0000 0
        283d 95d2 11b5 d600 c04f d918 d019 0000 283d 95d2 11b5 d600 c04f d918 d019 0000283d 95d2 11b5 d600 c04f d918 d019 0000283d 95d2 11b5 d600 c04f d918 d019 0000283d 95d2 1
        001e 0000 0000 1f00 0000 0400 0000 4400 001e 0000 0000 1f00 0000 0400 0000 4400001e 0000 0000 1f00 0000 0400 0000 4400001e 0000 0000 1f00 0000 0400 0000 4400001e 0000 0
          
          """)
          number = int()
          print(C)
          time.sleep(3)
        def reset(): 
          #this is when the user guesses the right username and password 
          for i in range(1):
            username = input("\033[97mplease enter your \033[32musername\033[97m:")
            password = input("please enter your \033[32mpassword\033[97m:\033[0;37;47m")
            if (credential.get(username) == password):
                print("\033[0;38;47mlogin \033[32msucceeded\033[97m")
                print("""  
            
        //  \033[96m _______ \033[93m __   __ \033[31m _______  \033[35m _______  ______    _______  _______  ______    _______  __   __     //
        //  \033[96m       | \033[93m|  | |  |\033[31m|       |  \033[35m        ||    _ |  |       ||       ||    _ |  |   _   ||  |_|  |   //
        //  \033[96m    ___| \033[93m|  |_|  |\033[31m|    ___|  \033[35m     _  ||   | ||  |   _   ||    ___||   | ||  |  |_|  ||       |   //
        //  \033[96m   |___  \033[93m|       |\033[31m|   |___   \033[35m    |_| ||   |_||_ |  | |  ||   | __ |   |_||_ |       ||       |   // 

        //  \033[96m    ___| \033[93m|_     _|\033[31m|    ___|  \033[35m     ___||    __  ||  |_|  ||   ||  ||    __  ||       ||       |   //
        //  \033[96m   |___  \033[93m |   |   \033[31m|   |___   \033[35m    |    |   |  | ||       ||   |_| ||   |  | ||   _   || ||_|| |   //
        //  \033[96m_______| \033[93m |___|   \033[31m|_______|  \033[35m ___|    |___|  |_||_______||_______||___|  |_||__| |__||_|   |_|   //


        //  \033[32m╔═╗┌─┐┌─┐┌─┐┌─┐┌─┐  ┌─┐┬─┐┌─┐┌┐┌┌┬┐┌─┐┌┬┐  
        //  ╠═╣│  │  ├┤ └─┐└─┐  │ ┬├┬┘├─┤│││ │ ├┤  ││  
        //  ╩ ╩└─┘└─┘└─┘└─┘└─┘  └─┘┴└─┴ ┴┘└┘ ┴ └─┘─┴┘  \033[97m


             """)
                #time.sleep(4.3)
                #A2 = 'welcome'
                #A3 = "1"
                #A1 = input("Do you wnat to enter the Wine server? If so type [welcome] twice x2  :)\n>>>\033[35m")
                #if A1 == input("welcome\033[97m\n"):
                    #print("\033[97mWrong answer, you're not a member of the server please leave now ^~^")
                    #print((hostname), (IPAddr))
                    #time.sleep(4.5)
                    #print(C)
                    #sys.exit()
                #if A1 == input("1"):
                    #print("Welcome to the Wine Server, I hope you enjoy your stay ")
                #else:
                    #print("\033[94mthat isn't a valid statement, please try again")
                    #print(C)
                    #reset()
                success = True
                break

            else:
                Fail = "\033[0;38;47m\033[31mlogin failed\033[97m"
                print(Fail)
                reset()

        reset()
        while True:
          for i in range(0, 2):
            print("""\033[94m
        |----------------------------------------------------------------------------------------------------------------------------------------|
            """)
            if Port1 == 'Tor port1: 9058a':
              print((W),(Tor))
              time.sleep(2)
              print((G), (OK1))
            else:
              print((W), (Tor), (R), (N), (Ko4))
              time.sleep(6)
            if Port2 == 'Tor Port2: 9085':
              print((W),(Tor))
              time.sleep(2)
              print((G), (OK2))
            else:
              print((W), (Tor), (R), (N), (Ko4))
              time.sleep(3)
            if Port3 == 'Tor port3: 9075a':
              print((W),(Tor))
              time.sleep(7)
              print((G), (OK3))
            else:
              print((W), (Tor), (R), (N), (Ko4))
              time.sleep(3)
            if Port4 == 'Tor port4: 9056':
              print((W),(Tor))
              time.sleep(1)
              print((G), (OK4))
              time.sleep(2)
            else:
              print((W), (Tor), (R), (N), (Ko4))
              time.sleep(3)
            print("""\033[94m
        |----------------------------------------------------------------------------------------------------------------------------------------|
            """)
            print(C)
            time.sleep(2)
          break
        print("""
                                                                                   \033[97mGreat! You're connected to all the Ports needed. 
                                                           You can now go ahead and crack that password! (Please Note that I Andrew Dumais do not condone any unethical hacking, this is for learning purposes only, please respect that)

            """)
        time.sleep(10)
        #By Andrew Dumais/Bleot_blot/wave\033[31m
        #Convert PY to EXE2q
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        while True:
          print(C)
          print("Hi this is a generic brute force password cracker\033[97m, I hope you use it for \033[32mgood\033[97m not \033[31mbad \033[97m:)")
          print("""

             

                                              _██_    \033[96mE\033[93m Y\033[31m E\033[97m    _██_
                                            ‹(•¿•)›           ‹(•¿•)›
                                            ..(█)             ..(█)
                                          .../ I             .../ I""")
          userA1 = input("What is the username?\n>>>\033[94m")
          #conneck API later for the instagram sequal server!
          #I have made a scrubber account for you, but in the meantime you should put the API in, while I am fixing the res.
          if userA1 == "mcr_fan__account":
            userA2 = input("\033[97mAre you sure this is the account?[\033[32mY/\033[31mN\033[97m]\n>>>\033[94m")
            if userA2 == 'Y':
              userA3 = input('\n\033[97m   You can now have a wonderful time cracking this password. Click the "\033[93menter\033[97m" key to continue the program. \033[32m\n   Note\033[97m:   (\033[31mThis could take several minutes\033[97m)')
              break
            if userA2 == 'N':
              print("Awe, that's okie, you'll enter it right next time ^.^")
              print(C)
              time.sleep(2)
          else:
            print("\033[97mThat's not a \033[31mvalid username\033[97m! Try another one, please and thank you.")
            time.sleep(2)
            print(C)
            time.sleep(.50)
        
        def guessing_username(fake):
          charss = string.ascii_lowercase + string.digits
          attemptss = 0
          for username_length in range(1, 11):
            for guessing in itertools.product(charss, repeat=username_length):
              attemptss += 1
              guessing = ''.join(guessing)
              print("\033[31m")
              #add cache for users who want to store passwords they've already cracked. We also, need to add another cache for them to start off where they left off, as this process can take a very long time to crack a password. In a little, we should give multiple options for: rainbow tables, dictionaries, brute force etc. There is a plan text API on github we can replicate (don't download it if you're not usong a tor proxy)
              
              if guessing == fake:
                return '\n\n\033[97mpassword:\033[97m = (\033[32m{}\033[97m)\npassword was found in: [\033[33m{}\033[97m] requests.'.format(guessing, attemptss)
                #prints the requests screen to the user
              print('\033[94m\033[0;37;47mpassword attempts\033[0;38;47m\033[32m---->\033[31m', '\033[97m(\033[31m', guessing, '\033[97m)', ' ''\033[97m|','\033[97m', '(\033[33m', attemptss, '\033[97m)',    '\033[32m<----\033[94mNumber of requests sent', ' \033[97m|  \033[94mElapsed time  \033[97m[\033[93m',time.perf_counter(),'\033[97m]')
        #This is just the "test case" don't worry you won't be using this "print(guessing_username(''))" as a official function.
        #We need to imput a rainbow table here at some point, sonething like hashcat; use Java if you need to, but make sure you add the depeniences for python. (if you knwo Jython use that instead, but I udnerstand if you don't)
        #add timer for the amount of time it takes for the script to pull the passwords plan text (not hashed)
        print(guessing_username('and1'))
        if guessing_username == 'an':
          print("Awesome job! We've succefully cracked that password, I hope you have a wonderful time on this new account ^~^")
          app()
        reset()


        #===============================================================================================================================================
        #===============================================================================================================================================
        #===============================================================================================================================================
        #===============================================================================================================================================
        #Stript this for the def statements inside of it (it's a piece of our old code ("The best special gift" etc...))



        #===============================================================================================================================================
        #===============================================================================================================================================
        #===============================================================================================================================================
        #===============================================================================================================================================
    ###########################################################################################################################################################################################################################################################################
    elif q1 == 'cm tic':
        R = '\033[31m'
        G = '\033[32m'
        W = '\033[97m'
        C = '\033[H\033[J'
        U = '\n\n\n\n\n\n\n\n\n\n\n'
        board=[i for i in range(0,9)]
        player, computer = '',''
        #// Corners, Center and Others, respectively
        moves=((1,7,3,9),(5,),(2,4,6,8))
        #// Winner combinations
        winners=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
        #// Table
        tab=range(1,10)
        def print_board():
            x=1
            for i in board:
                end = ' \033[93m| '
                if x%3 == 0:
                    end = ' \n'
                    if i != 1: end+='---------\n';
                char=' '
                if i in ('X','O'): char=i;
                x+=1
                print(char,end=end)
        def select_char():
            print(W)
            chars=('X','O')
            if random.randint(0,1) == 0:
                return chars[::-1]
            return chars
        def can_move(brd, player, move):
            if move in tab and brd[move-1] == move-1:
                return True
            return False
        def can_win(brd, player, move):
            places=[]
            x=0
            for i in brd:
                if i == player: places.append(x);
                x+=1
            win=True
            for tup in winners:
                win=True
                for ix in tup:
                    if brd[ix] != player:
                        win=False
                        break
                if win == True:
                    break
            return win
        def make_move(brd, player, move, undo=False):
            if can_move(brd, player, move):
                brd[move-1] = player
                win=can_win(brd, player, move)
                if undo:
                    brd[move-1] = move-1
                return (True, win)
            return (False, False)
        #// AI goes here
        def computer_move():
            move=-1
            #// If I can win, others do not matter.
            for i in range(1,10):
                if make_move(board, computer, i, True)[1]:
                    move=i
                    break
            if move == -1:
               #// If player can win, block him.
                for i in range(1,10):
                    if make_move(board, player, i, True)[1]:
                        move=i
                        break
            if move == -1:
                #// Otherwise, try to take one of desired places.
                for tup in moves:
                    for mv in tup:
                        if move == -1 and can_move(board, computer, mv):
                            move=mv
                            break
            return make_move(board, computer, move)
        def space_exist():
            return board.count('X') + board.count('O') != 9
        player, computer = select_char()
        print('Player is [%s] and computer is [%s]' % (player, computer))
        result='%%% Deuce ! %%%'
        while space_exist():
            print_board()
            print('\033[97mMake your move ! [1-9] : \033[94m', end='')
            move = int(input())
            moved, won = make_move(board, player, move)
            if not moved:
                print(' >> Invalid number ! Try again !')
                continue
            #//
            if won:
                print(G, (C))
                result='\033[32m*** Congratulations ! You won ! ***'
                print(Time_50)
                print(U)
                break
                sys.exit()
            elif computer_move()[1]:
                result='\033[31m=== You lose ! =='
                print(U,(Time_50))
                break;
        print(C)
        print_board()
        print(result)

    ################################################################################# 
    ##################################################elif q1 == "Tic":
      # Author: aqeelanwar
        # Created: 12 March,2020, 7:06 PM
        # Email: aqeel.anwar@gatech.edu
        size_of_board = 600
        symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
        symbol_thickness = 50
        symbol_X_color = '#EE4035'
        symbol_O_color = '#0492CF'
        Green_color = '#7BC043'


        class Tic_Tac_Toe():
            # ------------------------------------------------------------------
            # Initialization Functions:
            # ------------------------------------------------------------------
            def __init__(self):
                self.window = Tk()
                self.window.title('Tic-Tac-Toe')
                self.canvas = Canvas(self.window, width=size_of_board, height=size_of_board)
                self.canvas.pack()
                # Input from user in form of clicks
                self.window.bind('<Button-1>', self.click)

                self.initialize_board()
                self.player_X_turns = True
                self.board_status = np.zeros(shape=(3, 3))

                self.player_X_starts = True
                self.reset_board = False
                self.gameover = False
                self.tie = False
                self.X_wins = False
                self.O_wins = False

                self.X_score = 0
                self.O_score = 0
                self.tie_score = 0

            def mainloop(self):
                self.window.mainloop()

            def initialize_board(self):
                for i in range(2):
                    self.canvas.create_line((i + 1) * size_of_board / 3, 0, (i + 1) * size_of_board / 3, size_of_board)

                for i in range(2):
                    self.canvas.create_line(0, (i + 1) * size_of_board / 3, size_of_board, (i + 1) * size_of_board / 3)

            def play_again(self):
                self.initialize_board()
                self.player_X_starts = not self.player_X_starts
                self.player_X_turns = self.player_X_starts
                self.board_status = np.zeros(shape=(3, 3))

            # ------------------------------------------------------------------
            # Drawing Functions:
            # The modules required to draw required game based object on canvas
            # ------------------------------------------------------------------

            def draw_O(self, logical_position):
                logical_position = np.array(logical_position)
                # logical_position = grid value on the board
                # grid_position = actual pixel values of the center of the grid
                grid_position = self.convert_logical_to_grid_position(logical_position)
                self.canvas.create_oval(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
                                        grid_position[0] + symbol_size, grid_position[1] + symbol_size, width=symbol_thickness,
                                        outline=symbol_O_color)

            def draw_X(self, logical_position):
                grid_position = self.convert_logical_to_grid_position(logical_position)
                self.canvas.create_line(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
                                        grid_position[0] + symbol_size, grid_position[1] + symbol_size, width=symbol_thickness,
                                        fill=symbol_X_color)
                self.canvas.create_line(grid_position[0] - symbol_size, grid_position[1] + symbol_size,
                                        grid_position[0] + symbol_size, grid_position[1] - symbol_size, width=symbol_thickness,
                                        fill=symbol_X_color)

            def display_gameover(self):

                if self.X_wins:
                    self.X_score += 1
                    text = 'Winner: Player 1 (X)'
                    color = symbol_X_color
                elif self.O_wins:
                    self.O_score += 1
                    text = 'Winner: Player 2 (O)'
                    color = symbol_O_color
                else:
                    self.tie_score += 1
                    text = 'Its a tie'
                    color = 'gray'

                self.canvas.delete("all")
                self.canvas.create_text(size_of_board / 2, size_of_board / 3, font="cmr 60 bold", fill=color, text=text)

                score_text = 'Scores \n'
                self.canvas.create_text(size_of_board / 2, 5 * size_of_board / 8, font="cmr 40 bold", fill=Green_color,
                                        text=score_text)

                score_text = 'Player 1 (X) : ' + str(self.X_score) + '\n'
                score_text += 'Player 2 (O): ' + str(self.O_score) + '\n'
                score_text += 'Tie                    : ' + str(self.tie_score)
                self.canvas.create_text(size_of_board / 2, 3 * size_of_board / 4, font="cmr 30 bold", fill=Green_color,
                                        text=score_text)
                self.reset_board = True

                score_text = 'Click to play again \n'
                self.canvas.create_text(size_of_board / 2, 15 * size_of_board / 16, font="cmr 20 bold", fill="gray",
                                        text=score_text)

            # ------------------------------------------------------------------
            # Logical Functions:
            # The modules required to carry out game logic
            # ------------------------------------------------------------------

            def convert_logical_to_grid_position(self, logical_position):
                logical_position = np.array(logical_position, dtype=int)
                return (size_of_board / 3) * logical_position + size_of_board / 6

            def convert_grid_to_logical_position(self, grid_position):
                grid_position = np.array(grid_position)
                return np.array(grid_position // (size_of_board / 3), dtype=int)

            def is_grid_occupied(self, logical_position):
                if self.board_status[logical_position[0]][logical_position[1]] == 0:
                    return False
                else:
                    return True

            def is_winner(self, player):

                player = -1 if player == 'X' else 1

                # Three in a row
                for i in range(3):
                    if self.board_status[i][0] == self.board_status[i][1] == self.board_status[i][2] == player:
                        return True
                    if self.board_status[0][i] == self.board_status[1][i] == self.board_status[2][i] == player:
                        return True

                # Diagonals
                if self.board_status[0][0] == self.board_status[1][1] == self.board_status[2][2] == player:
                    return True

                if self.board_status[0][2] == self.board_status[1][1] == self.board_status[2][0] == player:
                    return True

                return False

            def is_tie(self):

                r, c = np.where(self.board_status == 0)
                tie = False
                if len(r) == 0:
                    tie = True

                return tie

            def is_gameover(self):
                # Either someone wins or all grid occupied
                self.X_wins = self.is_winner('X')
                if not self.X_wins:
                    self.O_wins = self.is_winner('O')

                if not self.O_wins:
                    self.tie = self.is_tie()

                gameover = self.X_wins or self.O_wins or self.tie

                if self.X_wins:
                    print('X wins')
                if self.O_wins:
                    print('O wins')
                if self.tie:
                    print('Its a tie')

                return gameover





            def click(self, event):
                grid_position = [event.x, event.y]
                logical_position = self.convert_grid_to_logical_position(grid_position)

                if not self.reset_board:
                    if self.player_X_turns:
                        if not self.is_grid_occupied(logical_position):
                            self.draw_X(logical_position)
                            self.board_status[logical_position[0]][logical_position[1]] = -1
                            self.player_X_turns = not self.player_X_turns
                    else:
                        if not self.is_grid_occupied(logical_position):
                            self.draw_O(logical_position)
                            self.board_status[logical_position[0]][logical_position[1]] = 1
                            self.player_X_turns = not self.player_X_turns

                    # Check if game is concluded
                    if self.is_gameover():
                        self.display_gameover()
                        # print('Done')
                else:  # Play Again
                    self.canvas.delete("all")
                    self.play_again()
                    self.reset_board = False


        game_instance = Tic_Tac_Toe()
        game_instance.mainloop()




    else:
        print((R),"That's not a valid statement!")
        time.sleep(1.5)
        print(C)
        cm()
    return cm
cm() 


def update_list(list):
    for elem in list:
        elem.update()


def draw_list(list):
    for elem in list:
        elem.draw()


def cleanup_list(list):
    i = 0
    while i < len(list):
        elem = list[i]
        if not elem.alive:
            list.pop(i)
        else:
            i += 1


class Background:
    def __init__(self):
        self.star_list = []
        for i in range(STAR_COUNT):
            self.star_list.append(
                (random() * pyxel.width, random() * pyxel.height, random() * 1.5 + 1)
            )

    def update(self):
        for i, (x, y, speed) in enumerate(self.star_list):
            y += speed
            if y >= pyxel.height:
                y -= pyxel.height
            self.star_list[i] = (x, y, speed)

    def draw(self):
        for (x, y, speed) in self.star_list:
            pyxel.pset(x, y, STAR_COLOR_HIGH if speed > 1.8 else STAR_COLOR_LOW)


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = PLAYER_WIDTH
        self.h = PLAYER_HEIGHT
        self.alive = True

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= PLAYER_SPEED

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += PLAYER_SPEED

        if pyxel.btn(pyxel.KEY_UP):
            self.y -= PLAYER_SPEED

        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += PLAYER_SPEED

        self.x = max(self.x, 0)
        self.x = min(self.x, pyxel.width - self.w)
        self.y = max(self.y, 0)
        self.y = min(self.y, pyxel.height - self.h)

        if pyxel.btnp(pyxel.KEY_SPACE):
            Bullet(
                self.x + (PLAYER_WIDTH - BULLET_WIDTH) / 2, self.y - BULLET_HEIGHT / 2
            )

            pyxel.play(0, 0)

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, self.w, self.h, 0)


class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = BULLET_WIDTH
        self.h = BULLET_HEIGHT
        self.alive = True

        bullet_list.append(self)

    def update(self):
        self.y -= BULLET_SPEED

        if self.y + self.h - 1 < 0:
            self.alive = False

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, BULLET_COLOR)


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = ENEMY_WIDTH
        self.h = ENEMY_HEIGHT
        self.dir = 1
        self.alive = True
        self.offset = int(random() * 60)

        enemy_list.append(self)

    def update(self):
        if (pyxel.frame_count + self.offset) % 60 < 30:
            self.x += ENEMY_SPEED
            self.dir = 1
        else:
            self.x -= ENEMY_SPEED
            self.dir = -1

        self.y += ENEMY_SPEED

        if self.y > pyxel.height - 1:
            self.alive = False

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 8, 0, self.w * self.dir, self.h, 0)


class Blast:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = BLAST_START_RADIUS
        self.alive = True

        blast_list.append(self)

    def update(self):
        self.radius += 1

        if self.radius > BLAST_END_RADIUS:
            self.alive = False

    def draw(self):
        pyxel.circ(self.x, self.y, self.radius, BLAST_COLOR_IN)
        pyxel.circb(self.x, self.y, self.radius, BLAST_COLOR_OUT)


class App:
    def __init__(self):
        pyxel.init(120, 160, caption="Pyxel Shooter")

        pyxel.image(0).set(
            0,
            0,
            [
                "00c00c00",
                "0c7007c0",
                "0c7007c0",
                "c703b07c",
                "77033077",
                "785cc587",
                "85c77c58",
                "0c0880c0",
            ],
        )

        pyxel.image(0).set(
            8,
            0,
            [
                "00088000",
                "00ee1200",
                "08e2b180",
                "02882820",
                "00222200",
                "00012280",
                "08208008",
                "80008000",
            ],
        )

        pyxel.sound(0).set("a3a2c1a1", "p", "7", "s", 5)
        pyxel.sound(1).set("a3a2c2c2", "n", "7742", "s", 10)

        self.scene = SCENE_TITLE
        self.score = 0
        self.background = Background()
        self.player = Player(pyxel.width / 2, pyxel.height - 20)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        self.background.update()

        if self.scene == SCENE_TITLE:
            self.update_title_scene()
        elif self.scene == SCENE_PLAY:
            self.update_play_scene()
        elif self.scene == SCENE_GAMEOVER:
            self.update_gameover_scene()

    def update_title_scene(self):
        if pyxel.btnp(pyxel.KEY_ENTER):
            self.scene = SCENE_PLAY

    def update_play_scene(self):
        if pyxel.frame_count % 6 == 0:
            Enemy(random() * (pyxel.width - PLAYER_WIDTH), 0)

        for a in enemy_list:
            for b in bullet_list:
                if (
                    a.x + a.w > b.x
                    and b.x + b.w > a.x
                    and a.y + a.h > b.y
                    and b.y + b.h > a.y
                ):
                    a.alive = False
                    b.alive = False

                    blast_list.append(
                        Blast(a.x + ENEMY_WIDTH / 2, a.y + ENEMY_HEIGHT / 2)
                    )

                    pyxel.play(1, 1)

                    self.score += 10

        for enemy in enemy_list:
            if (
                self.player.x + self.player.w > enemy.x
                and enemy.x + enemy.w > self.player.x
                and self.player.y + self.player.h > enemy.y
                and enemy.y + enemy.h > self.player.y
            ):
                enemy.alive = False
                blast_list.append(
                    Blast(
                        self.player.x + PLAYER_WIDTH / 2,
                        self.player.y + PLAYER_HEIGHT / 2,
                    )
                )

                pyxel.play(1, 1)

                self.scene = SCENE_GAMEOVER

        self.player.update()
        update_list(bullet_list)
        update_list(enemy_list)
        update_list(blast_list)

        cleanup_list(enemy_list)
        cleanup_list(bullet_list)
        cleanup_list(blast_list)

    def update_gameover_scene(self):
        update_list(bullet_list)
        update_list(enemy_list)
        update_list(blast_list)

        cleanup_list(enemy_list)
        cleanup_list(bullet_list)
        cleanup_list(blast_list)

        if pyxel.btnp(pyxel.KEY_ENTER):
            self.scene = SCENE_PLAY
            self.player.x = pyxel.width / 2
            self.player.y = pyxel.height - 20
            self.score = 0

            enemy_list.clear()
            bullet_list.clear()
            blast_list.clear()

    def draw(self):
        pyxel.cls(0)

        self.background.draw()

        if self.scene == SCENE_TITLE:
            self.draw_title_scene()
        elif self.scene == SCENE_PLAY:
            self.draw_play_scene()
        elif self.scene == SCENE_GAMEOVER:
            self.draw_gameover_scene()

        pyxel.text(39, 4, "SCORE {:5}".format(self.score), 7)

    def draw_title_scene(self):
        pyxel.text(35, 66, "Pyxel Shooter", pyxel.frame_count % 16)
        pyxel.text(31, 126, "- PRESS ENTER -", 13)

    def draw_play_scene(self):
        self.player.draw()
        draw_list(bullet_list)
        draw_list(enemy_list)
        draw_list(blast_list)

    def draw_gameover_scene(self):
        draw_list(bullet_list)
        draw_list(enemy_list)
        draw_list(blast_list)

        pyxel.text(43, 66, "GAME OVER", 8)
        pyxel.text(31, 126, "- PRESS ENTER -", 13)


App()