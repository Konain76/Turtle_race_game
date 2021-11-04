from turtle import Turtle
import random
y_pos = [-180, -120, -60, 0, 60, 120, 180]

colors = ["red", "orange", "yellow", "green", "purple", "violet", "blue"]

class Turt:

    def __init__(self):
        self.all_turtles = []
        self.create_turtles()
        self.is_race_on = True

    def create_turtles(self):
        for i in range(7):
            new_turtle = Turtle()
            new_turtle.shape("turtle")
            new_turtle.color(colors[i])
            new_turtle.penup()
            new_turtle.goto(x=-230, y=y_pos[i])
            self.all_turtles.append(new_turtle)

    def race(self, user_choice):
        for turtle in self.all_turtles:
            if turtle.xcor() > 230:
                winning_turtle = turtle.pencolor()
                self.is_race_on = False
                if user_choice == winning_turtle:
                    print(f"you won {winning_turtle} turtle is the winner")
                else:
                    print(f"you lose {winning_turtle} turtle is the winner")
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)