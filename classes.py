"""
Date:           02/01/2020
Made by:        Clara Martens Avila
Description:    Classes, some of which are not yet used, to run a game in Jaqcards.

"""

## CHARACTER CLASSES ##
class Character:
    def __init__(self, char_name, char_surname, gender, home=None, loc=None, sex_or=0):
        self.name = char_name
        self.surname = char_surname
        self.description = ""
        self.job = None
        self.state = "alive"
        self.home_location = home
        self.location = loc
        self.diguise = None
        # {person: goodwill}
        self.people = {}
        # 0=not available, 1=hetero, 2=bi
        self.sexual_orientation = sex_or
        # 0=not specified, 1=female, 2=male
        self.gender = gender
        # {"keyword": Goal}
        self.goals = {}


class Playable_Character(Character):
    def __init__(self, char_name, char_surname, gender, home=None, loc=None, sex_or=0):
        super().__init__(char_name, char_surname, gender, home=None, loc=None, sex_or=0)
        # Consists of Item()s
        self.inventory = []
        self.marks = 0


class Non_Playable_Character(Character):
    def __init__(self, char_name, char_surname, gender, home=None, loc=None, sex_or=0, job=None):
        super().__init__(char_name, char_surname, gender, home=None, loc=None, sex_or=0)
        self.job = job


## WORLD CLASSES ##
class Job:
    def __init__(self, job_title, loc=None, work_hours=[7, 18]):
        self.location = job
        self.job = job_title
        self.working_hours = work_hours


class Location:
    def __init__(self, title, img=None, description=""):
        self.name = title
        self.img = img
        self.people_present = []
        self.description = description


class Store(Location):
    def __init__(self, title, img=None, description="", workers=[], inventory=[]):
        super().__init__(title, img, description)
        self.employees = workers
        self.items = inventory


class Item:
    def __init__(self, name, category, title, img=None, description="", food=False):
        self.category = category
        self.food = food
        self.description = description


## GAMEPLAY CLASSES ##
class Goal:
    def __init__(self, keyword, title, description, multiplier=1, points=0):
        self.key = keyword
        self.title = title
        self.description = description
        self.multiplier = multiplier
        self.points = points

    def update_points(self, aggr):
        self.points += aggr * self.multiplier

    def set_points(self, p):
        self.points = p

    def update_multiplier(self, aggr):
        self.multiplier += aggr

    def set_multiplier(self, new_mul):
        self.multiplier = new_mul


class Card:
    def __init__(self):
        self.i = 0
        self.no_options = 0
        self.text = []
        self.dialogue = []
        self.options = []
        self.changes = []


class Switch:
    def __init__(self):
        self.i = 0
        self.condition = []
        self.default = 0


## PROCESSES ##
