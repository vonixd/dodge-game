import pygame
import math
import random

pygame.init()
width = 1920
height = 1040
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('lol dodge')
font = pygame.font.SysFont('comicsans', 40)
black = (0,0,0)
bg = (50,50,50)
white = (255,255,255)
yellow = (240,240,10)
red = (255,0,20)
green = (10,245,20)
orange = (240,140,10)
clock = pygame.time.Clock()
FPS = 120
class Button(object):
    def __init__(self, x, y, text,  color1, color = black):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.color1 = color1
        self.textt = font.render(self.text, True, self.color)
        self.text_r = self.textt.get_rect()
        self.text_r.x = self.x
        self.text_r.y = self.y
    def draw(self, win):
        pygame.draw.rect(win, self.color1, self.text_r)

        win.blit(self.textt, (self.x, self.y))


bt = Button(width/2-100, height/2-100, 'PLAY', yellow)
bt_q = Button(width/2-110, height/2 + 100, 'QUIT', yellow)
bt_c = Button(width/2-160, height/2, 'CONTROLS', yellow)












def main():
    global FPS, bg, cut
    class Entity(object):
        def __init__(self, x, y, radius, color = green, dx=0, dy=0):
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color
            self.dx = dx
            self.dy = dy
        def draw(self, win):
            pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
    class Move(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def draw(self, win):
            pygame.draw.circle(win, yellow, (self.x,self.y), 5)
        def get_pos(self):
            return self.x,self.y
    class Bullet(object):
        def __init__(self, x, y, radius, dx, dy, speed,  color = black):
            self.x = x
            self.y = y
            self.radius = radius
            self.dx = dx * speed
            self.dy = dy * speed
            self.color = color
        def draw(self, win):
            pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
    class Abilities(object):
        def __init__(self, x, y, text, color1, color2, color=black):
            self.x = x
            self.y = y
            self.text = text
            self.color = color
            self.color1 = color1
            self.textt = font.render(self.text, True, self.color)
            self.text_r = self.textt.get_rect()
            self.text_r.x = self.x
            self.text_r.y = self.y
            self.color2 = color2

        def draw(self, win, bar):
            pygame.draw.rect(win, self.color1, self.text_r)
            pygame.draw.rect(win, self.color2, (self.text_r.x,self.text_r.y,self.text_r.width, self.text_r.height-bar))
            win.blit(self.textt, (self.x, self.y))
    class Boss(object):
        def __init__(self, x, y,radius, color = red, health = 40):
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color
            self.health = health
            self.timer = 0



        def draw(self, win):
            pygame.draw.circle(win, self.color, (self.x, self.y), self.radius+15)
            pygame.draw.rect(win, self.color,(width/3,20,self.health*20, 10))
        def timer_add(self):
            self.timer += 1
        def moving(self, win):

            if self.timer >= 5*FPS and self.timer < 5.4*FPS:
                self.p_x, self.p_y = player.x, player.y
                pygame.draw.circle(win,yellow,(self.p_x, self.p_y), self.radius/4)
            elif self.timer >= 5.4*FPS and self.timer < 5.8*FPS:
                pygame.draw.circle(win,yellow,(self.p_x, self.p_y), self.radius/2)
            elif self.timer >= 5.8*FPS and self.timer < 6*FPS:
                pygame.draw.circle(win,yellow,(self.p_x, self.p_y), self.radius)
            if self.timer >= 6*FPS:
                self.x,self.y = self.p_x,self.p_y
                self.timer = 0
        def shooting(self,win):
            if self.timer < 5*FPS:

                distance = math.sqrt((player.x-self.x)**2+(player.y-self.y)**2)
                dx = (player.x-self.x) / distance
                dy = (player.y-self.y) / distance
                speed = 1.5
                boss_bullets.append(Bullet(self.x,self.y,60,dx,dy,speed,orange))
            for b_b in boss_bullets:
                b_b.x += b_b.dx
                b_b.y += b_b.dy
                if b_b.x > width or b_b.x < 0 or b_b.y > height or b_b.y < 0:
                    boss_bullets.remove(b_b)
                for b in bullets:
                    if b.x > b_b.x - b_b.radius and b.x < b_b.x + b_b.radius:
                        if b.y > b_b.y - b_b.radius and b.y < b_b.y + b_b.radius:
                            bullets.remove(b)

                b_b.draw(win)











    def escape():
        global play, cut

        esc = True
        bt_resume = Button(width/2-120, height/2 - 100, 'RESUME', yellow)
        bt_quit = Button(width/2-100, height/2 + 100, 'QUIT', yellow)
        while esc:
            pos = pygame.mouse.get_pos()
            win.fill(bg)
            key = pygame.key.get_pressed()
            for event in pygame.event.get():
                # game exit
                if event.type == pygame.QUIT:
                    esc = False
                if bt_resume.text_r.collidepoint(pos):
                    bt_resume.color1 = red
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            esc = False
                else:
                    bt_resume.color1 = yellow
                if bt_quit.text_r.collidepoint(pos):
                    bt_quit.color1 = red
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            cut = True
                            esc = False

                else:
                    bt_quit.color1 = yellow
                if key[pygame.K_ESCAPE]:
                    esc = False
            bt_resume.draw(win)
            bt_quit.draw(win)

            pygame.display.update()



    def create_respawn_point():
        for i in range(10):
            respawn_point_list.append(Entity(random.randint(0, width), 0,5))
        for i in range(10):
            respawn_point_list.append(Entity(random.randint(0, width), height - 10,5))
        for i in range(10):
            respawn_point_list.append(Entity(0, random.randint(0, height),5))
        for i in range(10):
            respawn_point_list.append(Entity(width - 10, random.randint(0, height),5))



    def redraw_window(win):
        player.draw(win)
        for move in movement_list:
            move.draw(win)
        for b in bullets:
            b.draw(win)
        for enemy in enemy_list:
            enemy.draw(win)
        text = font.render(f'score: {score}', True, white)
        win.blit(text, (width-len(f'score: {score}')*20-10,30))
        q_ab.draw(win,max_cd-cd)
        d_ab.draw(win,(max_t_cd-t_cd)/17)
        s_ab.draw(win,(max_s_cd - s_cd)/34)
    q_ab = Abilities(width / 2.6, height-100, 'Q',(80,140,140), (20,20,20), white)
    d_ab = Abilities(width / 1.6, height - 100, 'D', (80, 140, 140), (20, 20, 20), white)
    s_ab = Abilities(width / 2, height - 100, 'S', (80, 140, 140), (20, 20, 20), white)


    fireball_list = []
    boss = Boss(-2000, -2000, 180)
    boss_bullets = []
    fighted_boss = 0
    fighting = False
    cut = False
    slowmo = False
    max_s_cd = 15*FPS +1
    s_cd = 15 * FPS
    teleport = False
    max_t_cd = 8*FPS
    t_cd = 8*FPS
    score = 0
    timer = 0
    respawn_point_list = []
    enemy_list = []
    bullets = []
    shoot = False
    max_cd = 120
    cd = 110
    clicked = False
    move = False
    movement_list = []
    player = Entity(400,400, 20)
    play = True

    while play:
        clock.tick(FPS)
        if fighting:
            boss.timer_add()
        timer += 1
        if cd < 121:
            cd += 1
        if t_cd < 8*FPS +1:
            t_cd += 1
        else:
            t_cd = 8*FPS + 1
        if s_cd < 15*FPS + 1:
            s_cd += 1
        pos = pygame.mouse.get_pos()
        win.fill(bg)
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            #game exit
            if event.type == pygame.QUIT:
                play = False
            if key[pygame.K_ESCAPE]:
                escape()
                if cut:
                    play = False


            #checking mouse for clicking
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                move = True
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                move = False

            #using abilites
            if key[pygame.K_s] and s_cd > 15*FPS:
                if not fighting:
                    slowmo = True
                    s_cd = 0
                else:
                    teleport = True
                    s_cd = 0
            if key[pygame.K_q] and cd > FPS:
                cd = 0
                shoot = True
            elif cd > 0:
                shoot = False
            if key[pygame.K_d] and t_cd > 8*FPS:
                t_cd = 0
                teleport = True


        #movement
        if move:
            movement_list.clear()
            movement_list.append(Move(pos[0], pos[1]))
        if clicked:
            for mov in movement_list:
                if mov.x > player.x - player.radius and mov.x < player.x + player.radius:
                    if mov.y > player.y - player.radius and mov.y < player.y + player.radius:
                        movement_list.clear()

                try:
                    distance = math.sqrt((mov.x-player.x)**2+(mov.y-player.y)**2)
                    player.dx = (mov.x-player.x) / distance

                    player.dy = (mov.y-player.y) / distance

                    speed = 4

                    player.x += player.dx * speed
                    player.y += player.dy * speed
                except:
                    distance = math.sqrt((mov.x - player.x) ** 2 + (mov.y - player.y) ** 2)-2
                    player.dx = (mov.x - player.x) / distance

                    player.dy = (mov.y - player.y) / distance

                    speed = 4

                    player.x += player.dx * speed
                    player.y += player.dy * speed

        if teleport:
            player.x,player.y = pos
            teleport = False
        if slowmo:
            bg = (70,50,70)
            FPS = 12
            slowmo = False
        if slowmo == False and s_cd >= 4*FPS:
            bg = (50,50,50)
            FPS = 120
        #shooting
        if shoot:
            clicked = False
            distance = math.sqrt((pos[0]-player.x)**2+(pos[1]-player.y)**2)
            dx = (pos[0]-player.x) / distance
            dy = (pos[1]-player.y) / distance


            bullets.append(Bullet(player.x, player.y, 6, dx, dy, 10, white))
        for b in bullets:
            b.x += b.dx
            b.y += b.dy
            if b.x > width or b.x < 0 or b.y > height or b.y < 0:
                bullets.remove(b)
        if cd >= 10:
            clicked = True

        shoot = False
        #enemy
        create_respawn_point()
        if len(enemy_list) < 3 and fighting == False:
            randi = random.choice(respawn_point_list)
            enemy_list.append(Entity(randi.x, randi.y, 20, red))
        for enemy in enemy_list:
            distance = math.sqrt((player.x-enemy.x)**2+(player.y-enemy.y)**2)
            speed = 3
            enemy.dx = (player.x - enemy.x) / distance
            enemy.dy = (player.y - enemy.y) / distance

            enemy.x += enemy.dx * speed
            enemy.y += enemy.dy * speed
            if player.x > enemy.x - enemy.radius and player.x < enemy.x + enemy.radius:
                if player.y > enemy.y - enemy.radius and player.y < enemy.y + enemy.radius:
                    play = False



            for b in bullets:
                if b.x > enemy.x-enemy.radius and b.x < enemy.x + enemy.radius:
                    if b.y > enemy.y - enemy.radius and b.y < enemy.y + enemy.radius:
                        cd = 110
                        bullets.remove(b)
                        enemy_list.remove(enemy)
                        score += 1
                        if t_cd < 8*FPS:
                            t_cd += 110
        if len(fireball_list) <= timer/120/10 and fighted_boss >= 1 :
            randomm = random.choice(respawn_point_list)
            distance = math.sqrt((player.x-randomm.x)**2+(player.y-randomm.y)**2)
            dx = (player.x-randomm.x)/distance
            dy =(player.y-randomm.y)/distance
            fireball_list.append(Bullet(randomm.x,randomm.y,60,dx,dy,2,orange ))
        for fire in fireball_list:
            fire.x += fire.dx
            fire.y += fire.dx
            if fire.x > width or fire.x < 0 or fire.y > height or fire.y < 0:
                fireball_list.remove(fire)
            if player.x > fire.x - fire.radius and player.x < fire.x + fire.radius:
                if player.y > fire.y - fire.radius and player.y < fire.y + fire.radius:
                    play = False
            fire.draw(win)
        #boss fight
        if score == 50 and fighting == False:
            text = font.render('BOSS FIGHT', True, white)
            win.blit(text, (width / 2-100, height / 2-100))
            pygame.display.update()
            pygame.time.wait(1200)
            fighting = True

        if fighting :
            boss.draw(win)
            boss.shooting(win)
            boss.moving(win)
            if boss.health <= 0:
                del boss
                fighted_boss = 1
                fighting = False
            else:
                for b in bullets:
                    if b.x > boss.x - boss.radius and b.x < boss.x + boss.radius:
                        if b.y > boss.y - boss.radius and b.y < boss.y + boss.radius:
                            cd = 110
                            bullets.remove(b)
                            boss.health -= 1
                            if t_cd < 8 * FPS:
                                t_cd += 110
                if player.x > boss.x - boss.radius and player.x < boss.x + boss.radius:
                    if player.y > boss.y - boss.radius and player.y < boss.y + boss.radius:
                        play = False
                for b_b in boss_bullets:
                    if player.x > b_b.x - b_b.radius and player.x < b_b.x + b_b.radius:
                        if player.y > b_b.y - b_b.radius and player.y < b_b.y + b_b.radius:
                            play = False









        redraw_window(win)
        pygame.display.update()

def controls():
    q = Button(width/2-100, height/2-100,'q = shoot bullet ', (60,60,60))
    d = Button(width / 2 - 100, height / 2, 'd = teleport ', (60, 60, 60))
    s = Button(width / 2 - 100, height / 2 + 100, 's = slowmotion ', (60, 60, 60))
    qu = Button(width / 2 - 100, height / 2 + 200, 'BACK TO MENU', yellow)
    cont = True
    while cont:
        pos = pygame.mouse.get_pos()
        win.fill(bg)

        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cont = False
            if key[pygame.K_ESCAPE]:
                cont = False
            if qu.text_r.collidepoint(pos):
                qu.color1 = red
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        cont = False
            else:
                qu.color1 = yellow

        q.draw(win)
        d.draw(win)
        s.draw(win)
        qu.draw(win)
        pygame.display.update()










run = True
while run:
    bg = (50,50,50)
    pos = pygame.mouse.get_pos()
    win.fill(bg)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if bt.text_r.collidepoint(pos):
            bt.color1 = red
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    main()
        else:
            bt.color1 = yellow
        if bt_q.text_r.collidepoint(pos):
            bt_q.color1 = red
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    run = False
        else:
            bt_q.color1 = yellow
        if bt_c.text_r.collidepoint(pos):
            bt_c.color1 = red
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    controls()
        else:
            bt_c.color1 = yellow

    bt.draw(win)
    bt_q.draw(win)
    bt_c.draw(win)
    pygame.display.update()

pygame.quit()


