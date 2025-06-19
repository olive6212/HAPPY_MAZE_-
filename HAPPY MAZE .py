import pygame  # eisagogi vivliothikis
import time
import threading
pygame.init()# initialize = arxikopoiw, ksekina na douleuei to library
width=1000
height=600
screen = pygame.display.set_mode((width,height))  # ftiaxnw tis diastaseis tou parathurou
running = True
running2=False
x=55
y=58
start=time.time()
print(time.time())
timer=0
clock=pygame.time.Clock()
w6_h=100
w14_h=100
w9_h=70
w24_2=382
w14_3=40


def resize():
    global w6_h
    global w14_h
    global w9_h
    global w24_2
    while True: #gia na megalone sinexia
        for i in range (90):
            w6_h +=1  #athzisi megethous
            w14_h +=3
            w9_h +=1
            w24_2 +=1
            time.sleep(0.01)
        for i in range (90):
            w6_h -=1 #miosi megathous
            w14_h -=3
            w9_h -=1
            w24_2 -=1
            time.sleep(0.01)




resize_thread=threading.Thread(target=resize)
resize_thread.daemon=True
resize_thread.start()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_w ]or pressed[pygame.K_UP]:
        y-=5
    if pressed[pygame.K_s]or pressed[pygame.K_DOWN]:
        y+=5
    if pressed[pygame.K_a]or pressed[pygame.K_LEFT]:
        x-=5
    if pressed[pygame.K_d]or pressed[pygame.K_RIGHT]:
        x+=5
    screen.fill((229,135 ,190))#xroma tis othonis
    mouse_pos = pygame.mouse.get_pos()
    player = pygame.draw.rect(screen, (86,251,15), pygame.Rect(x,y, 40,40))
    tap=pygame.draw.rect(screen,(0, 0, 0),pygame.Rect(0,0,width,20))
    tright = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0,0, 20,height))
    tleft= pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(width-20,0,20,height))
    tdown = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0,height-20,width,20))
    finsh=pygame.draw.rect(screen,(90,9,10),pygame.Rect(897,516,90,90))
    w1=pygame.draw.rect(screen,(0,0,0),pygame.Rect(102,14,40,65))
    w2=pygame.draw.rect(screen,(0,0,0),pygame.Rect(130,270,40,150))
    w3=pygame.draw.rect(screen,(0,0,0),pygame.Rect(124,150,650,30))
    w4=pygame.draw.rect(screen,(0,0,0),pygame.Rect(82,344,700,40))
    w5=pygame.draw.rect(screen, (0, 0, 0),pygame.Rect(218,88,40,200))
    w6=pygame.draw.rect(screen,(0,0,0),pygame.Rect(398,15,40,w6_h))
    w7=pygame.draw.rect(screen,(0,0,0),pygame.Rect(463,274,40,100))
    w8=pygame.draw.rect(screen,(0,0,0),pygame.Rect(514,88,40,100))
    w9=pygame.draw.rect(screen,(0,0,0),pygame.Rect(614,20,40,w9_h))
    w10=pygame.draw.rect(screen,(0,0,0),pygame.Rect(719,80,40,100))
    w11=pygame.draw.rect(screen,(0,0,0),pygame.Rect(886,17,40,90))
    w11=pygame.draw.rect(screen,(0,0,0),pygame.Rect(316,257,40,200))
    w12=pygame.draw.rect(screen,(0,0,0),pygame.Rect(590,350,40,100))
    w13=pygame.draw.rect(screen,(0,0,0),pygame.Rect(769,256,250,40))
    w14=pygame.draw.rect(screen,(0,0,0),pygame.Rect(876,268,40,w14_h))
    w15=pygame.draw.rect(screen,(0,0,0),pygame.Rect(902,172,90,40))
    w16=pygame.draw.rect(screen,(0,0,0),pygame.Rect(136,520,40,70))
    w17=pygame.draw.rect(screen,(0,0,0),pygame.Rect(465,270,200,40))
    w18=pygame.draw.rect(screen,(0,0,0),pygame.Rect(679,181,10,37))
    w19=pygame.draw.rect(screen,(0,0,0),pygame.Rect(10,200,60,40))
    w20=pygame.draw.rect(screen,(0,0,0),pygame.Rect(236,620,40,70))
    w21=pygame.draw.rect(screen,(0,0,0),pygame.Rect(465,498,40,90))
    w22=pygame.draw.rect(screen,(0,0,0),pygame.Rect(436,820,40,90))
    w23=pygame.draw.rect(screen,(0,0,0),pygame.Rect(376,502,100,40))
    w24=pygame.draw.rect(screen,(0,0,0),pygame.Rect(720,w24_2,40,100))
    w25=pygame.draw.rect(screen,(0,0,0),pygame.Rect(677,174,40,200))

    if player.colliderect(tap) or player.colliderect(tright) or player.colliderect(tleft) or player.colliderect(tdown) or player.colliderect(w1)or player.colliderect(w2)or player.colliderect(w3)or player.colliderect(w4)or player.colliderect(w5)or player.colliderect(w6)or player.colliderect(w7)or player.colliderect(w8)or player.colliderect(w9)or player.colliderect(w10)or player.colliderect(w11)or player.colliderect(w12) or player.colliderect(w13)or player.colliderect(w14)or player.colliderect(w15)or player.colliderect(w16)or player.colliderect(w17)or player.colliderect(w18)or player.colliderect(w19)or player.colliderect(w20)or player.colliderect(w21)or player.colliderect(w22)or player.colliderect(w23)or player.colliderect(w24)or player.colliderect(w25):


            if pressed[pygame.K_w] or pressed[pygame.K_UP]:
                y += 5
            if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
                y -= 5
            if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
                x += 5
            if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
                x -= 5

    if player.colliderect(finsh):
        x=55
        y=58
        end=time.time()
        timer=round(end-start,2)
        print (timer)
        start=end
        running=False
        running2=True
    font1=pygame.font.SysFont("Tahoma",20,True,True)##typos grammatoseiras, megethos, entona, plagia
    text1 = font1.render("Time:  " + str(timer), True, (0, 0, 0))
    screen.blit(text1, (767, 26))

    font1 = pygame.font.SysFont("Tahoma", 20, True, True)  ##typos grammatoseiras, megethos, entona, plagia
    text2 = font1.render("Time:  " + str(timer), True, (0, 0, 0))
    screen.blit(text2, (767, 26))


    print(mouse_pos)
    pygame.display.flip()
    clock.tick(500)

while running2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running2 = False

    screen.fill((0,0,0))


    font1=pygame.font.SysFont("Tahoma",40,True,True)
    text2 = font1.render("Time:  " + str(timer), True, (21,233,211))
    screen.blit(text2, (345,236))

    font1 = pygame.font.SysFont("Tahoma", 60, True, True)
    text3=font1.render("hi YOU WON :) "+str(),True,(21,233,211))

    screen.blit(text3, (251,354))
    pygame.display.flip()