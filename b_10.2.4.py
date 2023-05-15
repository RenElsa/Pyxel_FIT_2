import pyxel
import math

pyxel.init(200, 200)

class Ball:
    def __init__(ball):
        esound()
        ball.x = pyxel.rndi(4, 196)
        ball.y = 0
        ball.dir = pyxel.rndi(30, 150)
        ball.score = 0
        ball.missed = 0
        ball.over = False
        pyxel.run(ball.update, ball.draw)

    def update(ball):
        if ball.over == False:
            ball.pad_x = pyxel.mouse_x - 20
            if ball.y >= 200:
                ball.missed += 1
                if ball.missed >= 10:
                    ball.over = True
                else:
                    ball.x = pyxel.rndi(4, 196)
                    ball.y = 0
                    ball.dir = pyxel.rndi(30, 150)
            else:
                ball.x += 5 * math.cos(math.radians(ball.dir))
                ball.y += 5 * math.sin(math.radians(ball.dir))
                if ball.x <= 4 or ball.x >= 196:
                    ball.dir = 180 - ball.dir
                if ball.y >= 195 and ball.x >= ball.pad_x and ball.x <= ball.pad_x + 40:
                    ball.score += 1
                    ball.x = pyxel.rndi(4, 196)
                    ball.y = 0
                    ball.dir = pyxel.rndi(30, 150)

                    pyxel.play(0, 0)

                if ball.y >= 200:
                    ball.missed += 1
                    if ball.missed >= 10:
                        ball.over = True
                    else:
                        ball.x = pyxel.rndi(4, 196)
                        ball.y = 0
                        ball.dir = pyxel.rndi(30, 150)

                    pyxel.play(0, 1)

    def draw(ball):
        pyxel.cls(7)
        pyxel.rect(ball.pad_x, 199, 40, 1, 6)
        pyxel.circ(ball.x, ball.y, 4, 0)
        pyxel.text(10, 10, "Score: {}".format(ball.score), 3)
        pyxel.text(10, 20, "Missed: {}".format(ball.missed), 3)
        if ball.over:
            pyxel.text(80, 100, "Game Over", 8)

def esound():
    pyxel.sound(0).set("c3e3g3c4c4", "s", "7", ("n" * 4), 7)
    pyxel.sound(1).set("f4b3f2b1f1", "p", ("7" * 7 + "6543"), ("n" * 4), 9,)

Ball()