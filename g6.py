from multiprocessing.resource_sharer import stop
import pgzrun
from random import randint

WIDTH = 700
HEIGHT = 500

#actor
p = Actor('char1',(50,200))
c= Actor('char2',(randint(0,WIDTH),randint(0,HEIGHT)))
e= Actor('enemy1',(500,300))
#VARIABLES
speed=3
espeed=1
score = 0 #global variable 

def draw():
    screen.fill('black')
    p.draw()
    screen.draw.text(f'score: {score}',(600,460), color='white', fontsize=25)
    c.draw()
    e.draw()
    
def update():
    player_controls()
    update_score()
    enemy_movement()
    
def player_controls():
    if keyboard.UP and not p.top<0:
        p.y += -10
        p.angle=0
    elif keyboard.DOWN and not p.bottom>HEIGHT:
        p.y += 10
        p.angle=0
    elif keyboard.RIGHT and not p.right>WIDTH:
        p.x += 10
        p.angle=-10
    elif keyboard.LEFT and not p.left<0:
        p.x += -10
        p.angle=10
        
def enemy_movement():
    if p.x > e.x:
        e.x += espeed
    if p.y > e.y:
        e.y += espeed
    if p.x < e.x:
        e.x -= espeed
    if p.y < e.y:
        e.y -= espeed
    if p.colliderect(e):
        p.image = 'splat'
        
        
def update_score():
    global score
    
    if p.colliderect(c):
        score +=10
        c.pos=(randint(0,WIDTH),randint(0,HEIGHT))
        sounds.s1.play()
    

pgzrun.go()