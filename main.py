
# # import another_module

# # print(another_module.another_var)

# # import turtle 

# # timmy = turtle.Turtle() #To make syntax more like the powerpoints you can import like this

# from turtle import Turtle, Screen

# timmy = Turtle() 
# # print(timmy)

# timmy.shape("turtle") #Another object function for the turtle class

# timmy.color("green")

# timmy.forward(100)

# my_screen = Screen()

# print(my_screen.canvheight) #object attribute

# my_screen.exitonclick() #object method

from prettytable import PrettyTable, MARKDOWN #MARKDOWN is style in the prettytable class. So importing this 

table1 = PrettyTable()
print(table1)

table1.field_names = ["First name", "Last name", "SSN"]

table1.add_row(["Kazim", "Shabbir", 334])
print(table1)


table = PrettyTable()
table.add_column("City Name", ["Houston", "Chicago", "Seattle", "Boston", "NYC"])
print(table)

table.add_column("Population", ["12000", "13000", "1472", "78634", "66666"])

print(table)

#setting table style
table.set_style(MARKDOWN)