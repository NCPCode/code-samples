# text adventure game for NCP code
# this isn't much now, but soon you will be able to make more advanced games

# it might seem like a lot of code, but it's made up of simple pieces
# next week, we can learn to simplify this a bit

print("You are in a forest with plentiful trees. To your left, you see a cave. To your right, you see a sign post.")
response = input("Do you go left or right? ")

if response == "left":
  print("Inside the cave, you find a group of sleeping bats.")
  response = input("Do you wake the bats? (answer yes or no) ")

  if response == "yes":
    print("The bats fight back. You are no longer alive.")
    print("GAME OVER")

  elif response == "no":
    print("The bats respect you.")
    response = input("Do you become a bat? (answer yes or no) ")

    if response == "yes":
      print("You win!")

    elif response == "no":
      print("The bats eat you. You are no longer alive.")
      print("GAME OVER")

    else:
      print("Please enter a valid response next time!")

  else:
    print("Please enter a valid response next time!")


elif response == "right":
  print("A bat is resting on the sign post.")
  response = input("Do you shake the sign post? (answer yes or no) ")

  if response == "yes":
    print("The sign breaks off and crushes you.")
    print("GAME OVER")

  elif response == "no":
    print("The bat wakes up and starts flying, lifting the sign post with it.")
    response = input("Do you grab on to the sign post? (answer yes or no) ")

    if response == "yes":
      print("You are lifted off of the ground. As you fly, the world collapses on beneath you.")
      print("You win!")

    elif response == "no":
      print("A hole opens up beneath you and you fall down.")
      print("GAME OVER")

    else:
      print("Please enter a valid response next time!")

  else:
    print("Please enter a valid response next time!")


else:
  print("Please enter a valid response next time!")

