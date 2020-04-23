
#imported modules

import math
import numpy


#Constants inicialization

CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
CANVAS_SCORE = 50

class TankClass:
    def __init__(self, team, id, mapa, ini):
        self.step = 3
        self.size_l = 29.5 #1/2 largo
        self.size_w = 15.5 #1/2 ancho
        self.total_bullets = 3
        self.bullets = self.total_bullets
        self.id = id
        self.team = team
        self.mapa = mapa
        self.lives = 3
        self.half_diagonal = .5*numpy.linalg.norm((31,59))
        if mapa == 1:
            if ini == 1:
                self.position_x = 50
                self.position_y =175
                self.pointer_x = 250
                self.pointer_y = 175
                self.tank_orientation = 360
                self.pointer_orientation = 180
            elif ini == 2:
                self.position_x = 950
                self.position_y = 475
                self.pointer_x = 250
                self.pointer_y = 475
                self.tank_orientation = 180
                self.pointer_orientation = 360
            elif ini == 3:
                self.position_x = 50
                self.position_y =475
                self.pointer_x = 250
                self.pointer_y = 475
                self.tank_orientation = 360
                self.pointer_orientation = 180
            elif ini == 4:
                self.position_x = 950
                self.position_y = 175
                self.pointer_x = 250
                self.pointer_y = 175
                self.tank_orientation = 180
                self.pointer_orientation = 360
            elif ini == 5:
                self.position_x = 500
                self.position_y = 125
                self.pointer_x = 250
                self.pointer_y = 175
                self.tank_orientation = 270
                self.pointer_orientation = 90
            elif ini == 6:
                self.position_x = 500
                self.position_y = 525
                self.pointer_x = 250
                self.pointer_y = 525
                self.tank_orientation = 90
                self.pointer_orientation = 270
        elif mapa == 2:
           if ini == 1:
                self.position_x = 50
                self.position_y = 250
                self.pointer_x = 250
                self.pointer_y = 150
                self.tank_orientation = 45
                self.pointer_orientation = 225
           elif ini == 2:
                self.position_x = 450
                self.position_y = 100
                self.pointer_x = 250
                self.pointer_y = 150
                self.tank_orientation = 225
                self.pointer_orientation = 45
                
           elif ini == 3:
                self.position_x = 550
                self.position_y = 550
                self.pointer_x = 250
                self.pointer_y = 150
                self.tank_orientation = 45
                self.pointer_orientation = 225
                
           elif ini == 4:
                self.position_x = 950
                self.position_y = 100
                self.pointer_x = 250
                self.pointer_y = 150
                self.tank_orientation = 225
                self.pointer_orientation = 45
                
           elif ini == 5:
                self.position_x = 50
                self.position_y = 550
                self.pointer_x = 250
                self.pointer_y = 150
                self.tank_orientation = 45
                self.pointer_orientation = 225
                
           else:
                self.position_x = 950
                self.position_y = 400
                self.pointer_x = 250
                self.pointer_y = 150
                self.tank_orientation = 225
                self.pointer_orientation = 45
    
    def get_position(self):
        return (self.position_x, self.position_y)
    
    def get_tank_orientation(self):
        return self.tank_orientation
    
    def get_pointer(self):
        return (self.pointer_x, self.pointer_y)
    
    def get_team(self):
        return self.team
    
    def get_pointer_orientation(self):
        return self.pointer_orientation
    
    def set_pointer(self, pointer_pos):
        newX, newY = pointer_pos
        self.pointer_x = newX
        self.pointer_y = newY
        diff_x = newX - self.position_x
        diff_y = newY - self.position_y
        if diff_x == 0:
            if diff_y >= 0:
                self.pointer_orientation = 90
            else:
                self.pointer_orientation = 270
        else:
            pointer_radians = numpy.arctan(diff_y/diff_x)
            pointer_degrees = math.degrees(pointer_radians)
            if diff_x > 0:
                if diff_y <= 0:
                    self.pointer_orientation =  - pointer_degrees
                else:
                    self.pointer_orientation = 360 - pointer_degrees
            else:
                self.pointer_orientation = 180 - pointer_degrees
        print(self.pointer_orientation)
    
    def tank_kill(self):
        self.lives=self.lives-1
    
    def tank_death(self):
        return self.lives<=0
    
    def reload(self):
        self.bullets = self.total_bullets
    
    def has_bullets(self):
        return self.bullets > 0
    
    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            pointer_radiants = math.radians(self.pointer_orientation)
            length_canon = 20
            canon_x = length_canon*math.cos(pointer_radiants)
            canon_y = length_canon*math.sin(pointer_radiants)
            return BulletClass(self.team, self.position_x+canon_x, self.position_y-canon_y, self.pointer_x, self.pointer_y)
    
    def move(self, movement): #canvas 500x300
        if movement == 1:#arriba
            if self.mapa == 1:
                if self.tank_orientation == 270 and ((self.position_x <= 100 and self.position_x+ self.size_l >= 100) or (self.position_x <= 400 and self.position_x+ self.size_l >= 400) or (self.position_x <= 600 and self.position_x+ self.size_l >= 600) or (self.position_x <= 900 and self.position_x+ self.size_l >= 900)) and (self.position_y < 120 or (self.position_y > 255 and self.position_y < 395) or self.position_y > 530) :
                    self.position_y -= self.step
                elif self.tank_orientation == 270 and ((self.position_x >= 100 and self.position_x - self.size_l <= 100) or (self.position_x >= 400 and self.position_x - self.size_l <= 400) or (self.position_x >= 600 and self.position_x - self.size_l <= 600) or (self.position_x >= 900 and self.position_x - self.size_l <= 900)) and (self.position_y < 120 or (self.position_y > 255 and self.position_y < 395) or self.position_y > 530):
                    self.position_y -= self.step
                elif self.tank_orientation == 270 and ((self.position_x <= 170 and self.position_x + self.size_l >= 170) or (self.position_x <= 670 and self.position_x + self.size_l >= 670)) and self.position_y < 235 and self.position_y > 140:
                    self.position_y -= self.step
                elif self.tank_orientation == 270 and ((self.position_x >= 330 and self.position_x - self.size_l <= 330) or (self.position_x >= 830 and self.position_x - self.size_l <= 830)) and self.position_y < 235 and self.position_y > 140:
                    self.position_y -= self.step
                elif self.tank_orientation == 270 and ((self.position_x <= 170 and self.position_x + self.size_l >= 170) or (self.position_x <= 670 and self.position_x + self.size_l >= 670)) and self.position_y < 510 and self.position_y > 415:
                    self.position_y -= self.step
                elif self.tank_orientation == 270 and ((self.position_x >= 330 and self.position_x - self.size_l <= 330) or (self.position_x >= 830 and self.position_x - self.size_l <= 830)) and self.position_y < 510 and self.position_y > 415:
                    self.position_y -= self.step 
                elif self.tank_orientation == 270 and self.position_x <= 475 and self.position_x + self.size_l >= 475 and self.position_y < 353.75 and self.position_y > 271.25:
                    self.position_y -= self.step
                elif self.tank_orientation == 270 and self.position_x >= 525 and self.position_x - self.size_l <= 525 and self.position_y < 353.75 and self.position_y > 271.25:
                    self.position_y -= self.step 
                else:
                    if self.position_y >= 120 and self.position_y -self.size_l <= 120 and ((self.position_x-self.size_w < 100 and self.position_x+self.size_w > 100) or (self.position_x-self.size_w < 400 and self.position_x+self.size_w > 400) or (self.position_x-self.size_w < 600 and self.position_x+self.size_w > 600) or (self.position_x-self.size_w < 900 and self.position_x+self.size_w > 900)):
                        self.position_y = 120 + self.size_l
                    elif self.position_y >= 395 and self.position_y -self.size_l <= 395 and ((self.position_x-self.size_w < 100 and self.position_x+self.size_w > 100) or (self.position_x-self.size_w < 400 and self.position_x+self.size_w > 400) or (self.position_x-self.size_w < 600 and self.position_x+self.size_w > 600) or (self.position_x-self.size_w < 900 and self.position_x+self.size_w > 900)):
                        self.position_y = 395 + self.size_l
                    elif self.position_y >= 325 and self.position_y - self.size_l <= 325 and (self.position_x+self.size_w <= 400 or self.position_x- self.size_w >= 600):
                        self.position_y = 325 + self.size_l
                    elif self.position_y >= 235 and self.position_y - self.size_l <= 235 and ((self.position_x-self.size_w < 330 and self.position_x+self.size_w > 170) or (self.position_x-self.size_w < 830 and self.position_x+self.size_w > 670)):
                        self.position_y = 235 + self.size_l
                    elif self.position_y >= 510 and self.position_y - self.size_l <= 510 and ((self.position_x-self.size_w < 330 and self.position_x+self.size_w > 170) or (self.position_x-self.size_w < 830 and self.position_x+self.size_w > 670)):
                        self.position_y = 510 + self.size_l
                    elif self.position_y >= 353.75 and self.position_y - self.size_l <= 353.75 and self.position_x-self.size_w < 525 and self.position_x+self.size_w > 475:
                        self.position_y = 353.75 + self.size_l
                    elif self.position_y - self.step < self.size_l+CANVAS_SCORE:
                        self.position_y = self.size_l+CANVAS_SCORE
                    else:
                        self.position_y -= self.step
                    
                    if self.tank_orientation != 90:
                        if self.tank_orientation < 90:
                            self.tank_orientation += 7.5
                        elif self.tank_orientation <= 270:
                            self.tank_orientation -= 7.5
                        elif self.tank_orientation >= 360:
                            self.tank_orientation = 7.5
                        else:
                            self.tank_orientation += 7.5
                   
            elif self.mapa == 2:
                if self.tank_orientation == 270 and self.position_x - self.size_l < 50 and self.position_x > 50 and self.position_y+self.size_l >200 and self.position_y < 300:
                    self.position_y -= self.step
                elif self.tank_orientation == 270 and self.position_x - self.size_l < 250 and self.position_x > 250 and ((self.position_y +self.size_l > 112.5 and self.position_y  < 175) or (self.position_y +self.size_l > 237.5 and self.position_y+self.size_l  <= 330)):
                    self.position_y -= self.step
                elif self.tank_orientation == 270 and self.position_x - self.size_l < 70 and self.position_x > 70 and self.position_y +self.size_l > 370 and self.position_y+self.size_l  <= 462.5 :
                    self.position_y -= self.step
                elif self.tank_orientation == 270 and ((self.position_x - self.size_l < 50 and self.position_x > 50) or (self.position_x - self.size_l < 500 and self.position_x > 500)) and self.position_y +self.size_l > 500 and self.position_y+self.size_l  <= 600:
                    self.position_y -= self.step
                elif self.tank_orientation == 270 and self.position_x - self.size_l < 475 and self.position_x > 475 and self.position_y +self.size_l > 237.5 and self.position_y+self.size_l  <= 271 :
                    self.position_y -= self.step
                elif self.tank_orientation == 270 and self.position_x - self.size_l < 850 and self.position_x > 850 and self.position_y +self.size_l > 280 and self.position_y+self.size_l  <= 372.5:
                    self.position_y -= self.step
                elif self.tank_orientation == 270 and self.position_x - self.size_l < 750 and self.position_x > 750 and self.position_y +self.size_l > 475 and self.position_y+self.size_l  <= 537.5:
                    self.position_y -= self.step
                elif self.tank_orientation == 270 and self.position_x + self.size_l > 250 and self.position_x < 250 and self.position_y +self.size_l > 175 and self.position_y+self.size_l  <= 237.5:
                    self.position_y -= self.step
                elif self.tank_orientation == 270 and self.position_x + self.size_l > 150 and self.position_x < 150 and self.position_y +self.size_l > 370 and self.position_y+self.size_l  <= 462.5:
                    self.position_y -= self.step
                elif self.tank_orientation == 270 and self.position_x + self.size_l > 525 and self.position_x < 525 and self.position_y +self.size_l > 412.5 and self.position_y+self.size_l  <= 505:
                    self.position_y -= self.step
                elif self.tank_orientation == 270 and ((self.position_x + self.size_l > 450 and self.position_x < 450) or (self.position_x + self.size_l > 950 and self.position_x < 950)) and self.position_y +self.size_l > 150 and self.position_y+self.size_l  <= 242.5:
                    self.position_y -= self.step
                elif self.tank_orientation == 270 and self.position_x + self.size_l > 925 and self.position_x < 925 and self.position_y +self.size_l > 280 and self.position_y+self.size_l  <= 372.5:
                    self.position_y -= self.step
                elif self.tank_orientation == 270 and self.position_x + self.size_l > 950 and self.position_x < 950 and self.position_y +self.size_l > 450 and self.position_y+self.size_l  <= 542.5:
                    self.position_y -= self.step
                elif self.tank_orientation == 270 and self.position_x + self.size_l > 750 and self.position_x < 750 and ((self.position_y +self.size_l > 412 and self.position_y+self.size_l  <= 475) or (self.position_y +self.size_l > 537.5 and self.position_y+self.size_l  <= 600)):
                    self.position_y -= self.step
                ##
                elif self.tank_orientation == 270 and ((self.position_x + self.size_l > 125 and self.position_x < 125) or (self.position_x > 125 and self.position_x - self.size_l< 125)) and self.position_y > 112.5 and self.position_y+self.size_l  <= 237.5:
                    self.position_y -= self.step
                elif self.tank_orientation == 270 and ((self.position_x + self.size_l > 375 and self.position_x < 375) or (self.position_x  > 375 and self.position_x - self.size_l< 375)) and ((self.position_y  > 112.5 and self.position_y + self.size_l  < 175) or (self.position_y - self.size_l  > 175 and self.position_y + self.size_l  < 370)):
                    self.position_y -= self.step
                elif self.tank_orientation == 270 and ((self.position_x + self.size_l > 262.5 and self.position_x < 262.5) or (self.position_x>262.5 and self.position_x - self.size_l< 262.5)) and self.position_y - self.size_l  > 370 and self.position_y < 537.5:
                    self.position_y -= self.step
                elif self.tank_orientation == 270 and ((self.position_x + self.size_l > 625 and self.position_x < 625) or (self.position_x > 625 and self.position_x - self.size_l< 625)) and ((self.position_y  > 280 and self.position_y + self.size_l  < 412.5) or (self.position_y - self.size_l  > 412.5 and self.position_y + self.size_l  < 537.5)):
                    self.position_y -= self.step
                elif self.tank_orientation == 270 and ((self.position_x + self.size_l > 737.5 and self.position_x < 737.5) or (self.position_x >737.5 and self.position_x - self.size_l< 737.5)) and self.position_y  > 112.5 and self.position_y + self.size_l < 280:
                    self.position_y -= self.step
                elif self.tank_orientation == 270 and ((self.position_x + self.size_l > 875 and self.position_x < 875) or (self.position_x  > 875 and self.position_x - self.size_l< 875)) and self.position_y - self.size_l > 412 and self.position_y+self.size_l  <= 537.5:
                    self.position_y -= self.step
                elif self.tank_orientation == 270 and ((self.position_x + self.size_l > 100 and self.position_x < 100) or (self.position_x  > 100 and self.position_x - self.size_l< 100)) and ((self.position_y > 250  and self.position_y+self.size_l  < 300) or (self.position_y > 550  and self.position_y+self.size_l  < 600)):
                    self.position_y -= self.step   
                elif self.tank_orientation == 270 and ((self.position_x + self.size_l > 500 and self.position_x < 500) or (self.position_x > 500 and self.position_x - self.size_l< 500)) and ((self.position_y- self.size_l > 50  and self.position_y+self.size_l  < 150) or (self.position_y-self.size_l > 500  and self.position_y+self.size_l  < 600)):
                    self.position_y -= self.step
                elif self.tank_orientation == 270 and ((self.position_x + self.size_l > 900 and self.position_x < 900) or (self.position_x  > 900 and self.position_x - self.size_l< 900)) and ((self.position_y- self.size_l > 50  and self.position_y+self.size_l  < 100) or (self.position_y-self.size_l > 350  and self.position_y+self.size_l  < 400)):
                    self.position_y -= self.step
                elif self.tank_orientation == 270 and ((self.position_x + self.size_l > 400 and self.position_x < 400) or (self.position_x  > 400 and self.position_x - self.size_l< 400)) and self.position_y- self.size_l > 50  and self.position_y+self.size_l  < 100:
                    self.position_y -= self.step
                else:
                    if self.position_y >= 200 and self.position_y-self.size_l <= 200 and self.position_x-self.size_w < 50:
                        self.position_y = 200+self.size_l
                    elif self.position_y >= 237.5 and self.position_y-self.size_l <= 237.5 and ((self.position_x+self.size_w >= 125 and self.position_x-self.size_w < 250) or (self.position_x+self.size_w >= 375 and self.position_x-self.size_w < 475)):
                        self.position_y = 237.5+self.size_l
                    elif self.position_y >= 175 and self.position_y-self.size_l <= 175 and self.position_x+self.size_w > 250 and self.position_x-self.size_w <= 375:
                        self.position_y = 175+self.size_l
                    elif self.position_y >= 112.5 and self.position_y-self.size_l <= 112.5 and self.position_x+self.size_w >= 125 and self.position_x-self.size_w < 250:
                        self.position_y = 112.5+self.size_l
                    elif self.position_y >= 150 and self.position_y-self.size_l <= 150 and ((self.position_x+self.size_w > 450 and self.position_x-self.size_w <500) or (self.position_x+self.size_w > 950 and self.position_x-self.size_w <1000)):
                        self.position_y = 150+self.size_l
                    elif self.position_y > 100 and self.position_y-self.size_l <= 100 and self.position_x+self.size_w >=400 and self.position_x-self.size_w < 400:
                        self.position_y = 100+self.size_l
                    elif self.position_y > 370 and self.position_y-self.size_l <= 370 and ((self.position_x+self.size_w >= 150 and self.position_x-self.size_w < 375) or ( self.position_x-self.size_w < 70)):
                        self.position_y = 370+self.size_l
                    elif self.position_y > 300 and self.position_y - self.size_l <= 300 and self.position_x - self.size_w < 100:
                        self.position_y = 300 + self.size_l
                    elif self.position_y > 500 and self.position_y - self.size_l <= 500 and ((self.position_x-self.size_w < 50) or (self.position_x - self.size_w <= 550 and self.position_x + self.size_w >= 500)):
                        self.position_y = 500 + self.size_l
                    elif self.position_y > 537.5 and self.position_y - self.size_l <= 537.5 and ((self.position_x -self.size_w <= 262.5  and self.position_x + self.size_w >= 262.5) or (self.position_x + self.size_w >= 625 and self.position_x-self.size_w <= 625) or (self.position_x + self.size_w >= 750 and self.position_x-self.size_w <= 875)):
                        self.position_y = 537.5 + self.size_l
                    elif self.position_y > 412.5 and self.position_y - self.size_l <= 412.5 and ((self.position_x + self.size_w >= 525 and self.position_x-self.size_w <= 615) or (self.position_x + self.size_w >= 750 and self.position_x-self.size_w <= 875)):
                        self.position_y = 412.5 + self.size_l
                    elif self.position_y > 475 and self.position_y - self.size_l <= 475 and self.position_x + self.size_w >= 625 and self.position_x-self.size_w <= 750:
                        self.position_y = 475 + self.size_l
                    elif self.position_y > 450 and self.position_y - self.size_l <= 450 and self.position_x + self.size_w >= 950 and self.position_x-self.size_w <= 1000:
                        self.position_y = 450 + self.size_l
                    elif self.position_y > 400 and self.position_y - self.size_l <= 400 and self.position_x + self.size_w >= 900 and self.position_x-self.size_w <= 900:
                        self.position_y = 400 + self.size_l
                    elif self.position_y > 350 and self.position_y - self.size_l <= 350 and self.position_x + self.size_w >= 900 and self.position_x-self.size_w <= 1000:
                        self.position_y = 350 + self.size_l
                    elif self.position_y > 280 and self.position_y - self.size_l <= 280 and ((self.position_x + self.size_w >= 625 and self.position_x-self.size_w <= 850) or (self.position_x + self.size_w >= 925 and self.position_x-self.size_w <= 1000)) :
                        self.position_y = 280 + self.size_l
                    elif self.position_y > 150 and self.position_y - self.size_l <= 150 and self.position_x + self.size_w >= 950 and self.position_x-self.size_w <= 1000:
                        self.position_y = 150 + self.size_l
                    elif self.position_y > 100 and self.position_y - self.size_l <= 100 and self.position_x + self.size_w >= 900 and self.position_x-self.size_w <= 900:
                        self.position_y = 100 + self.size_l
                
                    elif self.position_y - self.step < self.size_l+CANVAS_SCORE:
                        self.position_y = self.size_l+CANVAS_SCORE
                    else:
                        self.position_y -= self.step
                    if self.tank_orientation != 90:
                        if self.tank_orientation < 90:
                            self.tank_orientation += 7.5
                        elif self.tank_orientation <= 270:
                            self.tank_orientation -= 7.5
                        elif self.tank_orientation >= 360:
                            self.tank_orientation = 7.5
                        else:
                            self.tank_orientation += 7.5    
        elif movement == 2:#derecha
            if self.mapa == 1:
                if self.tank_orientation == 180 and self.position_y < 140 and self.position_y + self.size_l >= 140 and ((self.position_x > 170 and self.position_x < 330) or (self.position_x > 670 and self.position_x < 830)):
                    self.position_x += self.step
                elif self.tank_orientation == 180 and self.position_y < 415 and self.position_y + self.size_l >= 415 and ((self.position_x > 170 and self.position_x < 330) or (self.position_x > 670 and self.position_x < 830)):
                    self.position_x += self.step
                elif self.tank_orientation == 180 and self.position_y < 271.25 and self.position_y + self.size_l >= 271.25 and self.position_x > 475 and self.position_x < 525:
                    self.position_x += self.step
                elif self.tank_orientation == 180 and self.position_y > 235 and self.position_y - self.size_l <= 235 and ((self.position_x > 170 and self.position_x < 330) or (self.position_x > 670 and self.position_x < 830)):
                    self.position_x += self.step
                elif self.tank_orientation == 180 and self.position_y > 510 and self.position_y - self.size_l <= 510 and ((self.position_x > 170 and self.position_x < 330) or (self.position_x > 670 and self.position_x < 830)):
                    self.position_x += self.step
                elif self.tank_orientation == 180 and self.position_y > 353.75 and self.position_y - self.size_l <= 353.75 and self.position_x > 475 and self.position_x < 525:
                    self.position_x += self.step
                else:
                    if self.position_x <= 100 and self.position_x+self.size_l >= 100 and (self.position_y-self.size_w < 120 or (self.position_y+self.size_w > 255 and self.position_y-self.size_w < 395) or self.position_y+self.size_w > 530):
                        self.position_x =100-self.size_l
                    elif self.position_x <= 400 and self.position_x+self.size_l >= 400 and (self.position_y-self.size_w < 120 or (self.position_y+self.size_w > 255 and self.position_y-self.size_w < 395) or self.position_y+self.size_w > 530):
                        self.position_x = 400-self.size_l
                    elif self.position_x <= 600 and self.position_x+self.size_l >= 600 and (self.position_y-self.size_w < 120 or (self.position_y+self.size_w > 255 and self.position_y-self.size_w < 395) or self.position_y+self.size_w > 530):
                        self.position_x = 600-self.size_l
                    elif self.position_x <= 900 and self.position_x+self.size_l >= 900 and (self.position_y-self.size_w < 120 or (self.position_y+self.size_w > 255 and self.position_y-self.size_w < 395) or self.position_y+self.size_w > 530):
                        self.position_x = 900-self.size_l
                    elif self.position_x <= 170 and self.position_x+self.size_l >= 170 and ((self.position_y+self.size_w > 140 and self.position_y-self.size_w < 235) or (self.position_y+self.size_w > 415 and self.position_y-self.size_w < 510)):
                        self.position_x = 170-self.size_l
                    elif self.position_x <= 670 and self.position_x+self.size_l >= 670 and ((self.position_y+self.size_w > 140 and self.position_y-self.size_w < 235) or (self.position_y+self.size_w > 415 and self.position_y-self.size_w < 510)):
                        self.position_x = 670-self.size_l
                    elif self.position_x <= 475 and self.position_x+self.size_l >= 475 and self.position_y+self.size_w > 271.25 and self.position_y-self.size_w < 353.75:
                        self.position_x = 475-self.size_l
                    elif self.position_x+self.step > CANVAS_WIDTH-self.size_l:
                        self.position_x = CANVAS_WIDTH-self.size_l
                    else:
                        self.position_x += self.step
                    if self.tank_orientation != 360:
                        if self.tank_orientation >= 180:
                            self.tank_orientation += 7.5
                        elif self.tank_orientation <= 7.5:
                            self.tank_orientation = 360
                        else:
                            self.tank_orientation -= 7.5
                    
            elif self.mapa == 2:
                if self.tank_orientation == 180 and ((self.position_y <= 112.5 and self.position_y + self.size_l >= 112.5) or (self.position_y >= 112.5 and self.position_y - self.size_l <= 112.5)) and self.position_x - self.size_l <= 250 and self.position_x + self.size_l >= 125:
                    self.position_x += self.step
                elif self.tank_orientation == 180 and ((self.position_y <= 175 and self.position_y + self.size_l >= 175) or (self.position_y >= 175 and self.position_y - self.size_l <= 175)) and self.position_x + self.size_l >= 250 and self.position_x + self.size_l <= 375:
                    self.position_x += self.step
                elif self.tank_orientation == 180 and ((self.position_y <= 237.5 and self.position_y + self.size_l >= 237.5) or (self.position_y >= 237.5 and self.position_y - self.size_l <= 237.5)) and ((self.position_x - self.size_l <= 250 and self.position_x >= 125) or (self.position_x - self.size_l <= 475 and self.position_x - self.size_l >= 375)):
                    self.position_x += self.step
                elif self.tank_orientation == 180 and ((self.position_y <= 200 and self.position_y + self.size_l >= 200) or (self.position_y >= 200 and self.position_y - self.size_l <= 200)) and self.position_x - self.size_l <= 50 and self.position_x >= 0:
                    self.position_x += self.step
                elif self.tank_orientation == 180 and ((self.position_y <= 300 and self.position_y + self.size_l >= 300) or (self.position_y >= 300 and self.position_y - self.size_l <= 300)) and self.position_x - self.size_l <= 100 and self.position_x >= 0:
                    self.position_x += self.step
                elif self.tank_orientation == 180 and ((self.position_y <= 370 and self.position_y + self.size_l >= 370) or (self.position_y >= 370 and self.position_y - self.size_l <= 370)) and ((self.position_x - self.size_l <= 70 and self.position_x >= 0) or (self.position_x + self.size_l <= 375 and self.position_x >=150)):
                    self.position_x += self.step
                elif self.tank_orientation == 180 and ((self.position_y <= 500 and self.position_y + self.size_l >= 500) or (self.position_y >= 500 and self.position_y - self.size_l <= 500)) and ((self.position_x - self.size_l <= 50 and self.position_x >= 0) or (self.position_x - self.size_l <= 550 and self.position_x >= 500)) :
                    self.position_x += self.step
                elif self.tank_orientation == 180 and self.position_y <= 550 and self.position_y + self.size_l >= 550 and self.position_x - self.size_l <= 100 and self.position_x + self.size_l >= 100 :
                    self.position_x += self.step
                elif self.tank_orientation == 180 and self.position_y >= 237.5 and self.position_y - self.size_l <= 237 and self.position_x - self.size_l <= 475 and self.position_x + self.size_l >= 375 :
                    self.position_x += self.step
                elif self.tank_orientation == 180 and ((self.position_y <= 412.5 and self.position_y + self.size_l >= 412.5) or (self.position_y >= 412.5 and self.position_y - self.size_l <= 412.5)) and self.position_x + self.size_l <= 625 and self.position_x > 525 :
                    self.position_x += self.step
                elif self.tank_orientation == 180 and ((self.position_y <= 150 and self.position_y + self.size_l >= 150) or (self.position_y >= 150 and self.position_y - self.size_l <= 150)) and ((self.position_x + self.size_l <= 500 and self.position_x + self.size_l >= 450) or (self.position_x <= 1000 and self.position_x + self.size_l >= 950)) :
                    self.position_x += self.step
                elif self.tank_orientation == 180 and self.position_y >= 100 and self.position_y - self.size_l <= 100 and ((self.position_x - self.size_l <= 400 and self.position_x>= 400) or (self.position_x - self.size_l <= 900 and self.position_x + self.size_l >= 900)) :
                    self.position_x += self.step
                elif self.tank_orientation == 180 and ((self.position_y <= 280 and self.position_y + self.size_l >= 280) or (self.position_y >= 280 and self.position_y - self.size_l <= 280)) and ((self.position_x - self.size_l <= 850 and self.position_x - self.size_l >= 737.5) or (self.position_x  <= 1000 and self.position_x >= 925) or (self.position_x + self.size_l <= 737.5 and self.position_x + self.size_l >= 625)) :
                    self.position_x += self.step
                elif self.tank_orientation == 180 and ((self.position_y <= 350 and self.position_y + self.size_l >= 350) or (self.position_y >= 350 and self.position_y - self.size_l <= 350)) and self.position_x - self.size_l <= 1000 and self.position_x >= 900:
                    self.position_x += self.step 
                elif self.tank_orientation == 180 and ((self.position_y <= 450 and self.position_y + self.size_l >= 450) or (self.position_y >= 450 and self.position_y - self.size_l <= 450)) and self.position_x - self.size_l <= 1000 and self.position_x >= 950:
                    self.position_x += self.step
                elif self.tank_orientation == 180 and self.position_y >= 400 and self.position_y - self.size_l <= 400 and self.position_x - self.size_l <= 900 and self.position_x >= 900:
                    self.position_x += self.step
                elif self.tank_orientation == 180 and ((self.position_y <= 412 and self.position_y + self.size_l >= 412) or (self.position_y >= 412 and self.position_y - self.size_l <= 412)) and self.position_x - self.size_l <= 875 and self.position_x +self.size_l >= 750:
                    self.position_x += self.step
                elif self.tank_orientation == 180 and ((self.position_y <= 537.5 and self.position_y + self.size_l >= 527.5) or (self.position_y >= 537.5 and self.position_y - self.size_l <= 537.5)) and ((self.position_x - self.size_l <= 875 and self.position_x + self.size_l >= 750) or (self.position_x - self.size_l <= 262.5 and self.position_x - self.size_l >= 262.5)):
                    self.position_x += self.step
                elif self.tank_orientation == 180 and ((self.position_y <= 475 and self.position_y + self.size_l >= 475) or (self.position_y >= 475 and self.position_y - self.size_l <= 475)) and self.position_x - self.size_l <= 750 and self.position_x - self.size_l >= 625 :
                    self.position_x += self.step
                    
                else:
                    if self.position_x < 100 and self.position_x+self.size_l >= 100 and ((self.position_y+self.size_w > 250 and self.position_y - self.size_w <= 300) or (self.position_y+self.size_w > 550 and self.position_y - self.size_w <= 600)):
                        self.position_x = 100-self.size_l
                    elif self.position_x < 125 and self.position_x+self.size_l >= 125 and self.position_y+self.size_w > 112.5 and self.position_y-self.size_w < 237.5:
                        self.position_x = 125-self.size_l
                    elif self.position_x < 375 and self.position_x+self.size_l >= 375 and self.position_y+self.size_w > 112.5 and self.position_y-self.size_w < 370:
                        self.position_x = 375 -self.size_l
                    elif self.position_x < 250 and self.position_x+self.size_l >= 250 and self.position_y+self.size_w >= 175 and self.position_y-self.size_w < 175:
                        self.posiiton_x = 250-self.size_l
                    elif self.position_x < 400 and self.position_x+self.size_l >= 400 and self.position_y-self.size_w <= 100 and self.position_y+self.size_w >= 0:
                        self.position_x = 400-self.size_l
                    elif self.position_x < 450 and self.position_x+self.size_l >= 450 and self.position_y-self.size_w <= 150 and self.position_y+self.size_w >= 150:
                        self.position_x = 450-self.size_l
                    elif self.position_x < 150 and self.position_y + self.size_l >= 150 and self.position_y-self.size_w < 370 and self.position_y+self.size_w > 370:
                        self.position_x = 150 - self.size_l
                    elif self.position_x < 262.5 and self.position_x + self.size_l >= 262.5 and self.position_y - self.size_w < 537.5 and self.position_y + self.size_w > 370:
                        self.position_x = 262.5 - self.size_l
                    elif self.position_x < 500 and self.position_x + self.size_l >= 500 and ((self.position_y+self.size_w >500) or (self.position_y - self.size_w <= 150 and self.position_y + self.size_w >= 50)):
                        self.position_x = 500 - self.size_l
                    elif self.position_x < 525 and self.position_x + self.size_l >= 525 and self.position_y - self.size_w <= 412.5 and self.position_y + self.size_w >= 412.5:
                        self.position_x = 525 - self.size_l
                    elif self.position_x < 625 and self.position_x + self.size_l >= 625 and self.position_y - self.size_w <= 537.5 and self.position_y + self.size_w >= 280:
                        self.position_x = 625 - self.size_l
                    elif self.position_x < 737.5 and self.position_x + self.size_l >= 737.5 and self.position_y - self.size_w <= 280 and self.position_y + self.size_w >= 112.5:
                        self.position_x = 737.5 - self.size_l
                    elif self.position_x < 900 and self.position_x + self.size_l >= 900 and ((self.position_y - self.size_w <= 100 and self.position_y + self.size_w >= 50) or (self.position_y - self.size_w <= 400 and self.position_y + self.size_w >= 350)):
                        self.position_x = 900 - self.size_l
                    elif self.position_x < 950 and self.position_x + self.size_l >= 950 and ((self.position_y - self.size_w <= 150 and self.position_y + self.size_w >= 150) or (self.position_y - self.size_w <= 450 and self.position_y + self.size_w >= 450)):
                        self.position_x = 950 - self.size_l
                    elif self.position_x < 925 and self.position_x + self.size_l >= 925 and self.position_y - self.size_w <= 280 and self.position_y + self.size_w >= 280:
                        self.position_x = 925 - self.size_l
                    elif self.position_x < 750 and self.position_x + self.size_l >= 750 and ((self.position_y - self.size_w <= 412 and self.position_y + self.size_w >= 412) or (self.position_y - self.size_w <= 537.5 and self.position_y + self.size_w >= 537.5)):
                        self.position_x = 750 - self.size_l
                    elif self.position_x < 875 and self.position_x + self.size_l >= 875 and self.position_y - self.size_w <= 537.5 and self.position_y + self.size_w >= 412:
                        self.position_x = 875 - self.size_l
                    elif self.position_x < 600 and self.position_x + self.size_l >= 600 and self.position_y - self.size_w <= 600 and self.position_y + self.size_w >= 550:
                        self.position_x = 600 - self.size_l
                    elif self.position_x+self.step> CANVAS_WIDTH-self.size_l:
                        self.position_x = CANVAS_WIDTH-self.size_l
                    else:
                        self.position_x += self.step
                    
                    if self.tank_orientation != 360:
                        if self.tank_orientation >= 180:
                            self.tank_orientation += 7.5
                        elif self.tank_orientation <= 7.5:
                            self.tank_orientation = 360
                        else:
                            self.tank_orientation -= 7.5
                 
        elif movement == 3:#abajo
            if self.mapa == 1:
                if self.tank_orientation == 90 and ((self.position_x <= 100 and self.position_x+ self.size_l >= 100) or (self.position_x <= 400 and self.position_x+ self.size_l >= 400) or (self.position_x <= 600 and self.position_x+ self.size_l >= 600) or (self.position_x <= 900 and self.position_x+ self.size_l >= 900)) and (self.position_y  < 120 or (self.position_y > 255 and self.position_y < 395) or self.position_y > 530) :
                    self.position_y += self.step
                elif self.tank_orientation == 90 and ((self.position_x >= 100 and self.position_x - self.size_l <= 100) or (self.position_x >= 400 and self.position_x - self.size_l <= 400) or (self.position_x >= 600 and self.position_x - self.size_l <= 600) or (self.position_x >= 900 and self.position_x - self.size_l <= 900)) and (self.position_y  < 120 or (self.position_y > 255 and self.position_y < 395) or self.position_y > 530):
                    self.position_y += self.step
                elif self.tank_orientation == 90 and ((self.position_x <= 170 and self.position_x + self.size_l >= 170) or (self.position_x <= 670 and self.position_x + self.size_l >= 670)) and self.position_y < 235 and self.position_y > 140:
                    self.position_y += self.step
                elif self.tank_orientation == 90 and ((self.position_x >= 330 and self.position_x - self.size_l <= 330) or (self.position_x >= 830 and self.position_x - self.size_l <= 830)) and self.position_y < 235 and self.position_y > 140:
                    self.position_y += self.step
                elif self.tank_orientation == 90 and ((self.position_x <= 170 and self.position_x + self.size_l >= 170) or (self.position_x <= 670 and self.position_x + self.size_l >= 670)) and self.position_y < 510 and self.position_y > 415:
                    self.position_y += self.step
                elif self.tank_orientation == 90 and ((self.position_x >= 330 and self.position_x - self.size_l <= 330) or (self.position_x >= 830 and self.position_x - self.size_l <= 830)) and self.position_y < 510 and self.position_y > 415:
                    self.position_y += self.step 
                elif self.tank_orientation == 90 and self.position_x <= 475 and self.position_x + self.size_l >= 475 and self.position_y < 353.75 and self.position_y > 271.25:
                    self.position_y += self.step
                elif self.tank_orientation == 90 and self.position_x >= 525 and self.position_x - self.size_l <= 525 and self.position_y  < 353.75 and self.position_y > 271.25:
                    self.position_y += self.step 
                else:
                    if self.position_y <= 255 and self.position_y + self.size_l >= 255 and ((self.position_x-self.size_w < 100 and self.position_x+self.size_w > 100) or (self.position_x-self.size_w < 400 and self.position_x+self.size_w > 400) or (self.position_x-self.size_w < 600 and self.position_x+self.size_w > 600) or (self.position_x-self.size_w < 900 and self.position_x+self.size_w > 900)):
                        self.position_y = 255 - self.size_l
                    elif self.position_y <= 530 and self.position_y + self.size_l >= 530 and ((self.position_x-self.size_w < 100 and self.position_x+self.size_w > 100) or (self.position_x-self.size_w < 400 and self.position_x+self.size_w > 400) or (self.position_x-self.size_w < 600 and self.position_x+self.size_w > 600) or (self.position_x-self.size_w < 900 and self.position_x+self.size_w > 900)):
                        self.position_y = 530 - self.size_l
                    elif self.position_y <= 325 and self.position_y + self.size_l >= 325 and (self.position_x+self.size_w <= 400 or self.position_x- self.size_w >= 600):
                        self.position_y = 325 - self.size_l
                    elif self.position_y <= 140 and self.position_y + self.size_l >= 140 and ((self.position_x-self.size_w < 330 and self.position_x+self.size_w > 170) or (self.position_x-self.size_w < 830 and self.position_x+self.size_w > 670)):
                        self.position_y = 140 - self.size_l
                    elif self.position_y <= 415 and self.position_y + self.size_l >= 415 and ((self.position_x-self.size_w < 330 and self.position_x+self.size_w > 170) or (self.position_x-self.size_w < 830 and self.position_x+self.size_w > 670)):
                        self.position_y = 415 - self.size_l
                    elif self.position_y <= 271.25 and self.position_y + self.size_l >= 271.25 and self.position_x-self.size_w < 525 and self.position_x+self.size_w > 475:
                        self.position_y = 271.25 - self.size_l
                    elif self.position_y+self.step > CANVAS_HEIGHT-self.size_l:
                        self.position_y = CANVAS_HEIGHT-self.size_l
                    else:
                        self.position_y += self.step
                        
                    if self.tank_orientation != 270:
                        if self.tank_orientation > 270:
                            self.tank_orientation -= 7.5
                        elif self.tank_orientation >= 90:
                            self.tank_orientation += 7.5
                        elif self.tank_orientation <= 7.5:
                            self.tank_orientation = 360
                        else:
                            self.tank_orientation -= 7.5
            
            elif self.mapa == 2:
                if self.tank_orientation == 90 and self.position_x - self.size_l < 50 and self.position_x > 50 and self.position_y > 137 and self.position_y < 300:
                    self.position_y += self.step
                elif self.tank_orientation == 90 and self.position_x - self.size_l < 250 and self.position_x > 250 and ((self.position_y  > 50 and self.position_y - self.size_l < 112.5) or (self.position_y  > 175 and self.position_y - self.size_l  < 237.5)):
                    self.position_y += self.step
                elif self.tank_orientation == 90 and self.position_x - self.size_l < 70 and self.position_x > 70 and self.position_y  > 307 and self.position_y - self.size_l  < 370 :
                    self.position_y += self.step
                elif self.tank_orientation == 90 and ((self.position_x - self.size_l < 50 and self.position_x > 50) or (self.position_x - self.size_l < 500 and self.position_x > 500)) and self.position_y  > 437 and self.position_y - self.size_l < 500:
                    self.position_y += self.step
                elif self.tank_orientation == 90 and self.position_x - self.size_l < 475 and self.position_x > 475 and self.position_y > 174.5 and self.position_y - self.size_l < 237.5:
                    self.position_y += self.step
                elif self.tank_orientation == 90 and ((self.position_x - self.size_l < 850 and self.position_x > 850) or (self.position_x + self.size_l > 925 and self.position_x < 925)) and self.position_y > 217 and self.position_y - self.size_l < 280:
                    self.position_y += self.step
                elif self.tank_orientation == 90 and self.position_x - self.size_l < 750 and self.position_x > 750 and ((self.position_y > 349 and self.position_y - self.size_l <412) or (self.position_y > 475 and self.position_y - self.size_l < 537.5)):
                    self.position_y += self.step
                elif self.tank_orientation == 90 and self.position_x - self.size_l < 900 and self.position_x > 900 and self.position_y > 400 and self.position_y - self.size_l < 450:
                    self.position_y += self.step
                elif self.tank_orientation == 90 and self.position_x + self.size_l > 250 and self.position_x < 250 and self.position_y > 112 and self.position_y - self.size_l  < 175:
                    self.position_y += self.step
                elif self.tank_orientation == 90 and self.position_x + self.size_l > 150 and self.position_x < 150 and self.position_y > 307 and self.position_y - self.size_l  < 370:
                    self.position_y += self.step
                elif self.tank_orientation == 90 and self.position_x + self.size_l > 525 and self.position_x < 525 and self.position_y > 349.5 and self.position_y - self.size_l  < 412.5 :
                    self.position_y += self.step
                elif self.tank_orientation == 90 and ((self.position_x + self.size_l > 450 and self.position_x < 450) or (self.position_x + self.size_l > 950 and self.position_x < 950)) and self.position_y > 50 and self.position_y - self.size_l  < 150:
                    self.position_y += self.step
                elif self.tank_orientation == 90 and self.position_x + self.size_l > 950 and self.position_x < 950 and self.position_y > 350 and self.position_y - self.size_l  < 450:
                    self.position_y += self.step
                elif self.tank_orientation == 90 and self.position_x + self.size_l > 750 and self.position_x < 750 and ((self.position_y  > 349 and self.position_y - self.size_l <412) or (self.position_y  > 475 and self.position_y+self.size_l  <537.5)):
                    self.position_y += self.step
                #
                elif self.tank_orientation == 90 and ((self.position_x + self.size_l > 125 and self.position_x < 125) or (self.position_x  > 125 and self.position_x - self.size_l< 125)) and self.position_y > 112.5 and self.position_y+self.size_l  <= 237.5:
                    self.position_y += self.step
                elif self.tank_orientation == 90 and ((self.position_x + self.size_l > 375 and self.position_x < 375) or (self.position_x  > 375 and self.position_x - self.size_l< 375)) and ((self.position_y  > 112.5 and self.position_y + self.size_l  < 175) or (self.position_y - self.size_l  > 175 and self.position_y + self.size_l  < 370)):
                    self.position_y += self.step
                elif self.tank_orientation == 90 and ((self.position_x + self.size_l > 262.5 and self.position_x < 262.5) or (self.position_x >262.5 and self.position_x - self.size_l < 262.5)) and self.position_y - self.size_l  > 370 and self.position_y < 537.5:
                    self.position_y += self.step
                elif self.tank_orientation == 90 and ((self.position_x + self.size_l > 625 and self.position_x < 625) or (self.position_x  > 625 and self.position_x - self.size_l < 625)) and ((self.position_y  > 280 and self.position_y + self.size_l  < 412.5) or (self.position_y - self.size_l  > 412.5 and self.position_y + self.size_l  < 537.5)):
                    self.position_y += self.step
                elif self.tank_orientation == 90 and ((self.position_x + self.size_l > 737.5 and self.position_x < 737.5) or (self.position_x  >737.5 and self.position_x- self.size_l < 737.5)) and self.position_y  > 112.5 and self.position_y + self.size_l < 280:
                    self.position_y += self.step
                elif self.tank_orientation == 90 and ((self.position_x + self.size_l > 875 and self.position_x < 875) or (self.position_x  > 875 and self.position_x - self.size_l < 875)) and self.position_y - self.size_l > 412 and self.position_y+self.size_l  <= 537.5:
                    self.position_y += self.step
                elif self.tank_orientation == 270 and ((self.position_x + self.size_l > 100 and self.position_x < 100) or (self.position_x > 100 and self.position_x - self.size_l < 100)) and ((self.position_y > 250  and self.position_y+self.size_l  < 300) or (self.position_y > 550  and self.position_y+self.size_l  < 600)):
                    self.position_y += self.step   
                elif self.tank_orientation == 90 and ((self.position_x + self.size_l > 500 and self.position_x < 500) or (self.position_x > 500 and self.position_x - self.size_l < 500)) and ((self.position_y- self.size_l > 50  and self.position_y+self.size_l  < 150) or (self.position_y-self.size_l > 500  and self.position_y+self.size_l  < 600)):
                    self.position_y += self.step
                elif self.tank_orientation == 90 and ((self.position_x + self.size_l > 900 and self.position_x < 900) or (self.position_x > 900 and self.position_x - self.size_l< 900)) and ((self.position_y- self.size_l > 50  and self.position_y+self.size_l  < 100) or (self.position_y-self.size_l > 350  and self.position_y+self.size_l  < 400)):
                    self.position_y += self.step
                elif self.tank_orientation == 90 and ((self.position_x + self.size_l > 400 and self.position_x < 400) or (self.position_x  > 400 and self.position_x - self.size_l< 400)) and self.position_y- self.size_l > 50  and self.position_y+self.size_l  < 100:
                    self.position_y += self.step
                else:
                    if self.position_y < 200 and self.position_y+self.size_l >= 200 and self.position_x-self.size_w < 50:#derecha
                        self.position_y = 200-self.size_l
                    elif self.position_y < 250 and self.position_y+self.size_l >= 250 and self.position_x +self.size_w >=100 and self.position_x-self.size_w <=100:#raya cuadradoabajo dr
                        self.position_y=250-self.size_l
                    elif self.position_y < 112.5 and self.position_y+self.size_l >= 112.5 and ((self.position_x+self.size_w > 125 and self.position_x-self.size_w < 250) or (self.position_x+self.size_w >= 375 and self.position_x-self.size_w < 375) or (self.position_x+self.size_w >= 737.5 and self.position_x-self.size_w < 737.5)):
                        self.position_y = 112.5-self.size_l
                    elif self.position_y < 175 and self.position_y+self.size_l >= 175 and self.position_x+self.size_w > 250 and self.position_x-self.size_w < 375:#raya central central
                        self.position_y = 175 - self.size_l
                    elif self.position_y < 237.5 and self.position_y+self.size_l >= 237.5 and ((self.position_x-self.size_w < 250 and self.position_x+self.size_w > 125) or (self.position_x+self.size_w >= 375 and self.position_x-self.size_w < 475)):
                        self.position_y = 237.5-self.size_l
                    elif self.position_y < 150 and self.position_y+self.size_l >= 150 and ((self.position_x + self.size_w > 450 and self.position_x - self.size_w <= 500)or (self.position_x + self.size_w > 950 and self.position_x - self.size_w <= 1000)):
                        self.position_y = 150 - self.size_l
                    elif self.position_y < 370 and self.position_y + self.size_l >= 370 and ((self.position_x + self.size_w > 0 and self.position_x - self.size_w <= 70) or (self.position_x + self.size_w > 150 and self.position_x - self.size_w <= 375)):
                        self.position_y = 370 - self.size_l
                    elif self.position_y < 500 and self.position_y + self.size_l >= 500 and ((self.position_x + self.size_w > 0 and self.position_x - self.size_w <= 50) or (self.position_x + self.size_w > 500 and self.position_x - self.size_w <= 550)):
                        self.position_y = 500 - self.size_l
                    elif self.position_y < 412.5 and self.position_y + self.size_l >= 412.5 and ((self.position_x + self.size_w > 525 and self.position_x - self.size_w <= 625) or (self.position_x + self.size_w > 750 and self.position_x - self.size_w <= 875)):
                        self.position_y = 412.5 - self.size_l
                    elif self.position_y < 280 and self.position_y + self.size_l >= 280 and ((self.position_x + self.size_w > 625 and self.position_x - self.size_w <= 850) or (self.position_x + self.size_w > 925 and self.position_x - self.size_w <= 1000)):
                        self.position_y = 280 - self.size_l
                    elif self.position_y < 550 and self.position_y + self.size_l >= 550 and ((self.position_x + self.size_w > 100 and self.position_x - self.size_w <= 100) or (self.position_x + self.size_w > 600 and self.position_x - self.size_w <= 600)):
                        self.position_y = 550 - self.size_l
                    elif self.position_y < 350 and self.position_y + self.size_l >= 350 and self.position_x + self.size_w > 900 and self.position_x - self.size_w <= 1000:
                        self.position_y = 350 - self.size_l
                    elif self.position_y < 450 and self.position_y + self.size_l >= 450 and self.position_x + self.size_w > 950 and self.position_x - self.size_w <= 1000:
                        self.position_y = 450 - self.size_l
                    elif self.position_y < 475 and self.position_y + self.size_l >= 475 and self.position_x + self.size_w > 625 and self.position_x - self.size_w <= 750:
                        self.position_y = 475 - self.size_l
                    elif self.position_y < 537.5 and self.position_y + self.size_l >= 537.5 and self.position_x + self.size_w > 750 and self.position_x - self.size_w <= 875:
                        self.position_y = 537.5 - self.size_l
                    elif self.position_y < 300 and self.position_y + self.size_l >= 300 and  self.position_x - self.size_w <= 100:
                        self.position_y = 300 - self.size_l
                    elif self.position_y+self.step > CANVAS_HEIGHT-self.size_l:
                        self.position_y = CANVAS_HEIGHT-self.size_l
                    else:
                        self.position_y += self.step
                   
                    if self.tank_orientation != 270:
                        if self.tank_orientation > 270:
                            self.tank_orientation -= 7.5
                        elif self.tank_orientation >= 90:
                            self.tank_orientation += 7.5
                        elif self.tank_orientation <= 7.5:
                            self.tank_orientation = 360
                        else:
                            self.tank_orientation -= 7.5
                            
        elif movement == 4:#izquierda
            if self.mapa == 1:
                if self.tank_orientation == 360 and self.position_y < 140 and self.position_y + self.size_l >= 140 and ((self.position_x > 170 and self.position_x < 330) or (self.position_x > 670 and self.position_x < 830)):
                    self.position_x -= self.step
                elif self.tank_orientation == 360 and self.position_y < 415 and self.position_y + self.size_l >= 415 and ((self.position_x > 170 and self.position_x < 330) or (self.position_x > 670 and self.position_x < 830)):
                    self.position_x -= self.step
                elif self.tank_orientation == 360 and self.position_y < 271.25 and self.position_y + self.size_l >= 271.25 and self.position_x > 475 and self.position_x < 525:
                    self.position_x -= self.step
                elif self.tank_orientation == 360 and self.position_y > 235 and self.position_y - self.size_l <= 235 and ((self.position_x > 170 and self.position_x < 330) or (self.position_x > 670 and self.position_x < 830)):
                    self.position_x -= self.step
                elif self.tank_orientation == 360 and self.position_y > 510 and self.position_y - self.size_l <= 510 and ((self.position_x > 170 and self.position_x < 330) or (self.position_x > 670 and self.position_x < 830)):
                    self.position_x -= self.step
                elif self.tank_orientation == 360 and self.position_y > 353.75 and self.position_y - self.size_l <= 353.75 and self.position_x > 475 and self.position_x < 525:
                    self.position_x -= self.step
                else:
                    if self.position_x >= 400 and self.position_x-self.size_l <= 400 and (self.position_y-self.size_w <= 120 or (self.position_y+self.size_w > 255 and self.position_y-self.size_w < 395) or self.position_y+self.size_w > 530):
                        self.position_x=400+self.size_l
                    elif self.position_x >= 100 and self.position_x-self.size_l <= 100 and (self.position_y-self.size_w <= 120 or (self.position_y+self.size_w > 255 and self.position_y-self.size_w < 395) or self.position_y+self.size_w > 530):
                        self.position_x = 100+self.size_l
                    elif self.position_x >= 600 and self.position_x-self.size_l <= 600 and (self.position_y-self.size_w <= 120 or (self.position_y+self.size_w > 255 and self.position_y-self.size_w < 395) or self.position_y+self.size_w > 530):
                        self.position_x = 600+self.size_l
                    elif self.position_x >= 900 and self.position_x-self.size_l <= 900 and (self.position_y-self.size_w <= 120 or (self.position_y+self.size_w > 255 and self.position_y-self.size_w < 395) or self.position_y+self.size_w > 530):
                        self.position_x = 900+self.size_l
                    elif self.position_x >= 330 and self.position_x-self.size_l <= 330  and ((self.position_y-self.size_w < 235 and self.position_y+self.size_w > 140) or (self.position_y+self.size_w > 415 and self.position_y-self.size_w < 510)):
                        self.position_x = 330 + self.size_l
                
                    elif self.position_x >= 830 and self.position_x - self.size_l <= 830 and ((self.position_y+self.size_w > 140 and self.position_y-self.size_w < 235) or (self.position_y+self.size_w > 415 and self.position_y-self.size_w < 510)):
                        self.position_x = 830 + self.size_l
                    elif self.position_x >= 525 and self.position_x - self.size_l <= 525 and self.position_y+self.size_w > 271.25 and self.position_y-self.size_w < 353.75:
                        self.position_x = 525 + self.size_l
                    elif self.position_x-self.step < self.size_l:
                        self.position_x = self.size_l
                    else:
                        self.position_x -= self.step
                        
                    if self.tank_orientation != 180:
                        if self.tank_orientation < 180:
                            self.tank_orientation += 7.5
                        else:
                            self.tank_orientation -= 7.5
                  
            elif self.mapa == 2:
                if self.tank_orientation == 360 and ((self.position_y <= 112.5 and self.position_y + self.size_l >= 112.5) or (self.position_y >= 112.5 and self.position_y - self.size_l <= 112.5)) and ((self.position_x - self.size_l <= 250 and self.position_x + self.size_l >= 125) or (self.position_x - self.size_l <= 737.5 and self.position_x + self.size_l >= 737.5)):
                    self.position_x -= self.step
                elif self.tank_orientation == 360 and ((self.position_y <= 175 and self.position_y + self.size_l >= 175) or (self.position_y >= 175 and self.position_y - self.size_l <= 175)) and self.position_x + self.size_l >= 250 and self.position_x + self.size_l <= 375:
                    self.position_x -= self.step
                elif self.tank_orientation == 360 and ((self.position_y <= 237.5 and self.position_y + self.size_l >= 237.5) or (self.position_y >= 237.5 and self.position_y - self.size_l <= 237.5)) and ((self.position_x - self.size_l <= 250 and self.position_x >= 125) or (self.position_x - self.size_l <= 475 and self.position_x - self.size_l >= 375)):
                    self.position_x -= self.step
                elif self.tank_orientation == 360 and ((self.position_y <= 200 and self.position_y + self.size_l >= 200) or (self.position_y >= 200 and self.position_y - self.size_l <= 200)) and self.position_x - self.size_l <= 50 and self.position_x >= 0:
                    self.position_x -= self.step
                elif self.tank_orientation == 360 and ((self.position_y <= 300 and self.position_y + self.size_l >= 300) or (self.position_y >= 300 and self.position_y - self.size_l <= 300)) and self.position_x - self.size_l <= 100 and self.position_x >= 0:
                    self.position_x -= self.step
                elif self.tank_orientation == 360 and ((self.position_y <= 370 and self.position_y + self.size_l >= 370) or (self.position_y >= 370 and self.position_y - self.size_l <= 370)) and ((self.position_x - self.size_l <= 70 and self.position_x >= 0) or (self.position_x + self.size_l <= 375 and self.position_x + self.size_l >=150)):
                    self.position_x -= self.step
                elif self.tank_orientation == 360 and ((self.position_y <= 500 and self.position_y + self.size_l >= 500) or (self.position_y >= 500 and self.position_y - self.size_l <= 500)) and ((self.position_x - self.size_l <= 50 and self.position_x >= 0) or (self.position_x - self.size_l <= 550 and self.position_x >= 500)) :
                    self.position_x -= self.step
                elif self.tank_orientation == 360 and self.position_y <= 550 and self.position_y + self.size_l >= 550 and self.position_x - self.size_l <= 100 and self.position_x + self.size_l >= 100 :
                    self.position_x -= self.step
                elif self.tank_orientation == 360 and self.position_y >= 237.5 and self.position_y - self.size_l <= 237 and self.position_x - self.size_l <= 475 and self.position_x + self.size_l >= 375 :
                    self.position_x -= self.step
                elif self.tank_orientation == 360 and ((self.position_y <= 412.5 and self.position_y + self.size_l >= 412.5) or (self.position_y >= 412.5 and self.position_y - self.size_l <= 412.5)) and self.position_x + self.size_l <= 625 and self.position_x + self.size_l > 525 :
                    self.position_x -= self.step
                elif self.tank_orientation == 360 and ((self.position_y <= 150 and self.position_y + self.size_l >= 150) or (self.position_y >= 150 and self.position_y - self.size_l <= 150)) and ((self.position_x + self.size_l <= 500 and self.position_x + self.size_l >= 450) or (self.position_x <= 1000 and self.position_x + self.size_l >= 950)) :
                    self.position_x -= self.step
                elif self.tank_orientation == 360 and self.position_y >= 100 and self.position_y - self.size_l <= 100 and ((self.position_x - self.size_l <= 400 and self.position_x>= 400) or (self.position_x - self.size_l <= 900 and self.position_x + self.size_l >= 900)) :
                    self.position_x -= self.step
                elif self.tank_orientation == 360 and ((self.position_y <= 280 and self.position_y + self.size_l >= 280) or (self.position_y >= 280 and self.position_y - self.size_l <= 280)) and ((self.position_x - self.size_l <= 850 and self.position_x - self.size_l >= 737.5) or (self.position_x  <= 1000 and self.position_x + self.size_l >= 925) or (self.position_x + self.size_l <= 737.5 and self.position_x + self.size_l >= 625)) :
                    self.position_x -= self.step
                elif self.tank_orientation == 360 and ((self.position_y <= 350 and self.position_y + self.size_l >= 350) or (self.position_y >= 350 and self.position_y - self.size_l <= 350)) and self.position_x - self.size_l <= 1000 and self.position_x >= 900:
                    self.position_x -= self.step 
                elif self.tank_orientation == 360 and ((self.position_y <= 450 and self.position_y + self.size_l >= 450) or (self.position_y >= 450 and self.position_y - self.size_l <= 450)) and self.position_x - self.size_l <= 1000 and self.position_x >= 950:
                    self.position_x -= self.step
                elif self.tank_orientation == 360 and self.position_y >= 400 and self.position_y - self.size_l <= 400 and self.position_x - self.size_l <= 900 and self.position_x >= 900:
                    self.position_x -= self.step
                elif self.tank_orientation == 360 and ((self.position_y <= 412 and self.position_y + self.size_l >= 412) or (self.position_y >= 412 and self.position_y - self.size_l <= 412)) and self.position_x - self.size_l <= 875 and self.position_x +self.size_l >= 750:
                    self.position_x -= self.step
                elif self.tank_orientation == 360 and ((self.position_y <= 537.5 and self.position_y + self.size_l >= 527.5) or (self.position_y >= 537.5 and self.position_y - self.size_l <= 537.5)) and ((self.position_x - self.size_l <= 875 and self.position_x + self.size_l >= 750) or (self.position_x - self.size_l <= 262.5 and self.position_x + self.size_l >= 262.5)):
                    self.position_x -= self.step
                elif self.tank_orientation == 360 and ((self.position_y <= 475 and self.position_y + self.size_l >= 475) or (self.position_y >= 475 and self.position_y - self.size_l <= 475)) and self.position_x - self.size_l <= 750 and self.position_x - self.size_l >= 625 :
                    self.position_x -= self.step
                else:
                    if self.position_x > 50 and self.position_x-self.size_l <= 50 and ((self.position_y+self.size_w >= 200 and self.position_y-self.size_w <=200) or (self.position_y+self.size_w >= 500 and self.position_y-self.size_w <=500)):
                        self.poosition_x = 50 + self.size_l
                    elif self.position_x > 100 and self.position_x - self.size_l <= 100 and ((self.position_y+self.size_w >= 250 and self.position_y-self.size_w <=300) or (self.position_y+self.size_w >= 550 and self.position_y-self.size_w <=600)):
                        self.position_x = 100 + self.size_l
                    elif self.position_x > 125 and self.position_x-self.size_l <= 125 and self.position_y-self.size_w <237.5 and self.position_y+self.size_w > 112.5: 
                        self.position_x = 125+self.size_l
                    elif self.position_x > 250 and self.position_x-self.size_l <= 250 and ((self.position_y-self.size_w < 112.5 and self.position_y+self.size_w > 112.5) or(self.position_y-self.size_w < 237.5 and self.position_y+self.size_w > 237.5)):
                        self.position_x = 250 + self.size_l
                    elif self.position_x > 375 and self.position_x - self.size_l <= 375 and self.position_y-self.size_w <370 and self.position_y+self.size_w > 112.5:
                        self.position_x = 375 + self.size_l
                    elif self.position_x > 400 and self.position_x - self.size_l <= 400 and self.position_y-self.size_w < 100:
                        self.position_x = 400+self.size_l
                    elif self.position_x > 70 and self.position_x - self.size_l <= 70 and self.position_y - self.size_w < 370  and self.position_y+self.size_w > 370:
                        self.position_x = 70+self.size_l
                    elif self.position_x > 262.5 and self.position_x - self.size_l <= 262.5 and self.position_y-self.size_w < 537.5 and self.position_y+self.size_w > 370:
                        self.position_x = 262.5+self.size_l
                    elif self.position_x > 475 and self.position_x - self.size_l <= 475 and self.position_y-self.size_w < 237.5 and self.position_y+self.size_w > 237.5:
                        self.position_x = 475+self.size_l
                    elif self.position_x > 550 and self.position_x - self.size_l <= 550 and self.position_y-self.size_w < 500 and self.position_y+self.size_w > 500:
                        self.position_x = 550+self.size_l
                    elif self.position_x > 600 and self.position_x - self.size_l <= 600 and self.position_y-self.size_w < 600 and self.position_y+self.size_w > 550:
                        self.position_x = 600+self.size_l
                    elif self.position_x > 500 and self.position_x - self.size_l <= 500 and ((self.position_y-self.size_w < 600 and self.position_y+self.size_w > 500)or(self.position_y-self.size_w < 150 and self.position_y+self.size_w > 50)):
                        self.position_x = 500+self.size_l
                    elif self.position_x > 900 and self.position_x - self.size_l <= 900 and ((self.position_y-self.size_w < 150 and self.position_y+self.size_w > 50)or(self.position_y-self.size_w < 400 and self.position_y+self.size_w > 350)):
                        self.position_x = 900+self.size_l
                    elif self.position_x > 737.5 and self.position_x - self.size_l <= 737.5 and self.position_y-self.size_w < 280 and self.position_y+self.size_w > 112.5:
                        self.position_x = 737.5+self.size_l
                    elif self.position_x > 850 and self.position_x - self.size_l <= 850 and self.position_y-self.size_w < 280 and self.position_y+self.size_w > 280:
                        self.position_x = 850+self.size_l
                    elif self.position_x > 625 and self.position_x - self.size_l <= 625  and self.position_y-self.size_w < 537.5 and self.position_y+self.size_w > 280:
                        self.position_x = 625 +self.size_l
                    elif self.position_x > 750 and self.position_x - self.size_l <= 750  and self.position_y-self.size_w < 475 and self.position_y+self.size_w > 475:
                        self.position_x = 750 +self.size_l
                    elif self.position_x > 875 and self.position_x - self.size_l <= 875  and self.position_y-self.size_w < 537.5 and self.position_y+self.size_w > 412:
                        self.position_x = 875 +self.size_l
                    elif self.position_x-self.step < self.size_l:
                        self.position_x = self.size_l
                    else:
                        self.position_x -= self.step
                   
                    if self.tank_orientation != 180:
                        if self.tank_orientation < 180:
                            self.tank_orientation += 7.5
                        else:
                            self.tank_orientation -= 7.5



           
class BulletClass:
    def __init__(self, team, position_x, position_y, target_x, target_y):
        self.velocity = 3
        self.team = team
        self.position_x = position_x
        self.position_y = position_y
        distance_x = target_x - position_x
        distance_y = target_y - position_y
        self.bounce = 0
        module = math.sqrt(distance_x**2 + distance_y**2)
        self.increment_x = float(distance_x)/module*self.velocity
        self.increment_y = float(distance_y)/module*self.velocity

    def move(self,mapa):
        """
        Output: Si se debe mantener la bala o no, es decir, si aún no ha chocado 2 veces.
        """
        newX = self.position_x + self.increment_x
        newY = self.position_y + self.increment_y
        if mapa == 1:
            if self.bounce==2:
                return False
            
            elif self.position_x <= 100 and newX >= 100 and (newY <= 120 or (newY >= 255 and newY <= 395) or newY >= 530):
                self.bounce += 1
                self.position_x = 200-newX
                self.increment_x *= -1
            
            elif self.position_x <= 400 and newX >= 400 and (newY <= 120 or (newY >= 255 and newY <= 395) or newY >= 530):
                self.bounce += 1
                self.position_x = 800-newX
                self.increment_x *= -1
            
            elif self.position_x <= 600 and newX >= 600 and (newY <= 120 or (newY >= 255 and newY <= 395) or newY >= 530):
                self.bounce += 1
                self.position_x = 1200-newX
                self.increment_x *= -1
                
            elif self.position_x <= 900 and newX >= 900 and (newY <= 120 or (newY >= 255 and newY <= 395) or newY >= 530):
                self.bounce += 1
                self.position_x = 1800-newX
                self.increment_x *= -1
                
            elif self.position_x >= 105 and newX <= 105 and (newY <= 120 or (newY >= 255 and newY <= 395) or newY >= 530):
                self.bounce += 1
                self.position_x = 210-newX
                self.increment_x *= -1
            
            elif self.position_x >= 405 and newX <= 405 and (newY <= 120 or (newY >= 255 and newY <= 395) or newY >= 530):
                self.bounce += 1
                self.position_x = 810-newX
                self.increment_x *= -1
            
            elif self.position_x >= 605 and newX <= 605 and (newY <= 120 or (newY >= 255 and newY <= 395) or newY >= 530):
                self.bounce += 1
                self.position_x = 1210-newX
                self.increment_x *= -1
                
            elif self.position_x >= 905 and newX <= 905 and (newY <= 120 or (newY >= 255 and newY <= 395) or newY >= 530):
                self.bounce += 1
                self.position_x = 1810-newX
                self.increment_x *= -1
                
            elif self.position_x <= 170 and newX >= 170 and ((newY >= 140 and newY <= 230) or (newY >= 415 and newY <= 510)):
                self.position_x = 340-newX
                self.bounce +=1
                self.increment_x *= -1
                
            elif self.position_x <= 670 and newX >= 670 and ((newY >= 140 and newY <= 230) or (newY >= 415 and newY <= 510)):
                self.position_x = 1340 - newX
                self.bounce +=1
                self.increment_x *= -1
            
            elif self.position_x >= 330 and newX <= 330 and ((newY > 140 and newY < 230) or (newY > 415 and newY < 510)):
                self.position_x = 660-newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_x >= 830 and newX <= 830 and ((newY > 140 and newY < 230) or (newY > 415 and newY < 510)):
                self.position_x = 1660-newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_x >= 525 and newX <= 525 and newY > 271.25 and newY < 353.75:
                self.position_x = 1050-newX
                self.bounce += 1
                self.increment_x *= -1
            
            elif self.position_x <= 475 and newX >= 475 and newY > 271.25 and newY < 353.75:
                self.position_x = 950-newX
                self.bounce += 1
                self.increment_x *= -1
            
            elif newX > CANVAS_WIDTH:
                self.position_x = 2*CANVAS_WIDTH - newX
                self.bounce += 1
                self.increment_x *= -1
            
            elif newX < 0:
                self.position_x = abs(newX)+5
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_y >= 235 and newY <= 235 and ((newX >= 170 and newX <= 330) or (newX >= 670 and newX <= 830)):
                self.position_y = 470-newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_y >= 510 and newY <= 510 and ((newX >= 170 and newX <= 330) or (newX >= 670 and newX <= 830)):
                self.position_y = 1020 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_y <= 140 and newY >= 140 and ((newX >= 170 and newX <= 330) or (newX >= 670 and newX <= 830)):
                self.position_y = 280-newY
                self.bounce+=1
                self.increment_y *= -1
                
            elif self.position_y <= 415 and newY >= 415 and ((newX >= 170 and newX <= 330) or (newX >= 670 and newX <= 830)):
                self.position_y = 280-newY
                self.bounce+=1
                self.increment_y *= -1
                
            elif self.position_y < 325 and newY >= 325 and (newX < 400 or newX > 600):
                self.position_y = 650-newY
                self.bounce+=1
                self.increment_y *= -1
                
            elif self.position_y > 325 and newY <= 325 and (newX < 400 or newX > 600):
                self.position_y = 650-newY
                self.bounce+=1
                self.increment_y *= -1
                
            elif self.position_y <= 271.25 and newY >= 271.25 and newX >= 475 and newX <= 525:
                self.position_y = 542.5 -newY
                self.bounce+=1
                self.increment_y *= -1
                
            elif self.position_y >= 353.75 and newY <= 353.75 and newX >= 475 and newX <= 525:
                self.position_y = 707.5 -newY
                self.bounce+=1
                self.increment_y *= -1
                
            elif newY > CANVAS_HEIGHT:
                self.position_y = 2*CANVAS_HEIGHT - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif newY < CANVAS_SCORE:
                self.position_y = 2*CANVAS_SCORE-newY+5
                self.bounce += 1
                self.increment_y *= -1
            else:
                self.position_x = newX
                self.position_y = newY
            return True
        
        elif mapa == 2:
            if self.bounce==2:
                return False
            
            elif self.position_y >= 205 and newY <= 205 and newX < 50:
                self.position_y = 410 - newY
                self.bounce += 1
                self.increment_y *= -1
            
            elif self.position_y <= 200 and newY >= 200 and newX<50:
                self.position_y = 400 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_x <= 100 and newX >= 100 and ((newY>= 250 and newY <= 300) or (newY >= 550 and newY <= 600)):
                self.position_x = 200 - newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_x >= 105 and newX <= 105 and ((newY>= 250 and newY <= 300) or (newY >= 550 and newY <= 600)):
                self.position_x = 210 - newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_x <= 125 and newX >= 125 and newY < 237.5 and newY>= 112.5:
                self.position_x = 250 - newX
                self.bounce += 1
                self.increment_x *= -1
            
            elif self.position_x >= 130 and newX <= 130 and newY < 237.5 and newY >= 112.5:
                self.position_x = 260 - newX
                self.bounce += 1
                self.increment_x *= -1
                    
            elif self.position_y <= 112.5 and newY >= 112.5 and newX >= 125 and newX <= 250:
                self.position_y = 225 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_y >= 117.5 and newY <= 117.5 and newX >= 125 and newX <= 250:
                self.position_y = 235 - newY
                self.bounce += 1
                self.increment_y *= -1
            
            elif self.position_y <= 237.5 and newY >= 237.5  and newX >= 125 and newX <= 250:
                self.position_y = 475 - newY
                self.bounce += 1
                self.increment_y *= -1
            
            elif self.position_y >= 242.5 and newY <= 242.5 and newX >= 125 and newX <= 250:
                self.position_y = 485 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_y <= 175 and newY >= 175 and newX >= 250 and newX <= 375:
                self.position_y = 350 - newY
                self.bounce += 1
                self.increment_y *= -1
            
            elif self.position_y >= 180 and newY <= 180 and newX >= 250 and newX <= 375:
                self.position_y = 360 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_x <= 375 and newX >= 375 and newY >= 112.5 and newY <= 370:
                self.position_x = 750 - newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_x >= 380 and newX <= 380 and newY >= 112.5 and newY <= 370:
                self.position_x = 760 - newX
                self.bounce += 1
                self.increment_x *= -1
            
            elif self.position_x <= 400 and newX >= 400 and newY <= 112.5:
                self.position_x = 800 - newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_x >= 405 and newX <= 405 and newY <= 112.5:
                self.position_x = 810 - newX
                self.bounce += 1
                self.increment_x *= -1
            
            elif self.position_y <= 150 and newY >= 150  and ((newX >= 450 and newX <= 500) or (newX>= 950)):
                self.position_y = 300 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_y >= 155 and newY <= 155 and ((newX >= 450 and newX <= 500) or (newX>= 950)):
                self.position_y = 310 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_y <= 370 and newY >= 370  and ((newX >= 150 and newX <= 375) or (newX<=70)):
                self.position_y = 740 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_y >= 375 and newY <= 375 and ((newX >= 150 and newX <= 375) or (newX<=70)):
                self.position_y = 750 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_y <= 500 and newY >= 500 and ((newX >= 500 and newX <= 550) or (newX<=50)):
                self.position_y = 1000 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_y >= 505 and newY <= 505 and ((newX >= 500 and newX <= 550) or (newX<=50)):
                self.position_y = 1010 - newY
                self.bounce += 1
                self.increment_y *= -1
            
            elif self.position_x <= 262.5 and newX >= 262.5 and newY >= 370 and newY <= 537.5:
                self.position_x = 525 - newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_x >= 267.5 and newX <= 267.5 and newY >= 370 and newY <= 537.5:
                self.position_x = 535 - newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif ((self.position_y <= 237.5 and newY >= 237.5) or (self.position_y >= 237.5 and newY <= 237.5)) and newX >= 375 and newX <= 475:
                self.position_y = 475 - newY
                self.bounce += 1
                self.increment_y *= -1
            
            elif self.position_y <= 237.5 and newY >= 237.5 and newX >= 375 and newX <= 475:
                self.position_y = 475 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_y >= 242.5 and newY <= 242.5 and newX >= 375 and newX <= 475:
                self.position_y = 485 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_y <= 280 and newY >= 280 and ((newX >= 625 and newX <= 850) or newX >= 925):
                self.position_y = 560 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_y >= 285 and newY <= 285 and ((newX >= 625 and newX <= 850) or newX >= 925):
                self.position_y = 570 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_y <= 350 and newY >= 350  and newX >= 900 :
                self.position_y = 700 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_y >= 355 and newY <= 355 and newX >= 900 :
                self.position_y = 710 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_y <= 450 and newY >= 450 and newX >= 950 :
                self.position_y = 900 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_y >= 455 and newY <= 455 and newX >= 950 :
                self.position_y = 910 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_y <= 412 and newY >= 412  and ((newX >= 525 and newX <= 625) or (newX >= 750 and newX <= 875)):
                self.position_y = 824 - newY
                self.bounce += 1
                self.increment_y *= -1
            
            elif self.position_y >= 417 and newY <= 417 and ((newX >= 525 and newX <= 625) or (newX >= 750 and newX <= 875)):
                self.position_y = 834 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_y <= 475 and newY >= 475 and newX >= 625 and newX <= 625:
                self.position_y = 950 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_y >= 480 and newY <= 480 and newX >= 625 and newX <= 625:
                self.position_y = 960 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_y <= 537.5 and newY >= 537.5 and newX >= 750 and newX <= 875:
                self.position_y = 1075 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_y >= 542.5 and newY <= 542.5 and newX >= 750 and newX <= 875:
                self.position_y = 1085 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_y <= 300 and newY >= 300  and  newX <= 100:
                self.position_y = 600 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_y >= 305 and newY <= 305 and  newX <= 100:
                self.position_y = 610 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_x <= 500 and newX >= 500  and ((newY >= 500 and newY <= 600) or (newY >= 50 and newY <= 150)):
                self.position_x = 1000 - newX
                self.bounce += 1
                self.increment_x *= -1
            
            elif self.position_x >= 505 and newX <= 505 and ((newY >= 500 and newY <= 600) or (newY >= 50 and newY <= 150)):
                self.position_x = 1010 - newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_x <= 900 and newX >= 900 and ((newY >= 350 and newY <= 400) or (newY >= 50 and newY <= 150)):
                self.position_x = 1800 - newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_x >= 905 and newX <= 905 and ((newY >= 350 and newY <= 400) or (newY >= 50 and newY <= 150)):
                self.position_x = 1810 - newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_x <= 737.5 and newX >= 737.5 and newY >= 112.5 and newY <= 280:
                self.position_x = 1475 - newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_x >= 742.5 and newX <= 742.5 and newY >= 112.5 and newY <= 280:
                self.position_x = 1485 - newX
                self.bounce += 1
                self.increment_x *= -1
            
            elif self.position_x <= 625 and newX >= 625 and newY >= 280 and newY <= 537.5:
                self.position_x = 1250 - newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_x >= 630 and newX <= 630 and newY >= 280 and newY <= 537.5:
                self.position_x = 1260 - newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_x <= 875 and newX >= 875 and newY >= 412 and newY <= 537.5:
                self.position_x = 1750 - newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_x >= 880 and newX <= 880 and newY >= 412 and newY <= 537.5:
                self.position_x = 1760 - newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_x <= 600 and newX >= 600 and newY >= 550 and newY <= 600:
                self.position_x = 1200 - newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_x >= 605 and newX <= 605 and newY >= 550 and newY <= 600:
                self.position_x = 1210 - newX
                self.bounce += 1
                self.increment_x *= -1
                
            #bordes de las rayas
            elif self.position_y < 250 and newY >= 250 and newX >= 98 and newX <= 105:
                self.position_y = 500 - newY
                self.bounce += 1
                self.increment_y *= -1
            
            elif self.position_y < 550 and newY >= 550 and newX >= 98 and newX <= 105:
                self.position_y = 1010 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_x >= 55 and newX <= 55 and newY <= 202 and newY >= 198:
                self.position_x = 110 - newX
                self.bounce += 1
                self.increment_x *= -1
            
            elif self.position_x >= 70 and newX <= 70 and newY <= 373 and newY >= 368:
                self.position_x = 140 - newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_x >= 250 and newX <= 250 and newY <= 120 and newY >= 111.5:
                self.position_x = 500 - newX
                self.bounce += 1
                self.increment_x *= -1
             
            elif self.position_x >= 250 and newX <= 250 and newY <= 245 and newY >= 236.5:
                self.position_x = 500 - newX
                self.bounce += 1
                self.increment_x *= -1
            
            elif self.position_x >= 475 and newX <= 475 and newY <= 240 and newY >= 236.5:
                self.position_x = 950 - newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_x >= 550 and newX <= 550 and newY <= 503 and newY >= 498:
                self.position_x = 1010 - newX
                self.bounce += 1
                self.increment_x *= -1
             
            elif self.position_x >= 50 and newX <= 50 and newY <= 503 and newY >= 498:
                self.position_x = 100 - newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_x >= 850 and newX <= 850 and newY <= 283 and newY >= 278:
                self.position_x = 1700 - newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_x >= 750 and newX <= 750 and newY <= 479 and newY >= 472:
                self.position_x = 1500 - newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_x <= 250 and newX >= 250 and newY <= 180 and newY >= 172.5:
                self.position_x = 500 - newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_x <= 150 and newX >= 150 and newY <= 374 and newY >= 368:
                self.position_x = 300 - newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_x <= 525 and newX >= 525 and newY <= 415 and newY >= 411:
                self.position_x = 1050 - newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_x <= 450 and newX >= 450 and newY <= 155 and newY >= 152.5:
                self.position_x = 900 - newX
                self.bounce += 1
                self.increment_x *= -1
             
            elif self.position_x <= 950 and newX >= 950 and newY <= 155 and newY >= 152.5:
                self.position_x = 1900 - newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_x <= 925 and newX >= 925 and newY <= 285 and newY >= 278:
                self.position_x = 1850 - newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_x <= 950 and newX >= 950 and newY <= 455 and newY >= 452.5:
                self.position_x = 1810 - newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_x <= 750 and newX >= 750 and newY <= 415 and newY >= 410:
                self.position_x = 1500 - newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_x <= 750 and newX >= 750 and newY <= 541 and newY >= 536:
                self.position_x = 1500 - newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_y < 112.5 and newY >= 112.5 and newX >= 372.5 and newX <= 377.5:
                self.position_y = 225 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_y > 237.5 and newY <= 237.5 and newX >= 372.5 and newX <= 377.5:
                self.position_y = 475 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_y > 100 and newY <= 100 and newX >=  398 and newX <= 405:
                self.position_y = 200 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_y < 550 and newY >= 550 and newX >= 498 and newX <= 505:
                self.position_y = 1100 - newY
                self.bounce += 1
                self.increment_y *= -1
            
            elif self.position_y < 112.5 and newY >= 112.5 and newX >= 735 and newX <= 740:
                self.position_y = 225 - newY
                self.bounce += 1
                self.increment_y *= -1
            
            elif self.position_y > 537.5 and newY <= 537.5 and ((newX >=  398 and newX <= 405) or (newX >= 623 and newX <= 628)):
                self.position_y = 1075 - newY
                self.bounce += 1
                self.increment_y *= -1
            
            elif self.position_y > 150 and newY <= 150 and newX >= 898 and newX <= 903:
                self.position_y = 300 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif newY > CANVAS_HEIGHT:
                self.position_y = 2*CANVAS_HEIGHT - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif newY < CANVAS_SCORE:
                self.position_y = 2*CANVAS_SCORE-newY+5
                self.bounce += 1
                self.increment_y *= -1
            
            elif newX > CANVAS_WIDTH:
                self.position_x = 2*CANVAS_WIDTH - newX
                self.bounce += 1
                self.increment_x *= -1
                if newY < CANVAS_SCORE:
                    self.position_y=2*CANVAS_SCORE-newY
                    self.increment_y *= 1
                elif newY > CANVAS_HEIGHT:
                    self.position_y=2*CANVAS_HEIGHT-newY
                    self.increment_y *= -1
            
            elif newX < 0:
                self.position_x = abs(newX)+5
                self.bounce += 1
                self.increment_x *= -1
                if newY < CANVAS_SCORE:
                    self.position_y=2*CANVAS_SCORE-newY
                    self.increment_y *= -1
                elif newY > CANVAS_HEIGHT:
                    self.position_y=2*CANVAS_HEIGHT-newY
                    self.increment_y *= -1
            
            else:
                self.position_x = newX
                self.position_y = newY
            return True
    
    def close(self, tank):
        """
        Output: Booleano que indica si la bala está cerca del tanque, si el tanque es de otro equipo
        """
        return self.get_team()!=tank.get_team() and tank.half_diagonal>numpy.linalg.norm((self.position_x-tank.position_x,self.position_y-tank.position_y))
    def impact(self,tank):
        angle = (-1)*tank.tank_orientation*2*math.pi/360
        vector_translated = (self.position_x-tank.position_x, self.position_y-tank.position_y)
        vector_rotated = (math.cos(angle) * vector_translated[0] - math.sin(angle) * vector_translated[1], math.sin(angle) * vector_translated[0] + math.cos(angle) * vector_translated[1])
        return (abs(vector_rotated[0])<30 and abs(vector_rotated[1])<16)
        
    def get_position(self):
        return (int(self.position_x), int(self.position_y))
    
    def get_team(self):
        return self.team
