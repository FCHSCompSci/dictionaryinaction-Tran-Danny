import random
import time

team1 = 0
team2 = 0

win_lost = ["Your team won the round", "The other team won the round"]


attackers = ["sledge", "thatcher", "ash", "thermite", "twitch", "montagne"]
defenders = [""]

user_profile = {
     'username': "username",
     'rank': "rank",
     'spawn': "spawn",
     'operator': "operator"
 }
team_side = ["Attacking", "Defending"]
choose_side = (random.choice(team_side))


def map_theme():
   att_spawn = ["main entrance", "teacups", "bumper cars"]
   def_spawn = ["2nd floor office", "2nd floor daycare", "1st floor execution", "1st floor drug lab"]
   att_def = choose_side
   if att_def[0] == "A":
       print(att_spawn)
       print("--------------------------------------------------------------------------------------")
       spawned = input("Choose a spawn from the list above. ")
       user_profile['spawn'] = spawned
       team()
   elif att_def[0] == "D":
       print(def_spawn)
       print("--------------------------------------------------------------------------------------")
       spawned = input("Choose a spawn from the list above. ")
       user_profile['spawn'] = spawned
       team()


def map_bank():
   team()


def map_sky():
   team()


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
 while True:
     user = input("Enter your username. ")
     rank = input("Now enter your rank elo. ")
     break

 user_profile['username'] = user
 user_profile['rank'] = rank
 searching()


def team():
   the_side = choose_side
   if the_side[0] == "A":
     print("Your team attacking.")
     choose_op()
   elif the_side[0] == "D":
     print("Your team defending.")
     choose_op()


def choose_op():
 operator = input("Choose what operator you would like to play? ")
 user_profile['operator'] = operator
 print("--------------------------------------------------------------------------------------")
 print(user_profile)
 score()


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


def score():
  your = team1
  other = team2
  chance = (random.choice(win_lost))
  if chance == "Your team won the round":
      your = your + 1
      print("You and your team won")
  else:
       chance == "The other team won the round"
       other = other + 1
       print("Other team won")
  print("--------------------------------------------------------------------------------------")
  again = input("Would you like to play another game? ")
  if again[0].lower == "y":
      print("Time for the next game.")
      start_siege()
  else:
      print("Okay! Hope you had a good time.")


