from classes import *
import sys
import time
import textwrap

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
            card = self.cards[i]
            if loop:
                self.print_text(card.text, card.options)
            loop = True
            if len(card.options) > 0:
                ip = input("\nYour choice: ")
                
                if ip is "1":
                    changes = card.changes[0]
                    i = i + card.modifier[0]
                elif ip is "2":
                    changes = card.changes[1]
                    i = i + card.modifier[1]
                else: 
                    print("That wasn't a choice.")
                    loop = False
                    continue

                print("------------------")
                
                for change in changes:
                    self.change_variables(int(change[0]), change[1])
            else:
                print("------------------")
                i = i + card.modifier[0]
                wait = input()
                                 
    
    def read_cards(self):
        argument = sys.argv[1]
        file = open(argument)
        
        cur = Card()
        o = -1
        for line in file:
            cur_line = line.split(' ')
            action = sanitize(cur_line[0])
            if action is "&":
                #print("I made a new card") 
                cur.no_ops = o + 1
                self.cards.append(cur)
                cur = Card()
                o = -1
            elif action is "*":
                #print("I came upon an option") 
                txt = line.replace("* ", "")
                txt = sanitize(txt)
                cur.options.append(txt)
                cur.changes.append([])
                o += 1
            elif action is "/":
                #print("I found a string") 
                i = sanitize(cur_line[1])
                index = int(i)               
                txt = line.replace("/ {}".format(i), "")
                txt = sanitize(txt)
                cur.changes[o].append((index, txt))
            elif action is "!":
                #print("I found an int") 
                i = sanitize(cur_line[1])
                i = int(i)               
                txt = cur_line[2].replace("! ", "")
                number = sanitize(txt)
                number = int(number)
                cur.changes[o].append((i, number))
            elif cur_line[0] is "+":
                #print("I changed the index")
                i = sanitize(cur_line[1])
                i = int(i)
                cur.modifier.append(i)
            else:
                #print("I added some text") 
                sentence = sanitize(line)
                cur.text.append(sentence)
   
new_game = Greek_Game()                
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  