
# import another_module

# print(another_module.another_var)

# import turtle 

# timmy = turtle.Turtle() #To make syntax more like the powerpoints you can import like this

from turtle import Turtle, Screen

timmy = Turtle() 
# print(timmy)

timmy.shape("turtle") #Another object function for the turtle class

timmy.color("green")

turtle.forward(100)

my_screen = Screen()

print(my_screen.canvheight) #object attribute

my_screen.exitonclick() #object method