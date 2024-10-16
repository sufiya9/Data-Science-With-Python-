import pgzrun

WIDTH=1000
HEIGHT=800
box=Rect((50,160),(100,100))
box2=Rect((105,200),(100,100))

def draw():
    screen.fill("black")
    screen.draw.text('hola sufiya ',(50,50),color='white')
    screen.draw.text('this is my laptop💻 ',(50,80),color='green',fontsize=50)
    screen.draw.text('this is a game programming',(50,120),color='blue',fontsize=50)
    screen.draw.rect(box,color="yellow")
    screen.draw.filled_rect(box2,color="red")

def update():
    box.x +=1
    box2.y +=2

pgzrun.go()