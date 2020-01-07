# Jaqcards
Jaqcards is an interpeter for text-based choose-your-own-adventure storygames. The input files are in a straight-forward
format that's easy for anyone to write, whether you're a programmer or not (it's comparable to Markdown, if that sounds familiar).

Right now I'm working on a three-part story on the historical character of Alkybiades (loosely inspired by AC Odyssey) which
you can already play the first chapter of.

## For Players
### If you have python3 installed on your computer:
Just clone or download this repository and run the Alkybiades game with this command:
```
python3 init_game.py SnakeInTheGrass
```
This will initialize all the right files listed in the SnakeInTheGrass file.
### If you don't have python3 installed on your computer:
I'm working on creating a neat executable to download. Till then, stay tuned...
## For Story Writers
Check out the help.input file in the input folder! This file also appears when you run init_game.py with 'help' as argument.
Here follows a quick recap of the basic concepts you need to understand:
### Jumping around cards
Each story is told through a sequence of cards. Ideally a card is a few lines of text with or without dialogue. Some cards have
options on them, more on that later. The default jump from one card to the next in the story is +1. In special cases you can set
this to more and have the reader jump around cards (though this happens under the hood, the reader never notices). You can move both
forwards and backwards with jumps.
### Actions
Some cards give the player options on how to continue. Maybe there are two ways to go home, either through main street
or passing by the church. Each option then sets into motion a few actions. One action will be that choosing the church route makes
you jump over the cards specifying the trip through main street. Imagine you want to keep track of how religious your player
is showing to be. Then one action you can set into motion by the church choice is to add points to a thing we call goals.
### Goals and switches
One thing that distinguishes Jaqcard stories from choose-your-own-adventure books is that Jaqcard can keep track of values. 
Specifically, it can keep track of writer-defined "goals". A goal can be for example "show compassion to character X". Now
everytime your player shows compassion to X you can add points to that goal. And how do you reintigrate this into your game
later? Well, with switches. Switches are special cards that only contain conditions. So, at the end of a conversation with X
you could have a switch that checks if the points for that goals are more than 60, and if they are, X can show their gratitude
towards the player.

### Testing your story
To make it easier to skip to the part of your story that you want to test there are a few commands you can type instead of typing enter when you go to the next card. Be aware that this isn't the case when Jaqcards is waiting for user input.
```
whereami - prints the index of the current card
goto [index] - jumps to the specified index
```
### Input files
Goals belong to a character and charactes need to be defined. You therefore need (at least) three input files. 
1. A character file, defining the characters that are gonna have goals
2. A goal file, defining the goals for each character
3. One or more cards files (if there are more they're considered chapters)

You can read more on all of this in the help.input file in the input folder! Be sure to check out the existing story as well.

## For Developers
I mean, if you're here you probably have some idea of what you want to do with this so... Just do it. The code is quite
self explanatory.
