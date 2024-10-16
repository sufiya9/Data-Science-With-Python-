import pgzrun

WIDTH = 700
HEIGHT = 500

#actor
p = Actor('char1',(50,200))

def draw():
    screen.fill('white')
    p.draw()
    
def update():
    player_controls()
    
def player_controls():
    if keyboard.UP and not p.top<0:
        p.y += -2
        p.angle=-10
    elif keyboard.DOWN and not p.bottom>HEIGHT:
        p.y += 2
        p.angle=10
    elif keyboard.RIGHT and not p.right>WIDTH:
        p.x += 2
        p.angle=10
    elif keyboard.LEFT and not p.left<0:
        p.x += -2
        p.angle=-10

pgzrun.go()
    