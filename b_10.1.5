import pyxel
import math

pyxel.init(200, 200)

class Ball:
    def __init__(self):
        self.x = pyxel.rndi(4, 196)
        self.y = 0
        self.dir = pyxel.rndi(30, 150)
        self.score = 0
        self.over = False

    def update(self):
        if self.over == False:
            self.pad_x = pyxel.mouse_x - 20
            if self.y >= 200:
                self.over = True
            else:
                self.x += 3 * math.cos(math.radians(self.dir))
                self.y += 3 * math.sin(math.radians(self.dir))
                if self.x <= 4 or self.x >= 196:
                    self.dir = 180 - self.dir
                if self.y >= 195 and self.x >= self.pad_x and self.x <= self.pad_x + 40:
                    self.score += 1
                    self.x = pyxel.rndi(4, 196)
                    self.y = 0
                    self.dir = pyxel.rndi(30, 150)

                    pyxel.play(0, 0)

                if self.y >= 200:
                    self.x = pyxel.rndi(4, 196)
                    self.y = 0
                    self.dir = pyxel.rndi(30, 150)

                    pyxel.play(0, 1)

    def draw(self):
        pyxel.circ(self.x, self.y, 4, 0)

class ThreeBall:
    def __init__(self):
        self.balls = [Ball() for i in range(3)]
        pyxel.run(self.update, self.draw)

    def update(self):
        for ball in self.balls:
            ball.update()

    def draw(self):
        pyxel.cls(7)
        pyxel.rect(pyxel.mouse_x - 20, 199, 40, 1, 6)
        for ball in self.balls:
            ball.draw()
        pyxel.text(10, 10, "Score: {}".format(sum([ball.score for ball in self.balls])), 3)

def esound():
    pyxel.sound(0).set("c3e3g3c4c4", "s", "7", ("n" * 4), 7)
    pyxel.sound(1).set("f4b3f2b1f1", "p", ("7" * 7 + "6543"), ("n" * 4), 9,)

esound()
ThreeBall()
