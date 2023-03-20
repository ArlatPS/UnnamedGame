import pygame

class Hound:
    def __init__(self,x,y):
        self.speed = 2
        self.range = 1000
        self.hp = 20
        self.x = x
        self.y = y
        self.alive = True
        self.turn = 'left'

    def spawn(self,width,height):
        self.rect = pygame.Rect(self.x,self.y,width, height)
    
    #mobs to lista wszystkich kwadratów mobów 
    def move(self,playerx, playery,mobs):
        #usunięcie z listy samego siebie
        mobs_without = []
        for mob in mobs:
            if mob != self:
                mobs_without.append(mob)

        #poruszanie ze zderzeniami
        if abs(playerx - self.x) + abs(playery - self.y) < self.range:
            if abs(playerx - self.x) >= abs(playery - self.y):
                if playerx <= self.x:
                    can_move = True
                    self.rect.x -= self.speed
                    for mob in mobs_without:
                        if mob.rect.colliderect(self.rect):
                            can_move = False
                    self.rect.x += self.speed
                    if can_move:
                        self.x -= self.speed
                        self.rect.x -= self.speed
                        self.turn = 'left'
                else:
                    can_move = True
                    self.rect.x += self.speed
                    for mob in mobs_without:
                        if mob.rect.colliderect(self.rect):
                            can_move = False
                    self.rect.x -= self.speed
                    if can_move:
                        self.x += self.speed
                        self.rect.x += self.speed
                        self.turn = 'right'
            else:
                if playery <= self.y:
                    can_move = True
                    self.rect.y -= self.speed
                    for mob in mobs_without:
                        if mob.rect.colliderect(self.rect):
                            can_move = False
                    self.rect.y += self.speed
                    if can_move:
                        self.y -= self.speed
                        self.rect.y -= self.speed
                else:
                    can_move = True
                    self.rect.y += self.speed
                    for mob in mobs_without:
                        if mob.rect.colliderect(self.rect):
                            can_move = False
                    self.rect.y -= self.speed
                    if can_move:
                        self.y += self.speed
                        self.rect.y += self.speed
    def hurt(self,dmg):
        self.hp -= dmg

class SkeleWiz:
    def __init__(self,x,y):
        self.speed = 1
        self.range = 1500
        self.project_speed = 15
        self.hp = 15
        self.x = x
        self.y = y
        self.alive = True
        self.turn = 'left'
        self.cooldown = 30
        self.cooldown_add = 121

    def spawn(self,width,height):
        self.rect = pygame.Rect(self.x,self.y,width+5, height+5)

    def move(self,playery,mobs):
        mobs_without = []
        for mob in mobs:
            if mob != self:
                mobs_without.append(mob)

        if playery != self.y:
            if playery < self.y:
                can_move = True
                self.rect.y -= self.speed
                for mob in mobs_without:
                    if mob.rect.colliderect(self.rect):
                        can_move = False
                self.rect.y += self.speed
                if can_move:
                    self.y -= self.speed
                    self.rect.y -= self.speed
            else:
                can_move = True
                self.rect.y -= self.speed
                for mob in mobs_without:
                    if mob.rect.colliderect(self.rect):
                        can_move = False
                self.rect.y += self.speed
                if can_move:
                    self.y += self.speed
                    self.rect.y += self.speed


    
    def shoot(self,playerx,playery,enemy_project):
        if abs(playerx - self.x) + abs(playery - self.y) < self.range:
            if abs(playerx - self.x) >= abs(playery - self.y):
                if playerx <= self.x:
                    enemy_project.append([self.x,self.y,'a',self.project_speed])
                    self.turn = 'left'
                else:
                    enemy_project.append([self.x,self.y,'d',self.project_speed])
                    self.turn = 'right'
            else:
                if playery <= self.y:
                    enemy_project.append([self.x,self.y,'w',self.project_speed])
                else:
                    enemy_project.append([self.x,self.y,'s',self.project_speed])



    def hurt(self,dmg):
        self.hp -= dmg

class Knight:
    def __init__(self,x,y):
        self.speed = 2
        self.range = 2000
        self.hp = 40
        self.x = x
        self.y = y
        self.alive = True
        self.turn = 'left'

    def spawn(self,width,height):
        self.rect = pygame.Rect(self.x,self.y,width, height)
    
    #mobs to lista wszystkich kwadratów mobów 
    def move(self,playerx, playery,mobs):
        #usunięcie z listy samego siebie
        mobs_without = []
        for mob in mobs:
            if mob != self:
                mobs_without.append(mob)

        #poruszanie ze zderzeniami
        if abs(playerx - self.x) + abs(playery - self.y) < self.range:
            if abs(playerx - self.x) >= abs(playery - self.y):
                if playerx <= self.x:
                    can_move = True
                    self.rect.x -= self.speed
                    for mob in mobs_without:
                        if mob.rect.colliderect(self.rect):
                            can_move = False
                    self.rect.x += self.speed
                    if can_move:
                        self.x -= self.speed
                        self.rect.x -= self.speed
                        self.turn = 'left'
                else:
                    can_move = True
                    self.rect.x += self.speed
                    for mob in mobs_without:
                        if mob.rect.colliderect(self.rect):
                            can_move = False
                    self.rect.x -= self.speed
                    if can_move:
                        self.x += self.speed
                        self.rect.x += self.speed
                        self.turn = 'right'
            else:
                if playery <= self.y:
                    can_move = True
                    self.rect.y -= self.speed
                    for mob in mobs_without:
                        if mob.rect.colliderect(self.rect):
                            can_move = False
                    self.rect.y += self.speed
                    if can_move:
                        self.y -= self.speed
                        self.rect.y -= self.speed
                else:
                    can_move = True
                    self.rect.y += self.speed
                    for mob in mobs_without:
                        if mob.rect.colliderect(self.rect):
                            can_move = False
                    self.rect.y -= self.speed
                    if can_move:
                        self.y += self.speed
                        self.rect.y += self.speed
    def hurt(self,dmg):
        self.hp -= dmg

class Phantom:
    def __init__(self,x,y):
        self.speed = 3
        self.range = 1200
        self.hp = 25
        self.x = x
        self.y = y
        self.alive = True
        self.turn = 'left'

    def spawn(self,width,height):
        self.rect = pygame.Rect(self.x,self.y,width, height)
    
    #mobs to lista wszystkich kwadratów mobów 
    def move(self,playerx, playery,mobs):
        #usunięcie z listy samego siebie
        mobs_without = []
        for mob in mobs:
            if mob != self:
                mobs_without.append(mob)

        #poruszanie ze zderzeniami
        if abs(playerx - self.x) + abs(playery - self.y) < self.range:
            if abs(playerx - self.x) >= abs(playery - self.y):
                if playerx <= self.x:
                    can_move = True
                    self.rect.x -= self.speed
                    for mob in mobs_without:
                        if mob.rect.colliderect(self.rect):
                            can_move = False
                    self.rect.x += self.speed
                    if can_move:
                        self.x -= self.speed
                        self.rect.x -= self.speed
                        self.turn = 'left'
                else:
                    can_move = True
                    self.rect.x += self.speed
                    for mob in mobs_without:
                        if mob.rect.colliderect(self.rect):
                            can_move = False
                    self.rect.x -= self.speed
                    if can_move:
                        self.x += self.speed
                        self.rect.x += self.speed
                        self.turn = 'right'
            else:
                if playery <= self.y:
                    can_move = True
                    self.rect.y -= self.speed
                    for mob in mobs_without:
                        if mob.rect.colliderect(self.rect):
                            can_move = False
                    self.rect.y += self.speed
                    if can_move:
                        self.y -= self.speed
                        self.rect.y -= self.speed
                else:
                    can_move = True
                    self.rect.y += self.speed
                    for mob in mobs_without:
                        if mob.rect.colliderect(self.rect):
                            can_move = False
                    self.rect.y -= self.speed
                    if can_move:
                        self.y += self.speed
                        self.rect.y += self.speed
    def hurt(self,dmg):
        self.hp -= dmg

class Bat:
    def __init__(self,x,y):
        self.speed = 7
        self.range = 6000
        self.hp = 15
        self.x = x
        self.y = y
        self.alive = True
        self.turn = 'right'

    def spawn(self,width,height):
        self.rect = pygame.Rect(self.x,self.y,width, height)
    
    #mobs to lista wszystkich kwadratów mobów 
    def move(self,playerx, playery,mobs):
        #usunięcie z listy samego siebie
        mobs_without = []
        for mob in mobs:
            if mob != self:
                mobs_without.append(mob)

        #poruszanie ze zderzeniami
        if abs(playerx - self.x) + abs(playery - self.y) < self.range:
            if abs(playerx - self.x) >= abs(playery - self.y):
                if playerx <= self.x:
                    can_move = True
                    self.rect.x -= self.speed
                    for mob in mobs_without:
                        if mob.rect.colliderect(self.rect):
                            can_move = False
                    self.rect.x += self.speed
                    if can_move:
                        self.x -= self.speed
                        self.rect.x -= self.speed
                        self.turn = 'left'
                else:
                    can_move = True
                    self.rect.x += self.speed
                    for mob in mobs_without:
                        if mob.rect.colliderect(self.rect):
                            can_move = False
                    self.rect.x -= self.speed
                    if can_move:
                        self.x += self.speed
                        self.rect.x += self.speed
                        self.turn = 'right'
            else:
                if playery <= self.y:
                    can_move = True
                    self.rect.y -= self.speed
                    for mob in mobs_without:
                        if mob.rect.colliderect(self.rect):
                            can_move = False
                    self.rect.y += self.speed
                    if can_move:
                        self.y -= self.speed
                        self.rect.y -= self.speed
                else:
                    can_move = True
                    self.rect.y += self.speed
                    for mob in mobs_without:
                        if mob.rect.colliderect(self.rect):
                            can_move = False
                    self.rect.y -= self.speed
                    if can_move:
                        self.y += self.speed
                        self.rect.y += self.speed
    def hurt(self,dmg):
        self.hp -= dmg

class Automaton:
    def __init__(self,x,y):
        self.speed = 5
        self.range = 6000
        self.hp = 100
        self.x = x
        self.y = y
        self.alive = True
        self.turn = 'right'
        self.shoot_dir = 'right'
        self.distance = 300
        self.shot_range = 600
        self.shooting = False
        self.pre_shooting = False
        self.cooldown = 20
        self.cooldown_value = 120
        self.pre_time = 60
        self.shooting_time = 60
        self.laserx = 0
        self.lasery = 0
    
    def spawn(self,width,height):
        self.rect = pygame.Rect(self.x,self.y,width, height)
    
    def move(self,playerx, playery,mobs):
        #usunięcie z listy samego siebie
        mobs_without = []
        for mob in mobs:
            if mob != self:
                mobs_without.append(mob)

        #poruszanie ze zderzeniami
        if abs(playerx - self.x) + abs(playery - self.y) < self.range:
            if abs(playerx - self.x) >= abs(playery - self.y) and abs(playerx - self.x) > self.distance and not self.shooting:
                if playerx <= self.x:
                    can_move = True
                    self.rect.x -= self.speed
                    for mob in mobs_without:
                        if mob.rect.colliderect(self.rect):
                            can_move = False
                    self.rect.x += self.speed
                    if can_move:
                        self.x -= self.speed
                        self.rect.x -= self.speed
                else:
                    can_move = True
                    self.rect.x += self.speed
                    for mob in mobs_without:
                        if mob.rect.colliderect(self.rect):
                            can_move = False
                    self.rect.x -= self.speed
                    if can_move:
                        self.x += self.speed
                        self.rect.x += self.speed
            elif abs(playery - self.y) > 10: # warunek powoduje że się nie trzęsie
                if playery <= self.y:
                    can_move = True
                    self.rect.y -= self.speed
                    for mob in mobs_without:
                        if mob.rect.colliderect(self.rect):
                            can_move = False
                    self.rect.y += self.speed
                    if can_move:
                        self.y -= self.speed
                        self.rect.y -= self.speed
                else:
                    can_move = True
                    self.rect.y += self.speed
                    for mob in mobs_without:
                        if mob.rect.colliderect(self.rect):
                            can_move = False
                    self.rect.y -= self.speed
                    if can_move:
                        self.y += self.speed
                        self.rect.y += self.speed
            
        #obrócony do gracza
        if not (self.shooting or self.pre_shooting):
            if playerx >= self.x:
                self.turn = 'right'
            else:
                self.turn = 'left'

    def hurt(self,dmg):
        self.hp -= dmg
