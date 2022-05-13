from asyncio.windows_events import NULL
from random import *
from re import T
from turtle import *
from freegames import path


car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None, 'taps':0}
hide = [True] * 64
writer = Turtle(visible=False)

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']
    state['taps'] +=1

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    if True in hide:
        for count in range(64):
            if hide[count]:
                x, y = xy(count)
                square(x, y)

        mark = state['mark']

        if mark is not None and hide[mark]:
            x, y = xy(mark)
            up()
            goto(x + 25, y)
            color('black')
            write(tiles[mark], font=('Arial', 30, 'normal'), align="center")

            
        update()
        up()
        writer.clear()
        writer.goto(0, 210)
        writer.color('blue')
        writer.write("Taps " + str(state['taps']), align="center")
        ontimer(draw, 100)
    else:
        clear()
        up()
        goto(0,0)
        
        color("white")
        write("GANASTE!!", font=("Comic Sans",50, "normal",) ,align="center")
        input("Enter..")
        quit()


shuffle(tiles)
setup(500, 500, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()