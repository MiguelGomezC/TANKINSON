
#imported modules

import math
import numpy


#Constants inicialization

CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
CANVAS_SCORE = 50

class TankClass:
    def __init__(self, team, id, mapa):
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
            if team == 1:
                self.position_x = 50
                self.position_y = (CANVAS_HEIGHT+CANVAS_SCORE)/2
                self.pointer_x = 250
                self.pointer_y = (CANVAS_HEIGHT+CANVAS_SCORE)/2
                self.tank_orientation = 360
                self.pointer_orientation = 180
            else:
                self.position_x = 450
                self.position_y = (CANVAS_HEIGHT+CANVAS_SCORE)/2
                self.pointer_x = 250
                self.pointer_y = (CANVAS_HEIGHT+CANVAS_SCORE)/2
                self.tank_orientation = 180
                self.pointer_orientation = 360
        elif mapa == 2:
           if team == 1:
                self.position_x = 50
                self.position_y = 250
                self.pointer_x = 250
                self.pointer_y = 150
                self.tank_orientation = 45
                self.pointer_orientation = 225
           else:
                self.position_x = 450
                self.position_y = 100
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
            """        
            elif self.mapa == 2:
                if self.position_y >= 200 and self.position_y-self.size_l <= 200 and self.position_x-self.size_w < 50:
                    self.position_y = 200+self.size_l
                elif self.position_y >= 237.5 and self.position_y-self.size_l <= 237.5 and self.position_x+self.size_w >= 125 and self.position_x-self.size_w < 250:
                    self.position_y = 237.5+self.size_l
                elif self.position_y >= 175 and self.position_y-self.size_l <= 175 and self.position_x+self.size_w > 250 and self.position_x-self.size_w <= 375:
                    self.position_y = 175+self.size_l
                elif self.position_y >= 112.5 and self.position_y-self.size_l <= 112.5 and self.position_x+self.size_w >= 125 and self.position_x-self.size_w < 250:
                    self.position_y = 112.5+self.size_l
                elif self.position_y > 150 and self.position_y-self.size_l <= 150 and self.position_x+self.size_w > 450:
                    self.position_y = 150+self.size_l
                elif self.position_y > 100 and self.position_y-self.size_l <= 100 and self.position_x+self.size_w >=400 and self.position_x-self.size_w < 400:
                    self.position_y = 100+self.size_l
                elif self.position_y > 237.5 and self.position_y+self.size_l >= 237.5 and self.position_x+self.size_w >= 375 and self.position_x-self.size_w < 375:
                    self.position_y = 237.5+self.size_l
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
             """       
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
            """        
            elif self.mapa == 2:
                if self.position_x < 100 and self.position_x+self.size_l >= 100 and self.position_y+self.size_w > 250:
                    self.position_x = 100-self.size_l
                elif self.position_x < 125 and self.position_x+self.size_l >= 125 and self.position_y+self.size_w > 112.5 and self.position_y-self.size_w < 237.5:
                    self.position_x = 125-self.size_l
                elif self.position_x < 375 and self.position_x+self.size_l >= 375 and self.position_y+self.size_w > 112.5 and self.position_y-self.size_w < 237.5:
                    self.position_x = 375 -self.size_l
                elif self.position_x < 250 and self.position_x+self.size_l >= 250 and self.position_y+self.size_w >= 175 and self.position_y-self.size_w < 175:
                    self.posiiton_x = 250-self.size_l
                elif self.position_x < 400 and self.position_x+self.size_l >= 400 and self.position_y-self.size_w <= 100 and self.position_y+self.size_w >= 0:
                    self.position_x = 400-self.size_l
                elif self.position_x < 450 and self.position_x+self.size_l >= 450 and self.position_y-self.size_w <= 150 and self.position_y+self.size_w >= 150:
                    self.position_x = 450-self.size_l
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
                """    
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
             """
            elif self.mapa == 2:
                if self.position_y < 200 and self.position_y+self.size_l >= 200 and self.position_x-self.size_w < 50:#derecha
                    self.position_y = 200-self.size_l
                elif self.position_y < 250 and self.position_y+self.size_l >= 250 and self.position_x +self.size_w >=100 and self.position_x-self.size_w <=100:#raya cuadradoabajo dr
                    self.position_y=250-self.size_l
                elif self.position_y < 112.5 and self.position_y+self.size_l >= 112.5 and self.position_x+self.size_w > 125 and self.position_x-self.size_w < 250:#centro arriba
                    self.position_y = 112.5-self.size_l
                elif self.position_y < 175 and self.position_y+self.size_l >= 175 and self.position_x+self.size_w > 250 and self.position_x-self.size_w < 375:#raya central central
                    self.position_y = 175 - self.size_l
                elif self.position_y < 237.5 and self.position_y+self.size_l >= 237.5 and self.position_x-self.size_w < 250 and self.position_x+self.size_w > 125:#raya centro abajo
                    self.position_y = 237.5-self.size_l
                elif self.position_y < 150 and self.position_y+self.size_l >= 150 and self.position_x + self.size_w > 450:#raya derecha
                    self.position_y = 150 - self.size_l
                elif self.position_y < 112.5 and self.position_y+self.size_l >= 112.5 and self.position_x+self.size_w >= 375 and self.position_x-self.size_w < 375:#raya centro arriba derecha
                    self.position_y = 112.5-self.size_l
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
              """      
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
             """       
            elif self.mapa == 2:
                if self.position_x > 50 and self.position_x-self.size_l <= 50 and self.position_y+self.size_w >= 200 and self.position_y-self.size_w <=200:
                    self.poosition_x = 50 + self.size_l
                elif self.position_x > 100 and self.position_x - self.size_l <= 100 and self.position_y+self.size_w >= 250:
                    self.position_x = 100 + self.size_l
                elif self.position_x > 125 and self.position_x-self.size_l <= 125 and self.position_y-self.size_w <237.5 and self.position_y+self.size_w > 112.5: 
                    self.position_x = 125+self.size_l
                elif self.position_x > 250 and self.position_x-self.size_l <= 250 and self.position_y-self.size_w < 112.5 and self.position_y+self.size_w > 112.5:
                    self.position_x = 250 + self.size_l
                elif self.position_x > 250 and self.position_x-self.size_l <= 250 and self.position_y-self.size_w < 237.5 and self.position_y+self.size_w > 237.5:
                    self.position_x = 250 + self.size_l 
                elif self.position_x > 375 and self.position_x - self.size_l <= 375 and self.position_y-self.size_w <237.5 and self.position_y+self.size_w > 112.5:
                    self.position_x = 375 + self.size_l
                elif self.position_x > 400 and self.position_x - self.size_l <= 400 and self.position_y-self.size_w < 100:
                    self.position_x = 400+self.size_l
                elif self.position_x-self.step < self.size_l:
                    self.position_x = self.size_l
                else:
                    self.position_x -= self.step
                    
            if self.tank_orientation != 180:
                if self.tank_orientation < 180:
                    self.tank_orientation += 7.5
                else:
                    self.tank_orientation -= 7.5
                """



           
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
                
            elif self.position_x <= 100 and newX >= 100 and newY>= 250:
                self.position_x = 200 - newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_x >= 105 and newX <= 105 and newY >= 250:
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
            
            elif self.position_y <= 237.5 and newY >= 237.5 and newX >= 125 and newX <= 250:
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
        
            elif self.position_x <= 375 and newX >= 375 and newY >= 112.5 and newY <= 237.5:
                self.position_x = 750 - newX
                self.bounce += 1
                self.increment_x *= -1
            
            elif self.position_x >= 380 and newX <= 380 and newY >= 112.5 and newY <= 237.5:
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
            
            elif self.position_y <= 150 and newY >= 150 and newX >= 450:
                self.position_y = 300 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_y >= 155 and newY <= 155 and newX >= 450:
                self.position_y = 310 - newY
                self.bounce += 1
                self.increment_y *= -1
            
            elif self.position_y < 250 and newY >= 250 and newX >= 98 and newX <= 105:
                self.position_y = 500 - newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_x >= 55 and newX <= 55 and newY <= 202 and newY >= 198:
                self.position_x = 110 - newX
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
                
            elif self.position_x <= 250 and newX >= 250 and newY <= 180 and newY >= 172.5:
                self.position_x = 500 - newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_x <= 450 and newX >= 450 and newY <= 155 and newY >= 152.5:
                self.position_x = 900 - newX
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
