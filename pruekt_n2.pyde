
z =1
x =1
c =1
def setup():
    size(1000,1000)
    background(255)
def draw():
    global z,x,c
    push()
    clear()

    line(500,0,500,500)
    line(500,1000,500,500)
    line(40000,0,500,500)
    pop()
    push()
    if keyPressed:
        if key == ENTER:
            fill(0)

    else:
        fill(255)

    text(u"Привет",10,50)
    pop()

    z +=1
    x -=1
    c +=1
