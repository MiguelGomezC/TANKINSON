

#imported modules

from multiprocessing.connection import Client
from multiprocessing import Queue

from tkinter import *
import time, random
import tankClass
last_movement = 0

#Constants inicialization

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 300
CANVAS_SCORE = 50

def draw_board(canvas, message):
    canvas.delete('all')
    board, id, mapa = message
    board_tanks, board_bullets = board
    for key, tank in board_tanks:
        (x_tank, y_tank)  = tank.get_position()
        t_team = tank.get_team()
        t_orientation = tank.get_tank_orientation()
        
        #Mira como está orientado el tanque y elige la foto correspondiente
        if t_orientation > 169:
            if t_orientation > 259:
                if t_orientation > 304:
                    if t_orientation > 326.5:
                        if t_orientation > 349:
                            canvas.create_image(x_tank-34, y_tank-27, image=tank_img_5, anchor=NW)
                        else:
                            canvas.create_image(x_tank-34, y_tank-27, image=tank_img_6, anchor=NW)
                    else:
                        canvas.create_image(x_tank-31, y_tank-29, image=tank_img_7, anchor=NW)
                else:
                    if t_orientation > 281.5:
                        canvas.create_image(x_tank-26, y_tank-31, image=tank_img_8, anchor=NW)
                    else:
                        canvas.create_image(x_tank-22, y_tank-30, image=tank_img_9, anchor=NW)
            else:
                if t_orientation > 214:
                    if t_orientation > 236:
                        canvas.create_image(x_tank-26, y_tank-31, image=tank_img_10, anchor=NW)
                    else:
                        canvas.create_image(x_tank-28, y_tank-31, image=tank_img_11, anchor=NW)
                else:
                    if t_orientation > 191.5:
                        canvas.create_image(x_tank-32, y_tank-28, image=tank_img_12, anchor=NW)
                    else:
                        canvas.create_image(x_tank-31, y_tank-26, image=tank_img_13, anchor=NW)
            
        else:
            if t_orientation > 79:
                if t_orientation > 124:
                    if t_orientation > 146.5:
                        canvas.create_image(x_tank-30, y_tank-28, image=tank_img_14, anchor=NW)
                    else:
                        canvas.create_image(x_tank-31, y_tank-29, image=tank_img_15, anchor=NW)
                else:
                    if t_orientation > 101.5:
                        canvas.create_image(x_tank-26, y_tank-30, image=tank_img_16, anchor=NW)
                    else:
                        canvas.create_image(x_tank-19, y_tank-29, image=tank_img_1, anchor=NW)
            else:
                if t_orientation > 34:
                    if t_orientation > 56.5:
                        canvas.create_image(x_tank-22, y_tank-28, image=tank_img_2, anchor=NW)
                    else:
                        canvas.create_image(x_tank-29, y_tank-28, image=tank_img_3, anchor=NW)
                else:
                    if t_orientation > 11.5:
                        canvas.create_image(x_tank-34, y_tank-28, image=tank_img_4, anchor=NW)
                    else:
                        canvas.create_image(x_tank-34, y_tank-27, image=tank_img_5, anchor=NW)
        
        p_orientation = tank.get_pointer_orientation()
        #Mira donde apunta el tanque y elige la foto correspondiente
        if p_orientation > 169:
            if p_orientation > 259:
                if p_orientation > 304:
                    if p_orientation > 326.5:
                        if p_orientation > 349:
                            canvas.create_image(x_tank-20, y_tank-25, image=turret_img_5, anchor=NW)
                        else:
                            canvas.create_image(x_tank-25, y_tank-25, image=turret_img_6, anchor=NW)
                    else:
                        canvas.create_image(x_tank-25, y_tank-27, image=turret_img_7, anchor=NW)
                else:
                    if p_orientation > 281.5:
                        canvas.create_image(x_tank-27, y_tank-25, image=turret_img_8, anchor=NW)
                    else:
                        canvas.create_image(x_tank-23, y_tank-24, image=turret_img_9, anchor=NW)
            else:
                if p_orientation > 214:
                    if p_orientation > 236:
                        canvas.create_image(x_tank-26, y_tank-23, image=turret_img_10, anchor=NW)
                    else:
                        canvas.create_image(x_tank-28, y_tank-28, image=turret_img_11, anchor=NW)
                else:
                    if p_orientation > 191.5:
                        canvas.create_image(x_tank-30, y_tank-23, image=turret_img_12, anchor=NW)
                    else:
                        canvas.create_image(x_tank-30, y_tank-25, image=turret_img_13, anchor=NW)
            
        else:
            if p_orientation > 79:
                if p_orientation > 124:
                    if p_orientation > 146.5:
                        canvas.create_image(x_tank-28, y_tank-24, image=turret_img_14, anchor=NW)
                    else:
                        canvas.create_image(x_tank-30, y_tank-29, image=turret_img_15, anchor=NW)
                else:
                    if p_orientation > 101.5:
                        canvas.create_image(x_tank-24, y_tank-27, image=turret_img_16, anchor=NW)
                    else:
                        canvas.create_image(x_tank-25, y_tank-29, image=turret_img_1, anchor=NW)
            else:
                if p_orientation > 34:
                    if p_orientation > 56.5:
                        canvas.create_image(x_tank-21, y_tank-28, image=turret_img_2, anchor=NW)
                    else:
                        canvas.create_image(x_tank-28, y_tank-28, image=turret_img_3, anchor=NW)
                else:
                    if p_orientation > 11.5:
                        canvas.create_image(x_tank-24, y_tank-28, image=turret_img_4, anchor=NW)
                    else:
                        canvas.create_image(x_tank-20, y_tank-25, image=turret_img_5, anchor=NW)
        if tank.id == id: #Solo muestre donde apunta este cliente
            x_pointer, y_pointer = tank.get_pointer()
            canvas.create_line(x_pointer, y_pointer+5, x_pointer, y_pointer+15, fill='black')
            canvas.create_line(x_pointer, y_pointer-5, x_pointer, y_pointer-15, fill='black')
            canvas.create_line(x_pointer+5, y_pointer, x_pointer+15, y_pointer, fill='black')
            canvas.create_line(x_pointer-5, y_pointer, x_pointer-15, y_pointer, fill='black')
            
    for bullet in board_bullets:
        x_bullet, y_bullet = bullet.get_position()
        b_team = bullet.get_team()
        if b_team == 0:
            canvas.create_image(x_bullet-6, y_bullet-7, image=small_bullet_blue_img, anchor=NW)
        else:
            canvas.create_image(x_bullet-6, y_bullet-7, image=small_bullet_red_img, anchor=NW)
    #Para crear el marcador,solo hay un rectangulo gris ahora mismo si va a grey99 ->negro y grey1->blanco y entre medias los demas tonos de gris
    canvas.create_rectangle(0,0,CANVAS_WIDTH,CANVAS_SCORE,fill="grey70")
    canvas.create_rectangle(10, 10, 150, 40, fill= "grey50")
    canvas.create_rectangle(340, 10, 490, 40, fill= "grey50")
    canvas.create_text(50, 25, text="Equipo 1", fill="black", font=("Arial", 15))
    canvas.create_text(380, 25, text="Equipo 2", fill="black", font=("Arial", 15))
    #ESTRELLAS GRISES (EQUIPO 1)
    
    #canvas.create_image(95,20,image = estrella_gris, anchor= NW)
    #canvas.create_image(110,20,image = estrella_gris, anchor= NW)
    canvas.create_image(125,20,image = estrella_gris, anchor= NW)
    
    #ESTRELLAS AMARILLAS (EQUIPO 1)
    canvas.create_image(95,20,image = estrella_amarilla, anchor= NW)
    canvas.create_image(110,20,image = estrella_amarilla, anchor= NW)
    #canvas.create_image(125,20,image = estrella_amarilla, anchor= NW)

    #ESTRELLAS GRISES (EQUIPO 2)
    
    #canvas.create_image(425,20,image = estrella_gris, anchor= NW)
    canvas.create_image(440,20,image = estrella_gris, anchor= NW)
    canvas.create_image(455,20,image = estrella_gris, anchor= NW)
    
    #ESTRELLAS AMARILLAS (EQUIPO 2)
    canvas.create_image(425,20,image = estrella_amarilla, anchor= NW)
    #canvas.create_image(440,20,image = estrella_amarilla, anchor= NW)
    #canvas.create_image(455,20,image = estrella_amarilla, anchor= NW)
    
    #Has perdido
    """
    canvas.create_rectangle(40, 40, 460, 260,fill= "yellow")
    canvas.create_rectangle(60, 60, 440, 240,fill= "grey30")
    canvas.create_text(245, 100, text="GAME OVER", fill="black", font=("Arial", 40, "bold"))
    canvas.create_image(110,135,image = estrella_gameover, anchor= NW)
    canvas.create_image(200,135,image = estrella_gameover, anchor= NW)
    canvas.create_image(290,135,image = estrella_gameover, anchor= NW)
    """
    #Has ganado
    """
    canvas.create_rectangle(40, 40, 460, 260,fill= "yellow")
    canvas.create_rectangle(50, 50, 450, 250,fill= "grey20")
    canvas.create_text(245, 100, text="YOU WIN!", fill="yellow", font=("Arial", 40, "bold"))
    canvas.create_image(200,135,image = trofeo, anchor= NW)
    """
    
    if mapa==1:
        canvas.create_line(100,50,100,120,fill="grey99")
        canvas.create_line(400,50,400,120,fill="grey99")
        canvas.create_line(100,230,100,300,fill="grey99")
        canvas.create_line(400,230,400,300,fill="grey99")
        canvas.create_rectangle(170,140,330,210,fill="grey99")
    elif mapa == 2:
        canvas.create_line(0,200,50,200,fill="grey99")
        canvas.create_line(100,250,100,300,fill="grey99")
        canvas.create_line(400,50,400,100,fill="grey99")
        canvas.create_line(450,150,500,150,fill="grey99")
        canvas.create_line(125,112.5,125,237.5,fill="grey99")
        canvas.create_line(375,112.5,375,237.5,fill="grey99")
        canvas.create_line(125,112.5,250,112.5,fill="grey99")
        canvas.create_line(250,175,375,175,fill="grey99")
        canvas.create_line(125,237.5,250,237.5,fill="grey99")
    
if __name__ == '__main__':    

    root = Tk()
    root.title("MyTank")
    root.resizable(0, 0)
    
    frame = Frame(root)    
    frame.pack()

    canvas = Canvas(frame, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="black") 
    canvas.pack()
    canvas.create_rectangle(0,0,CANVAS_WIDTH,CANVAS_SCORE,fill="grey50")
    
    
    shoot = False #Si está disparando
    shooted = False #Si ha disparado y no ha recargado
    last_time_shooted = time.time() #Cuando ha disparado por última vez
    reload = False #Si puede recargar
    pointer_x, pointer_y = 0,0
    movement = 0
    last_movement = 0
    
    tank_img_1 = PhotoImage(file='images/tank_1.png')
    tank_img_2 = PhotoImage(file='images/tank_2.png')
    tank_img_3 = PhotoImage(file='images/tank_3.png')
    tank_img_4 = PhotoImage(file='images/tank_4.png')
    tank_img_5 = PhotoImage(file='images/tank_5.png')
    tank_img_6 = PhotoImage(file='images/tank_6.png')
    tank_img_7 = PhotoImage(file='images/tank_7.png')
    tank_img_8 = PhotoImage(file='images/tank_8.png')
    tank_img_9 = PhotoImage(file='images/tank_9.png')
    tank_img_10 = PhotoImage(file='images/tank_10.png')
    tank_img_11 = PhotoImage(file='images/tank_11.png')
    tank_img_12 = PhotoImage(file='images/tank_12.png')
    tank_img_13 = PhotoImage(file='images/tank_13.png')
    tank_img_14 = PhotoImage(file='images/tank_14.png')
    tank_img_15 = PhotoImage(file='images/tank_15.png')
    tank_img_16 = PhotoImage(file='images/tank_16.png')
    
    turret_img_1 = PhotoImage(file='images/turret_1.png')
    turret_img_2 = PhotoImage(file='images/turret_2.png')
    turret_img_3 = PhotoImage(file='images/turret_3.png')
    turret_img_4 = PhotoImage(file='images/turret_4.png')
    turret_img_5 = PhotoImage(file='images/turret_5.png')
    turret_img_6 = PhotoImage(file='images/turret_6.png')
    turret_img_7 = PhotoImage(file='images/turret_7.png')
    turret_img_8 = PhotoImage(file='images/turret_8.png')
    turret_img_9 = PhotoImage(file='images/turret_9.png')
    turret_img_10 = PhotoImage(file='images/turret_10.png')
    turret_img_11 = PhotoImage(file='images/turret_11.png')
    turret_img_12 = PhotoImage(file='images/turret_12.png')
    turret_img_13 = PhotoImage(file='images/turret_13.png')
    turret_img_14 = PhotoImage(file='images/turret_14.png')
    turret_img_15 = PhotoImage(file='images/turret_15.png')
    turret_img_16 = PhotoImage(file='images/turret_16.png')
    
    big_bullet_img = PhotoImage(file='images/big_bullet.png')
    small_bullet_blue_img = PhotoImage(file='images/small_bullet_blue.png')
    small_bullet_red_img = PhotoImage(file='images/small_bullet_red.png')
 
    estrella_amarilla = PhotoImage(file='images/amarilla2.png')
    estrella_gris =  PhotoImage(file='images/gris2.png')
    estrella_gameover = PhotoImage(file='images/gris4.png')
    trofeo = PhotoImage(file='images/trofeo.png')

    
    def aiming(event):        
        global pointer_x
        global pointer_y 
        pointer_x, pointer_y = event.x, event.y 
    
    def shooting(event):  
        global shoot
        shoot = True
    
    def moving(event):
        global movement        
        key_pressed = event.keysym
        if key_pressed == 'Up' or key_pressed == 'w':
            movement = 1
        elif key_pressed == 'Right' or key_pressed == 'd':
            movement = 2
        elif key_pressed == 'Down' or key_pressed == 's':
            movement = 3
        elif key_pressed == 'Left' or key_pressed == 'a':
            movement = 4

    canvas.bind("<Motion>", aiming)
    canvas.bind("<Button-1>", shooting)
    canvas.bind_all("<Key>", moving)

    print ('trying to connect')
    conn = Client(address=('127.0.0.1', 6000), authkey=b'secret')
    print ('connection accepted')

    def normal_act():
        global shoot, shooted, last_time_shooted, reload
        global movement
        if shoot:
            last_time_shooted = time.time()
            shooted = True
        elif shooted:
            current_time = time.time()
            diff = current_time - last_time_shooted
            if diff >= 3:
                reload = True
                shooted = False
        pointer_position = (pointer_x, pointer_y)
        state = (pointer_position, movement, shoot, reload)
        conn.send(state)
        message = conn.recv()
        shoot = False
        draw_board(canvas, message)
    
    def repet_act():
        global shoot, shooted, last_time_shooted, reload
        global movement
        key = movement
        for i in range(15):
            if shoot:
                last_time_shooted = time.time()
                shooted = True
            elif shooted:
                current_time = time.time()
                diff = current_time - last_time_shooted
                if diff >= 3:
                    reload = True
                    shooted = False
            pointer_position = (pointer_x, pointer_y)
            state = (pointer_position, key, shoot, reload)
            conn.send(state)
            shoot = False
            message = conn.recv()
            draw_board(canvas, message)
            root.update()
            time.sleep(0.03)
            if movement != key:
                repet_act()
                break

    try:
        while 1:
            if movement == last_movement or movement == 0:
                normal_act()
            else:
                repet_act()
            if movement != 0:
                last_movement = movement
            movement = 0
            root.update()

    except TclError:
        pass
   

