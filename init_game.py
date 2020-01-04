"""
Date:           02/01/2020
Made by:        Clara Martens Avila
Description:    An intepreter that gets certain kinds of files as
                input and runs them as a CLI-based Choose Your Own
                Adventure Game.

"""

from classes import *
import sys
import signal
import os.path
import textwrap


def sanitize(string):
    san = string.strip()
    sanit = san.replace("\n", "")
    return sanit


class New_Game:

    def __init__(self):
        # Global vars
        self.characters = {}
        self.hop_size = 0
        self.chapter_files = []
        self.no_chapters = 1

        # Extra inits
        signal.signal(signal.SIGINT, self.signal_handler)

        # Initialization of characters and cards
        f1, f2 = self.check_files()
        self.init_characters(f1)
        self.init_goals(f2)

        # Start game
        for chapter in self.chapter_files:
            self.i = 0
            self.seen = 0
            self.hop = False
            self.cards = []
            self.init_cards(chapter)
            print("Press enter to continue.")
            self.play_game()

    def signal_handler(self, sig, frame):
        print("\nExiting the game. No progress saved.")
        sys.exit()

    def check_files(self):
        """
        Checks if all files are given as arguments, and are indeed
        files.
        """
        files = []

        if sys.argv[1] == 'help':
            file = open('input/help.input')
            for line in file:
                print(sanitize(line))
            ans = input("\n\nDo you want some examples? [Y/n] ")
            ans = sanitize(ans)
            if ans == 'Y':
                file = open('input/examples.input')
                for line in file:
                    print(sanitize(line))
            sys.exit()

        if len(sys.argv) is not 4:
            if len(sys.argv) is 2:
                if os.path.isfile(sys.argv[1]):
                    gamefile = open(sys.argv[1])
                    f_line = True
                    for f in gamefile:
                        fi = sanitize(f)
                        if f_line:
                            self.no_chapters = int(fi)
                            f_line = False
                        else:
                            files.append(fi)
            else:
                print(
                    "This game requires 3 files as arguments OR a file containing these three:")
                print("-A character file")
                print("-A goal file")
                print("-A card file")
                print(
                    "If you're not sure about the input format, run 'python3 init_game help'.")
                sys.exit()
        else:
            files.append(sys.argv[1])
            files.append(sys.argv[2])
            files.append(sys.argv[3])

        for file in files:
            if not os.path.isfile(file):
                print(
                    "{} was not recognized as file. Please try again with a correct filepath.".format(file))
                sys.exit()

        print("Hold on while we load your game...")
        characters = files[0]
        goals = files[1]
        self.chapter_files = files[2:]
        print("... found {} chapters...".format(len(self.chapter_files)))
        return characters, goals

    def init_characters(self, file_name):
        """
        Initializes all characters from the character file.
        """
        file = open(file_name)
        attributes = []
        for line in file:
            line = line.split(' ')
            if line[0] == '&':
                cid = sanitize(line[1])
                if cid == 'you':
                    self.characters[cid] = Playable_Character(*attributes)
                else:
                    self.characters[cid] = Non_Playable_Character(*attributes)
                attributes = []
            else:
                item = sanitize(line[0])
                attributes.append(item)

        if len(self.characters) == 0:
            print(
                "Something went wrong. Please check your character file before trying again.")
            sys.exit()

        print("... succesfully loaded {} characters...".format(len(self.characters)))

    def init_goals(self, file_name):
        """
        Initializes all goals from the goal file.
        """
        no_goals = 0
        key = ""
        g_key = ""
        goals = {}
        goal_atr = []

        file = open(file_name)
        for line in file:
            if line[0] == '&':
                temp = line.split(' ')
                key = sanitize(temp[1])
                self.characters[key].goals = goals
                goals = {}
            elif line[0] == '+':
                temp = line.split(' ')
                g_key = sanitize(temp[1])
                goal_atr.insert(0, g_key)
                goals[g_key] = Goal(*goal_atr)
                goal_atr = []
                no_goals += 1
            else:
                atr = sanitize(line)
                goal_atr.append(atr)

        if no_goals == 0:
            print(
                "Something went wrong. Please check your goal file before trying again.")
            sys.exit()

        print("... succesfully loaded {} goals...".format(no_goals))

    def init_cards(self, file_name):
        """
        Initializes all cards from the card file.
        """
        file = open(file_name)
        cur = Card()
        switch = False
        cur_switch = Switch()
        o = -1
        count = 0
        for line in file:
            cur_line = line.split(' ')
            action = sanitize(cur_line[0])
            if action == '&':
                cur.no_options = o + 1
                count += 1
                cur.i = count
                self.cards.append(cur)
                cur = Card()
                o = -1
            elif action == '+':
                switch = True
            elif action == '++':
                cur_switch.default = cur_line[1]
                self.cards.append(cur_switch)
                cur_switch = Switch()
                switch = False
            elif action == '*':
                txt = line.replace("* ", "")
                txt = sanitize(txt)
                cur.options.append(txt)
                cur.changes.append([])
                o += 1
            elif action == '-':
                txt = sanitize(line)
                cur.dialogue.append(txt)
            elif action == '%':
                pass
            elif action == 'ju' or action == 'xXx' or action == 'XXX':
                do_thing = sanitize(line)
                cur.changes[o].append(do_thing)
            elif action == '!' or action == '#':
                if switch:
                    con = sanitize(line)
                    cur_switch.condition.append(con)
                else:
                    # ! you spartan 10
                    chan = sanitize(line)
                    cur.changes[o].append(chan)
            else:
                sentence = sanitize(line)
                cur.text.append(sentence)

        self.no_cards = len(self.cards)
        if self.no_cards == 0:
            print(
                "Something went wrong. Please check your card file before trying again.")
            sys.exit()

        print("... succesfully loaded {} cards for this chapter...".format(self.no_cards))

    def ask_input(self, options):
        """
        Generates a loop till the user gives correct input.
        """
        while True:
            ip = ""
            try:
                ip = input("\n-Your choice: ")
            except EOFError:
                pass
            try:
                ip = int(ip)
            except:
                print("Your choice needs to be a number.")
                continue
            if 1 <= ip <= options:
                print("")
                return ip
            print("That input wasn't valid.")

    def check_commands(self):
        """
        Checks for user commands.
        """
        u = ""
        try:
            u = input("")
        except EOFError:
            pass
        u_in = sanitize(u)
        if u_in == "":
            return
        elif u_in == 'exit':
            print("Are you sure you want to leave the game?")
            u2 = input("[Y/n]: ")
            if u2 == 'Y':
                sys.exit()
        elif u_in == "back":
            if self.i > 0:
                self.hop = True
                self.hop_size = -1
        elif u_in == "wherami":
            print(self.i)

        if 'goto' in u_in:
            command = u_in.split(' ')
            self.i = int(command[1])

    def print_card(self, card):
        """
        Prints all the text associated to the card.
        """
        print("-" * 70)

        # If title card
        if card.text != []:
            if card.text[0][0] == '[':
                print('\n' * 2)
                for line in card.text:
                    text = sanitize(line[2:])
                    spaces = (70 - len(text)) / 2
                    space = ' ' * int(spaces)
                    print(space + text)
                print('\n')
                return

        # Print normal text
        whole = ""
        for line in card.text:
            whole += line + " "

        arr = textwrap.wrap(whole)

        for line in arr:
            print(line)

        # Print dialogue
        for line in card.dialogue:
            line = textwrap.wrap(line)
            for sen in line:
                print(sen)

        # Print options
        if card.no_options > 0:
            print("")

        i = 1
        for option in card.options:
            print("++ {}:".format(i))
            op = textwrap.wrap(option)
            for line in op:
                print(line)
            i += 1

    def change_vars(self, changes):
        """
        Changes variables depending on the choice of the user.
        """
        for change in changes:
            c = change.split(" ")
            first_c = c[0]
            if first_c == '!':
                # ! you spartan 10
                obj = self.characters[c[1]]
                goal = c[2]
                obj.goals[goal].points = c[3]
            elif first_c == '#':
                # # you name Kassandra
                obj = self.characters[c[1]]
                atr = c[2]
                new_value = c[3]
                setattr(obj, atr, new_value)
            elif first_c == 'ju':
                self.hop = True
                self.hop_size = int(c[1])
            elif first_c == 'xXx':
                print("You've reached the end of the chapter.")
                print("You've seen {} out of {} cards.".format(
                    self.seen, len(self.cards)))
                self.i += 100000
            elif first_c == 'XXX':
                print("You've reached the end of the game.")
                print("You've seen {} out of {} cards in this chapter.".format(
                    self.seen, len(self.cards)))
                sys.exit()
            else:
                print("One of the changes was not formatted correctly.")


    def get_switched_index(self, switch):
        """
        Returns new variable based on what condition is true.
        """
        # ! you spartan 5 1 10
        for condition in switch.condition:
            c=condition.split(" ")
            first_c=c[0]
            if first_c == '!':
                obj=self.characters[c[1]]
                goal_list=getattr(obj, "goals", "error")
                p=int(goal_list[c[2]].points)
                if p > int(c[3]):
                    return int(c[4]), int(c[5])
            elif first_c == '#':
                obj=self.characters[c[1]]
                atr=c[2]
                cur_value=getattr(obj, atr, "error")
                if cur_value == c[3]:
                    return int(c[4]), int(c[5])

        return int(switch.default), 1


    def play_game(self):
        """
        Contains the actual game loop, including (sub-)jump_i.
        """

        while self.i < self.no_cards:
            card=self.cards[self.i]

            if isinstance(card, Card):
                self.print_card(card)
                if card.no_options > 0:
                    user=self.ask_input(card.no_options) - 1
                    self.change_vars(card.changes[user])
                else:
                    self.check_commands()

                if self.hop:
                    self.i += self.hop_size
                    self.hop=False
                else:
                    self.i += 1
            elif isinstance(card, Switch):
                modifier, self.hop_size=self.get_switched_index(card)
                self.i += modifier
                self.hop=True

            self.seen += 1

new_game=New_Game()
