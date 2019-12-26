import sys

def ask_opinion():
    name = sys.argv[0]
    file = open(name)
    for line in file:
        print("Be happy!")
    while True:
        op = input("Are you happy?")
        print(op)

ask_opinion()