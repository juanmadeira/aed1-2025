import graphics as gf

def getAxis():
    center_x = dot.getCenter().getX()
    center_y = dot.getCenter().getY()
    return center_x, center_y

def moveDot(dx, dy):
    if (((center_x + vel*dx - radius) <= 0) or
        ((center_y + vel*dy - radius) <= 0) or
        ((center_x + vel*dx + radius) >= 600) or
        ((center_y + vel*dy + radius) >= 400)):
        return False
    else:
        return dot.move(vel*dx, vel*dy)

def createLine(window, Ax, Ay, Bx, By):
    limits = [Ax, Ay, Bx, By]
    # obstacles.append(limits)

    A = gf.Point(Ax, Ay)
    B = gf.Point(Bx, By)
    line = gf.Line(A, B)
    return line.draw(window)

win = gf.GraphWin("Window", 600, 400)
obstacles = [0, 0, 600, 0], [600, 0, 600, 400], [600, 400, 0, 400], [0, 400, 0, 0]

center = gf.Point(50, 50)
color = gf.color_rgb(0, 0, 0)
radius = 20
dot = gf.Circle(center, radius)
dot.setFill(color)
dot.draw(win)

dx = 5
dy = 5

vel = 1
min_vel= 0
max_vel = 25

key_left = "LEFT"
key_down = "DOWN"
key_up = "UP"
key_right = "RIGHT"
key_slow = "F"
key_fast = "A"
 
createLine(win, 300, 50, 300, 250)

i = 0
while True:
    key = win.checkKey()
    key = key.upper()
    center_x, center_y = getAxis()
    if key != "":
        print(i, key, f"{center_x, center_y}")
        print(f"vel.: {vel}")
        print(f"obstacles: {obstacles}\n")
    if key == "ESCAPE":
        break

    # movimentação
    elif key == key_left:
        moveDot(-dx, 0)
    elif key == key_down:
        moveDot(0, dy)
    elif key == key_up:
        moveDot(0, -dy)
    elif key == key_right:
        moveDot(dx, 0)
    
    # velocidade
    elif key == key_fast:
        vel += 1
        if vel > max_vel:
            vel = max_vel
    elif key == key_slow:
        vel -= 1
        if vel < min_vel:
            vel = min_vel

    i += 1