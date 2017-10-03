from turtle import *

# set up the player turtle
player = Turtle()
player.penup()
player.setx(-100)
player.pendown()

player.left(90)

projectiles = []

counter = 0

# this is the "game loop"
# it will continuously run, doing things every time
# most applications have this type of infinite loop
# we'll talk more about on day 4 with pygame
while True:
  player.forward(1)
  # make sure the player is in bounds
  if player.ycor() < 0:
    player.sety(0)
    player.clear()
  
  for x in projectiles:
    x.forward(10)
    x.clear()
    
    # stop moving turtles that leave the screen
    if x.xcor() > 300:
      x.hideturtle()
      projectiles.remove(x)
  
  # the % operator is called modulus, and it gives the remainder of a division
  # you can think of this as meaning 'every 50th iteration of the loop'
  if counter % 50 == 0:
    # make a new projectile
    
    projectile = Turtle()
    
    # position the projectile
    projectile.speed(0) # makes it super fast
    
    projectile.penup()
    projectile.hideturtle()
    projectile.setpos(player.pos())
    
    # make the project behave normally again
    projectile.showturtle()
    projectile.pendown()
    
    projectile.pencolor("red")
    
    projectiles.append(projectile)
  
  counter += 1
