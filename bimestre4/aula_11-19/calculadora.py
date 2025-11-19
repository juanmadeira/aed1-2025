import graphics as gf

win = gf.GraphWin("Calculadora", 513, 647)
calc_img = gf.Image(gf.Point(256, 323), "./calculadora.png")
calc_img.draw(win)

buttons = {
    "0": [(27,528),(130,626)],
    "1": [(269,405),(370,504)],
    "2": [(147,405),(249,504)],
    "3": [(27,405),(130,504)],
    "4": [(27,287),(130,388)],
    "5": [(147,287),(249,388)],
    "6": [(269,287),(370,368)],
    "7": [(27,163),(130,268)],
    "8": [(147,163),(249,268)],
    "9": [(269,163),(370,268)],
    "+": [(388,528),(492,626)],
    "-": [(388,405),(493,504)],
    "*": [(388,287),(493,388)],
    "/": [(388,163),(493,268)],
    ".": [(147,528),(249,626)],
    "=": [(263,528),(370,626)],
}

def get_key(click):
    x = click.getX()
    y = click.getY()

    for key, value in buttons.items():
        start = value[0]
        end = value[1]
        if x >= start[0] and y >= start[1] and x <= end[0] and y <= end[1]:
            return key

while True:
    click = win.getMouse()
    key = get_key(click)
    print(key)