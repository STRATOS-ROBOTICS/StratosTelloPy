from djitellopy import Tello
import cv2
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *
import numpy as np
import time
import subprocess



pygame.font.init()
# Speed of the drone
S = 90
# Frames per second of the pygame window display
FPS = 25
stratos = True                         
count = 0

font = pygame.font.SysFont("Times New Roman", 18)
PICTURENAME = 'capture1.png'

red = [255, 0, 0]



class FrontEnd(object):
    """ Maintains the Tello display and moves it through the keyboard keys.
        Press escape key to quit.
        The controls are:
            - T: Takeoff
            - L: Land
            - Arrow keys: Forward, backward, left and right.
            - A and D: Counter clockwise and clockwise rotations
            - W and S: Up and down.
            - 8 flip frontward
            - 4 flip left
            - 6 flip left
            - 2 flip right
    """

    def __init__(self):
        # Init pygame
        pygame.init()

        # Creat pygame window

        
        pygame.display.set_caption("Tello video stream")
        self.screen = pygame.display.set_mode([960, 720])
        pygame.display.set_caption("Tello video stream2")
        self.screen2 = pygame.display.set_mode([960, 720])
        icon = pygame.image.load('INTERFACES/Interface1/icone.png')
        pygame.display.set_icon(icon)        
        clickable_area = pygame.Rect((25, 25), (100, 100))
        clickable_area2 = pygame.Rect((150, 25), (50, 100))
        rect_surf = pygame.Surface(clickable_area.size)
        rect_surf2 = pygame.Surface(clickable_area2.size)
        
  

       
        # Init Tello object that interacts with the Tello drone
        self.tello = Tello()
        
        # Drone velocities between -100~100
        self.for_back_velocity = 0
        self.left_right_velocity = 0
        self.up_down_velocity = 0
        self.yaw_velocity = 0
        self.speed = 60
        
        self.send_rc_control = False


        # create update timer
        pygame.time.set_timer(USEREVENT + 1, 50)

    def run(self):

        if not self.tello.connect():
            print("Tello not connected")
            return

        if not self.tello.set_speed(self.speed):
            print("Not set speed to lowest possible")
            return

        # In case streaming is on. This happens when we quit this program without the escape key.
        if not self.tello.streamoff():
            print("Could not stop video stream")
            return

        if not self.tello.streamon():
            print("Could not start video stream")
            return

        frame_read = self.tello.get_frame_read()
        
        variablebattery = self.tello.get_battery()
        variablebattery2 = variablebattery.replace("\r\n", "%")  
        count = 0
        head = pygame.image.load("INTERFACES/MILITAIRE/HUDM1.png").convert_alpha()

        should_stop = False
        while not should_stop:

            for event in pygame.event.get():
                if event.type == USEREVENT + 1:
                    self.update()
                elif event.type == QUIT:
                    should_stop = True
                elif event.type == KEYDOWN:
                    if event.key == K_c:
                         head = pygame.image.load("INTERFACES/MILITAIRE/HUDM2.png")                    
                         count = count + 1                      
                         if count == 2 :
                            head = pygame.image.load("INTERFACES/MILITAIRE/HUDM3.png")
                         if count == 3 :
                            head = pygame.image.load("INTERFACES/MILITAIRE/HUDM2.png")                          
                         if count == 4 :
                            head = pygame.image.load("INTERFACES/MILITAIRE/HUDM1.png")
                            count = 0 
                    if event.key == K_x:
                         head = pygame.image.load("INTERFACES/MILITAIRE/HUDM2.png")                    
                         count = count + 1                      
                         if count == 2 :
                            head = pygame.image.load("INTERFACES/MILITAIRE/HUDM3.png")
                         if count == 3 :
                            head = pygame.image.load("INTERFACES/MILITAIRE/HUDM4.png")                         
                         if count == 4 :
                            head = pygame.image.load("INTERFACES/MILITAIRE/HUDM1.png")
                            count = 0                        
                        
                    if event.key == K_m:
                         MENU = True
                         while MENU:
                                    self.screen.fill([0, 255, 0])
                                    frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2RGB)
                                    frame = np.rot90(frame)
                                    frame = np.flipud(frame)
                                    frame = pygame.surfarray.make_surface(frame)
                                    self.screen.blit(frame, (0, 0))
                                    self.screen.blit(head, (15, 90))
                                    pygame.display.update()
                                    for event in pygame.event.get():                                
                                       if event.type == KEYDOWN:
                                         if event.key == pygame.K_m:
                                            MENU = False



                    if event.key == K_h:                        
                         head = pygame.image.load("INTERFACES/neutre.png")
                         count = count + 1                      
                         if count == 2 :     
                                        head = pygame.image.load("INTERFACES/MILITAIRE/HUDM1.png")
                                        count = 0         
                    if event.key == K_LSHIFT:
                        count = 0                        
                        b = True                        
                        head = pygame.image.load("INTERFACES/INTERFACEIRONMAN/HUDIM11.png")                        
                        TakeOffButtonIM = pygame.image.load("INTERFACES/INTERFACEIRONMAN/TakeOffButtonIM.png")
                        LandButtonIM = pygame.image.load("INTERFACES/INTERFACEIRONMAN/TakeOffButtonIM.png")
                        ReturnToLandButtonIM = pygame.image.load("INTERFACES/INTERFACEIRONMAN/ReturnToLandButtonIM.png")
                        Mission01ButtonIM = pygame.image.load("INTERFACES/INTERFACEIRONMAN/Mission01ButtonIM.png")
                        Mission02ButtonIM = pygame.image.load("INTERFACES/INTERFACEIRONMAN/Mission02ButtonIM.png")
                        Mission03ButtonIM = pygame.image.load("INTERFACES/INTERFACEIRONMAN/Mission03ButtonIM.png")
                        Mission04ButtonIM = pygame.image.load("INTERFACES/INTERFACEIRONMAN/Mission04ButtonIM.png")
                        PredatorButtonIM = pygame.image.load("INTERFACES/INTERFACEIRONMAN/PredatorButtonIM.png")
                        ThermiqueButtonIM = pygame.image.load("INTERFACES/INTERFACEIRONMAN/ThermiqueButtonIM.png")
                        InvertButtonIM = pygame.image.load("INTERFACES/INTERFACEIRONMAN/InvertButtonIM.png")
                        ContourButtonIM = pygame.image.load("INTERFACES/INTERFACEIRONMAN/ContourButtonIM.png")
                        button01IM = pygame.image.load("INTERFACES/INTERFACEIRONMAN/Button01IM.png")
                        self.forward_back_velocity = 0
                        self.left_right_velocity = 0
                        self.up_down_velocity = 0
                        self.yaw_velocity = 0
                        #self.speed = s
                        s = 90 
                        while b:                                          
                                   #s = 60
                                   #if self.send_rc_control:
                                                           #self.tello.send_rc_control(self.left_right_velocity, self.for_back_velocity, self.up_down_velocity,
                                                           #self.yaw_velocity)


                                   keys = pygame.key.get_pressed()
                                   #ret, frame = frame_read
                                   self.screen.fill([0,0,0])
                                   frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2RGB)
                                   frame = np.rot90(frame)                                   
                                   frame = np.flipud(frame)                                   
                                   afficher = font.render((variablebattery2), 1, (255, 255, 255))
                                   frame = pygame.surfarray.make_surface(frame)
                                   self.screen.blit(frame, (0,0))
                                   #self.screen.blit(button01IM,(100,10))            
                                   self.screen.blit(button01IM,(180,10))   
                                   self.screen.blit(ReturnToLandButtonIM,(20,10))
                                   #self.screen.blit(button01,(170,10))
                                   self.screen.blit(Mission01ButtonIM,(320,10))
                                   self.screen.blit(Mission02ButtonIM,(470,10))
                                   self.screen.blit(Mission03ButtonIM,(620,10))
                                   self.screen.blit(Mission04ButtonIM,(770,10))
                                   self.screen.blit(TakeOffButtonIM,(20,620))
                                   self.screen.blit(LandButtonIM,(140,620))
                                   self.screen.blit(PredatorButtonIM,(260,620))
                                   self.screen.blit(ThermiqueButtonIM,(380,620))
                                   self.screen.blit(InvertButtonIM,(620,620))
                                   self.screen.blit(ContourButtonIM,(500,620))
                                   self.screen.blit(PhotoButton,(760,610))
                                   self.screen.blit(RecordButton,(850,622))
                                   self.screen.blit(head,(0,0))
                                   self.screen.blit(afficher, (900,90))                                   
                                   pygame.display.update()                               
                                   for event in pygame.event.get():                                
                                      if event.type == KEYDOWN:
                                        if event.key == pygame.K_c:
                                            count = count + 1 
                                            if count == 1 :
                                              head = pygame.image.load("INTERFACES/INTERFACEIRONMAN/HUDIM5.png")                                            
                                            if count == 2 :
                                              head = pygame.image.load("INTERFACES/INTERFACEIRONMAN/HUDIM4.png")                                                        
                                            if count == 3 :
                                              head = pygame.image.load("INTERFACES/INTERFACEIRONMAN/HUDIM2.png")                                    
                                            if count == 4 :
                                              head = pygame.image.load("INTERFACES/INTERFACEIRONMAN/HUDIM3.png")                              
                                            if count == 5 :
                                              head = pygame.image.load("INTERFACES/INTERFACEIRONMAN/HUDIM11.png")                                              
                                              count = 0                                          
                                        if event.key == K_x:
                                            head = pygame.image.load("INTERFACES/INTERFACEIRONMAN/HUDIM4.png")                    
                                            count = count + 1                      
                                            if count == 2 :
                                              head = pygame.image.load("INTERFACES/INTERFACEIRONMAN/HUDIM2.png")
                                            if count == 3 :
                                              head = pygame.image.load("INTERFACES/INTERFACEIRONMAN/HUDIM3.png")
                                                                                    
                                            if count == 4 :
                                              head = pygame.image.load("INTERFACES/INTERFACEIRONMAN/HUDIM4.png")
                                              count = 0                                        
                                        if event.key == K_LCTRL:
                                           head = pygame.image.load("INTERFACES/MILITAIRE/HUDM1.png")                                            
                                           b = False
                                        if event.key == pygame.K_UP:  # set forward velocity
                                           self.forward_back_velocity = s
                                           self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity,
                                                                      self.yaw_velocity)
                                        if event.key == pygame.K_DOWN:  # set forward velocity
                                           self.forward_back_velocity = -s
                                           self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity,
                                                                      self.yaw_velocity)          
                                        if event.key == pygame.K_RIGHT:  # set forward velocity
                                           self.left_right_velocity = s
                                           self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity,
                                                                      self.yaw_velocity)
                                        if event.key == pygame.K_LEFT:  # set forward velocity
                                           self.left_right_velocity = -s
                                           self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity,
                                                                      self.yaw_velocity)        
                                        if event.key == pygame.K_d:  # set forward velocity
                                           self.yaw_velocity = s
                                           self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity,
                                                                      self.yaw_velocity)         
                                        if event.key == pygame.K_a:  # set forward velocity
                                           self.yaw_velocity = -s
                                           self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity,
                                                                      self.yaw_velocity)
                                        if event.key == pygame.K_s:  # set forward velocity
                                           self.up_down_velocity = s
                                           self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity,
                                                                      self.yaw_velocity)                                        
                                        if event.key == pygame.K_w:  # set forward velocity
                                           self.up_down_velocity = -s
                                           self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity,
                                                                      self.yaw_velocity)
                                      if event.type == KEYUP:
                                        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:  # set zero forward/backward velocity
                                           self.forward_back_velocity = 0
                                           self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity,
                                                                      self.yaw_velocity)
                                        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:  # set zero forward/backward velocity
                                           self.left_right_velocity = 0
                                           self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity,
                                                                      self.yaw_velocity)
                                        if event.key == pygame.K_a or event.key == pygame.K_d:  # set zero forward/backward velocity
                                           self.yaw_velocity = 0
                                           self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity,
                                                                      self.yaw_velocity)
                                        if event.key == pygame.K_w or event.key == pygame.K_s:  # set zero forward/backward velocity
                                           self.yaw_velocity = 0 
                                           self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity,
                                                                      self.yaw_velocity)
                                        if event.key == pygame.K_t:  # takeoff
                                           self.tello.takeoff()                                         
                                           self.send_rc_control = True
                                        if event.key == pygame.K_j:
                                           nb_joysticks = pygame.joystick.get_count()
                                           if nb_joysticks > 0:
                                              mon_joystick = pygame.joystick.Joystick(0)
                                              mon_joystick.init()
                                              nb_boutons = mon_joystick.get_numbuttons()
                                              if nb_boutons >= 4:
                                                 omega = True
                                                 while omega:
                                                      self.screen.fill([0,0,0])
                                                      MANETTE01 = pygame.image.load("INTERFACES/MANETTE01.png")
                                                      frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2RGB)
                                                      frame = np.rot90(frame)                                   
                                                      frame = np.flipud(frame)                                   
                                                      afficher = font.render((variablebattery2), 1, (255, 255, 255))
                                                      frame = pygame.surfarray.make_surface(frame)
                                                      self.screen.blit(frame, (0,0))
                                                      self.screen.blit(button01IM,(100,10))            
                                                      self.screen.blit(MANETTE01,(25,25))   
                                                      self.screen.blit(head,(0,0))
                                                      self.screen.blit(afficher, (900,90))                                   
                                                      pygame.display.update()
                                                      for event in pygame.event.get():
                                                          if event.type==pygame.JOYAXISMOTION:

                                                            if event.axis==1:                      
                                                              if event.value<-0.5:
                                                                   self.forward_back_velocity = s
                                                                   self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity,  self.up_down_velocity, self.yaw_velocity)
                                                                   print ("avance")                  
                                                              else:
                                                                   self.forward_back_velocity = 0
                                                                   self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity,  self.up_down_velocity, self.yaw_velocity)
                                                              if event.value>0.5:
                                                                   self.forward_back_velocity = -s
                                                                   self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity,  self.up_down_velocity, self.yaw_velocity)
                                                                   print ("recule")                                                             
                                                                 
                                                            if event.axis==3:                      
                                                              if event.value<-0.5:
                                                                   self.left_right_velocity = -s
                                                                   self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity,  self.up_down_velocity, self.yaw_velocity)
                                                                   print ("gauche")                  
                                                              else:
                                                                   self.left_right_velocity = 0
                                                                   self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity,  self.up_down_velocity, self.yaw_velocity)
                                                              if event.value>0.5:
                                                                   self.left_right_velocity = s
                                                                   self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity,  self.up_down_velocity, self.yaw_velocity)
                                                                   print ("droite") 

                                                          if event.type == JOYBUTTONDOWN and event.button == 5:
                                                                   print ("R1")
                                                                   self.yaw_velocity = s
                                                                   self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity, self.yaw_velocity)
                                                          if event.type == JOYBUTTONUP and event.button == 5:
                                                                   self.yaw_velocity = 0
                                                                   self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity,  self.up_down_velocity, self.yaw_velocity)



                                                          if event.type == JOYBUTTONDOWN and event.button == 0:
                                                              print ("Takeoff")
                                                              self.tello.takeoff()
                                                              self.send_rc_control = True                                                                   
                                                              print("x !")
                                                           #else:
                                                                #print("Vous n'avez pas branché de Joystick...")
                                                          if event.type == JOYBUTTONDOWN and event.button == 1:
                                                              print ("land")
                                                              self.tello.land()
                                                              self.send_rc_control = False                                                                   
                                                              print("rond")
                                                          if event.type == JOYBUTTONDOWN and event.button == 2:
                                                              print ("Triangle")
                                                              self.tello.send_command_without_return("rc  00 00 00 00")
                                                              #self.send_rc_control = True                                                                   
                                                              print("Boum !")
                                                          if event.type == JOYBUTTONDOWN and event.button == 3:
                                                              #if event.key == pygame.K_c:
                                                                 count = count + 1 
                                                                 if count == 1 :
                                                                    head = pygame.image.load("INTERFACES/INTERFACEIRONMAN/HUDIM5.png")                                            
                                                                 if count == 2 :
                                                                    head = pygame.image.load("INTERFACES/INTERFACEIRONMAN/HUDIM4.png")
                                                                    count = 0                                                                    
                                                                    print ("carré")                
                                                          if event.type == JOYBUTTONDOWN and event.button == 4:
                                                              print ("L1")
                                                              self.yaw_velocity = -s
                                                              self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity, self.yaw_velocity)
                                                          if event.type == JOYBUTTONUP and event.button == 4:
                                                              print ("L1")
                                                              self.yaw_velocity = 0
                                                              self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity, self.yaw_velocity)


                                                          if event.type == JOYBUTTONDOWN and event.button == 6:
                                                              print ("L2")
                                                              self.up_down_velocity = -s
                                                              self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity, self.yaw_velocity)


                                                          if event.type == JOYBUTTONUP and event.button == 6:
                                                              self.up_down_velocity = 0
                                                              self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity, self.yaw_velocity)
                                                          if event.type == JOYBUTTONDOWN and event.button == 7:
                                                              self.up_down_velocity = s
                                                              self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity, self.yaw_velocity)                
                                                          if event.type == JOYBUTTONUP and event.button == 7:
                                                              self.up_down_velocity = 0
                                                              self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity, self.yaw_velocity)  
                                                          if event.type == JOYBUTTONDOWN and event.button == 8:
                                                              print("share")
                                                          if event.type == JOYBUTTONDOWN and event.button == 9:
                                                              print("options")
                                                          if event.type == JOYBUTTONDOWN and event.button == 10:
                                                              print("PS")
                                                          if event.type == JOYBUTTONDOWN and event.button == 11:
                                                              self.tello.send_command_without_return("rc  00 00 00 00")
                                                              print("LEFTTANALOG")
                                                          if event.type == JOYBUTTONDOWN and event.button == 12:
                                                              self.tello.send_command_without_return("rc  00 00 00 00")
                                                              print("RIGHTANALOG")

                                                          if event.type == JOYHATMOTION:
                                                            if event.value==(0, 1):
                                                               self.tello.flip("f")
                                                               self.send_rc_control = True
                                                               print("haut")                                                            
                                                            if event.value==(0, -1):
                                                               self.tello.flip("b")
                                                               self.send_rc_control = True
                                                               print("bas")
                                                            if event.value==(-1, 0):
                                                               self.tello.flip("l")
                                                               self.send_rc_control = True
                                                               print("gauche")
                                                            if event.value==(1, 0):
                                                               self.tello.flip("r")
                                                               self.send_rc_control = True
                                                               print("droite")
                                                          if event.type == KEYDOWN:
                                                            if event.key == pygame.K_ESCAPE:
                                                               omega = False
                                      if event.type == KEYDOWN:
                                        if event.key == K_LSHIFT:
                                           count = 0                                            
                                           c = True
                                           head = pygame.image.load("INTERFACES/INTERFACEPREDATOR/HUDP1.png")                                            
                                           while c:
                                                    button01P = pygame.image.load("INTERFACES/INTERFACEPREDATOR/button01P.png")                                         
                                                    self.screen.fill([0,0,0])
                                                    frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2HSV)
                                                    frame = np.rot90(frame)                                   
                                                    frame = np.flipud(frame)                                   
                                                    afficher = font.render((variablebattery2), 1, (255, 255, 255))
                                                    frame = pygame.surfarray.make_surface(frame)
                                                    self.screen.blit(frame, (0,0))
                                                    self.screen.blit(button01P,(100,10))            
                                                    self.screen.blit(button01P,(250,10))   
                                                    self.screen.blit(head,(0,0))
                                                    self.screen.blit(afficher, (900,90))                                   
                                                    pygame.display.update()                                                   
                                                    for event in pygame.event.get():                                
                                                        if event.type == KEYDOWN:
                                                            if event.key == K_ESCAPE:
                                                               should_stop = True                                                            
                                                               #capture = False                                                               
                                                               frame_read.stop()
                                                               #break                                                            
                                                               pygame.quit()                                                            
                                                            #if event.type == KEYDOWN:
                                                               
                                                            #if event.type == KEYUP:
                                                               #self.keyup(event.key)                                                            
                                                            if event.key == K_c:
                                                               head = pygame.image.load("INTERFACES/INTERFACEPREDATOR/HUDP2.png")                    
                                                               count = count + 1                                                            
                                                               if count == 1 :
                                                                  head = pygame.image.load("INTERFACES/INTERFACEPREDATOR/HUDP3.png")                                                        
                                                               if count == 2 :
                                                                  head = pygame.image.load("INTERFACES/INTERFACEPREDATOR/HUDP1.png")                                                            
                                                                  count = 0                                                            
                                                            if event.key == K_LCTRL:
                                                               head = pygame.image.load("INTERFACES/INTERFACEIRONMAN/HUDIM1.png")                                                               
                                                               c = False                    
                                                            if event.key == K_KP0:                                                            
                                                               b = False
                                                               c = False

                                                            if event.key == pygame.K_UP:  # set forward velocity
                                                               self.forward_back_velocity = s
                                                               self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity,
                                                                                          self.yaw_velocity)
                                                            if event.key == pygame.K_DOWN:  # set forward velocity
                                                               self.forward_back_velocity = -s
                                                               self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity,
                                                                                          self.yaw_velocity)          
                                                            if event.key == pygame.K_RIGHT:  # set forward velocity
                                                               self.left_right_velocity = s
                                                               self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity,
                                                                                          self.yaw_velocity)
                                                            if event.key == pygame.K_LEFT:  # set forward velocity
                                                               self.left_right_velocity = -s
                                                               self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity,
                                                                                          self.yaw_velocity)        
                                                            if event.key == pygame.K_d:  # set forward velocity
                                                               self.yaw_velocity = s
                                                               self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity,
                                                                                          self.yaw_velocity)         
                                                            if event.key == pygame.K_a:  # set forward velocity
                                                               self.yaw_velocity = -s
                                                               self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity,
                                                                                          self.yaw_velocity)
                                                            if event.key == pygame.K_s:  # set forward velocity
                                                               self.up_down_velocity = s
                                                               self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity,
                                                                                          self.yaw_velocity)                                        
                                                            if event.key == pygame.K_w:  # set forward velocity
                                                               self.up_down_velocity = -s
                                                               self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity,
                                                                                          self.yaw_velocity)
                                                        if event.type == KEYUP:
                                                            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:  # set zero forward/backward velocity
                                                               self.forward_back_velocity = 0
                                                               self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity,
                                                                                          self.yaw_velocity)
                                                            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:  # set zero forward/backward velocity
                                                               self.left_right_velocity = 0
                                                               self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity,
                                                                                          self.yaw_velocity)
                                                            if event.key == pygame.K_a or event.key == pygame.K_d:  # set zero forward/backward velocity
                                                               self.yaw_velocity = 0
                                                               self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity,
                                                                                          self.yaw_velocity)
                                                            if event.key == pygame.K_w or event.key == pygame.K_s:  # set zero forward/backward velocity
                                                               self.yaw_velocity = 0 
                                                               self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity,
                                                                                          self.yaw_velocity)
                                                            if event.key == pygame.K_t:  # takeoff
                                                               self.tello.takeoff()                                         
                                                               self.send_rc_control = True
                                                        if event.type == KEYDOWN:
                                                            if event.key == pygame.K_j:
                                                               nb_joysticks = pygame.joystick.get_count()
                                                               if nb_joysticks > 0:
                                                                  mon_joystick = pygame.joystick.Joystick(0)
                                                                  mon_joystick.init()
                                                                  nb_boutons = mon_joystick.get_numbuttons()
                                                                  if nb_boutons >= 4:
                                                                     carburo = True
                                                                     while carburo:
                                                                                 self.screen.fill([0,0,0])
                                                                                 MANETTE01 = pygame.image.load("INTERFACES/MANETTE01.png")
                                                                                 frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2HSV)
                                                                                 frame = np.rot90(frame)                                   
                                                                                 frame = np.flipud(frame)                                   
                                                                                 afficher = font.render((variablebattery2), 1, (255, 255, 255))
                                                                                 frame = pygame.surfarray.make_surface(frame)
                                                                                 self.screen.blit(frame, (0,0))
                                                                                 self.screen.blit(button01IM,(100,10))            
                                                                                 self.screen.blit(MANETTE01,(25,25))   
                                                                                 self.screen.blit(head,(0,0))
                                                                                 self.screen.blit(afficher, (900,90))                                   
                                                                                 pygame.display.update()
                                                                                 for event in pygame.event.get():
                                                                                    if event.type==pygame.JOYAXISMOTION:

                                                                                      if event.axis==1:                      
                                                                                        if event.value<-0.5:
                                                                                           self.forward_back_velocity = s
                                                                                           self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity,  self.up_down_velocity, self.yaw_velocity)
                                                                                           print ("avance")                  
                                                                                        else:
                                                                                             self.forward_back_velocity = 0
                                                                                             self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity,  self.up_down_velocity, self.yaw_velocity)
                                                                                        if event.value>0.5:
                                                                                           self.forward_back_velocity = -s
                                                                                           self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity,  self.up_down_velocity, self.yaw_velocity)
                                                                                           print ("recule")                                                             
                                                                 
                                                                                      if event.axis==3:                      
                                                                                        if event.value<-0.5:
                                                                                           self.left_right_velocity = -s
                                                                                           self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity,  self.up_down_velocity, self.yaw_velocity)
                                                                                           print ("gauche")                  
                                                                                        else:
                                                                                             self.left_right_velocity = 0
                                                                                             self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity,  self.up_down_velocity, self.yaw_velocity)
                                                                                        if event.value>0.5:
                                                                                           self.left_right_velocity = s
                                                                                           self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity,  self.up_down_velocity, self.yaw_velocity)
                                                                                           print ("droite") 

                                                                                    if event.type == JOYBUTTONDOWN and event.button == 5:
                                                                                       print ("R1")
                                                                                       self.yaw_velocity = s
                                                                                       self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity, self.yaw_velocity)
                                                                                    if event.type == JOYBUTTONUP and event.button == 5:
                                                                                       self.yaw_velocity = 0
                                                                                       self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity,  self.up_down_velocity, self.yaw_velocity)



                                                                                    if event.type == JOYBUTTONDOWN and event.button == 0:
                                                                                       print ("Takeoff")
                                                                                       self.tello.takeoff()
                                                                                       self.send_rc_control = True                                                                   
                                                                                       print("x !")
                                                           #else:
                                                                #print("Vous n'avez pas branché de Joystick...")
                                                                                    if event.type == JOYBUTTONDOWN and event.button == 1:
                                                                                       print ("land")
                                                                                       self.tello.land()
                                                                                       self.send_rc_control = False                                                                   
                                                                                       print("rond")
                                                                                    if event.type == JOYBUTTONDOWN and event.button == 2:
                                                                                       print ("Triangle")
                                                                                       self.tello.send_command_without_return("rc  00 00 00 00")
                                                              #self.send_rc_control = True                                                                   
                                                                                       print("Boum !")
                                                                                    if event.type == JOYBUTTONDOWN and event.button == 3:
                                                              #if event.key == pygame.K_c:
                                                                                       count = count + 1 
                                                                                    if count == 1 :
                                                                                       head = pygame.image.load("INTERFACES/INTERFACEIRONMAN/HUDIM5.png")                                            
                                                                                    if count == 2 :
                                                                                       head = pygame.image.load("INTERFACES/INTERFACEIRONMAN/HUDIM4.png")
                                                                                       count = 0                                                                    
                                                                                       print ("carré")                
                                                                                    if event.type == JOYBUTTONDOWN and event.button == 4:
                                                                                       print ("L1")
                                                                                       self.yaw_velocity = -s
                                                                                       self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity, self.yaw_velocity)
                                                                                    if event.type == JOYBUTTONUP and event.button == 4:
                                                                                       print ("L1")
                                                                                       self.yaw_velocity = 0
                                                                                       self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity, self.yaw_velocity)


                                                                                    if event.type == JOYBUTTONDOWN and event.button == 6:
                                                                                       print ("L2")
                                                                                       self.up_down_velocity = -s
                                                                                       self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity, self.yaw_velocity)


                                                                                    if event.type == JOYBUTTONUP and event.button == 6:
                                                                                       self.up_down_velocity = 0
                                                                                       self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity, self.yaw_velocity)
                                                                                    if event.type == JOYBUTTONDOWN and event.button == 7:
                                                                                       self.up_down_velocity = s
                                                                                       self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity, self.yaw_velocity)                
                                                                                    if event.type == JOYBUTTONUP and event.button == 7:
                                                                                       self.up_down_velocity = 0
                                                                                       self.tello.send_rc_control(self.left_right_velocity, self.forward_back_velocity, self.up_down_velocity, self.yaw_velocity)  
                                                                                    if event.type == JOYBUTTONDOWN and event.button == 8:
                                                                                       print("share")
                                                                                    if event.type == JOYBUTTONDOWN and event.button == 9:
                                                                                       print("options")
                                                                                    if event.type == JOYBUTTONDOWN and event.button == 10:
                                                                                       print("PS")
                                                                                    if event.type == JOYBUTTONDOWN and event.button == 11:
                                                                                       self.tello.send_command_without_return("rc  00 00 00 00")
                                                                                       print("LEFTTANALOG")
                                                                                    if event.type == JOYBUTTONDOWN and event.button == 12:
                                                                                       self.tello.send_command_without_return("rc  00 00 00 00")
                                                                                       print("RIGHTANALOG")

                                                                                    if event.type == JOYHATMOTION:
                                                                                      if event.value==(0, 1):
                                                                                         self.tello.flip("f")
                                                                                         self.send_rc_control = True
                                                                                         print("haut")                                                            
                                                                                      if event.value==(0, -1):
                                                                                         self.tello.flip("b")
                                                                                         self.send_rc_control = True
                                                                                         print("bas")
                                                                                      if event.value==(-1, 0):
                                                                                         self.tello.flip("l")
                                                                                         self.send_rc_control = True
                                                                                         print("gauche")
                                                                                      if event.value==(1, 0):
                                                                                         self.tello.flip("r")
                                                                                         self.send_rc_control = True
                                                                                         print("droite")
                                                                                    if event.type == KEYDOWN:
                                                                                      if event.key == pygame.K_ESCAPE:
                                                                                         carburo = False


                                                            if event.key == K_LSHIFT:
                                                               d = True                    
                                                               while d:
                                                                       self.screen.fill([0,0,0])
                                                                       frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2GRAY)
                                                                       frame = cv2.Canny(frame, 25, 75)
                                                                       frame = np.rot90(frame)
                                                                       frame = np.flipud(frame)
                                                                       frame = pygame.surfarray.make_surface(frame)
                                                                       self.screen.blit(frame, (0,0))
                                                                       pygame.display.update()
                                                                       for event in pygame.event.get():                                
                                                                           if event.type == KEYDOWN:
                                                                              if event.key == K_ESCAPE:
                                                                                 should_stop = True                                                            
                                                                                 pygame.quit()                                                                 
                                                                              if event.key == K_KP0:
                                                                                 d = False
                                                                                 c = False
                                                                                 b = False
                                                                              if event.key == K_LCTRL:
                                                                                 d = False                    
                                                                              if event.key == K_LSHIFT:
                                                                                 e = True                    
                                                                                 while e:                    
                                                                                         #button01IM = pygame.image.load("button01IM.png")                                         
                                                                                         #head3 = pygame.image.load("HUDIM.png")                                                                          
                                                                                         self.screen.fill([0, 0, 0])                                                                                         
                                                                                         
                                                                                         
                                                                                         frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2RGB)        
                                                                                         frame = cv2.bitwise_not(frame)
                                                                                         frame = np.rot90(frame)
                                                                                         frame = np.flipud(frame)
                                                                                         frame = pygame.surfarray.make_surface(frame)
                                                                                         self.screen.blit(frame, (0, 0))
                                                                                         #self.screen.blit(head3, (10, 75))
                                                                                         pygame.display.update()                    
                                                                                         for event in pygame.event.get():                                
                                                                                            if event.type == KEYDOWN:
                                                                                               if event.key == K_ESCAPE:                                                                                               
                                                                                                  pygame.quit()
                                                                                               if event.key == K_KP0:                                                                                               
                                                                                                  e = False
                                                                                                  d = False
                                                                                                  c = False
                                                                                                  b = False
                                                                                               if event.key == K_LCTRL:
                                                                                                  e = False                    
                    
                                                                                               if event.key == K_LSHIFT:
                                                                                                  f = True
                                                                                                  while f:
                                                                                                          #button01IM = pygame.image.load("button01IM.png")                                         
                                                                                                          #head3 = pygame.image.load("HUDIM.png")                                                                          
                                                                                                          self.screen.fill([0, 0, 0])                                                                                         
                                                                                         
                                                                                         
                                                                                                          frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_HLS2RGB)        
                                                                                                          #frame = cv2.bitwise_not(frame)
                                                                                                          frame = np.rot90(frame)
                                                                                                          frame = np.flipud(frame)
                                                                                                          frame = pygame.surfarray.make_surface(frame)
                                                                                                          self.screen.blit(frame, (0, 0))
                                                                                                          #self.screen.blit(head3, (10, 75))
                                                                                                          pygame.display.update()
                                                                                                          for event in pygame.event.get():                                
                                                                                                             if event.type == KEYDOWN:                                                                                               
                                                                                                                if event.key == K_LCTRL:
                                                                                                                   f = False        
                                                                                                                if event.key == K_LSHIFT:
                                                                                                                   g = True
                                                                                                                   while g:
                                                                                                          #button01IM = pygame.image.load("button01IM.png")                                         
                                                                                                          #head3 = pygame.image.load("HUDIM.png")                                                                          
                                                                                                                           self.screen.fill([0, 0, 0])                                                                                         
                                                                                         
                                                                                         
                                                                                                                           frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_RGB2HLS)        
                                                                                                                           #frame = cv2.bitwise_not(frame)
                                                                                                                           frame = np.rot90(frame)
                                                                                                                           frame = np.flipud(frame)
                                                                                                                           frame = pygame.surfarray.make_surface(frame)
                                                                                                                           self.screen.blit(frame, (0, 0))
                                                                                                                           #self.screen.blit(head3, (10, 75))
                                                                                                                           pygame.display.update()
                                                                                                                           for event in pygame.event.get():                                
                                                                                                                                if event.type == KEYDOWN:                                                                                               
                                                                                                                                    if event.key == K_LCTRL:
                                                                                                                                       g = False
                                                                                                                                    if event.key == K_LSHIFT:
                                                                                                                                       h = True                    
                                                                                                                                       while h:
                                                                                                                                              self.screen.fill([0,0,0])
                                                                                                                                              frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2GRAY)
                                                                                                                                              frame = cv2.bitwise_not(frame)
                                                                                                                                              frame = np.rot90(frame)
                                                                                                                                              frame = np.flipud(frame)
                                                                                                                                              frame = pygame.surfarray.make_surface(frame)
                                                                                                                                              self.screen.blit(frame, (0,0))
                                                                                                                                              pygame.display.update()
                                                                                                                                              for event in pygame.event.get():
                                                                                                                                                  if event.type == KEYDOWN:
                                                                                                                                                     if event.key == K_LCTRL:
                                                                                                                                                        h = False
                                                                                                                                                     if event.key == K_LSHIFT:
                                                                                                                                                        h = False              
                                                                                                                                                        g = False
                                                                                                                                                        f = False
                                                                                                                                                        e = False
                                                                                                                                                        d = False
                                                                                                                                                        c = False
                                                                                                                                                        b = False

                    if event.key == K_ESCAPE:
                       should_stop = True
                    else:
                        self.keydown(event.key)
                elif event.type == KEYUP:
                    self.keyup(event.key)
                elif event.type == MOUSEBUTTONUP: # quand je relache le bouton
                    if event.button == 1: # 1= clique gauche
                      if clickable_area.collidepoint(event.pos):
                        print ("hello")
                        print ("zone1-360continuous")
                        count = 0
                        Cell = True                         
                        print ("ok1")                         
                        while Cell:
                                        count = count + 1
                                        self.screen.fill([0, 0, 0])
                                        frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2RGB)        
                                        frame = np.rot90(frame)
                                        frame = np.flipud(frame)
                                        frame = pygame.surfarray.make_surface(frame)
                                        self.screen.blit(frame, (0, 0))
                                        pygame.display.update()
                                        if count == 100 :                    
                                                         print ("ok2")                            
                                                       
                                                         self.tello.send_command_without_return("rc 00 20 00 00")                                       
                                        if count == 250 :
                                                         self.tello.send_command_without_return("rc 20 00 00 -20")                                         
                                                        
                                                         print ("ok3")
                                        if count == 550 :                    
                                                         print ("ok4")                            
                                                        
                                                         self.tello.send_command_without_return("rc 00 -20 00 00")                                       
                                        if count == 650 :
                                                         self.tello.send_command_without_return("rc  00 00 00 00")                                         
                                                        
                                                         print ("ok5")                                                          
                                        #if count == 700 :
                                                         #self.tello.send_command_without_return("rc  00 -20 00 00")                                         
                                                         
                                                         #print ("ok6")                                                         
                                    
                                        #if count == 850 :
                                                         #self.tello.send_command_without_return("rc  00 00 00 -20")
                                        #if count == 1000 :
                                                         #self.tello.send_command_without_return("rc  -20 00 00 00")                                         
                                                        
                                                         #print ("ok6")                                                         
                                      
                                        #if count == 1150 :
                                                         #self.tello.send_command_without_return("rc  00 00 00 -20")
                                        #if count == 1300 :
                                                         #self.tello.send_command_without_return("rc  00 00 00 00")
                                                         #self.send_rc_control = True
                                                         Cell = False
                    if event.button == 1: # 1= clique gauche
                      if clickable_area2.collidepoint(event.pos):
                        print ("zone2-8")
                        count = 0
                        Freezer = True                         
                        print ("ok1")                         
                        while Freezer:
                                        count = count + 1
                                        self.screen.fill([0, 0, 0])
                                        frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2RGB)        
                                        frame = np.rot90(frame)
                                        frame = np.flipud(frame)
                                        frame = pygame.surfarray.make_surface(frame)
                                        self.screen.blit(frame, (0, 0))
                                        pygame.display.update()
                                        if count == 100 :                    
                                                         print ("ok2")                            
                                                       
                                                         self.tello.send_command_without_return("rc 60 60 00 60")                                       
                                        if count == 200 :
                                                         self.tello.send_command_without_return("rc -60 60 00 -60")                                         
                                                        
                                                         print ("ok3")
                                        if count == 300 :                    
                                                         print ("ok4")                            
                                                        
                                                         self.tello.send_command_without_return("rc -60 60 00 -60")                                       
                                        if count == 400 :
                                                         self.tello.send_command_without_return("rc  -60 60 00 -60")                                         
                                                        
                                                         print ("ok5")                                                          
                                        if count == 500 :
                                                         self.tello.send_command_without_return("rc  -60 60 00 -60")                                         
                                                         
                                                         print ("ok6")                                                         
                                    
                                        if count == 600 :
                                                          self.tello.send_command_without_return("rc  60 60 00 60")
                                        if count == 700 :
                                                          self.tello.send_command_without_return("rc  60 60 00 60")                                         
                                                        
                                                          print ("ok6")                                                         
                                      
                                        if count == 800 :
                                                          self.tello.send_command_without_return("rc  60 60 00 60")                    
                                        if count == 900 :
                                                          self.tello.send_command_without_return("rc  00 00 00 00")
                                                          Freezer = False
                    if event.button == 1: # 1= clique gauche
                      if clickable_area3.collidepoint(event.pos):
                        print ("MISSION-01-360I")
                        #self.send_rc_control = True                        
                        count = 0
                        stratos = True                         
                        print ("ok1")                         
                        while stratos:
                                        count = count + 1
                                        self.screen.fill([0, 0, 0])
                                        frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2RGB)        
                                        frame = np.rot90(frame)
                                        frame = np.flipud(frame)
                                        frame = pygame.surfarray.make_surface(frame)
                                        self.screen.blit(frame, (0, 0))
                                        pygame.display.update()
                                        if count == 100 :                    
                                                         print ("ok2")                            
                                                         #self.left_right_velocity = -60                                                         
                                                         self.tello.send_command_without_return("rc 60 00 00 -60")                                       
                                        if count == 800 :
                                                         self.tello.send_command_without_return("rc 00 00 00 00")                                         
                                                         #self.left_right_velocity = 0                                                         
                                                         print ("ok3")
                                                         stratos = False                    
                    if event.button == 1: # 1= clique gauche
                      if clickable_area4.collidepoint(event.pos):
                        print ("MISSION-02-360E")
                        
                        count = 0
                        stratos = True                         
                        print ("ok1")                         
                        while stratos:
                                        count = count + 1
                                        self.screen.fill([0, 0, 0])
                                        frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2RGB)        
                                        frame = np.rot90(frame)
                                        frame = np.flipud(frame)
                                        frame = pygame.surfarray.make_surface(frame)
                                        self.screen.blit(frame, (0, 0))
                                        pygame.display.update()
                                        if count == 400 :                    
                                                         print ("ok2")                            
                                                         self.tello.send_command_without_return("rc 60 00 00 60")                                       
                                        if count == 800 :
                                                         print ("ok3")
                                                         stratos = False 
                    if event.button == 1: # 1= clique gauche
                      if clickable_area5.collidepoint(event.pos):
                        print ("zone5-mission03-UP-DOWN")
                        count = 0
                        stratos = True                         
                        print ("ok1")                        
                        while stratos:
                                        count = count + 1
                                        self.screen.fill([0, 0, 0])
                                        frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2RGB)        
                                        frame = np.rot90(frame)
                                        frame = np.flipud(frame)
                                        frame = pygame.surfarray.make_surface(frame)
                                        self.screen.blit(frame, (0, 0))
                                        pygame.display.update()
                                        if count == 100 :                    
                                                         print ("ok2")                            
                                                         self.tello.send_command_without_return("rc 00 00 60 00")                                        
                                        if count == 750 :
                                                          self.tello.send_command_without_return("rc 00 00 00 30")
                                                          print ("ok3")                                        
                                        if count == 1700 :
                                                          self.tello.send_command_without_return("rc 00 00 -60 00")                    
                                        if count == 2300 :
                                                          self.tello.send_command_without_return("rc 00 00 00 00")                                                          
                                                          print ("ok4")
                                                          stratos = False
                if event.type == MOUSEBUTTONUP: # quand je relache le bouton
                    if event.button == 1: # 1= clique gauche
                      if clickable_area6.collidepoint(event.pos):
                        print ("zone6-mission04-GO&GOBACK-SENTINEL-PRIME")
                        print ("ok1")                         
                        count = 0
                        stratos = True                         
                        print ("ok1")                        
                        while stratos:
                                        count = count + 1
                                        self.screen.fill([0, 0, 0])
                                        frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2RGB)        
                                        frame = np.rot90(frame)
                                        frame = np.flipud(frame)
                                        frame = pygame.surfarray.make_surface(frame)
                                        self.screen.blit(frame, (0, 0))
                                        pygame.display.update()
                                        if count == 100 :                    
                                                         print ("ok2")                            
                                                         self.tello.send_command_without_return("rc 00 60 00 00")                                       
                                        if count == 1000 :
                                                         self.tello.send_command_without_return("rc 00 00 00 40")                                         
                                                         print ("ok3")
                                        if count == 1400 :
                                                                                                  
                                                         self.tello.send_command_without_return("rc 00 60 00 00")                                                         
                                                         print ("ok4")                    
                                        if count == 400 :                    
                                                         print ("ok5")                    
                                                         self.send_rc_control = True                                                         
                                                         stratos = False                    
                    if event.button == 1: # 1= clique gauche
                      if clickable_area7.collidepoint(event.pos):
                        print ("Takeoff")
                        self.tello.takeoff()
                        self.send_rc_control = True                    
                    if event.button == 1: # 1= clique gauche                     
                      if clickable_area8.collidepoint(event.pos):
                        self.tello.Land()                
                        self.send_rc_control = False                    
                    if event.button == 1: # 1= clique gauche
                      if clickable_area9.collidepoint(event.pos):
                         bcd = True                        
                         while bcd:
                                   #self.screen.fill([0, 0, 0])
                                   frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2HSV)        
                                   frame = np.rot90(frame)
                                   frame = np.flipud(frame)
                                   frame = pygame.surfarray.make_surface(frame)
                                   self.screen.blit(frame, (0, 0))
                                   pygame.display.update()
                                   #for event in pygame.event.get():
                                   for event in pygame.event.get():
                                      if event.type == KEYDOWN and event.key == pygame.K_LCTRL:                                   
                                        print ("ok")
                                        bcd = False
                          #for event in pygame.event.get():
                                     #if event.key == KEYDOWN:
                                                               #if event.key == pygame.K_LCTRL:
                                                                  #b = False
                                                               #i0f event.key == pygame.K_ESCAPE:
                                                                  #sys.exit(0)                            
                                                               #if event.key == pygame.K_LSHIFT:
                                                                  #b = True                                   
#pygame.display.flip()
                        #time.sleep(1 / FPS)                    
                if event.type == MOUSEBUTTONUP: # quand je relache le bouton
                    if event.button == 1:# 1= clique gauche
                      if clickable_area10.collidepoint(event.pos):
                        g = True
                        while g:
                                   #self.screen.fill([0, 0, 0])
                                   frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2GRAY)        
                                   frame = np.rot90(frame)
                                   frame = np.flipud(frame)
                                   frame = pygame.surfarray.make_surface(frame)
                                   self.screen.blit(frame, (0, 0))
                                   pygame.display.update()
                                   for event in pygame.event.get():
                                                   if event.type == KEYDOWN:
                                                       if event.key == pygame.K_LCTRL:                                   
                                                         g = False#pygame.display.flip()
                        time.sleep(1 / FPS)                    

                if event.type == MOUSEBUTTONUP:
                    if event.button == 1: # 1= clique gauche
                      if clickable_area11.collidepoint(event.pos):
                         OK = True
                         while OK:
                                  #frame_read = self.tello.get_frame_read()                                  
                                  self.screen.fill([0,0,0])
                                  frame = cv2.GaussianBlur(frame_read.frame, (7, 7), 5.64)
                                  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                                  frame = cv2.Canny(frame, 25, 75)
                                  frame = np.rot90(frame)
                                  frame = pygame.surfarray.make_surface(frame)
                                  self.screen.blit(frame, (0,0))
                                  pygame.display.update()  
                                  for event in pygame.event.get():
                                                   if event.type == KEYDOWN:
                                                       if event.key == pygame.K_LCTRL:                                   
                                                         OK = False
                if event.type == MOUSEBUTTONUP:

                    if event.button == 1: # 1= clique gauche
                      if clickable_area12.collidepoint(event.pos):
                        Sangoku = True
                        while Sangoku:
                                   self.screen.fill([0, 0, 0])
                                   frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2RGB)        
                                   frame = cv2.bitwise_not(frame)
                                   frame = np.rot90(frame)
                                   frame = np.flipud(frame)
                                   frame = pygame.surfarray.make_surface(frame)
                                   self.screen.blit(frame, (0, 0))
                                   pygame.display.update()
                                   for event in pygame.event.get():
                                       if event.type == KEYDOWN:
                                         if event.key == pygame.K_LCTRL:                                   
                                            Sangoku = False
                        #pygame.display.flip()
                        #time.sleep(1 / FPS) 
                if event.type == MOUSEBUTTONUP:
                    if event.button == 1: # 1= clique gauche
                      if clickable_area13.collidepoint(event.pos):
                        count = count + 1        
                        print (count)
                        pygame.image.save(self.screen, "frames/frame%d.jpg" % count)
                        frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2RGB)                        
                        cv2.imwrite("frames2/frame%d.jpg" % count, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))                        
                        pygame.display.update()
                        for event in pygame.event.get():
                                   if event.type == KEYDOWN:
                                      if event.key == pygame.K_LCTRL:                                   
                                         OK = False
                if event.type == MOUSEBUTTONUP:
                    if event.button == 1: # 1= clique gauche
                      if clickable_area14.collidepoint(event.pos):
                         count = 0                          
                         stratos = True
                         while stratos:                
                                    
                                      self.screen.fill([0, 0, 0])
                                      frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2RGB)        
                                      frame = np.rot90(frame)                                    
                                      frame = np.flipud(frame)                                    
                                      frame = pygame.surfarray.make_surface(frame)
                                      self.screen.blit(frame, (0, 0))
                                      pygame.display.update()
                                      frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2RGB)                                                   
                                      cv2.imwrite("frames/frame%d.jpg" % count, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
                                      count = count + 1    
                                      for event in pygame.event.get():                                
                                          if event.type == KEYDOWN:
                                            if event.key == K_ESCAPE:
                                               stratos = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        capture = False

            if frame_read.stopped:
                frame_read.stop()
                break
            

            self.screen.fill([0, 255, 0])
       
            frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2RGB)
            frame = np.rot90(frame)
            frame = np.flipud(frame)
            frame = pygame.surfarray.make_surface(frame)
            
            button01 = pygame.image.load("INTERFACES/Interface1/8Button.png")
            TakeOffButton = pygame.image.load("INTERFACES/Interface1/TakeOffButton.png")
            LandButton = pygame.image.load("INTERFACES/Interface1/LandButton.png")
            Mission01Button = pygame.image.load("INTERFACES/Interface1/360IButton.png")
            Mission02Button = pygame.image.load("INTERFACES/Interface1/360EButton.png")
            Mission03Button = pygame.image.load("INTERFACES/Interface1/UpDownButton.png")
            Mission04Button = pygame.image.load("INTERFACES/Interface1/GoBackButton.png")
            RecordButton = pygame.image.load("INTERFACES/Interface1/RecordButton.png")
            PhotoButton = pygame.image.load("INTERFACES/Interface1/PhotoButton.png")
            PredatorButton = pygame.image.load("INTERFACES/Interface1/PredatorButton.png")
            ReturnToLandButton = pygame.image.load("INTERFACES/Interface1/360C.png")
            ThermiqueButton = pygame.image.load("INTERFACES/Interface1/ThermiqueButton.png")
            InvertButton = pygame.image.load("INTERFACES/Interface1/InvertButton.png")
            ContourButton = pygame.image.load("INTERFACES/Interface1/ContourButton.png")
            DemoButton = pygame.image.load("INTERFACES/Interface1/DemoButton.png")
            clickable_area = pygame.Rect((25, 25), (100, 25))
            clickable_area2 = pygame.Rect((175, 25), (100, 25))
            clickable_area3 = pygame.Rect((325, 25), (100, 25))
            clickable_area4 = pygame.Rect((475, 25), (100, 25))
            clickable_area5 = pygame.Rect((625, 25), (100, 25))
            clickable_area6 = pygame.Rect((775, 25), (100, 25))
            clickable_area7 = pygame.Rect((25, 633), (100, 25))
            clickable_area8 = pygame.Rect((142, 633), (100, 25))
            clickable_area9 = pygame.Rect((262, 633), (100, 25))
            clickable_area10 = pygame.Rect((382, 633), (100, 25))
            clickable_area11 = pygame.Rect((502, 633), (100, 25))
            clickable_area12 = pygame.Rect((622, 633), (100, 25))  
            clickable_area13 = pygame.Rect((777, 625), (50, 50))
            clickable_area14 = pygame.Rect((855, 625), (50, 50))
            rect_surf = pygame.Surface(clickable_area.size)
            rect_surf2 = pygame.Surface(clickable_area2.size)
            rect_surf3 = pygame.Surface(clickable_area3.size)
            rect_surf4 = pygame.Surface(clickable_area4.size)
            rect_surf5 = pygame.Surface(clickable_area5.size)
            rect_surf6 = pygame.Surface(clickable_area6.size)
            rect_surf7 = pygame.Surface(clickable_area7.size)
            rect_surf8 = pygame.Surface(clickable_area8.size)
            rect_surf9 = pygame.Surface(clickable_area9.size)
            rect_surf10 = pygame.Surface(clickable_area10.size)
            rect_surf11 = pygame.Surface(clickable_area11.size)
            rect_surf12 = pygame.Surface(clickable_area12.size)
            rect_surf13 = pygame.Surface(clickable_area13.size)
            rect_surf14 = pygame.Surface(clickable_area14.size)
            afficher = font.render((variablebattery2), 1, (255, 255, 255))
            self.screen.blit(frame, (0, 0))
            self.screen.blit(head, (15, 90))
            self.screen.blit(ReturnToLandButton,(20,10))
            self.screen.blit(button01,(170,10))
            self.screen.blit(Mission01Button,(320,10))
            self.screen.blit(Mission02Button,(470,10))
            self.screen.blit(Mission03Button,(620,10))
            self.screen.blit(Mission04Button,(770,10))
            self.screen.blit(TakeOffButton,(20,620))
            self.screen.blit(LandButton,(140,620))
            self.screen.blit(PredatorButton,(260,620))
            self.screen.blit(ThermiqueButton,(380,620))
            self.screen.blit(InvertButton,(620,620))
            self.screen.blit(ContourButton,(500,620))
            self.screen.blit(PhotoButton,(760,610))
            self.screen.blit(RecordButton,(850,622))
            self.screen.blit(afficher, (900,90))

            #self.screen.blit(rect_surf, clickable_area)
            #self.screen.blit(rect_surf2, clickable_area2)
            #self.screen.blit(rect_surf3, clickable_area3)
            #self.screen.blit(rect_surf4, clickable_area4)
            #self.screen.blit(rect_surf5, clickable_area5)
            #self.screen.blit(rect_surf6, clickable_area6)
            #self.screen.blit(rect_surf7, clickable_area7)
            #self.screen.blit(rect_surf8, clickable_area8)
            #self.screen.blit(rect_surf9, clickable_area9)
            #self.screen.blit(rect_surf10, clickable_area10)
            #self.screen.blit(rect_surf11, clickable_area11)
            #self.screen.blit(rect_surf12, clickable_area12)
            #self.screen.blit(rect_surf13, clickable_area13)
            #self.screen.blit(rect_surf14, clickable_area14)
            pygame.display.update()

            #time.sleep(0.5 / FPS)

        # Call it always before finishing. I deallocate resources.
        self.tello.end()

    def keydown(self, key):
        """ Update velocities based on key pressed
        Arguments:
            key: pygame key
        """
        if key == pygame.K_UP:  # set forward velocity
            self.for_back_velocity = S
        elif key == pygame.K_DOWN:  # set backward velocity
            self.for_back_velocity = -S
        elif key == pygame.K_LEFT:  # set left velocity
            self.left_right_velocity = -S
        elif key == pygame.K_RIGHT:  # set right velocity
            self.left_right_velocity = S
        elif key == pygame.K_s:  # set up velocity
            self.up_down_velocity = S
        elif key == pygame.K_w:  # set down velocity
            self.up_down_velocity = -S
        elif key == pygame.K_a:  # set yaw clockwise velocity
            self.yaw_velocity = -S
        elif key == pygame.K_d:  # set yaw counter clockwise velocity
            self.yaw_velocity = S

    def keyup(self, key):
        """ Update velocities based on key released
        Arguments:
            key: pygame key
        """
        if key == pygame.K_UP or key == pygame.K_DOWN:  # set zero forward/backward velocity
            self.for_back_velocity = 0
        elif key == pygame.K_LEFT or key == pygame.K_RIGHT:  # set zero left/right velocity
            self.left_right_velocity = 0
        elif key == pygame.K_w or key == pygame.K_s:  # set zero up/down velocity
            self.up_down_velocity = 0
        elif key == pygame.K_a or key == pygame.K_d:  # set zero yaw velocity
            self.yaw_velocity = 0
        elif key == pygame.K_t:  # takeoff
            self.tello.takeoff()
            self.send_rc_control = True
        elif key == pygame.K_l:  # land
            self.tello.land()
            self.send_rc_control = False
        elif key == pygame.K_KP8: # flip front
            self.tello.flip("f")
            self.send_rc_control = True
        elif key == pygame.K_KP2: # flip back
            self.tello.flip("b") 
            self.send_rc_control = True
        elif key == pygame.K_KP4: # flip left
            self.tello.flip("l")
            self.send_rc_control = True
        elif key == pygame.K_KP6: # flip right
            self.tello.flip("r")
        elif key == pygame.K_f: # flip right
            self.screen.fill(red)
            pygame.display.update()
            pygame.display.flip() 

    def joystick(self, key):
        """ Update velocities based on key pressed
        Arguments:
            key: pygame key
        """
        if event.type == JOYBUTTONDOWN and event.button == 0:
           print ("Takeoff")
                                                              
        if event.type == JOYBUTTONDOWN and event.button == 1:
           print ("land")



    def update(self):
        """ Update routine. Send velocities to Tello."""
        if self.send_rc_control:
            self.tello.send_rc_control(self.left_right_velocity, self.for_back_velocity, self.up_down_velocity,
                                       self.yaw_velocity)


def main():
    frontend = FrontEnd()

    # run frontend
    frontend.run()


if __name__ == '__main__':
    main()
