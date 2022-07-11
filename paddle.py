import turtle
import math
import random
import time
WIDTH = 800
HEIGHT = 600
MARGIN = 30
def set_random_color(bloke):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle.colormode(255)
    bloke.color(r, g, b)
def screen():
    background = turtle.Screen()
    background.title("Paddle Game")
    background.bgcolor('black')
    background.setup(WIDTH,HEIGHT)
    return background
def ball():
    ball = turtle.Turtle()
    ball.clear()
    ball.speed(0)
    ball.shape("circle")
    ball.shapesize(0.75)
    ball.color('white')
    ball.penup()
    ball.hideturtle()
    ball.setpos(0,-260)
    ball.showturtle()
    return ball
def block_paeeini():
    paein = turtle.Turtle()
    paein.clear()
    paein.speed(0)
    paein.shape("square")
    set_random_color(paein)
    paein.shapesize(.35,4.8)
    paein.penup()
    paein.hideturtle()
    paein.goto(0,-275)
    paein.showturtle()
    paein.direction = "stop"
    return paein
def block():
    blockk = []
    for i in range (95):
        bloke = turtle.Turtle()
        bloke.speed(0)
        bloke.shape("square")
        bloke.shapesize(1,1.45)
        bloke.penup()
        bloke.hideturtle()
        blockk.append(bloke)
    return blockk
def block_chin(blk):
    blk_chin = turtle.Turtle()
    i = 0
    while i < len(blk):
        for x in range((-WIDTH//2)+MARGIN,(WIDTH//2)-MARGIN,40):
            for y in range ((HEIGHT//2)-200,HEIGHT//2,40): 
                set_random_color(blk[i])
                blk[i].hideturtle()
                blk[i].speed(0)
                blk[i].setpos(x,y) 
                blk[i].showturtle()
                i += 1
def ball_to_block(blk,bal):
    i = 0
    while i < len(blk):
        xba,yba = bal.position()
        xbl,ybl = blk[i].position()
        if abs(xbl-xba) < 33 and abs(ybl-yba) < 25:
            blk[i].setpos(10000,10000)
            return True
        i += 1
    return False
def key_listen(kilid):
    kilid.listen()
    kilid.onkey(go_left,"Left")
    kilid.onkey(go_right,"Right")
def go_left():
    x,y = zire_toop.position()
    zire_toop.setpos((x-60),y)
def go_right():
    x,y = zire_toop.position()
    zire_toop.setpos((x+60),y)
def ziretoop_ball(bal,zire_toop):
    xb,yb = bal.position()
    xz,yz = zire_toop.position()
    return abs(xb-xz) < 60 and abs(yb-yz) < 25
def Throw(harekat,teta):
    harekat.clear()
    x0,y0 = bal.position()
    v0 =35
    vx = v0*(math.cos(teta*math.pi/180))
    vy = v0*(math.sin(teta*math.pi/180))
    x = vx 
    y = vy
    x0 += x
    y0 += y
    harekat.penup()
    harekat.setpos(x0,y0)
    harekat.pendown()
def write_score():
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(-380,-200)
    pen.write("Score : " + "0" , align="left" , font=("Arial",20,"normal"))
    pen.penup()
    pen.hideturtle()
    pen.goto(190,-200)
    pen.write("High Score : " + "0", align="left" , font=("Arial",20,"normal"))
    return pen
def update_score():
    score_num.clear()
    score_num.goto(-380,-200)
    score_num.write("Score : " + str(score) , align="left" , font=("Arial",20,"normal"))
    score_num.goto(190,-200)
    score_num.write("High Score : " + str(high_score), align="left" , font=("Arial",20,"normal"))
sc = screen()
zire_toop = block_paeeini()
bal = ball()
blk = block()
score_num = write_score()
block_chin(blk)
key_listen(sc)
teta = random.randint(20,160)
score = 0
high_score = 0
turtle.colormode(255)
while True:
    x,y = bal.position()
    if x > (WIDTH//2)-MARGIN or x < (-WIDTH//2)+MARGIN :
        teta = 180 - teta
    elif  y > (HEIGHT//2)-MARGIN:
        teta = - teta
    elif y<(-HEIGHT//2)-10:
        bal.clear()
        bal.penup()
        bal.setpos(0,-260)
        teta = random.randint(20,160)
        if score > high_score:
            high_score = score
        score = 0
        update_score()
    Throw(bal,teta)
    if ball_to_block(blk,bal) :
        for i in range(len(blk)):
            xbl,ybl = blk[i].position()
            xba,yba = bal.position()
            if abs(xbl-xba) < 33 :
                teta = 180 - teta
            if abs(ybl-yba) < 25:
                teta = - teta
        score = score + 5
        update_score()
    if ziretoop_ball(bal,zire_toop):
        xb,yb = bal.position()
        xz,yz = zire_toop.position()
        if abs(xb-xz) < 60 and abs(yb-yz) < 25:
            teta = -teta
    sc.update()
