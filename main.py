from turtle import Turtle, Screen
from random import choice

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtles = []
start_position = -230

# Screen setup
s = Screen()
s.colormode(255)
s.setup(width=500, height=400)

# Turtle setup
for i in range(0, len(colors)):
    turtles.append({"turtle": Turtle(shape="turtle"), "position": start_position})
    turtles[i]["turtle"].pu()
    turtles[i]["turtle"].color(colors[i])
    turtles[i]["turtle"].goto(turtles[i]["position"], (i * 50) - 150)

choice = s.textinput(title="Turtle Race", prompt="Which turtle do you think will win the race? : ").lower()



s.exitonclick()
