
#imported modules

import math
import numpy


#Constants inicialization

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 300
CANVAS_SCORE = 50

class TankClass:
    def __init__(self, team, id, mapa):
        self.step = 3
        self.size = 29.5 #1/2 largo
        self.id = id
        self.team = team
        self.mapa = mapa
        self.lives = 3
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
    
    def shoot(self):
        pointer_radiants = math.radians(self.pointer_orientation)
        length_canon = 20
        canon_x = length_canon*math.cos(pointer_radiants)
        canon_y = length_canon*math.sin(pointer_radiants)
        return BulletClass(self.team, self.position_x+canon_x, self.position_y-canon_y, self.pointer_x, self.pointer_y)
    
    def move(self, movement): #canvas 500x300
        if movement == 1:#arriba
            if self.mapa == 1:
                if self.position_y >= 210 and self.position_y-self.size_l <= 210 and self.position_x+self.size_w >= 170 and self.position_x-self.size_w <= 330:
                    self.position_y = 210+self.size_l
                elif self.position_x+self.size_w >= 400 and self.position_x-self.size_w <= 400 and self.position_y-self.size_l <= 120:
                    self.position_y = 120+self.size_l
                elif self.position_x+self.size_w >= 100 and self.position_x-self.size_w <= 100 and self.position_y-self.size_l <= 120:
                    self.position_y = 120+self.size_l
                elif self.position_y - self.step < self.size_l+CANVAS_SCORE:
                    self.position_y = self.size_l+CANVAS_SCORE
                else:
                    self.position_y -= self.step
                    
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
                    
        elif movement == 2:#derecha
            if self.mapa == 1:
                if self.position_x <= 100 and self.position_x+self.size_l >= 100 and (self.position_y-self.size_w <= 120 or self.position_y+self.size_w >= 230):
                    self.position_x =100-self.size_l
                elif self.position_x <= 400 and self.position_x+self.size_l >= 400 and (self.position_y-self.size_w <= 120 or self.position_y+self.size_w >= 230):
                    self.position_x = 400-self.size_l
                elif self.position_x <= 170 and self.position_x+self.size_l >= 170 and self.position_y+self.size_w >= 140 and self.position_y-self.size_w <= 210:
                    self.position_x = 170-self.size_l
                elif self.position_x+self.step > CANVAS_WIDTH-self.size_l:
                    self.position_x = CANVAS_WIDTH-self.size_l
                else:
                    self.position_x += self.step
                    
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
                    
        elif movement == 3:#abajo
            if self.mapa == 1:
                if self.position_y <= 140 and self.position_y+self.size_l >= 140 and self.position_x+self.size_w >= 170 and self.position_x-self.size_w <= 330:
                    self.position_y = 140-self.size_l
                elif self.position_x+self.size_w >= 400 and self.position_x-self.size_w <= 400 and self.position_y+self.size_l >= 230:
                    self.position_y = 230-self.size_l
                elif self.position_x+self.size_w >= 100 and self.position_x-self.size_w <= 100 and self.position_y+self.size_l >= 230:
                    self.position_y = 230-self.size_l
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
                if self.position_x >= 400 and self.position_x-self.size_l <= 400 and (self.position_y-self.size_w <= 120 or self.position_y+self.size_w >= 230):
                    self.position_x=400+self.size_l
                elif self.position_x >= 100 and self.position_x-self.size_l <= 100 and (self.position_y-self.size_w <= 120 or self.position_y+self.size_w >= 230):
                    self.position_x = 100+self.size_l
                elif self.position_x >= 330 and self.position_x-self.size_l <= 330  and self.position_y-self.size_w <= 210 and self.position_y+self.size_w >= 140:
                    self.position_x = 330 + self.size_l
                elif self.position_x-self.step < self.size_l:
                    self.position_x = self.size_l
                else:
                    self.position_x -= self.step
                    
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
            
            elif self.position_x <= 100 and newX >= 100 and (newY <= 120 or newY >= 230):
                self.bounce += 1
                self.position_x = 200-newX
                self.increment_x *= -1
                
            elif self.position_x >= 105 and newX <= 105 and (newY <= 120 or newY >= 230):
                self.bounce += 1
                self.position_x = 210-newX
                self.increment_x *= -1
                
            elif self.position_x <= 170 and newX >= 170 and newY >= 140 and newY <= 230:
                self.position_x = 340-newX
                self.bounce +=1
                self.increment_x *= -1
             
            elif self.position_x <= 400 and newX >= 400 and (newY <= 120 or newY >= 230):
                self.position_x = 800-newX
                self.bounce += 1
                self.increment_x *= -1
            
            elif self.position_x >= 405 and newX <= 405 and (newY <= 120 or newY >= 230):
                self.position_x = 810-newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif newX > CANVAS_WIDTH:
                self.position_x = 2*CANVAS_WIDTH - newX
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_x >= 335 and newX <= 335 and newY > 140 and newY < 230:
                self.position_x = 670-newX
                self.bounce += 1
                self.increment_x *= -1
            
            elif newX < 0:
                self.position_x = abs(newX)+5
                self.bounce += 1
                self.increment_x *= -1
                
            elif self.position_y >= 215 and newY <= 215 and newX >= 170 and newX <= 330:
                self.position_y = 430-newY
                self.bounce += 1
                self.increment_y *= -1
                
            elif self.position_y <= 140 and newY >= 140 and newX >= 170 and newX <= 330:
                self.position_y = 280-newY
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
    
    def impact(self, tank):
        (x_tank, y_tank)  = tank.get_position()
        t_orientation = (tank.get_tank_orientation())%360 
        if t_orientation > 169:
            if t_orientation > 259:
                if t_orientation > 304:
                    if t_orientation > 330.5:
                        if t_orientation > 349:
                            return (x_tank-16<=self.position_x<=x_tank+16) and (y_tank-30<=self.position_y<=y_tank+30) #5
                        else:
                            return (x_tank-16<=self.position_x<=x_tank+16) and (y_tank-30<=self.position_y<=y_tank+30) #6
                    else:
                        return (x_tank-16<=self.position_x<=x_tank+16) and (y_tank-30<=self.position_y<=y_tank+30) #7
                else:
                    if t_orientation > 281.5:
                        return (x_tank-16<=self.position_x<=x_tank+16) and (y_tank-30<=self.position_y<=y_tank+30) #8
                    else:
                        return (x_tank-16<=self.position_x<=x_tank+16) and (y_tank-30<=self.position_y<=y_tank+30) #9
            else:
                if t_orientation > 214:
                    if t_orientation > 236:
                        return (x_tank-16<=self.position_x<=x_tank+16) and (y_tank-30<=self.position_y<=y_tank+30) #10
                    else:
                        return (x_tank-16<=self.position_x<=x_tank+16) and (y_tank-30<=self.position_y<=y_tank+30) #11
                else:
                    if t_orientation > 191.5:
                        return (x_tank-16<=self.position_x<=x_tank+16) and (y_tank-30<=self.position_y<=y_tank+30) #12
                    else:
                        return (x_tank-16<=self.position_x<=x_tank+16) and (y_tank-30<=self.position_y<=y_tank+30) #13
            
        else:
            if t_orientation > 79:
                if t_orientation > 124:
                    if t_orientation > 146.5:
                        return (x_tank-16<=self.position_x<=x_tank+16) and (y_tank-30<=self.position_y<=y_tank+30) #14
                    else:
                        return (x_tank-16<=self.position_x<=x_tank+16) and (y_tank-30<=self.position_y<=y_tank+30) #15
                else:
                    if t_orientation > 101.5:
                        return (x_tank-16<=self.position_x<=x_tank+16) and (y_tank-30<=self.position_y<=y_tank+30) #16
                    else:
                       return (x_tank-16<=self.position_x<=x_tank+16) and (y_tank-30<=self.position_y<=y_tank+30) 
            else:
                if t_orientation > 34:
                    if t_orientation > 56.5:
                        return (x_tank-16<=self.position_x<=x_tank+16) and (y_tank-30<=self.position_y<=y_tank+30) #2
                    else:
                        return (x_tank-16<=self.position_x<=x_tank+16) and (y_tank-30<=self.position_y<=y_tank+30) #3
                else:
                    if t_orientation > 11.5:
                        return (x_tank-16<=self.position_x<=x_tank+16) and (y_tank-30<=self.position_y<=y_tank+30) #4
                    else:
                        return (x_tank-16<=self.position_x<=x_tank+16) and (y_tank-30<=self.position_y<=y_tank+30) #5
                
        
    def get_position(self):
        return (int(self.position_x), int(self.position_y))
    
    def get_team(self):
        return self.team
