import pyxel
from random import randint

class Game:
    def __init__(self):
        self.TITLE = "snake"
        self.WIDTH = 200 #200
        self.HEIGHT = 160 #160
        self.CASE = 20
        self.direction = [1, 0]
        self.FRAME_REFRESH = 6
        self.food = [8, 3]
        self.snake = [[3, 3], [2, 3], [1, 3]]
        self.score = 0

        pyxel.init(self.WIDTH, self.HEIGHT, title=self.TITLE)
        pyxel.run(self.update, self.draw)

    def draw(self):
        pyxel.cls(0)

        pyxel.text(1, 1, f"Score: {self.score}", 8)
                    
        for anneau in self.snake[1:]:
            x, y = anneau
            pyxel.rect(x * self.CASE, y * self.CASE, self.CASE, self.CASE, 11)

        x_head, y_head = self.snake[0]
        pyxel.rect(x_head * self.CASE, y_head * self.CASE, self.CASE, self.CASE, 9)

        x_food, y_food = self.food
        pyxel.rect(x_food * self.CASE, y_food * self.CASE, self.CASE, self.CASE, 8)

    def update(self):
        if pyxel.frame_count % self.FRAME_REFRESH == 0:
            head = [self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1]]
            self.snake.insert(0, head)

            if head == self.food:
                while self.food in self.snake:
                    self.food = [
                        randint(0, int(self.WIDTH / self.CASE) - 1),
                        randint(0, int(self.HEIGHT / self.CASE) - 1)
                    ]
                self.score += 1
            else:
                self.snake.pop(-1)

        if pyxel.btn(pyxel.KEY_ESCAPE):
            exit()
        elif pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D) and self.direction in ([0, 1], [0, -1]):
            self.direction = [1, 0]
        elif pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q) and self.direction in ([0, 1], [0, -1]):
            self.direction = [-1, 0]
        elif pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_Z) and self.direction in ([1, 0], [-1, 0]):
            self.direction = [0, -1]
        elif pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S) and self.direction in ([1, 0], [-1, 0]):
            self.direction = [0, 1]

        head = self.snake[0]
        if (
            head in self.snake[1:]
            or head[0] < 0
            or head[0] > self.WIDTH / self.CASE - 1
            or head[1] < 0
            or head[1] > self.HEIGHT / self.CASE - 1
        ):
            exit()


Game()
