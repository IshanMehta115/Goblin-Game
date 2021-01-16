import pygame
pygame.mixer.init(22050, -16, 2, 64)
pygame.init()
pygame.mixer.init() 
import math
import random
import os
##################################Constants
screenWidth=850
screenHeight=500
enemyTime=0
window=pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("character_animation")
acceleration=5
bg=pygame.image.load(os.path.join(os.path.dirname(__file__),'pics/bg.jpg'))

bulletSound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__),'pics/Gun+Silencer.wav'))
hitSound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__),'pics/sound100.wav'))
bgmusic = pygame.mixer.music.load(os.path.join(os.path.dirname(__file__),'pics/music.mp3'))
jumpSound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__),"pics/456373__felixyadomi__hop9.wav"))
bombSound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__),'pics/bomb.wav'))
pygame.mixer.music.play(-1)
##################################
#
##################################Player
class player:
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=5
        self.walkLeft=[]
        self.walkRight=[]
        self.standing=[]
        self.left=False
        self.right=True
        self.inJump=False
        self.walkCount=0
        self.standing=True
        self.health=100
        self.hitbox=(self.x+20,self.y+16,20,48)
        self.ammo=7
        self.reloadTime=0
        self.bombTime=0
        self.bonusTime=0
        self.bonus=''
        self.score=0
        for i in range(9):
            self.walkLeft.append(pygame.image.load(os.path.join(os.path.dirname(__file__),'pics/L'+str(i+1)+'.png')))
            self.walkRight.append(pygame.image.load(os.path.join(os.path.dirname(__file__),'pics/R'+str(i+1)+'.png')))
            self.stand=pygame.image.load(os.path.join(os.path.dirname(__file__),'pics/standing.png'))
    def draw(self,window):
        if(not self.standing):
            if(self.left):
                window.blit(self.walkLeft[self.walkCount//3],(self.x,self.y))
            elif(self.right):
                window.blit(self.walkRight[self.walkCount//3],(self.x,self.y))
        else:
            if(self.left):
                window.blit(self.walkLeft[self.walkCount//3],(self.x,self.y))
            elif(self.right):
                window.blit(self.walkRight[self.walkCount//3],(self.x,self.y))
        self.hitbox=(self.x+20,self.y+16,20,48)
        pygame.draw.rect(window,(0,0,0),(47,47,406,26))
        pygame.draw.rect(window,(255,0,0),(50,50,400,20))
        pygame.draw.rect(window,(0,255,0),(50,50,4*self.health,20))
        if(self.reloadTime==0):
            pygame.draw.rect(window,(0,0,0),(47,80,87,15))
            pygame.draw.rect(window,(255,0,0),(47,83,3+self.ammo*(12),9))
            x=47
            for i in range(8):
                pygame.draw.rect(window,(0,0,0),(x,80,3,15))
                x+=12
        else:
            self.reloadTime-=1
            self.ammo=(70-self.reloadTime)//10
            pygame.draw.rect(window,(0,0,0),(47,80,87,15))
            pygame.draw.rect(window,(255,0,0),(47,83,3+self.ammo*(12),9))
            x=47
            for i in range(8):
                pygame.draw.rect(window,(0,0,0),(x,80,3,15))
                x+=12
        pygame.draw.rect(window,(0,0,0),(47,92,87,15))
        pygame.draw.rect(window,(255,0,0),(50,95,(1000-self.bombTime)*(81/1000),9))
        if(p.bonusTime>0):
            bonusText=fontEndGame.render(self.bonusText,1,(255,0,0))
            window.blit(bonusText,(screenWidth//2-bonusText.get_width()//2,screenHeight//2-bonusText.get_height()//2))
        #pygame.draw.rect(window,(255,0,0),self.hitbox,2)
    def attacked(self):
        if(self.health>0):
            self.health-=1
        if(self.health==0):
            global run
            run = False

##################################
#
##################################Plasma
time=0
class plasmaBall:
    def __init__(self,x,y,color,radius,facing):
        self.x=x
        self.y=y
        self.color=color
        self.radius=radius
        self.facing=facing
        self.vel=8*self.facing
    def draw(self,window):
        delta=math.sin(self.x)
        delta=delta**2
        delta*=255
        self.color=(255-delta,255-delta,255)
        pygame.draw.circle(window,self.color,(self.x,self.y),self.radius)

##################################
#
##################################Enemy
class enemy:
    def __init__(self,x,y,width,height,leftLimit,rightLimit):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=3
        self.walkLeft=[]
        self.walkRight=[]
        self.inJump=False
        self.walkCount=0
        self.standing=True
        self.leftLimit=leftLimit
        self.rightLimit=rightLimit
        self.hitbox=(self.x,self.y,64,64)
        self.health=10
        self.visible=True
        for i in range(11):
            self.walkLeft.append(pygame.image.load(os.path.join(os.path.dirname(__file__),'pics/L'+str(i+1)+'E.png')))
            self.walkRight.append(pygame.image.load(os.path.join(os.path.dirname(__file__),'pics/R'+str(i+1)+'E.png')))
            #self.stand=pygame.image.load('pics/standing.png')
    def draw(self,window):
        if(self.visible):
            if(self.vel<0):
                window.blit(self.walkLeft[self.walkCount//3],(self.x,self.y))
                self.hitbox=(self.x+30,self.y,20,64)
            else:
                window.blit(self.walkRight[self.walkCount//3],(self.x,self.y))
                self.hitbox=(self.x+20,self.y,20,64)
            pygame.draw.rect(window,(0,0,0),(self.hitbox[0]-18,self.hitbox[1]-23,56,16))
            pygame.draw.rect(window,(255,0,0),(self.hitbox[0]-15,self.hitbox[1]-20,50,10))
            pygame.draw.rect(window,(0,255,0),(self.hitbox[0]-15,self.hitbox[1]-20,5*self.health,10))
        #pygame.draw.rect(window,(255,0,0),self.hitbox,2)
    def hit(self):
        hitSound.play()
        p.score+=1
        if(self.health>0):
            self.health-=1
        if(self.health==0):
            self.visible=False
        #print(self.health)
##################################
#
##################################healthBox
class healthBox:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.pic=pygame.image.load(os.path.join(os.path.dirname(__file__),'pics/healthbox.png'))
        self.picked=False
        self.hitbox=(self.x,self.y,64,64)
        self.time = 600
    def draw(self,window):
        window.blit(self.pic,(self.x,self.y))
            #pygame.draw.rect(window,(255,0,0),(self.x,self.y,64,64))
##################################
#
run=True
clock=pygame.time.Clock()
p=player(100,screenHeight-128,64,64)
verVel=0
initY=p.y
bullets = []
enemies = []
#enemies.append(enemy(200,screenHeight-128,64,64,50,screenWidth-50-64))
font=pygame.font.SysFont('comicsans',30,True,True)
fontEndGame=pygame.font.SysFont('comicsans',100,True,True)
h=healthBox(-100,screenHeight-128)
def changeHeight():
    global p
    global verVel
    global initY
    p.y-=verVel
    verVel-=acceleration
    if(verVel<-30):
        p.y=initY
        p.inJump=False
        verVel=0
def draw():
    window.blit(bg,(0,0))
    p.draw(window)
    h.draw(window)
    for e in enemies:
        e.draw(window)
    text = font.render('score: '+str(p.score),1,(0,0,0))
    window.blit(text,(screenWidth-text.get_width()-20,10))
    for bullet in bullets:
        bullet.draw(window)
    pygame.display.update()
def touch(bullet,enemy):
    if bullet.x+bullet.radius>enemy.hitbox[0] and bullet.x-bullet.radius<enemy.hitbox[0]+enemy.hitbox[2]:
        if bullet.y+bullet.radius>enemy.hitbox[1] and bullet.y-bullet.radius<enemy.hitbox[1]+enemy.hitbox[3]:
            return True
    return False













while(run):
    #print(p.health)
    clock.tick(27)
    enemyTime=max(0,enemyTime-1)
    time=max(time-1,0)
    p.bombTime=max(p.bombTime-1,0)
    p.bonusTime=max(p.bonusTime-1,0)
    h.time=max(0,h.time-1)
    isPlayerAttacked=False
    if(enemyTime==0):
        enemies.append(enemy(random.randint(20,screenWidth-134),screenHeight-128,64,64,10,screenWidth-10-64))
        enemies[len(enemies)-1].vel=random.randint(0,1)
        enemies[len(enemies)-1].vel*=2
        enemies[len(enemies)-1].vel-=1
        enemies[len(enemies)-1].vel*=3
        enemyTime=150
    if h.time==0:
        h=healthBox(random.randint(10,screenWidth-64-10),screenHeight-128)
    for e in enemies:
        if p.hitbox[0]+p.hitbox[2]>e.hitbox[0] and p.hitbox[0]<e.hitbox[0]+e.hitbox[2]:
            if p.hitbox[1]+p.hitbox[3]>e.hitbox[1] and p.hitbox[1]<e.hitbox[1]+e.hitbox[3]:
                isPlayerAttacked=True
                if(run==False):
                    break
    if isPlayerAttacked:
        p.attacked()
        pass
    for events in pygame.event.get():
        if(events.type==pygame.QUIT):
            run=False
    keys=pygame.key.get_pressed()
    if(keys[pygame.K_SPACE]):
        if(p.left):
            facing=-1
        else:
            facing=1
        if(p.reloadTime==0 and p.ammo>0 and len(bullets)<10 and time==0):
            p.ammo-=1
            if(p.ammo==0):
                p.reloadTime=70
            time=10
            bulletSound.play()
            bullets.append(plasmaBall(int(p.x+p.width/2),int(p.y+p.width/2),(0,0,0),5,facing))
    for bullet in bullets:
        temp = bullet
        if 0<temp.x<screenWidth:
            for e in enemies:
                    if(touch(temp,e)):
                        e.hit()
                        if(temp in bullets):
                            bullets.pop(bullets.index(bullet))
                        if(e.visible==False):
                            enemies.pop(enemies.index(e))
            if(bullet in bullets):
                bullet.x+=bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    if(keys[pygame.K_q]):
        run=False
    if(keys[pygame.K_LEFT]):
        p.x=max(0,p.x-p.vel)
        if(p.right):
            p.walkCount=0
        p.left=True
        p.right=False
        p.standing=False
        p.walkCount=(p.walkCount+1)%27
    elif(keys[pygame.K_RIGHT]):
        p.x=min(screenWidth-p.width,p.x+p.vel)
        if(p.left):
            p.walkCount=0
        p.left=False
        p.right=True
        p.standing=False
        p.walkCount=(p.walkCount+1)%27
    else:
        p.standing=True
        p.walkCount=0
    if(keys[pygame.K_UP] and not p.inJump):
        p.inJump=True
        verVel=30
        initY=p.y
        #p.left=False
        #p.Right=False
        jumpSound.play()
    if(p.inJump):
        changeHeight()
    for e in enemies:
        if(e.vel>0):
            if(e.x+e.vel<e.rightLimit):
                e.x+=e.vel
            else:
                e.vel*=-1
        else:
            if(e.x+e.vel>e.leftLimit):
                e.x+=e.vel
            else:
                e.vel*=-1
        e.walkCount=(e.walkCount+1)%33
    if(keys[pygame.K_2] and p.bombTime==0):
        delta=len(enemies)
        enemies=[]
        enemyTime=50
        bombSound.play()
        p.bombTime=1000
        if(delta>0):
            p.bonusTime=50
            p.bonusText='+'+str(delta*10)
            p.score+=delta*10
    if(keys[pygame.K_r]):
        p.reloadTime=10*(7-p.ammo)
    if p.hitbox[0]+p.hitbox[2]>h.hitbox[0] and p.hitbox[0]<h.hitbox[0]+h.hitbox[2]:
            if p.hitbox[1]+p.hitbox[3]>h.hitbox[1] and p.hitbox[1]<h.hitbox[1]+h.hitbox[3]:
                if p.health<100:
                    p.health=min(p.health+10,100)
                    h=healthBox(-100,screenHeight-128)
                
    draw()
textEndGame=fontEndGame.render('You Lost',1,(0,0,0))
window.blit(textEndGame,(screenWidth//2-textEndGame.get_width()//2,screenHeight//2-textEndGame.get_height()//2))
fontScore=pygame.font.SysFont('comicsans',40,True,True)
textScore=fontScore.render('Your score: '+str(p.score),1,(0,0,0))
window.blit(textScore,((screenWidth//2-textScore.get_width()//2,screenHeight//2+textEndGame.get_height()//2)))
pygame.display.update()
pygame.time.delay(3000)
pygame.quit()
