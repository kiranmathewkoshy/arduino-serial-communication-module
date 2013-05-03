import pygame, sys
import serial
import time
from pygame.locals import *
k1=0
k2=0
k3=0
k4=0
ksp=0
p1=0
p2=0
p3=0
p4=0
psp=0

#COM port to which the arduino connects.
port=5


v='k'
print "Initialising System..."
pygame.init()
font = pygame.font.SysFont("calibri",18)
text1=font.render(str("Programmed by Kiran Mathew Koshy"),True,(255,0,0))
text2=font.render(str("Serial Communication Module"),True,(0,255,0))
text3=font.render(str("Frame Rate: 100"),True,(255,255,0))
text4=font.render(str("Serial data: ON"),True,(255,255,0))
text5=font.render(str("Port : COM "+str(port)),True,(255,255,0))
SIZE = (800,600)
BG_COLOUR = (0, 0, 0)
NORMAL_COLOR=(0,255,0)
SELECT_COLOR=(255,0,0)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Serial Communication Module by Kiran Mathew Koshy")
clock = pygame.time.Clock()
print "Attempting to connect to Arduino via COM "+str(port)
try:
	ser = serial.Serial(port-1, timeout=1)
	ser.setRTS(True)
	ser.setRTS(False)
	print "connrcting.."
except :
	print "Error opening COM Port"
	print "All Serial Communications are now disabled."
	text4=font.render(str("Serial Data: OFF"),True,(255,255,0))
	sys.exit()
def round_rect(screen,color,x,y,xh,yh,radius):
	pygame.draw.circle(screen,color,(x+radius,y+radius),radius,0)
	pygame.draw.rect(screen,color,pygame.Rect(x+radius,y,xh-(2*radius),radius))
	pygame.draw.circle(screen,color,(x+xh-radius,y+radius),radius,0)
	pygame.draw.rect(screen,color,pygame.Rect(x,y+radius,radius,yh-(2*radius)))
	pygame.draw.rect(screen,color,pygame.Rect(x+radius,y+radius,xh-(2*radius),yh-(2*radius)))
	pygame.draw.rect(screen,color,pygame.Rect(x+xh-radius,y+radius,radius,yh-(2*radius)))
	pygame.draw.circle(screen,color,(x+radius,y+yh-radius),radius,0)
	pygame.draw.rect(screen,color,pygame.Rect(x+radius,y+yh-radius,xh-(2*radius),radius))
	pygame.draw.circle(screen,color,(x+xh-radius,y+yh-radius),radius,0)
	
def draw():
    screen.fill(BG_COLOUR)
    screen.blit(text1,(40,120))
    screen.blit(text2,(250,10))
    screen.blit(text3,(40,90))
    screen.blit(text4,(40,30))
    screen.blit(text5,(40,60))
    screen.blit(text6,(40,180))
    rad=7
    round_rect(screen,NORMAL_COLOR,680,400,50,50,rad) #k1
    round_rect(screen,NORMAL_COLOR,680,460,50,50,rad) #k3
    round_rect(screen,NORMAL_COLOR,620,460,50,50,rad) #k4
    round_rect(screen,NORMAL_COLOR,740,460,50,50,rad) #k2
    round_rect(screen,NORMAL_COLOR,300,460,200,50,rad) #ksp
    if k4==1:
        round_rect(screen,SELECT_COLOR,620,460,50,50,rad) #k4
        ser.write('d')
    if k1==1:
        round_rect(screen,SELECT_COLOR,680,400,50,50,rad) #k1
        ser.write('a')
    if k2==1:
        round_rect(screen,SELECT_COLOR,740,460,50,50,rad) #k2
        ser.write('b')
    if k3==1:
        round_rect(screen,SELECT_COLOR,680,460,50,50,rad) #k3
        ser.write('c')
    if ksp==1:
        round_rect(screen,SELECT_COLOR,300,460,200,50,rad) #ksp
        ser.write('a')
    pygame.display.flip()
def run_game():
    global k1
    global k2
    global k3
    global k4
    global ksp
    global p1
    global p2
    global p3
    global p4
    global psp
    global v
    draw()
    while True:
        time_passed = clock.tick(100)
        pygame.event.pump()
        v=ser.readline(1)
        if(v=='f'):
            pygame.mixer.music.play()
            time.delay(2)
            pygame.mixer.music.pause()
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            k4=1
        else:
            k4=0
        if key[pygame.K_UP]:
            k1=1
        else:
            k1=0
        if key[pygame.K_RIGHT]:
            k2=1
        else:
            k2=0
        if key[pygame.K_DOWN]:
            k3=1
        else:
            k3=0
        if key[pygame.K_SPACE]:
            ksp=1
        else:
            ksp=0
        if key[pygame.K_ESCAPE]:
			sys.exit()
        if k1!=p1 or k2!=p2 or k3!=p3 or k4!=p4 or ksp!=psp:
            draw()
        p1=k1
        p2=k2
        p3=k3
        p4=k4
        psp=ksp
def exit_game():
    sys.exit()

if __name__ == "__main__":
    run_game()
