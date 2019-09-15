import pygame
from pygame.locals import *
import cv2
import numpy as np
import sys

#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
camera = cv2.VideoCapture(0)
pygame.init()
pygame.display.set_caption("OpenCV camera stream on Pygame")
screen = pygame.display.set_mode([960,720])
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 17.0, (960,720))
#camera = cv2.VideoCapture("udp://@0.0.0.0:11111?overrun_nonfatal=1&fifo_size=500000")
###
###img = cv2.cvtColor(frame,cv2.COLOR_BGR2Lab)
#img = cv2.cvtColor(frame,cv2.COLOR_BGR2XYZ)
try:	
 while True:
            button01 = pygame.image.load("button01.png")            
            head1 = pygame.image.load("HUD.png")
            ret, frame = camera.read()
            screen.fill([0,0,0])
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = np.rot90(frame)
            frame = cv2.flip(frame,0)            
            frame = pygame.surfarray.make_surface(frame)
            screen.blit(frame, (0,0))
            screen.blit(head1,(10,75))
            #ret, frame = camera.read() 
            #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)           
            #frame = cv2.flip(frame,90)
            #out.write(frame)
            #cv2.imshow('frame',frame)
            screen.blit(button01,(100,10))            
            screen.blit(button01,(250,10))            
            screen.blit(button01,(400,10))
            pygame.display.update()
            
            for event in pygame.event.get():
                            if event.type == KEYDOWN:
                               if event.key == pygame.K_LSHIFT:
                                  a = True
                                  while a:
                                         head1 = pygame.image.load("2.png")
                                         ret, frame = camera.read()
                                         screen.fill([0,0,0])
                                         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                                         frame = np.rot90(frame)
                                         frame = pygame.surfarray.make_surface(frame)
                                         screen.blit(frame, (0,0))
                                         screen.blit(head1,(10,75))
                                         pygame.display.update()
                                         for event in pygame.event.get():
                                                         if event.type == KEYDOWN:
                                                               if event.key == pygame.K_LCTRL:
                                                                  a = False
                                                               if event.key == pygame.K_ESCAPE:
                                                                  sys.exit(0)                            
                                                               if event.key == pygame.K_LSHIFT:
                                                                  b = True
                                                                  while b:
                                                                          ret, frame = camera.read()
                                                                          screen.fill([0,0,0])
                                                                          frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                                                                          frame = np.rot90(frame)
                                                                          frame = pygame.surfarray.make_surface(frame)
                                                                          screen.blit(frame, (0,0))
                                                                          pygame.display.update()
                                                                          for event in pygame.event.get():
                                                                                          if event.type == KEYDOWN:
                                                                                             if event.key == pygame.K_LCTRL:
                                                                                                b = False
                                                                                             if event.key == pygame.K_ESCAPE:
                                                                                                sys.exit(0)
                                                                                             if event.key == pygame.K_LSHIFT:
                                                                                                c = True
                                                                                                while c:
                                                                                                           ret, frame = camera.read()
                                                                                                           screen.fill([0,0,0])
                                                                                                           frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
                                                                                                           frame = np.rot90(frame)
                                                                                                           frame = pygame.surfarray.make_surface(frame)
                                                                                                           screen.blit(frame, (0,0))
                                                                                                           pygame.display.update()
                                                                                                           for event in pygame.event.get():
                                                                                                                           if event.type == KEYDOWN:
                                                                                                                              if event.key == pygame.K_LCTRL:
                                                                                                                                 c = False
                                                                                                                              if event.key == pygame.K_ESCAPE:
                                                                                                                                 sys.exit(0)              
                                                                                                                              if event.key == pygame.K_LSHIFT:
                                                                                                                                 d = True
                                                                                                                                 while d:
                                                                                                                                            ret, frame = camera.read()
                                                                                                                                            screen.fill([0,0,0])
                                                                                                                                            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                                                                                                                                            invert = cv2.bitwise_not(frame)
                                                                                                                                            invert = np.rot90(invert)
                                                                                                                                            invert = pygame.surfarray.make_surface(invert)
                                                                                                                                            screen.blit(invert, (0,0))
                                                                                                                                            pygame.display.update()
                                                                                                                                            for event in pygame.event.get():
                                                                                                                                                            if event.type == KEYDOWN:
                                                                                                                                                               if event.key == pygame.K_LCTRL:
                                                                                                                                                                  d = False
                                                                                                                                                               if event.key == pygame.K_ESCAPE:
                                                                                                                                                                  sys.exit(0)
                                                                                                                                                               if event.key == pygame.K_LSHIFT:
                                                                                                                                                                  e = True
                                                                                                                                                                  while e:
                                                                                                                                                                             ret, frame = camera.read()
                                                                                                                                                                             screen.fill([0,0,0])
                                                                                                                                                                             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                                                                                                                                                                             invert = cv2.bitwise_not(frame)
                                                                                                                                                                             invert = np.rot90(invert)
                                                                                                                                                                             invert = pygame.surfarray.make_surface(invert)
                                                                                                                                                                             screen.blit(invert, (0,0))
                                                                                                                                                                             pygame.display.update()
                                                                                                                                                                             for event in pygame.event.get():
                                                                                                                                                                                             if event.type == KEYDOWN:
                                                                                                                                                                                                if event.key == pygame.K_LCTRL:
                                                                                                                                                                                                   e = False
                                                                                                                                                                                                if event.key == pygame.K_ESCAPE:
                                                                                                                                                                                                   sys.exit(0)
                                                                                                                                                                                                if event.key == pygame.K_LSHIFT:
                                                                                                                                                                                                   f = True
                                                                                                                                                                                                   while f:
                                                                                                                                                                                                              ret, frame = camera.read()
                                                                                                                                                                                                              screen.fill([0,0,0])
                                                                                                                                                                                                              frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                                                                                                                                                                                                              invert = cv2.bitwise_not(frame)
                                                                                                                                                                                                              invert = np.rot90(invert)
                                                                                                                                                                                                              invert = pygame.surfarray.make_surface(invert)
                                                                                                                                                                                                              screen.blit(invert, (0,0))
                                                                                                                                                                                                              pygame.display.update()
                                                                                                                                                                                                              for event in pygame.event.get():
                                                                                                                                                                                                                              if event.type == KEYDOWN:
                                                                                                                                                                                                                                 if event.key == pygame.K_LCTRL:
                                                                                                                                                                                                                                    f = False
                                                                                                                                                                                                                                 if event.key == pygame.K_ESCAPE:
                                                                                                                                                                                                                                    sys.exit(0)                                                                                                                                                        
                                                                                                                                                                                                                                 if event.key == pygame.K_LSHIFT:
                                                                                                                                                                                                                                    g = True
                                                                                                                                                                                                                                    while g:
                                                                                                                                                                                                                                               ret, frame = camera.read()
                                                                                                                                                                                                                                               screen.fill([0,0,0])
                                                                                                                                                                                                                                               frame = cv2.GaussianBlur(frame, (7, 7), 5.64)
                                                                                                                                                                                                                                               frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                                                                                                                                                                                                                                               frame = cv2.Canny(frame, 25, 75)
                                                                                                                                                                                                                                               frame = np.rot90(frame)
                                                                                                                                                                                                                                               frame = pygame.surfarray.make_surface(frame)
                                                                                                                                                                                                                                               screen.blit(frame, (0,0))
                                                                                                                                                                                                                                               pygame.display.update()
                                                                                                                                                                                                                                               for event in pygame.event.get():
                                                                                                                                                                                                                                                              if event.type == KEYDOWN:
                                                                                                                                                                                                                                                                 if event.key == pygame.K_LCTRL:
                                                                                                                                                                                                                                                                    g = False
                                                                                                                                                                                                                                                                 if event.key == pygame.K_ESCAPE:
                                                                                                                                                                                                                                                                    sys.exit(0)
                                                                                                                                                                                                                                                                 if event.key == pygame.K_LSHIFT:
                                                                                                                                                                                                                                                                    h = True
                                                                                                                                                                                                                                                                    while h:
                                                                                                                                                                                                                                                                               ret, frame = camera.read()
                                                                                                                                                                                                                                                                               screen.fill([0,0,0])
                                                                                                                                                                                                                                                                               frame = cv2.GaussianBlur(frame, (7, 7), 5.64)
                                                                                                                                                                                                                                                                               frame = cv2.cvtColor(frame,cv2.COLOR_RGB2Luv)
                                                                                                                                                                                                                                                                               frame = np.rot90(frame)
                                                                                                                                                                                                                                                                               frame = pygame.surfarray.make_surface(frame)
                                                                                                                                                                                                                                                                               screen.blit(frame, (0,0))
                                                                                                                                                                                                                                                                               pygame.display.update()
                                                                                                                                                                                                                                                                               for event in pygame.event.get():
                                                                                                                                                                                                                                                                                              if event.type == KEYDOWN:
                                                                                                                                                                                                                                                                                                 if event.key == pygame.K_LCTRL:
                                                                                                                                                                                                                                                                                                    h = False
                                                                                                                                                                                                                                                                                                 if event.key == pygame.K_ESCAPE:
                                                                                                                                                                                                                                                                                                    sys.exit(0)
except (KeyboardInterrupt,SystemExit):
    pygame.quit()
cv2.destroyAllWindows()
