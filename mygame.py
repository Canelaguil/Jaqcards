import classes
import sys

        
class Greek_Game:
    def __init__(self):
        print("Hold on while we load your game...")
        # Instantiate Characters
        self.alkie = Non_Playable_Character("Deitomachos", None, 2, sex_or = 2)
        self.questguy = Non_Playable_Character("Sisenem", "The Wise", 2
        self.you = Playable_Character("", "Eagle Bearer", None, None, None, sex_or = 2)
        # Player goals
        is_athenian = Goal("ath", "Affiliation with Athens", "How much does Kassandra identify herself with Athens?")
        is_spartan = Goal("spar", "Affiliation with Sparta", "How much does Kassandra identify herself with Sparta?")
         
        # Global vars
        self.global[self.you.name, self.you.gender]
                                               
        self.cards = self.read_cards()
     
    def play_game():
        i = 0
        while True:
            card = cards[i]
            print(card.text)
            print("Option 1:") 
            print(card.options[0])
            print("Option 2:")
            print(card.options[1])
            ip = input("Your choice: ")
            if ip is "1":
                changes = card.changes1
            elif ip is "2":
                changes = card.changes2
            
                                               
    
    def read_cards(self): 
        cur = Card()
        o1 = True
        for line in sys.stdin:
            cur_line = line.split(' ')
            if cur_line[0] is "***":
                self.cards.append(cur)
                cur = Card()
            elif cur_line[0] is "*":
                txt = line.replace("* ", "")
                cur.options.append(txt)
                o1 = not o1
            elif cur_line[0] is "/":
                i = int(cur_line[1])               
                txt = line.replace("/ ", "")
                if o1:
                    cur.changes1.append((i, txt))
                else:
                    cur.changes2.append((i, txt))
            elif cur_line[0] is "//":
                i = int(cur_line[1])               
                txt = line.replace("// ", "")
                if o1:
                    cur.changes1.append((i, txt))
                else:
                    cur.changes2.append((i, txt))
            elif cur_line[0] is "+":
                i = int(cur_line[1])               
                txt = line.replace("/ ", "")
                if o1:
                    cur.changes1.append((i, txt))
                else:
                    cur.changes2.append((i, txt))
            else:
                cur.text.append(line.strip())
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  