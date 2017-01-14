from pygame import display as pantalla, init as pyinit
from pygame import font,Surface,transform,event, quit as pyquit, Rect
from pygame import QUIT, KEYDOWN, K_RIGHT, K_LEFT, K_ESCAPE, key
import sys


pyinit()
blanco = 255,255,255
negro = 0,0,0

top = 0
left = 0
right = 0
bottom = 0
cw = ['north','east','south','west']
idx = 0

fondo=pantalla.set_mode((250,250))
frect = Rect(0,0,200,200)
fuente = font.SysFont('verdana',30)

img = Surface((200,200))
img.fill(blanco)
rect = img.get_rect(center=frect.center)

render= fuente.render('0',1,negro,blanco)
r = render.get_rect()
img.blit(render,(0,0))

render= fuente.render('1',1,negro,blanco)
r = render.get_rect()
img.blit(render,(rect.w-r.w,0))

render= fuente.render('2',1,negro,blanco)
r = render.get_rect()
img.blit(render,(0,rect.h-r.h))

render= fuente.render('3',1,negro,blanco)
r = render.get_rect()
img.blit(render,(rect.w-r.w,rect.h-r.h))
x,y = 0,0


d = 90
while True:
    #fondo.fill(negro)
    for e in event.get():
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                pyquit()
                sys.exit()
            elif e.key == K_RIGHT:
                angle = d
            elif e.key == K_LEFT:
                angle = -d
                # idx += 1
                # if idx > len(cw)-1:
                    # idx = 0
                # rosa = fuente.render(cw[idx],1,negro,blanco)
                # if cw[idx] == 'north':
                    # y,x = top,left
                # elif cw[idx] == 'west':
                    # y,x = bottom,left
                # elif cw[idx] == 'south':
                    # y,x = bottom,right
                # elif cw[idx] == 'east':
                    # y,x = top,right
                    
                    
                #rrect = rosa.get_rect(center = (50,50))
            img = transform.rotate(img,angle)
                #img.blit(rosa,rrect)

    fondo.blit(img,(25,25))
    pantalla.flip()


