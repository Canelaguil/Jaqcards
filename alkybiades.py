from classes import *
import sys
import time
import textwrap

"""
TODO
-De o1 afhandeling van de modifiers goed krijgen (met index?)
"""
def sanitize(string):
    san = string.strip()
    sanit = san.replace("\n", "") 
    return sanit
        
class Greek_Game:
    def __init__(self):
        print("Hold on while we load your game...")
        # Instantiate Characters
        self.alkie = Non_Playable_Character("Deitomachos", None, 2)
        self.questguy = Non_Playable_Character("Sisenem", "The Wise", 2)
        self.you = Character("", "Eagle Bearer", 0)
        
        # Player goals
        is_athenian = Goal("ath", "Affiliation with Athens", "How much does Kassandra identify herself with Athens?")
        is_spartan = Goal("spar", "Affiliation with Sparta", "How much does Kassandra identify herself with Sparta?")
         
        # Global vars
        self.cards = []                        
        self.read_cards()
        self.play_game()
        
    def change_variables(self, vn, new_value):
        if vn == 0:
            self.you.name = new_value
        elif vn == 1:
            self.you.gender = new_value
        elif vn == 2:
            self.is_athenian.update_points(new_value)
        elif vn == 2:
            self.is_spartan.update_points(new_value)
    
    def print_text(self, text, options):
        whole = ""
        print("")
        for line in text:
            if line[0] == '-':
                if text[0] == line:
                    whole = whole + line + "\n"
                else: 
                    whole = whole + "\n" + line + "\n"
            else: 
                whole = whole + line + " "
        
        print(whole)
        if len(options) > 0:
            print("--Option 1:") 
            print(options[0])
            print("--Option 2:")
            print(options[1])
     
    def play_game(self):
        no_cards = len(self.cards)

        if no_cards == 0:
            print("The game didn't load correctly, please try again later.")
            sys.exit()

        print("Are you ready to start your adventure?") 
        wait = input("Press any key to continue.\n") 
        print("------------------")
        
        loop = True
        i = 0
        while i < no_cards:
            print(i)
            card = self.cards[i]
            if loop:
                self.print_text(card.text, card.options)
            loop = True
            if len(card.options) > 0:
                ip = input("Your choice: ")
                #ip = "1"
                
                if ip is "1":
                    changes = card.changes1
                    i = i + card.modifier1
                    print(card.modifier1)
                    print(i)
                elif ip is "2":
                    changes = card.changes2
                    i = i + card.modifier2
                    print(card.modifier2)
                    print(i)
                else: 
                    print("That wasn't a choice.")
                    loop = False
                    continue
                print(changes)
                print("------------------")
                
                for change in changes:
                    self.change_variables(int(change[0]), change[1])
            else:
                print("------------------")
                i = i + card.modifier1
                wait = input()
                                 
    
    def read_cards(self):
        argument = sys.argv[1]
        file = open(argument)
        
        cur = Card()
        o1 = True
        for line in file:
            cur_line = line.split(' ')
            action = sanitize(cur_line[0])
            if action is "&":
                #print("I made a new card") 
                self.cards.append(cur)
                cur = Card()
                o1 = True
            elif action is "*":
                print("I came upon an option") 
                print(o1)
                txt = line.replace("* ", "")
                txt = sanitize(txt)
                cur.options.append(txt)
                o1 = not o1
            elif action is "/":
                print("I found a string") 
                i = sanitize(cur_line[1])
                index = int(i)               
                txt = line.replace("/ {}".format(i), "")
                txt = sanitize(txt)
                if o1:
                    print(txt)
                    cur.changes1.append((index, txt))
                else:
                    cur.changes2.append((index, txt))
            elif action is "!":
                print("I found an int") 
                i = sanitize(cur_line[1])
                i = int(i)               
                txt = cur_line[2].replace("! ", "")
                number = sanitize(txt)
                number = int(number)
                if o1:
                    cur.changes1.append((i, number))
                else:
                    cur.changes2.append((i, number))
            elif cur_line[0] is "+":
                print("I changed the index")
                i = sanitize(cur_line[1])
                i = int(i)
                if not o1:
                    cur.modifier2 = i
                else:
                    cur.modifier1 = i
            else:
                #print("I added some text") 
                sentence = sanitize(line)
                cur.text.append(sentence)
   
new_game = Greek_Game()                
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  