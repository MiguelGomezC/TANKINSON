
#imported modules

import math
import numpy


#Constants inicialization

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 300
CANVAS_SCORE = 50

class TankClass:
    def __init__(self, team, id):
        self.step = 3
        self.size = 29.5 #1/2 largo
        self.id = id
        self.team = team
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
    
    def shoot(self):
        pointer_radiants = math.radians(self.pointer_orientation)
        length_canon = 20
        canon_x = length_canon*math.cos(pointer_radiants)
        canon_y = length_canon*math.sin(pointer_radiants)
        deviation_x = 3
        deviation_y = 3
        return BulletClass(self.team, self.position_x+canon_x+deviation_x, self.position_y-canon_y+deviation_y, self.pointer_x, self.pointer_y)
    
    def move(self, movement, mapa): #canvas 500x300
        if movement == 1:#arriba
            if mapa==1:
                if self.position_y >= 210 and self.position_y-self.size_l<=210 and self.position_x+self.size_w>=170 and self.position_x-self.size_w<=330:
                    self.position_y=210+self.size_l
                elif self.position_x+self.size_w >= 400 and self.position_x-self.size_w<=400 and self.position_y-self.size_l<=120:
                    self.position_y=120+self.size_l
                elif self.position_x+self.size_w >= 100 and self.position_x-self.size_w<=100 and self.position_y-self.size_l<=120:
                    self.position_y=120+self.size_l
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
            if mapa==1:
                if self.position_x<=100 and self.position_x+self.size_l>=100 and (self.position_y-self.size_w<=120 or self.position_y+self.size_w>=230):
                    self.position_x =100-self.size_l
                elif self.position_x<=400 and self.position_x+self.size_l>=400 and (self.position_y-self.size_w<=120 or self.position_y+self.size_w>=230):
                    self.position_x=400-self.size_l
                elif self.position_x<=170 and self.position_x+self.size_l >=170 and self.position_y+self.size_w>=140 and self.position_y-self.size_w<=210:
                    self.position_x=170-self.size_l
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
            if mapa==1:
                if self.position_y<=140 and self.position_y+self.size_l>=140 and self.position_x+self.size_w>= 170 and self.position_x-self.size_w<=330:
                    self.position_y=140-self.size_l
                elif self.position_x+self.size_w >= 400 and self.position_x-self.size_w<=400 and self.position_y+self.size_l>=230:
                    self.position_y=230-self.size_l
                elif self.position_x+self.size_w >= 100 and self.position_x-self.size_w<=100 and self.position_y+self.size_l>=230:
                    self.position_y=230-self.size_l
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
            if mapa==1:
                if self.position_x>=400 and self.position_x-self.size_l<=400 and (self.position_y-self.size_w<=120 or self.position_y+self.size_w>=230):
                    self.position_x=400+self.size_l
                elif self.position_x>=100 and self.position_x-self.size_l<=100 and (self.position_y-self.size_w <=120 or self.position_y+self.size_w >= 230):
                    self.position_x=100+self.size_l
                elif self.position_x>=330 and self.position_x-self.size_l<=330  and self.position_y-self.size_w<=210 and self.position_y+self.size_w>=140:
                    self.position_x = 330 + self.size_l
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
            elif ((self.position_x<=100 and newX>=100)or(self.position_x>100 and newX<=100)) and (newY<=120 or newY>=230):
                self.bounce+=1
                self.position_x=200-newX
                self.increment_x *= -1
            elif self.position_x<170 and newX>=170 and newY>=140 and newY<=230:
                self.position_x=340-newX
                self.bounce +=1
                self.increment_x *= -1
            elif ((self.position_x<400 and newX>=400) or (self.position_x>400 and newX<=400))and (newY<120 or newY>230):
                self.position_x=800-newX
                self.bounce+=1
                self.increment_x *= -1
            elif newX > CANVAS_WIDTH:
                self.position_x = 2*CANVAS_WIDTH - newX
                self.bounce+=1
                self.increment_x *= -1
            elif self.position_x>330 and newX<=330 and newY>140 and newY<230:
                self.position_x=660-newX
                self.bounce +=1
                self.increment_x *= -1
            elif newX<0:
                self.position_x = 15
                self.bounce +=1
                self.increment_x *= -1
            elif self.position_y>210 and newY<=210 and newX>=100 and newX<=400:
                self.position_y=420-newY
                self.bounce +=1
                self.increment_y *= -1
            elif self.position_y<140 and newY>=140 and newX>=100 and newX<=400:
                self.position_y=280-newY
                self.bounce+=1
                self.increment_y *= -1
            elif newY > CANVAS_HEIGHT:
                self.position_y = 2*CANVAS_HEIGHT - newY
                self.bounce +=1
                self.increment_y *= -1
            elif newY < CANVAS_SCORE:
                self.position_y = CANVAS_SCORE+15
                self.bounce +=1
                self.increment_y *= -1
            else:
                self.position_x = newX
                self.position_y = newY
            return True
                    
        
    def get_position(self):
        return (int(self.position_x), int(self.position_y))
    
    def get_team(self):
        return self.team
