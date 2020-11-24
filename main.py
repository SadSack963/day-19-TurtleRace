from turtle import Turtle, Screen
from random import randint, choice

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtles = []
start_position = -230

# Screen setup
s = Screen()
s.colormode(255)
s.setup(width=500, height=400)

# Turtle setup
for i in range(0, len(colors)):
    turtles.append({"color": colors[i], "turtle": Turtle(shape="turtle"), "position": start_position})
    turtles[i]["turtle"].pu()
    turtles[i]["turtle"].speed(1)
    turtles[i]["turtle"].color(turtles[i]["color"])
    turtles[i]["turtle"].goto(turtles[i]["position"], (i * 50) - 150)

race_running = False
choices = f"{colors[0]}"
for i in range(1, len(colors)):
    choices += "/" + colors[i]
user_choice = s.textinput(title="Turtle Race", prompt=f"Which turtle do you think will win the race?\n{choices} : ").lower()
if user_choice:
    race_running = True

while race_running:
    for turtle in turtles:
        i = randint(0, 10)
        turtle["turtle"].fd(i)
        turtle["position"] += i
        if turtle["position"] >= 230:
            race_running = False
            print(f"The {turtle['color']} turtle won the race")
            if turtle["color"] == user_choice:
                print(f"You won!")
            else:
                print(f"You lost. You chose the {user_choice} turtle.")


# s.exitonclick()
