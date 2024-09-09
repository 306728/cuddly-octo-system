import turtle
import random

colours = ["AliceBlue", "AntiqueWhite", "aquamarine", "azure3", "bisque", "black", "BlanchedAlmond", "blue", "blue4", "brown", "brown3", "burlywood2", "CadetBlue", "chartreuse4", "chocolate2", "coral2", "CornflowerBlue", "cornsilk2", "cyan", "DarkBlue", "DarkGoldenrod", "firebrick", "green", "HotPink", "khaki", "MediumBlue", "navy", "purple", "tan", "yellow"]

def draw_square(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Pretty patterns")

turt = turtle.Turtle()

turt.speed(0)

for i in range(random.randint(40, 70):
    turt.pensize(random.randint(5, 10))
    turt.color(random.choice(colours))
    draw_square(turt, i * random.randint(3, 10))
    turt.right(i)
