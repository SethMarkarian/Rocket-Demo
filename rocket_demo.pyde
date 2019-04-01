import random

def setup():
    global xstars, ystars, stars, xRocket, yRocket, angleRocket, rocketscale
    size(600,600)
    background(0)
    stars = []
    for i in range(100):
        stars.append((random.randrange(width), random.randrange(height)))
    xstars = 0
    ystars = 0
    xRocket = width/2
    yRocket = height/2
    angleRocket = 0
    rocketscale = 1


def draw():
    global xstars, ystars, stars, xRocket, yRocket, angleRocket, rocketscale
    background(0)
    pushMatrix()
    translate(xstars, ystars)
    for i in range(len(stars)):
        fill(255)
        if stars[i][0] + xstars > width:
            stars[i] = (stars[i][0] - width, stars[i][1])
        if stars[i][1] + ystars > height:
            stars[i] = (stars[i][0], stars[i][1] - height)
        ellipse(stars[i][0], stars[i][1], 5, 5)
    popMatrix()
    xstars += 1
    ystars += 1
    
    #rocket
    pushMatrix()
    translate(xRocket, yRocket)
    pushMatrix()
    scale(rocketscale)
    rotate(angleRocket)
    drawRocket()
    popMatrix()
    popMatrix()

    
    if keyPressed and key == CODED and keyCode == UP:
        yRocket -= 3 * cos(angleRocket)
        xRocket += 3 * sin(angleRocket)
    if keyPressed and key == CODED and keyCode == LEFT:
        angleRocket -= .05
    if keyPressed and key == CODED and keyCode == RIGHT:
        angleRocket += .05
    if keyPressed and key == CODED and keyCode == DOWN:
        yRocket += 3 * cos(angleRocket)
        xRocket -= 3 * sin(angleRocket)
    if keyPressed and key == "n":
        rocketscale /= 1.05
    if keyPressed and key == "m":
        rocketscale *= 1.05

    
def drawRocket():
    rectMode(CENTER)
    noStroke()
    fill(255, 0,0)
    rect(0, 0, 20, 50)
    fill(0, 0, 255)
    triangle(-10, -25, 10, -25, 0, -40)