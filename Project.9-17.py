import random
import time

def playing():
   print("--------------------------------------------------------------------------------------")
   x = 0
   y = 0
   win_lost = ["Your team won the round", "The other team won the round"]
   for x in range(0, 5):
       chance = print(random.choice(win_lost))
   if chance == "Your team won the round":
       x += 1
   else:
       y += 1
       if x == 3:
           print("You won")
       else:
           y == 3
           print("You lost")


def map_theme():
   print("ysef")

def map_bank():
   playing()

def team():
   team_side = ["Attacking", "Defending"]
   choose_side = (random.choice(team_side))
   if choose_side[0] == "A":
       print("Your team attacking.")
   elif choose_side[0] == "D":
       print("Your team defending.")
   decided_map()

def maps():
   map_play = ["Bank", "ThemePark", "Skyscraper", ]
   print("--------------------------------------------------------------------------------------")
   print(map_play)
   choose_map = input("Choose what map you would like to play out of that list. ")
   print("--------------------------------------------------------------------------------------")
   if choose_map[0].lower() == "b":
       map_bank()
   elif choose_map[0].lower() == "t":
       map_theme()
   elif choose_map[0].lower() == "s":
       map_sky()


def searching():
   time.sleep(1)
   print("--------------------------------------------------------------------------------------")
   print("Thank you! Hold on while we search for a game.")
   time.sleep(5)
   print("--------------------------------------------------------------------------------------")
   print("Match found!")
   maps()

def profile():
   print("--------------------------------------------------------------------------------------")
   user_profile = {
       'username': "username",
       'rank': "rank"
   }
   while True:
       user = input("Enter your username. ")
       rank = input("Now enter your rank elo. ")
       break

   user_profile['username'] = user
   user_profile['rank'] = rank
   print(user_profile)
   searching()

def choose_op():
   operator = input("Choose what operator you would like to play? ")
   print("--------------------------------------------------------------------------------------")

def start_siege():  # Starting the Main game
   star = True
   while star:
       play = input("Do you want to play? Yes or no? ")
       if play[0].lower() == "y":
           time.sleep(.5)
           print("Okay! Let's do this.")
           time.sleep(1)
           profile()
           break
       elif play[0].lower() == "n":
           print("alright, fine.")
           break
       else:
           print("Give a valid command.")
           star = True

start_siege()
