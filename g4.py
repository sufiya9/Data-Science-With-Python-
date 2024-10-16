import pgzrun

WIDTH = 700
HEIGHT = 500

#actor
p = Actor('char1',(450,200))
l = Actor('enemy',(50,200))

#PRE EXIST FUNTION
def draw():
    screen.fill('white')
    p.draw() 
    l.draw()
    
 #PRE EXIST FUNTION   
def update():
    player1_controls()
    player2_controls()
    
def player1_controls():
    if keyboard.W and not p.top<0:
        p.y += -2
        p.angle=-10
    elif keyboard.S and not p.bottom>HEIGHT:
        p.y += 2
        p.angle=+10
    elif keyboard.D and not p.right>WIDTH:
        p.x += 2
        p.angle=10
    elif keyboard.A and not p.left<0:
        p.x += -2
        p.angle=-10
        
def player2_controls():
    if keyboard.UP and not l.top<0:
        l.y += -2
        l.angle=-10
    elif keyboard.DOWN and not l.bottom>HEIGHT:
        l.y += 2
        l.angle=10
    elif keyboard.RIGHT and not l.right>WIDTH:
        l.x += 2
        l.angle=10
    elif keyboard.LEFT and not l.left<0:
        l.x += -2
        l.angle=-10

pgzrun.go()