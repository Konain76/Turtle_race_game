from turtle import Screen
from snake import Turt
m_t = Turt()
screen = Screen()
is_race_on = False

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="choosing bet", prompt="which turtle will win select one")


if user_bet:
    is_race_on = True

while m_t.is_race_on:

    m_t.race(user_bet)


screen.exitonclick()


























