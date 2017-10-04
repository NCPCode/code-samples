# text adventure game for NCP Code
# this is a more advanced version than last week's game
# it uses loops to make it easier to code, and to let the player do more

# this version lets you recover from typos (so if you accidentally type 'yws' instead of 'yes' you get to retry from where you were)
# it's also a little shorter

location = "forest" # the location variable will store where the user is 
                    # we will use this variable to figure out what to display

still_playing = True # this will store whether or not the user is still playing our game
response = ""

while still_playing:
  if location == "forest":
    print("You are in a forest with plentiful trees. To your left, you see a cave. To your right, you see a sign post.")
    response = input("Do you go left or right?")
    if response == "left":
      location = "bats1"
    elif response == "right":
      location = "sign"
  elif location == "bats1":
    print("Inside the cave, you find a group of sleeping bats.")
    response = input("Do you wake the bats? (answer yes or no)")
    if response == "yes":
      location = "bats3"
    elif response == "no":
      location = "bats2"
  elif location == "bats2":
    print("You are now the bat leader.")
  elif location == "sign":
    print("A bat is resting on the sign post.")
    response = input("Do you wake the bat?")
    if response == "yes":
      location = "bats3"
    elif response == "no":
      location = "bats2"
  elif location == "bats3":
    print("You have been killed by bats.")
    still_playing = False
