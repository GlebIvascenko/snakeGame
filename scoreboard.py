from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 250)
        self.color('white')
        self.speed("fastest")
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score}  High Score: {self.high_score}', move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")

        self.score = 0
        self.update_score()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f'GAME OVER', move=False, align=ALIGNMENT, font=FONT)

    def add_points(self):
        self.score += 10
        self.update_score()
