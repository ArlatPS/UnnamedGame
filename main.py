#version 0.1.0
import pygame,os,random

from mobs import Hound, Knight, Phantom, SkeleWiz, Bat, Automaton

#rozpoczęcie mixera
pygame.mixer.init()

#rozpoczęcie czcionek i moja czcionka
pygame.font.init()
ALA_200 = pygame.font.Font(os.path.join('assets','alagard.ttf'), 200)
ALA_75 = pygame.font.Font(os.path.join('assets','alagard.ttf'), 75)
ALA_50 = pygame.font.Font(os.path.join('assets','alagard.ttf'), 50)
ALA_125 = pygame.font.Font(os.path.join('assets','alagard.ttf'), 125)

#ustawienie okna, rozdzielczość 1080p
WIDTH, HEIGHT = 1920,1080
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Unnamed Game')

#częstotliwość odświeżania
FPS = 60

#podstawowe kolory
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREY = (128,128,128)

#tło dungeonu (1) 
DUNGEON_FLOOR_RAW = pygame.image.load(os.path.join('assets','floor_dungeon.jpg'))
DUNGEON_FLOOR = pygame.transform.scale(DUNGEON_FLOOR_RAW, (WIDTH,HEIGHT))
BOUNDS_DUNGEON = [240,1660,220,1030]

#tło yard (2)
YARD_FLOOR = pygame.transform.scale(pygame.image.load(os.path.join('assets','floor_yard.jpg')),(WIDTH, HEIGHT))
BOUNDS_YARD = [200,1770,190,940]

#tło library (3)
LIBRARY_FLOOR = pygame.transform.scale(pygame.image.load(os.path.join('assets','floor_lib_closed.jpg')),(WIDTH, HEIGHT))
LIBRARY_FLOOR_OPEN = pygame.transform.scale(pygame.image.load(os.path.join('assets','floor_lib_open.jpg')),(WIDTH, HEIGHT))
LIBRARY_FLOOR_BOSS = pygame.transform.scale(pygame.image.load(os.path.join('assets','floor_lib_boss.jpg')),(WIDTH, HEIGHT))
BOUNDS_LIBRARY = [240,1670,210,930]

#drzwi
DOOR_WIDTH, DOOR_HEIGHT = 120, 190
DOOR = pygame.transform.scale(pygame.image.load(os.path.join('assets','door.png')),(DOOR_WIDTH,DOOR_HEIGHT))

#model postaci
WIZARD_RAW = pygame.image.load(os.path.join('assets','wizard.png'))
WIZARD_SIZE = (72,104)
WIZARD = pygame.transform.scale(WIZARD_RAW, WIZARD_SIZE)
WIZARD_LEFT = pygame.transform.flip(WIZARD,True,False)
WIZARD_RED = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'red_wizard.png')), WIZARD_SIZE)
WIZARD_RED_LEFT = pygame.transform.flip(WIZARD_RED,True,False)

#modele pocisków
project_size = (66,34)
PROJECTILE_LEFT = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'pl_proj.png')), project_size)
PROJECTILE_RIGHT = pygame.transform.flip(PROJECTILE_LEFT,True,False)

enemy_project_size = (37,20)
PROJECTILE_ENEMY_RIGHT = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'en_proj.png')), enemy_project_size)
PROJECTILE_ENEMY_LEFT = pygame.transform.flip(PROJECTILE_ENEMY_RIGHT,True,False)

#splashe
SPLASH_RAW = pygame.image.load(os.path.join('assets', 'splash.png'))
SPLASH_RIGHT = pygame.transform.scale(SPLASH_RAW, (project_size[1],project_size[1]))
SPLASH_LEFT = pygame.transform.flip(SPLASH_RIGHT,True,False)
SPLASH_ENEMY_RIGHT = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'splash_enemy.png')), (project_size[1],project_size[1]))
SPLASH_ENEMY_LEFT = pygame.transform.flip(SPLASH_ENEMY_RIGHT,True,False)

#laser
LASER_WIDTH, LASER_HEIGHT = 600,60
PRE_LASER_RIGHT = pygame.transform.scale(pygame.image.load(os.path.join('assets','laser_pre.png')), (LASER_WIDTH, LASER_HEIGHT))
PRE_LASER_LEFT = pygame.transform.flip(PRE_LASER_RIGHT,True,False)
LASER_RIGHT = pygame.transform.scale(pygame.image.load(os.path.join('assets','laser.png')), (LASER_WIDTH, LASER_HEIGHT))
LASER_LEFT = pygame.transform.flip(LASER_RIGHT,True,False)

#serduszka
heart_size = (75,75)
HEART = pygame.transform.scale(pygame.image.load(os.path.join('assets','heart.png')), heart_size)
HALF_HEART = pygame.transform.scale(pygame.image.load(os.path.join('assets','half_heart.png')), heart_size)
EMPTY_HEART = pygame.transform.scale(pygame.image.load(os.path.join('assets','empty_heart.png')), heart_size)

#ikonki statystyk
icon_size = (50,50)
MOV_SPEED_ICON = pygame.transform.scale(pygame.image.load(os.path.join('assets','mov_speed.png')), icon_size)
DMG_ICON = pygame.transform.scale(pygame.image.load(os.path.join('assets','dmg_icon.png')), icon_size)
FRATE_ICON = pygame.transform.scale(pygame.image.load(os.path.join('assets','firing_rate.png')), icon_size)
PROJ_SPEED_ICON = pygame.transform.scale(pygame.image.load(os.path.join('assets','proj_speed.png')), (50,20))

#model chomper'a
HOUND_WIDTH, HOUND_HEIGHT = 105, 75
HOUND_LEFT = pygame.transform.scale(pygame.image.load(os.path.join('assets','chomper.png')), (HOUND_WIDTH, HOUND_HEIGHT))
HOUND_RIGHT = pygame.transform.flip(HOUND_LEFT,True,False)
HOUND_HURT_SOUND = pygame.mixer.Sound(os.path.join('assets','hound_hurt.wav'))
HOUND_HURT_SOUND.set_volume(.5)

#model SkeleWiz/obecnie nie skele
SKELE_WIDTH, SKELE_HEIGHT = 77,108
SKELE_LEFT = pygame.transform.scale(pygame.image.load(os.path.join('assets','small_wiz_evil.png')), (SKELE_WIDTH, SKELE_HEIGHT))
SKELE_RIGHT = pygame.transform.flip(SKELE_LEFT,True,False)

#model zjawy
PHANTOM_WIDTH, PHANTOM_HEIGHT = 82,105     
PHANTOM_LEFT = pygame.transform.scale(pygame.image.load(os.path.join('assets','phantom.png')), (PHANTOM_WIDTH, PHANTOM_HEIGHT))
PHANTOM_RIGHT = pygame.transform.flip(PHANTOM_LEFT,True,False)

#model rycerza
KNIGHT_WIDTH, KNIGHT_HEIGHT = 90,150
KNIGHT_LEFT = pygame.transform.scale(pygame.image.load(os.path.join('assets','knight.png')), (KNIGHT_WIDTH, KNIGHT_HEIGHT))
KNIGHT_RIGHT = pygame.transform.flip(KNIGHT_LEFT,True,False)

#model nietoperza
BAT_WIDTH, BAT_HEIGHT = 108,64
BAT_RIGHT = pygame.transform.scale(pygame.image.load(os.path.join('assets','bat.png')), (BAT_WIDTH, BAT_HEIGHT))
BAT_LEFT = pygame.transform.flip(BAT_RIGHT,True,False)

#model automatona
AUTO_WIDTH, AUTO_HEIGHT = 100,100
AUTO_LEFT = pygame.transform.scale(pygame.image.load(os.path.join('assets','automaton.png')), (AUTO_WIDTH, AUTO_HEIGHT))
AUTO_RIGHT = pygame.transform.flip(AUTO_LEFT,True,False)


#model bossa
BOSS_WIDTH, BOSS_HEIGHT = 330,570
BOSS = pygame.transform.scale(pygame.image.load(os.path.join('assets','boss_1.png')), (BOSS_WIDTH, BOSS_HEIGHT))
BOSS_2_WIDTH, BOSS_2_HEIGHT = 450,570
BOSS_2 = pygame.transform.scale(pygame.image.load(os.path.join('assets','boss_2.png')), (BOSS_2_WIDTH, BOSS_2_HEIGHT))

#lasery bossa
BOSS_LASER_WIDTH, BOSS_LASER_HEIGHT = 120,1000
BOSS_LASER_PRE = pygame.transform.scale(pygame.image.load(os.path.join('assets','boss_laser_pre.png')), (BOSS_LASER_WIDTH, BOSS_LASER_HEIGHT))
BOSS_LASER = pygame.transform.scale(pygame.image.load(os.path.join('assets','boss_laser.png')), (BOSS_LASER_WIDTH, BOSS_LASER_HEIGHT))

#dźwięki
CAST_SOUND = pygame.mixer.Sound(os.path.join('assets','cast.wav'))
CAST_SOUND.set_volume(.3)
LIGHT_HIT_SOUND = pygame.mixer.Sound(os.path.join('assets','light_hit.wav'))
LIGHT_HIT_SOUND.set_volume(.4)
DUNGEON_MUSIC = pygame.mixer.Sound(os.path.join('assets','back_haunted.wav'))
DUNGEON_MUSIC.set_volume(.2)
HURT_SOUND = pygame.mixer.Sound(os.path.join('assets','hurt.wav'))
HURT_SOUND.set_volume(.6)
YARD_MUSIC = pygame.mixer.Sound(os.path.join('assets','yard_music.wav'))
YARD_MUSIC.set_volume(.5)
ROBOT_DMG = pygame.mixer.Sound(os.path.join('assets','robot_dmg.wav'))
ROBOT_DMG.set_volume(3)
BOSS_MUSIC = pygame.mixer.Sound(os.path.join('assets','boss_fight.wav'))
BOSS_MUSIC.set_volume(.35)
LIB_MUSIC = pygame.mixer.Sound(os.path.join('assets','lib_music.wav'))
LIB_MUSIC.set_volume(.3)
LASER_PRE_SOUND = pygame.mixer.Sound(os.path.join('assets','pre_shot.wav'))
LASER_PRE_SOUND.set_volume(0.9)
LASER_SOUND = pygame.mixer.Sound(os.path.join('assets','laser_shot.wav'))
LASER_SOUND.set_volume(.6)


#prędkość poruszania
MOV_SPEED = 10

#szybkość strzelania
FIRING_RATE = 1.0

#szybkość pocisków
PROJECT_SPEED = 15

#obrażenia
WIZARD_DMG = 10

#życie gracza i długość niewrażliwości po obrażeniach
WIZARD_HP = 6
INVINCIBILITY_LEN = 90

#duży timer
BIG_TIMER = 4 * 3600

#przedmioty początkowe gracza
items = []

#zestawy przeciwników dla dungeon
#room 1
hounds = [Hound(1100,500),Hound(1100,200),Hound(1100,800)]
skeletons = [SkeleWiz(1300,200),SkeleWiz(1500,800)]
mobs = hounds + skeletons
room_dungeon_1 = [hounds,skeletons,mobs]

#room 2
hounds = [Hound(800,500),Hound(800,200),Hound(800,800),Hound(300,1000),Hound(400,200)]
skeletons = []
mobs = hounds + skeletons
room_dungeon_2 = [hounds, skeletons, mobs]

#room 3
hounds = []
skeletons = [SkeleWiz(1300,200),SkeleWiz(1500,800),SkeleWiz(800,200),SkeleWiz(1000,1000),SkeleWiz(1200,400)]
mobs = hounds + skeletons
room_dungeon_3 = [hounds, skeletons, mobs]

#room 4
hounds = [Hound(1200,400),Hound(1300,600)]
skeletons = [SkeleWiz(1600,200),SkeleWiz(1400,800),SkeleWiz(300,300)]
mobs = hounds + skeletons
room_dungeon_4 = [hounds,skeletons,mobs]

#room 5
hounds = [Hound(1450,450),Hound(1450,650)]
skeletons = [SkeleWiz(500,300),SkeleWiz(600,600),SkeleWiz(400,900)]
mobs = hounds + skeletons
room_dungeon_5 = [hounds,skeletons,mobs]

dungeon_rooms = [room_dungeon_1,room_dungeon_2,room_dungeon_3,room_dungeon_4,room_dungeon_5]

#zestaw dla yard
#room 1
knights = [Knight(1200,900), Knight(1200,300)]
phantoms = [Phantom(900,200),Phantom(700,900)]
mobs = knights + phantoms
room_yard_1 = [knights, phantoms, mobs]

#room 2
phantoms = [Phantom(700,-200),Phantom(1100,-200),Phantom(700,1180),Phantom(1100,1180)]
knights=[]
mobs = knights + phantoms
room_yard_2 = [knights,phantoms,mobs]

#room 3
knights = [Knight(1000,800),Knight(1600,600),Knight(1600,200),Knight(1000,400)]
phantoms = []
mobs = knights + phantoms
room_yard_3 = [knights, phantoms, mobs]

#room4
knights = [Knight(600,500),Knight(600,200),Knight(600,800)]
phantoms = [Phantom(1300,200),Phantom(1400,300),Phantom(1350,450)]
mobs = knights + phantoms
room_yard_4 = [knights, phantoms, mobs]

#room5
knights = [Knight(400,800),Knight(400,200)]
phantoms = [Phantom(1000,700),Phantom(1100,300),Phantom(700,450),Phantom(1600,-200),Phantom(1600,1200)]
mobs = knights + phantoms
room_yard_5 = [knights, phantoms, mobs]

yard_rooms = [room_yard_1,room_yard_2,room_yard_3, room_yard_4,room_yard_5]

#zestaw dla library
#room 1 - automaton introduction, mandatory
bats = []
automatons = [Automaton(320,500)]
mobs = bats + automatons
lib_room_1 = [bats,automatons,mobs]

#room 2
bats = [Bat(1400,100)]
automatons = [Automaton(300, 300), Automaton(300,800)]
mobs = bats + automatons
lib_room_2 = [bats,automatons,mobs]

#room 3
bats = [Bat(400,50), Bat(400,1000)]
automatons = [Automaton(920,500)]
mobs = bats + automatons
lib_room_3 = [bats,automatons,mobs]

#room4
bats = [Bat(1500,50), Bat(100,50), Bat(500,1000)]
automatons = [Automaton(320,500)]
mobs = bats + automatons
lib_room_4 = [bats,automatons,mobs]

#room5
bats = [Bat(300,50),Bat(600,50),Bat(1200,50),Bat(300,1000),Bat(600,1000),Bat(1200,1000)]
automatons = []
mobs = bats + automatons
lib_room_5 = [bats,automatons,mobs]

lib_rooms = [lib_room_2,lib_room_3,lib_room_4,lib_room_5]

#poruszanie WASD w granicach
def movement(keys_pressed,player,floor,facing):
    if floor == 'dungeon':
        floor_left, floor_right, floor_up, floor_down = BOUNDS_DUNGEON
    elif floor == 'yard':
        floor_left, floor_right, floor_up, floor_down = BOUNDS_YARD
    else:
        floor_left, floor_right, floor_up, floor_down = BOUNDS_LIBRARY
    #A
    if keys_pressed[pygame.K_a] and player.x - MOV_SPEED > floor_left:
        player.x -= MOV_SPEED
        facing = 'left'
    #D
    if keys_pressed[pygame.K_d] and player.x + MOV_SPEED + player.width < floor_right:
        player.x += MOV_SPEED
        facing = 'right'
    #W
    if keys_pressed[pygame.K_w] and player.y - MOV_SPEED > floor_up:
        player.y -= MOV_SPEED
    #S
    if keys_pressed[pygame.K_s] and player.y + MOV_SPEED +player.height < floor_down:
       player.y += MOV_SPEED
    return facing

#strzelanie - pociski to [x,y,kierunek]
def shooting(keys_pressed,projectiles,x,y,current_model,facing):
    if keys_pressed[pygame.K_d]:
        direction = 'd'
    elif keys_pressed[pygame.K_a]:
        direction = 'a'
    elif keys_pressed[pygame.K_w]:
         direction = 'w'
    elif keys_pressed[pygame.K_s]:
        direction = 's'
    else:
        if facing == 'right':
            direction = 'd'
        else:
            direction = 'a'
    # w zależności od kierunku modelu w innym miejscu pojawia się pocisk
    if current_model == WIZARD or current_model == WIZARD_RED:
        projectiles.append([x + WIZARD_SIZE[0] - 40,y + WIZARD_SIZE[1]//20 ,direction])
    else:
        projectiles.append([x ,y + WIZARD_SIZE[1]//20 ,direction])
    #dźwięk
    CAST_SOUND.play()

#zachowanie pocisków i tworzenie efektu
def projectiles_managment(projectiles,splashes,floor):
    if floor == 'dungeon':
        floor_left, floor_right, floor_up, floor_down = BOUNDS_DUNGEON
    elif floor == 'yard':
        floor_left, floor_right, floor_up, floor_down = BOUNDS_YARD
    else:
        floor_left, floor_right, floor_up, floor_down = BOUNDS_LIBRARY

    for projectile in projectiles:
        if projectile[2] == 'd':
            projectile[0] += PROJECT_SPEED
        elif projectile[2] == 'a':
            projectile[0] -= PROJECT_SPEED
        elif projectile[2] == 'w':
            projectile[1] -= PROJECT_SPEED
        elif projectile[2] == 's':
            projectile[1] += PROJECT_SPEED

        #kolizja z bokiem pokoju i utworzenie splasha
        if projectile[0] >= floor_right - project_size[0] or projectile[0] <= floor_left:
            if projectile[2] == 'd':
                splashes.append([projectile[0],projectile[1],0,'d'])
                projectiles.remove(projectile)
            else:
                splashes.append([projectile[0],projectile[1],0,'a'])
                projectiles.remove(projectile)
            #dźwięk
            LIGHT_HIT_SOUND.play()
        elif projectile[1] <= floor_up or projectile[1] >= floor_down - project_size[1]:
            splashes.append([projectile[0],projectile[1],0,'d'])
            projectiles.remove(projectile)
            #dźwięk
            LIGHT_HIT_SOUND.play()

#zarządzanie pociskami przeciwników (mają wzór [x,y,kierunek,prędkość])
def enemy_project_managment(enemy_project,enemy_splashes,floor):
    if floor == 'dungeon':
        floor_left, floor_right, floor_up, floor_down = BOUNDS_DUNGEON
    elif floor == 'yard':
        floor_left, floor_right, floor_up, floor_down = BOUNDS_YARD
    else:
        floor_left, floor_right, floor_up, floor_down = BOUNDS_LIBRARY

    for projectile in enemy_project:
        if projectile[2] == 'd':
            projectile[0] += projectile[3]
        elif projectile[2] == 'a':
            projectile[0] -= projectile[3]
        elif projectile[2] == 'w':
            projectile[1] -= projectile[3]
        elif projectile[2] == 's':
            projectile[1] += projectile[3]

        if projectile[2] == 'a':
            WIN.blit(PROJECTILE_ENEMY_LEFT, (projectile[0],projectile[1]))
        else:
            WIN.blit(PROJECTILE_ENEMY_RIGHT, (projectile[0],projectile[1]))

        if projectile[0] >= floor_right - enemy_project_size[0] or projectile[0] <= floor_left:
            if projectile[2] == 'd':
                enemy_splashes.append([projectile[0],projectile[1],0,'d'])
                enemy_project.remove(projectile)
            else:
                enemy_splashes.append([projectile[0],projectile[1],0,'a'])
                enemy_project.remove(projectile)
            #dźwięk
            LIGHT_HIT_SOUND.play()
        elif projectile[1] <= floor_up or projectile[1] >= floor_down - enemy_project_size[1]:
            enemy_splashes.append([projectile[0],projectile[1],0,'d'])
            enemy_project.remove(projectile)
            #dźwięk
            LIGHT_HIT_SOUND.play()

#rysowanie serc
def draw_hearts():
    if WIZARD_HP % 2 == 0:
        hearts = WIZARD_HP/2
        i = 0
        while i < hearts:
            WIN.blit(HEART, (20 + i * 80, 20))
            i +=1
    else:
        hearts = WIZARD_HP//2
        i = 0
        while i < hearts:
            WIN.blit(HEART, (20 + i * 80, 20))
            i +=1
        WIN.blit(HALF_HEART, (20 + i * 80, 20))
    if WIZARD_HP <= 4:
        WIN.blit(EMPTY_HEART, (180, 20))
    if WIZARD_HP <= 2:
        WIN.blit(EMPTY_HEART, (100, 20))

#pokazywanie czasu
def draw_timer():
    minute = str((round(BIG_TIMER/60)) // 60)
    second = str(round(BIG_TIMER/60) %60 )
    if int(second) <10:
        time = minute + ':0'+ second
    else:
        time = minute + ':'+ second
    text = ALA_75.render(time, True, WHITE)
    WIN.blit(text, (WIDTH - 200, 10))
    

#rysowanie statystyk
def draw_stats():
    speed = ALA_50.render(str(MOV_SPEED), True, WHITE)
    WIN.blit(MOV_SPEED_ICON, (30,120))
    WIN.blit(speed, (90, 120))
    dmg = ALA_50.render(str(WIZARD_DMG), True, WHITE)
    WIN.blit(DMG_ICON, (30,180))
    WIN.blit(dmg, (90, 180))
    firing = ALA_50.render(str(FIRING_RATE), True, WHITE)
    WIN.blit(FRATE_ICON, (30,240))
    WIN.blit(firing, (90, 240))
    proj = ALA_50.render(str(PROJECT_SPEED), True, WHITE)
    WIN.blit(PROJ_SPEED_ICON, (30,310))
    WIN.blit(proj, (90, 300))

#rysowanie okna
def draw_window(floor,player,current_model,projectiles,splashes,enemy_splashes,room):
    #tworzy tło dungeonu
    WIN.blit(floor,(0,0))
    #rysuje postać
    WIN.blit(current_model, (player.x,player.y))
    #rysuje pociski
    for projectile in projectiles:
        if projectile[2] == 'a':
            WIN.blit(PROJECTILE_RIGHT, (projectile[0],projectile[1]))
        else:
            WIN.blit(PROJECTILE_LEFT, (projectile[0],projectile[1]))
    #rysuje splashe
    for splash in splashes:
        if splash[3] == 'd':
            WIN.blit(SPLASH_RIGHT, (splash[0],splash[1]))
        else:
            WIN.blit(SPLASH_LEFT, (splash[0],splash[1]))
        if splash[2] >=30:
            splashes.remove(splash)
        splash[2] +=1
    for splash in enemy_splashes:
        if splash[3] == 'd':
            WIN.blit(SPLASH_ENEMY_RIGHT, (splash[0],splash[1]))
        else:
            WIN.blit(SPLASH_ENEMY_LEFT, (splash[0],splash[1]))
        if splash[2] >=30:
            enemy_splashes.remove(splash)
        splash[2] +=1

    #rysuje serduszka reprezentujące hp
    draw_hearts()

    #rysuje statystyki
    draw_stats()

    #rysuje timer
    draw_timer()
    
    #rysuje numer pokoju
    if room <= 3:
        num = room * 'I'
    elif room == 4:
        num = 'IV'
    elif room <= 8:
        num = 'V' + (room - 5) * 'I'
    elif room == 9:
        num = 'IX'
    else:
        num = 'X'
    text = ALA_75.render(num, True, WHITE)
    WIN.blit(text, (WIDTH - 150, HEIGHT - 125))

#ekran przy przegraniu - jako argmunet jest sposób przegrania
def draw_lose_screen(way):
    if way == 'hp':
        text = ALA_200.render('YOU DIED', True, RED)
        WIN.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
        pygame.display.update()
    elif way == 'time':
        text = ALA_200.render('TIME\'S UP', True, RED)
        WIN.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
        pygame.display.update()

#ekran zatrzymania
def draw_stop_screen():
    text = ALA_200.render('GAME STOPPED', True, WHITE)
    WIN.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    text2 = ALA_75 .render('press ESC to continue', True, WHITE)
    WIN.blit(text2, (WIDTH/2 - text.get_width()/2 + text2.get_width()/2, HEIGHT/2 + text.get_height()/2))
    pygame.display.update()


def main():
    #ustawienie zegara
    clock = pygame.time.Clock()

    #ustawienie obecnego poziomu
    room = 1

    #import ustawień do funkcji
    global WIZARD_HP,project_size, BIG_TIMER, MOV_SPEED,WIZARD_DMG, FIRING_RATE,\
            PROJECT_SPEED,INVINCIBILITY_LEN,PROJECTILE_ENEMY_RIGHT, PROJECTILE_ENEMY_LEFT

    #długości muzyki
    dungeon_music = 78 * 60 + 1
    dungeon_music_len = 78 * 60
    yard_music = 152 * 60 + 1
    yard_music_len = 152 * 60
    lib_music = 209 *60 + 1
    lib_music_len = lib_music - 1
    boss_music = 117 * 60 + 1
    boss_music_len = 117*60

    while True:
       
        projectiles = []
        splashes = []
        enemy_splashes = []
        timer = 0
        #na którym poziomie jest gracz
        if room <= 3: 
            floor = 'dungeon'
            floor_image = DUNGEON_FLOOR
        elif room <=6:
            floor = 'yard'
            floor_image = YARD_FLOOR
        else:
            floor = 'library'
            floor_image = LIBRARY_FLOOR


        #pozycja postaci i jej zwrot
        if not floor == 'library':
            player = pygame.Rect(250,500,WIZARD_SIZE[0],WIZARD_SIZE[1])
            facing = 'right'
        else:
            player = pygame.Rect(1250,500,WIZARD_SIZE[0],WIZARD_SIZE[1])
            facing = 'left'
            current_model = WIZARD_LEFT

        
        #czy gracz został uderzony w tej klatce - startowe wartości
        hit = False
        invincibility = 0

        #pierwsze klatki do wystartowania
        first_frames = 0

        #czy ekran pauzy
        stop = False
        
        #czy koniec rozgrywki
        end = False

        #tworzenie przeciwników
        if floor == 'dungeon': 
            #losowy indeks
            leng = len(dungeon_rooms)
            num = random.randint(1,leng)
            hounds,skeletons,mobs = dungeon_rooms[num-1]
            dungeon_rooms.remove(dungeon_rooms[num-1])

            for doggo in hounds:
                doggo.spawn(HOUND_WIDTH,HOUND_HEIGHT)
        
            for skele in skeletons:
                skele.spawn(SKELE_WIDTH,SKELE_HEIGHT)

        elif floor == 'yard':
            leng = len(yard_rooms)
            num = random.randint(1,leng)
            knights,phantoms,mobs = yard_rooms[num-1]
            yard_rooms.remove(yard_rooms[num-1])

            for knight in knights:
                knight.spawn(KNIGHT_WIDTH,KNIGHT_HEIGHT)
            for phantom in phantoms:
                phantom.spawn(PHANTOM_WIDTH,PHANTOM_HEIGHT)

        elif floor == 'library' and room != 10:
            if room == 7:
                bats,automatons,mobs = lib_room_1
            else:
                leng = len(lib_rooms)
                num = random.randint(1,leng)
                bats,automatons,mobs = lib_rooms[num-1]
                lib_rooms.remove(lib_rooms[num-1])

            for bat in bats:
                bat.spawn(BAT_WIDTH,BAT_HEIGHT)
        
            for auto in automatons:
                auto.spawn(AUTO_WIDTH,AUTO_HEIGHT)

        #projectiles przeciwników
        enemy_project = []

        #statsu pokoju
        floor_clear = False
        floor_clear_item = True
        final_room_entered = False
        boss_phase = 1

        #kończenie muzyki
        if room == 4 or room == 7 or room == 10:
            pygame.mixer.fadeout(200)
        

        #pętla w której działa gra
        while True:
            #1 FPS
            clock.tick(FPS)

            #muzyka dla dungeon
            if floor == 'dungeon' and dungeon_music > dungeon_music_len:
                DUNGEON_MUSIC.play()
                dungeon_music = 0
            elif floor == 'dungeon':
                dungeon_music += 1
            if floor == 'yard' and yard_music> yard_music_len:
                YARD_MUSIC.play()
                yard_music = 0
            elif floor == 'yard':
                yard_music +=1
            if floor == 'library' and lib_music > lib_music_len and not room == 10:
                LIB_MUSIC.play()
                lib_music = 0
            elif floor == 'library' and not room == 10:
                lib_music += 1
            if room == 10 and boss_music > boss_music_len:
                BOSS_MUSIC.play()
                boss_music = 0
            elif room == 10:
                boss_music += 1


            #zatrzymywanie gry
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if stop == False:
                            draw_stop_screen()
                            stop = True
                        else:
                            draw_window(floor_image,player,current_model,projectiles,splashes,enemy_splashes,room)
                            stop = False
                #wyjście z gry
                elif event.type == pygame.QUIT:
                    pygame.quit()
                

            #pobiera naciśnięte klawisze
            keys_pressed = pygame.key.get_pressed()

            #jeśli poniższe przyciski naciśnięte to czas się porusza
            if (keys_pressed[pygame.K_a] or keys_pressed[pygame.K_d] or keys_pressed[pygame.K_w] or \
                keys_pressed[pygame.K_s] or keys_pressed[pygame.K_SPACE] or first_frames < 1) and stop == False :
            
                #poruszanie się
                facing = movement(keys_pressed,player,floor,facing)
                    
                #w którą stronę skierowany jest gracz i czy dostał obrażenia
                if facing == 'right':
                    if invincibility >=60:
                        current_model = WIZARD_RED
                    else:
                        current_model = WIZARD
                else:
                    if invincibility >=60:
                        current_model = WIZARD_RED_LEFT
                    else:
                        current_model = WIZARD_LEFT

                #strzelanie na naciśnięcie SPACE - timer jest dla szybkości strzałów
                if not keys_pressed[pygame.K_SPACE] and timer % (60/FIRING_RATE) == 0:
                    timer = 0
                elif not keys_pressed[pygame.K_SPACE]:
                    timer +=1
                if keys_pressed[pygame.K_SPACE]:
                    if timer % (60/FIRING_RATE) == 0:
                        shooting(keys_pressed,projectiles,player.x,player.y,current_model,facing)
                    timer +=1

                #zachowanie pocisków
                projectiles_managment(projectiles,splashes,floor)

                
                #rysowanie
                draw_window(floor_image,player,current_model,projectiles,splashes,enemy_splashes,room)
                
                #moby wykonują akcje
                if floor == 'dungeon': 
                    #hounds wykonują swoje akcje
                    for doggo in hounds:
                        #poruszanie i wyświetlanie
                        doggo.move(player.x,player.y,mobs)
                        if doggo.turn == 'left':
                            WIN.blit(HOUND_LEFT, (doggo.x, doggo.y))
                        else:
                            WIN.blit(HOUND_RIGHT, (doggo.x, doggo.y))

                        #uderzenie gracza
                        if player.colliderect(doggo) and invincibility < 0:
                            hit = True
                            invincibility = INVINCIBILITY_LEN

                        #otrzymanie obrażeń
                        for projectile in projectiles:
                            project = pygame.Rect((projectile[0],projectile[1]),project_size)
                            if project.colliderect(doggo):
                                doggo.hurt(WIZARD_DMG)
                                HOUND_HURT_SOUND.play()
                                if projectile[2] == 'd':
                                    splashes.append([projectile[0],projectile[1],0,'d'])
                                else:
                                    splashes.append([projectile[0],projectile[1],0,'a'])
                                projectiles.remove(projectile)

                        #umieranie
                        if doggo.hp <= 0:
                            hounds.remove(doggo)
                            mobs.remove(doggo)
            
                    #szkielety wykonuja akcje 
                    for skele in skeletons:
                        #rusza się
                        skele.move(player.y,mobs)

                        #rysowanie
                        if skele.turn == 'right':
                            WIN.blit(SKELE_RIGHT,(skele.x,skele.y))
                        else:
                            WIN.blit(SKELE_LEFT,(skele.x,skele.y))

                        #strzelanie
                        if skele.cooldown <= 0:
                            skele.shoot(player.x,player.y,enemy_project)
                            skele.cooldown =+ skele.cooldown_add
                        skele.cooldown -=1

                        #otrzymywanie obrażeń
                        for projectile in projectiles:
                            project = pygame.Rect((projectile[0],projectile[1]),project_size)
                            if project.colliderect(skele):
                                skele.hurt(WIZARD_DMG)
                                HOUND_HURT_SOUND.play()
                                if projectile[2] == 'd':
                                    splashes.append([projectile[0],projectile[1],0,'d'])
                                else:
                                    splashes.append([projectile[0],projectile[1],0,'a'])
                                projectiles.remove(projectile)

                        #umieranie
                        if skele.hp <= 0:
                            skeletons.remove(skele)
                            mobs.remove(skele)

                elif floor == 'yard':
                    #zachowanie rycerzy
                    for knight in knights:
                        #poruszanie i wyświetlanie
                        knight.move(player.x,player.y,mobs)
                        if knight.turn == 'left':
                            WIN.blit(KNIGHT_LEFT, (knight.x, knight.y))
                        else:
                            WIN.blit(KNIGHT_RIGHT, (knight.x, knight.y))

                        #uderzenie gracza
                        if player.colliderect(knight) and invincibility < 0:
                            hit = True
                            invincibility = INVINCIBILITY_LEN

                        #otrzymanie obrażeń
                        for projectile in projectiles:
                            project = pygame.Rect((projectile[0],projectile[1]),project_size)
                            if project.colliderect(knight):
                                knight.hurt(WIZARD_DMG)
                                HOUND_HURT_SOUND.play()
                                if projectile[2] == 'd':
                                    splashes.append([projectile[0],projectile[1],0,'d'])
                                else:
                                    splashes.append([projectile[0],projectile[1],0,'a'])
                                projectiles.remove(projectile)

                        #umieranie
                        if knight.hp <= 0:
                            knights.remove(knight)
                            mobs.remove(knight)

                    #zachowanie zjaw
                    for phantom in phantoms:
                        #poruszanie i wyświetlanie
                        phantom.move(player.x,player.y,mobs)
                        if phantom.turn == 'left':
                            WIN.blit(PHANTOM_LEFT, (phantom.x, phantom.y))
                        else:
                            WIN.blit(PHANTOM_RIGHT, (phantom.x, phantom.y))

                        #uderzenie gracza
                        if player.colliderect(phantom) and invincibility < 0:
                            hit = True
                            invincibility = INVINCIBILITY_LEN

                        #otrzymanie obrażeń
                        for projectile in projectiles:
                            project = pygame.Rect((projectile[0],projectile[1]),project_size)
                            if project.colliderect(phantom):
                                phantom.hurt(WIZARD_DMG)
                                HOUND_HURT_SOUND.play()
                                if projectile[2] == 'd':
                                    splashes.append([projectile[0],projectile[1],0,'d'])
                                else:
                                    splashes.append([projectile[0],projectile[1],0,'a'])
                                projectiles.remove(projectile)

                        #umieranie
                        if phantom.hp <= 0:
                            phantoms.remove(phantom)
                            mobs.remove(phantom)

                elif floor == 'library' and room != 10:
                    #zachowanie automatonów
                    for auto in automatons:
                        #rusza się
                        auto.move(player.x,player.y,mobs)

                        #rysowanie
                        if auto.turn == 'right':
                            WIN.blit(AUTO_RIGHT,(auto.x,auto.y))
                        else:
                            WIN.blit(AUTO_LEFT,(auto.x,auto.y))

                        #strzelanie
                        #rozpoczęcie - pre laser
                        if auto.cooldown <= 0 and not auto.shooting and not auto.pre_shooting:
                            if abs(auto.x - player.x) <= auto.shot_range:
                                auto.pre_shooting = True
                                LASER_PRE_SOUND.play()
                                if auto.turn == 'right':
                                    auto.shoot_dir = 'right'
                                    WIN.blit(PRE_LASER_RIGHT, (auto.x, auto.y))
                                else:
                                    auto.shoot_dir = 'left'
                                    WIN.blit(PRE_LASER_LEFT, (auto.x, auto.y))
                        #wyświetlanie pre lasera
                        if auto.pre_shooting and auto.pre_time > 0:
                            if auto.shoot_dir == 'right':
                                WIN.blit(PRE_LASER_RIGHT, (auto.x + AUTO_WIDTH - 12, auto.y + AUTO_HEIGHT/5 - 5))
                            else:
                                WIN.blit(PRE_LASER_LEFT, (auto.x - LASER_WIDTH + 12, auto.y + AUTO_HEIGHT/5 - 5))
                            auto.pre_time -= 1
                        #uderza laser
                        if auto.pre_shooting and auto.pre_time == 0:
                            if auto.shoot_dir == 'right':
                                WIN.blit(LASER_RIGHT, (auto.x + AUTO_WIDTH - 12, auto.y + AUTO_HEIGHT/5 - 5))
                            else:
                                WIN.blit(LASER_LEFT, (auto.x - LASER_WIDTH + 12, auto.y + AUTO_HEIGHT/5 - 5))
                            auto.pre_shooting = False
                            auto.pre_time = 60
                            auto.shooting = True
                            LASER_SOUND.play()
                        #laser aktywny
                        if auto.shooting and auto.shooting_time >=0:
                            if auto.shoot_dir == 'right':
                                WIN.blit(LASER_RIGHT, (auto.x + AUTO_WIDTH - 12, auto.y + AUTO_HEIGHT/5 - 5))
                                auto.laserx = auto.x + AUTO_WIDTH - 12
                                auto.lasery = auto.y + AUTO_HEIGHT/5 - 5
                            else:
                                WIN.blit(LASER_LEFT, (auto.x - LASER_WIDTH + 12, auto.y + AUTO_HEIGHT/5 - 5))
                                auto.laserx = auto.x - LASER_WIDTH + 12
                                auto.lasery = auto.y + AUTO_HEIGHT/5 - 5
                            #tworzenie kwadratu lasera
                            laser = pygame.Rect((auto.laserx,auto.lasery), (LASER_WIDTH, LASER_HEIGHT))
                            if laser.colliderect(player) and invincibility < 0:
                                hit = True
                                invincibility = INVINCIBILITY_LEN
                            auto.shooting_time -= 1
                        #koniec stzrału
                        if auto.shooting and auto.shooting_time < 0:
                            auto.shooting = False
                            auto.shooting_time = 60
                            auto.cooldown = auto.cooldown_value
                        #cooldown spada
                        auto.cooldown -= 1

                        #otrzymywanie obrażeń
                        for projectile in projectiles:
                            project = pygame.Rect((projectile[0],projectile[1]),project_size)
                            if project.colliderect(auto):
                                auto.hurt(WIZARD_DMG)
                                ROBOT_DMG.play()
                                if projectile[2] == 'd':
                                    splashes.append([projectile[0],projectile[1],0,'d'])
                                else:
                                    splashes.append([projectile[0],projectile[1],0,'a'])
                                projectiles.remove(projectile)

                        #umieranie
                        if auto.hp <= 0:
                            automatons.remove(auto)
                            mobs.remove(auto)
                    
                    #zachowanie nietoperzy
                    for bat in bats:
                        #rusza się
                        bat.move(player.x,player.y,mobs)

                        #rysowanie
                        if bat.turn == 'right':
                            WIN.blit(BAT_RIGHT,(bat.x,bat.y))
                        else:
                            WIN.blit(BAT_LEFT,(bat.x,bat.y))
                        
                        #uderzenie gracza
                        if player.colliderect(bat) and invincibility < 0:
                            hit = True
                            invincibility = INVINCIBILITY_LEN

                        #otrzymywanie obrażeń
                        for projectile in projectiles:
                            project = pygame.Rect((projectile[0],projectile[1]),project_size)
                            if project.colliderect(bat):
                                bat.hurt(WIZARD_DMG)
                                HOUND_HURT_SOUND.play()
                                if projectile[2] == 'd':
                                    splashes.append([projectile[0],projectile[1],0,'d'])
                                else:
                                    splashes.append([projectile[0],projectile[1],0,'a'])
                                projectiles.remove(projectile)

                        #umieranie
                        if bat.hp <= 0:
                            bats.remove(bat)
                            mobs.remove(bat)


                #walka z bossem
                elif room == 10:
                    #ustawia za pierwszym wejściem wartość dla zmiennych i zmienia rozmiar projectile
                    if not final_room_entered:
                        mobs = ['boss']
                        PROJECTILE_ENEMY = pygame.transform.scale(PROJECTILE_LEFT, (60,60))
                        boss = pygame.Rect((200,250),(BOSS_WIDTH,BOSS_HEIGHT))
                        final_room_entered = True
                        boss_alive = True
                        boss_hp = 500          
                        boss_timer = 55
                        boss_cooldown = 30
                        boss_pre_shooting = False
                        boss_shooting = False
                        LASER_PRE_SOUND.set_volume(1)
                        LASER_SOUND.set_volume(1)

                    #boss dostaje obrażenia
                    for projectile in projectiles:
                        project = pygame.Rect((projectile[0],projectile[1]),project_size)
                        if project.colliderect(boss):
                            boss_hp -= WIZARD_DMG
                            ROBOT_DMG.play()
                            if projectile[2] == 'd':
                                splashes.append([projectile[0],projectile[1],0,'d'])
                            else:
                                splashes.append([projectile[0],projectile[1],0,'a'])
                            projectiles.remove(projectile)

                    if boss_phase == 1:
                        #boss i jego hp jest rysowane
                        WIN.blit(BOSS, (250,300))
                        #hp = ALA_50.render(str(boss_hp), True, GREY)
                        #WIN.blit(hp, (50, HEIGHT - 100))
                        
                        #gracz nie może wchodzić w bossa
                        if player.x <= 540 and invincibility<0 and len(mobs) > 0:
                            hit = True
                            invincibility = INVINCIBILITY_LEN
                        
                        #prędkość strzałów bossa
                        boss_speed = 10
                        #zestawy strzałów dla bossa
                        shot_1 = [250,450,550,650,750,850,950]
                        shot_2 = [250,350,550,650,750,850,950]
                        shot_3 = [250,350,450,650,750,850,950]
                        shot_4 = [250,350,450,550,750,850,950]
                        shot_5 = [250,350,450,550,650,850,950]
                        boss_shots = [shot_1,shot_2,shot_3,shot_4,shot_5]
                        boss_timer += 1

                        if boss_timer == 75 and boss_alive:
                            #wybór stzrału bossa
                            num = random.randint(1,5)
                            shot = boss_shots[num-1]
                            #strzelanie bossa (mają wzór [x,y,kierunek,prędkość])
                            for i in shot:
                                projectile = [540,i,'d',boss_speed]
                                enemy_project.append(projectile)
                            boss_timer = 0

                        #boss przechodzi do fazy 2
                        if boss_hp <= 0:
                            boss_phase = 2
                            boss_hp = 500
                    #faza druga
                    elif boss_phase == 2:
                        #inne tło
                        floor_image = LIBRARY_FLOOR_BOSS

                        #boss i jego hp jest rysowane
                        WIN.blit(BOSS_2, (240,300))
                        #hp = ALA_50.render(str(boss_hp), True, GREY)
                        #WIN.blit(hp, (50, HEIGHT - 100))
                        boss = pygame.Rect((240,300),(BOSS_2_WIDTH,BOSS_2_HEIGHT))

                        #boss dostaje obrażenia
                        for projectile in projectiles:
                            project = pygame.Rect((projectile[0],projectile[1]),project_size)
                            if project.colliderect(boss):
                                boss_hp -= WIZARD_DMG
                                ROBOT_DMG.play()
                                if projectile[2] == 'd':
                                    splashes.append([projectile[0],projectile[1],0,'d'])
                                else:
                                    splashes.append([projectile[0],projectile[1],0,'a'])
                                projectiles.remove(projectile)

                        #gracz nie wchodzi w bossa
                        if player.x <= 650 and invincibility<0 and len(mobs) > 0:
                            hit = True
                            invincibility = INVINCIBILITY_LEN

                        #boss atakuje laserami
                        
                        #możliwości
                        shot_1 = [675,925,1050,1175,1300,1425,1550]
                        shot_2 = [675,800,1050,1175,1300,1425,1550]
                        shot_3 = [675,800,925,1175,1300,1425,1550]
                        shot_4 = [675,800,925,1050,1300,1425,1550]
                        shot_5 = [675,800,925,1050,1175,1425,1550]
                        shot_6 = [675,800,925,1050,1175,1300,1550]
                        shots = [shot_1,shot_2,shot_3,shot_4,shot_5,shot_6]

                        if boss_cooldown <= 0:
                            if not (boss_pre_shooting or boss_shooting):
                                boss_pre_shooting = True
                                LASER_PRE_SOUND.play()
                                #losowy strzał  
                                num = random.randint(1,6)
                                shot = shots[num-1]
                                #dłg pre shoot
                                pre_shot_len = 60
                            #pre shooting
                            elif boss_pre_shooting:
                                for i in shot:
                                    WIN.blit(BOSS_LASER_PRE, (i,-75))
                                #koniec pre
                                if pre_shot_len <= 0:
                                    boss_pre_shooting = False
                                    boss_shooting = True
                                    boss_shoot_len = 60
                                    LASER_SOUND.play()
                                else:
                                    pre_shot_len -= 1
                                
                            elif boss_shooting:
                                for i in shot:
                                    WIN.blit(BOSS_LASER, (i,-75))
                                    laser = pygame.Rect((i,-75),(BOSS_LASER_WIDTH,BOSS_LASER_HEIGHT))
                                    if laser.colliderect(player) and invincibility<0 and len(mobs) > 0:
                                        hit = True
                                        invincibility = INVINCIBILITY_LEN
                                #koniec strzelania
                                if boss_shoot_len <= 0:
                                    boss_shooting = False
                                    pre_shot_len = 60
                                    boss_cooldown = 30
                                else:
                                    boss_shoot_len -= 1
                        else:
                            boss_cooldown -= 1

                        #boss umiera
                        if boss_hp <= 0:
                            boss_alive = False
                            mobs = []
                

                #gdy pocisk przeciwnika trafia gracza
                for projectile in enemy_project:
                    project = pygame.Rect((projectile[0],projectile[1]),project_size)
                    if project.colliderect(player) and invincibility < 0:
                        hit = True
                        invincibility = INVINCIBILITY_LEN
                        enemy_project.remove(projectile)
                        if projectile[2] == 'd':
                            enemy_splashes.append([projectile[0],projectile[1],0,'d'])
                        else:
                            enemy_splashes.append([projectile[0],projectile[1],0,'a'])


                #zarządzanie tymi co nie trafiły
                enemy_project_managment(enemy_project,enemy_splashes,floor)

                #dobre miejsce do update - nic nie miga
                pygame.display.update()

                #gracz otrzymuje obrażenia
                if hit:
                    WIZARD_HP -= 1
                    HURT_SOUND.play()
                    hit = False
                
                #spadek czsu niewrażliwosci z każdą klatką
                invincibility -= 1

                
                #odliczanie czasu
                BIG_TIMER -= 1
                
                #czas się skończył
                if BIG_TIMER == 0:
                    draw_lose_screen('time')
                    pygame.time.delay(6000)
                    end = True
                    break

                #gracz umiera
                if WIZARD_HP == 0:
                    draw_lose_screen('hp')
                    pygame.time.delay(6000)
                    end = True
                    break

                #czy pokój oczysczony z przeciwników
                if len(mobs) == 0:
                    floor_clear = True

                #pojawienie się drzwi dalej
                if floor_clear:
                    #otrzymanie przedmiotu
                    if floor_clear_item and room != 10:
                        if WIZARD_HP <=5:
                            WIZARD_HP += 1
                        if floor == 3 or floor ==6 and WIZARD_HP <=5:
                            WIZARD_HP += 1
                        while True:
                            num = random.randint(1,4)
                            if num == 1 and WIZARD_DMG < 20:
                                text = 'DMG UP'
                                WIZARD_DMG += 2.5
                                break
                            elif num == 2 and FIRING_RATE < 2:
                                text = 'FIRING RATE UP'
                                FIRING_RATE += 0.5
                                break
                            elif num == 3 and MOV_SPEED < 16:
                                text = 'MOVEMENT SPEED UP'
                                MOV_SPEED += 2
                                break
                            elif num == 4:
                                text = 'PROJECTILE SPEED UP'
                                PROJECT_SPEED += 2.5
                                break
                        text = ALA_125.render(text, True, WHITE)
                        WIN.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
                        pygame.display.update()
                        pygame.time.delay(1000)
                        floor_clear_item = False

                    #otworzenie drzwi
                    is_player_in = False   #czy wszedł
                    if floor == 'dungeon':
                        WIN.blit(DOOR,(1640,550))
                        if abs(player.x - 1580) < 25 and abs(player.y -590) < 25:
                            is_player_in = True
                    elif floor == 'yard':
                        WIN.blit(DOOR,(1720,490))
                        if abs(player.x - 1690) < 25 and abs(player.y -510) < 25:
                            is_player_in = True
                    elif floor == 'library' and room != 10:
                        floor_image = LIBRARY_FLOOR_OPEN
                        if abs(player.x - 240) < 20 and abs(player.y -520) < 30:
                            is_player_in = True
                    else:
                        is_player_in = True
                    pygame.display.update()
                    #wejscie w drzwi
                    if is_player_in:
                        #zakończenie
                        if room == 10:
                            text = ALA_200.render('YOU HAVE WON', True, RED)
                            WIN.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
                            pygame.display.update()
                            pygame.time.delay(5000)
                            end = True
                            break
                        else:
                            text = ALA_200.render('ROOM CLEARED', True, WHITE)
                            WIN.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
                            pygame.display.update()
                            pygame.time.delay(1000)
                            room+=1
                            break
            
            
            #licznik pierwszych klatek
            first_frames +=1

        #jeżeli trzeba przerwać obie pętle
        if end:
            break
        
        
#gra uruchamia się tylko gdy włączany jest ten plik
if __name__ == '__main__':
    main()