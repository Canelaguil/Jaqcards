import sys

def ask_opinion():
    x = "myvar"
    print(exec("%s = %d" % (x, 2)))
    print(myvar)

ask_opinion()