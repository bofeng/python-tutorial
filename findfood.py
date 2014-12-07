from turtle import Turtle
from random import randint
 
# Step 1, of course, get your turtle!
nick = Turtle()
 
# Step 2, generate a random coordinate for food
# randint(-200, 200): give me a random integer between -200 and 200
food_pos_x = randint(-200, 200)
food_pos_y = randint(-200, 200)
print "\t\tThe food's position is:", food_pos_x, food_pos_y
 
# Step 3, ask user: Go forward or backward, and how far?
direction = raw_input("Go forward or backward?")
distance = raw_input("how far?")
distance = int(distance)
 
# Step 4, move your turtle according to user's answer
if direction == "forward":
    # Your code here
else:
    # Your code here

# Step 5, ask user: turn right or left?    
turn = raw_input("Turn right or left?")
 
# Step 6, make a turn according to user's answer:
# If turn equals "right", then turn right for 90 degrees;
# Otherwise, turn left for 90 degrees.
# Your code here
 
# Step 7, after turtle made a turn,
# move forward according to user's answer
distance2 = raw_input("how far?")
distance2 = int(distance2)
nick.forward(distance2)
 
# Step 8, we are done with all movings, 
# now get turtle's current position, and print it out
turtle_pos_x, turtle_pos_y = nick.position()
turtle_pos_x = int(turtle_pos_x)
turtle_pos_y = int(turtle_pos_y)
print "Turtle's position is:", turtle_pos_x, turtle_pos_y
 
# Step 9, check if turtle found the food:
# Check if turtle x coordinate equals to food x coordinate
# And turtle y corrdinate equals to food y coordinate
# If both are equal, means turtle got the food, and you WIN !!
if (Your code here) and (Your code here):
    print "You find the food! You win!"
else:
    print "You lose :("
