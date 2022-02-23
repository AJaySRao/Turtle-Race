from turtle import Turtle, Screen
import random

s = Screen()
user_bet = s.textinput("Make you bet", "Which turtle will win the race? Enter a color: ")
s.screensize(600, 500)
colors = ['red', 'blue', 'orange', 'pink', 'green', 'purple', 'yellow']
y = [-150, -100, -50, 0, 50, 100, 150]
players = []

for i in range(7):
    t = Turtle()
    t.shape('turtle')
    t.penup()
    t.color(colors[i])
    t.goto(-270, y[i])
    players.append(t)

game_is_on = True
while game_is_on:
    for player in players:
        player.forward(random.randint(10, 50))

        if player.xcor() >= 270:
            if player == user_bet:
                print(f"{player.pencolor()} won the race. You won!")
            else:
                print(f"{player.pencolor()} won the race. You've lost!")
            game_is_on = False

s.exitonclick()
