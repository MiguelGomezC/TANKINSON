
#imported modules

import math
import numpy


#Constants inicialization

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 250


class TankClass:
    def __init__(self, team, id):
        self.step = 3
        self.size = 20#1/2 ancho del tanque (esta mal, hay que mirar las fotos)
        self.id = id
        self.team = team
        if team == 1:
            self.position_x = 50
            self.position_y = 125
            self.pointer_x = 250
            self.pointer_y = 125
            self.tank_orientation = 360
            self.pointer_orientation = 180
        else:
            self.position_x = 450
            self.position_y = 125
            self.pointer_x = 250
            self.pointer_y = 125
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
        return self.point_orientation
    
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
                    self.point_orientation =  - pointer_degrees
                else:
                    self.point_orientation = 360 - pointer_degrees
            else:
                self.point_orientation = 180 - pointer_degrees
        print(self.point_orientation)
    
    def shoot(self):
        pointer_radiants = math.radians(self.point_orientation)
        length_canon = 20
        canon_x = length_canon*math.cos(pointer_radiants)
        canon_y = length_canon*math.sin(pointer_radiants)
        deviation_x = 3
        deviation_y = 3
        return BulletClass(self.team, self.position_x+canon_x+deviation_x, self.position_y-canon_y+deviation_y, self.pointer_x, self.pointer_y)
    
    def move(self, movement): #canvas 500x250
        if movement == 1:#arriba
            if self.position_y+self.step < self.size:
                self.position_y = self.size
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
            if self.position_x+self.step> 500-self.size:
                self.position_x = 500-self.size
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
            if self.position_y+self.step > 250-self.size:
                self.position_y = 250-self.size
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
            if self.position_x-self.step < self.size:
                self.position_x = self.step
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
        self.bounce = False
        module = math.sqrt(distance_x**2 + distance_y**2)
        self.increment_x = float(distance_x)/module*self.velocity
        self.increment_y = float(distance_y)/module*self.velocity

    def move(self):
        """
        Output: Si se debe mantener la bala o no, es decir, si aún no ha chocado 2 veces.
        """
        newX = self.position_x + self.increment_x
        newY = self.position_y + self.increment_y
        if newX >= 0 and newX <= 500 and newY >= 0 and newY <= 250:#Choca con algo, de momento solo bordes
            self.position_x = newX
            self.position_y = newY
            return True
        else:
            if self.bounce:
                return False
            else:
                self.bounce = True
                if newX < 0:
                    self.position_x = abs(newX)
                    self.increment_x *= -1
                elif newX > 500:
                    self.position_x = 1000 - newX
                    self.increment_x *= -1
                elif newY < 0:
                    self.position_y = abs(newY)
                    self.increment_y *= -1
                elif newY > 250:
                    self.position_y = 500 - newY
                    self.increment_y *= -1
                return True
                    
        
    def get_position(self):
        return (int(self.position_x), int(self.position_y))
    
    def get_team(self):
        return self.team