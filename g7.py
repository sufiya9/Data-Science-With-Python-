import pgzrun
from random import randint

WIDTH=800
HEIGHT=500
espeed=1

p=Actor('char1',pos=(WIDTH//2, HEIGHT//2))
e= Actor('enemy1', pos=(70,70))
c=Actor('char2')
c.x=randint(100,WIDTH-100)
c.y=randint(100,HEIGHT-100)

is_game_over= False
is_game_started= False
score=0
spd=3
spd_e=1

def draw():
    if not is_game_started and not is_game_over:   #false
        show_intro_screen()
        
    elif is_game_started and not is_game_over:
        show_game_screen()
        
      
    elif is_game_over:
        show_gameover_screen()
        
def show_intro_screen():
    screen.fill('black')
    screen.draw.text('MY GAME',center=(WIDTH//2, HEIGHT//2), color='yellow', fontsize=100 )
    screen.draw.text('press space to start',center=(WIDTH//2, HEIGHT//2+50), color='red')
        
        
def show_game_screen():
    screen.fill('black')
    screen.draw.text(f'score {score}', (20,20))
    p.draw()
    e.draw()
    c.draw()
    
def show_gameover_screen():
    screen.fill('black')
    screen.draw.text('game over',center=(WIDTH//2, HEIGHT//2), color='red', fontsize=100 )
    screen.draw.text(f'score {score}', (20,20))
    
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
    global is_game_over
    if p.x > e.x:
        e.x += espeed
    if p.y > e.y:
        e.y += espeed
    if p.x < e.x:
        e.x -= espeed
    if p.y < e.y:
        e.y -= espeed
    if p.colliderect(e):
        p.images = 'splat'
        is_game_over=True
        
        
        
def update_score():
    global score
    
    if p.colliderect(c):
        score +=10
        c.pos=(randint(0,WIDTH),randint(0,HEIGHT))
        sounds.s1.play()
    
        
def update():
    global is_game_started
    if keyboard.SPACE and not is_game_started:
        is_game_started=True
    if is_game_started and not is_game_over:
        enemy_movement()
        player_controls()
        update_score()

pgzrun.go()