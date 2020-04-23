

#imported modules

from multiprocessing.connection import Client
from multiprocessing import Queue

from tkinter import *
import time, random
import tankClass

#Constants inicialization

CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
CANVAS_SCORE = 50


def draw_board(canvas, message):
    canvas.delete('all')
    board, id, mapa = message
    board_tanks, board_bullets = board
    team_lives=[0,0]
    if mapa==-1:
        canvas.create_rectangle(00, 0, 1000, 1000,fill= "yellow")
        canvas.create_rectangle(60, 70, 920, 520,fill= "grey30")
        canvas.create_text(490, 230, text="GAME OVER", fill="black", font=("Arial", 80, "bold"))
        canvas.create_image(250,330,image = estrella_gameover, anchor= NW)
        canvas.create_image(430,330,image = estrella_gameover, anchor= NW)
        canvas.create_image(610,330,image = estrella_gameover, anchor= NW)
        return None
    for key, tank in board_tanks:
        (x_tank, y_tank)  = tank.get_position()
        t_team = tank.get_team()
        t_orientation = tank.get_tank_orientation()
        if t_team==0:
            team_lives[0]+=1
        else:
            team_lives[1]+=1
        t_orientation = tank.get_tank_orientation()
        
        #Mira como está orientado el tanque y elige la foto correspondiente
        if t_team == 0:
          if t_orientation > 169:
              if t_orientation > 259:
                  if t_orientation > 304:
                      if t_orientation > 326.5:
                          if t_orientation > 349:
                              canvas.create_image(x_tank-34, y_tank-27, image=tank_blue_5, anchor=NW)
                          else:
                              canvas.create_image(x_tank-34, y_tank-27, image=tank_blue_6, anchor=NW)
                      else:
                          canvas.create_image(x_tank-31, y_tank-29, image=tank_blue_7, anchor=NW)
                  else:
                      if t_orientation > 281.5:
                          canvas.create_image(x_tank-26, y_tank-31, image=tank_blue_8, anchor=NW)
                      else:
                          canvas.create_image(x_tank-22, y_tank-30, image=tank_blue_9, anchor=NW)
              else:
                  if t_orientation > 214:
                      if t_orientation > 236:
                          canvas.create_image(x_tank-26, y_tank-31, image=tank_blue_10, anchor=NW)
                      else:
                          canvas.create_image(x_tank-28, y_tank-31, image=tank_blue_11, anchor=NW)
                  else:
                      if t_orientation > 191.5:
                          canvas.create_image(x_tank-32, y_tank-28, image=tank_blue_12, anchor=NW)
                      else:
                          canvas.create_image(x_tank-31, y_tank-26, image=tank_blue_13, anchor=NW)

          else:
              if t_orientation > 79:
                  if t_orientation > 124:
                      if t_orientation > 146.5:
                          canvas.create_image(x_tank-30, y_tank-28, image=tank_blue_14, anchor=NW)
                      else:
                          canvas.create_image(x_tank-31, y_tank-29, image=tank_blue_15, anchor=NW)
                  else:
                      if t_orientation > 101.5:
                          canvas.create_image(x_tank-26, y_tank-30, image=tank_blue_16, anchor=NW)
                      else:
                          canvas.create_image(x_tank-19, y_tank-29, image=tank_blue_1, anchor=NW)
              else:
                  if t_orientation > 34:
                      if t_orientation > 56.5:
                          canvas.create_image(x_tank-22, y_tank-28, image=tank_blue_2, anchor=NW)
                      else:
                          canvas.create_image(x_tank-29, y_tank-28, image=tank_blue_3, anchor=NW)
                  else:
                      if t_orientation > 11.5:
                          canvas.create_image(x_tank-34, y_tank-28, image=tank_blue_4, anchor=NW)
                      else:
                          canvas.create_image(x_tank-34, y_tank-27, image=tank_blue_5, anchor=NW)
        else:
            if t_orientation > 169:
                if t_orientation > 259:
                    if t_orientation > 304:
                        if t_orientation > 326.5:
                            if t_orientation > 349:
                                canvas.create_image(x_tank-34, y_tank-27, image=tank_red_5, anchor=NW)
                            else:
                                canvas.create_image(x_tank-34, y_tank-27, image=tank_red_6, anchor=NW)
                        else:
                            canvas.create_image(x_tank-31, y_tank-29, image=tank_red_7, anchor=NW)
                    else:
                        if t_orientation > 281.5:
                            canvas.create_image(x_tank-26, y_tank-31, image=tank_red_8, anchor=NW)
                        else:
                            canvas.create_image(x_tank-22, y_tank-30, image=tank_red_9, anchor=NW)
                else:
                    if t_orientation > 214:
                        if t_orientation > 236:
                            canvas.create_image(x_tank-26, y_tank-31, image=tank_red_10, anchor=NW)
                        else:
                            canvas.create_image(x_tank-28, y_tank-31, image=tank_red_11, anchor=NW)
                    else:
                        if t_orientation > 191.5:
                            canvas.create_image(x_tank-32, y_tank-28, image=tank_red_12, anchor=NW)
                        else:
                            canvas.create_image(x_tank-31, y_tank-26, image=tank_red_13, anchor=NW)
                
            else:
                if t_orientation > 79:
                    if t_orientation > 124:
                        if t_orientation > 146.5:
                            canvas.create_image(x_tank-30, y_tank-28, image=tank_red_14, anchor=NW)
                        else:
                            canvas.create_image(x_tank-31, y_tank-29, image=tank_red_15, anchor=NW)
                    else:
                        if t_orientation > 101.5:
                            canvas.create_image(x_tank-26, y_tank-30, image=tank_red_16, anchor=NW)
                        else:
                            canvas.create_image(x_tank-19, y_tank-29, image=tank_red_1, anchor=NW)
                else:
                    if t_orientation > 34:
                        if t_orientation > 56.5:
                            canvas.create_image(x_tank-22, y_tank-28, image=tank_red_2, anchor=NW)
                        else:
                            canvas.create_image(x_tank-29, y_tank-28, image=tank_red_3, anchor=NW)
                    else:
                        if t_orientation > 11.5:
                            canvas.create_image(x_tank-34, y_tank-28, image=tank_red_4, anchor=NW)
                        else:
                            canvas.create_image(x_tank-34, y_tank-27, image=tank_red_5, anchor=NW)
        
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
            
    #Dibujamos el marcador:
    
    canvas.create_rectangle(0,0,CANVAS_WIDTH,CANVAS_SCORE,fill="grey70")
    canvas.create_rectangle(10, 10, 150, 40, fill= "MediumPurple1")
    canvas.create_rectangle(850, 10, 990, 40, fill= "Plum2")
    canvas.create_text(50, 25, text="Equipo 1", fill="black", font=("Arial", 15))
    canvas.create_text(890, 25, text="Equipo 2", fill="black", font=("Arial", 15))
    
    #Dibujamos las estrellas según las vidas de cada tanque del equipo
    
    if team_lives[0]==0:
        canvas.create_image(95,20,image = estrella_gris, anchor= NW)
        canvas.create_image(110,20,image = estrella_gris, anchor= NW)
        canvas.create_image(125,20,image = estrella_gris, anchor= NW)
    elif team_lives[0]==1:
        canvas.create_image(95,20,image = estrella_amarilla, anchor= NW)
        canvas.create_image(110,20,image = estrella_gris, anchor= NW)
        canvas.create_image(125,20,image = estrella_gris, anchor= NW)
    elif team_lives[0]==2:
        canvas.create_image(95,20,image = estrella_amarilla, anchor= NW)
        canvas.create_image(110,20,image = estrella_amarilla, anchor= NW)
        canvas.create_image(125,20,image = estrella_gris, anchor= NW)
    else:
        canvas.create_image(95,20,image = estrella_amarilla, anchor= NW)
        canvas.create_image(110,20,image = estrella_amarilla, anchor= NW)
        canvas.create_image(125,20,image = estrella_amarilla, anchor= NW)
        
        
    if team_lives[1]==0:
        canvas.create_image(935,20,image = estrella_gris, anchor= NW)
        canvas.create_image(950,20,image = estrella_gris, anchor= NW)
        canvas.create_image(965,20,image = estrella_gris, anchor= NW)
    elif team_lives[1]==1:
        canvas.create_image(935,20,image = estrella_amarilla, anchor= NW)
        canvas.create_image(950,20,image = estrella_gris, anchor= NW)
        canvas.create_image(965,20,image = estrella_gris, anchor= NW)
    elif team_lives[1]==2:
        canvas.create_image(935,20,image = estrella_amarilla, anchor= NW)
        canvas.create_image(950,20,image = estrella_amarilla, anchor= NW)
        canvas.create_image(965,20,image = estrella_gris, anchor= NW)
    else:
        canvas.create_image(935,20,image = estrella_amarilla, anchor= NW)
        canvas.create_image(950,20,image = estrella_amarilla, anchor= NW)
        canvas.create_image(965,20,image = estrella_amarilla, anchor= NW)
    
    #Pasamos a dibijar el primer mapa
    
    if mapa==1:
        canvas.create_line(100,50,100,120,fill="grey99")
        canvas.create_line(100,255,100,395,fill="grey99")
        canvas.create_line(100,530,100,600,fill="grey99")
        canvas.create_line(400,50,400,120,fill="grey99")
        canvas.create_line(400,255,400,395,fill="grey99")
        canvas.create_line(400,530,400,600,fill="gray99")
        canvas.create_line(600,50,600,120,fill="grey99")
        canvas.create_line(600,255,600,395,fill="grey99")
        canvas.create_line(600,530,600,600,fill="grey99")
        canvas.create_line(900,50,900,120,fill="grey99")
        canvas.create_line(900,255,900,395,fill="grey99")
        canvas.create_line(900,530,900,600,fill="grey99")
        canvas.create_line(0,325,400,325,fill="grey99")
        canvas.create_line(600,325,1000,325,fill="grey99")
        canvas.create_rectangle(170,140,330,235,fill="grey99")
        canvas.create_rectangle(170,415,330,510,fill="grey99")
        canvas.create_rectangle(670,140,830,235,fill="grey99")
        canvas.create_rectangle(670,415,830,510,fill="grey99")
        canvas.create_rectangle(475,271.25,525,353.75,fill="grey99")
    
    #El segundo mapa: 
    
    elif mapa == 2:
        canvas.create_line(0,200,50,200,fill="grey99")
        canvas.create_line(100,250,100,300,fill="grey99")
        canvas.create_line(0,300,100,300,fill="grey99")
        
        canvas.create_line(125,112.5,125,237.5,fill="grey99")
        canvas.create_line(125,112.5,250,112.5,fill="grey99")
        canvas.create_line(125,237.5,250,237.5,fill="grey99")
        
        canvas.create_line(375,112.5,375,370,fill="grey99")
        canvas.create_line(250,175,375,175,fill="grey99")
        canvas.create_line(375,237.5,475,237.5,fill="grey99")
        canvas.create_line(150,370,375,370,fill="grey99")
        canvas.create_line(262.5,370,262.5,537.5,fill="grey99")
        
        canvas.create_line(0,370,75,370,fill="grey99")
        
        canvas.create_line(400,50,400,100,fill="grey99")
        canvas.create_line(450,150,500,150,fill="grey99")
        canvas.create_line(500,50,500,150,fill="grey99")
        
        
        
        canvas.create_line(0,500,50,500,fill="grey99")
        canvas.create_line(100,550,100,600,fill="grey99")
        
        
        canvas.create_line(950,150,1000,150,fill="grey99")
        canvas.create_line(900,50,900,100,fill="grey99")
        
        canvas.create_line(737.5,112.5,737.5,280,fill="grey99")
        canvas.create_line(625,280,850,280,fill="grey99")
        canvas.create_line(625,280,625,537.5,fill="grey99")
        canvas.create_line(625,475,750,475,fill="grey99")
        canvas.create_line(525,412.5,625,412.5,fil="grey99")
        
        canvas.create_line(925,280,1000,280,fill="grey99")
        
        canvas.create_line(600,550,600,600,fill="grey99")
        canvas.create_line(500,500,500,600,fill="grey99")
        canvas.create_line(500,500,550,500,fill="grey99")
        
    
        canvas.create_line(950,450,1000,450,fill="grey99")
        canvas.create_line(900,350,1000,350,fill="grey99")
        canvas.create_line(900,350,900,400,fill="grey99")
        
        
        canvas.create_line(750,537.5,875,537.5,fill="grey99")
        canvas.create_line(875,412,875,537.5,fill="grey99")
        canvas.create_line(750,412,875,412,fill="grey99")
    
    """
    
    #Has perdido
    
    canvas.create_rectangle(310, 190, 730, 410,fill= "yellow")
    canvas.create_rectangle(330, 210, 710, 390,fill= "grey30")
    canvas.create_text(515, 250, text="GAME OVER", fill="black", font=("Arial", 40, "bold"))
    canvas.create_image(400,285,image = estrella_gameover, anchor= NW)
    canvas.create_image(490,285,image = estrella_gameover, anchor= NW)
    canvas.create_image(580,285,image = estrella_gameover, anchor= NW)
    
    #Has ganado
    
    canvas.create_rectangle(310, 190, 730, 410,fill= "yellow")
    canvas.create_rectangle(330, 210, 710, 390,fill= "grey20")
    canvas.create_text(515, 250, text="YOU WIN!", fill="yellow", font=("Arial", 40, "bold"))
    canvas.create_image(470,285,image = trofeo, anchor= NW)
    
    """
if __name__ == '__main__':    

    root = Tk()
    root.title("MyTank")
    root.resizable(0, 0)
    root.iconbitmap("tanque2.ico")
    
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
    bullets = 3
    
    #Cargamos todas las imágenes
    
    tank_blue_1 = PhotoImage(file='images/tank_blue_1.png')
    tank_blue_2 = PhotoImage(file='images/tank_blue_2.png')
    tank_blue_3 = PhotoImage(file='images/tank_blue_3.png')
    tank_blue_4 = PhotoImage(file='images/tank_blue_4.png')
    tank_blue_5 = PhotoImage(file='images/tank_blue_5.png')
    tank_blue_6 = PhotoImage(file='images/tank_blue_6.png')
    tank_blue_7 = PhotoImage(file='images/tank_blue_7.png')
    tank_blue_8 = PhotoImage(file='images/tank_blue_8.png')
    tank_blue_9 = PhotoImage(file='images/tank_blue_9.png')
    tank_blue_10 = PhotoImage(file='images/tank_blue_10.png')
    tank_blue_11 = PhotoImage(file='images/tank_blue_11.png')
    tank_blue_12 = PhotoImage(file='images/tank_blue_12.png')
    tank_blue_13 = PhotoImage(file='images/tank_blue_13.png')
    tank_blue_14 = PhotoImage(file='images/tank_blue_14.png')
    tank_blue_15 = PhotoImage(file='images/tank_blue_15.png')
    tank_blue_16 = PhotoImage(file='images/tank_blue_16.png')
    
    tank_red_1 = PhotoImage(file='images/tank_red_1.png')
    tank_red_2 = PhotoImage(file='images/tank_red_2.png')
    tank_red_3 = PhotoImage(file='images/tank_red_3.png')
    tank_red_4 = PhotoImage(file='images/tank_red_4.png')
    tank_red_5 = PhotoImage(file='images/tank_red_5.png')
    tank_red_6 = PhotoImage(file='images/tank_red_6.png')
    tank_red_7 = PhotoImage(file='images/tank_red_7.png')
    tank_red_8 = PhotoImage(file='images/tank_red_8.png')
    tank_red_9 = PhotoImage(file='images/tank_red_9.png')
    tank_red_10 = PhotoImage(file='images/tank_red_10.png')
    tank_red_11 = PhotoImage(file='images/tank_red_11.png')
    tank_red_12 = PhotoImage(file='images/tank_red_12.png')
    tank_red_13 = PhotoImage(file='images/tank_red_13.png')
    tank_red_14 = PhotoImage(file='images/tank_red_14.png')
    tank_red_15 = PhotoImage(file='images/tank_red_15.png')
    tank_red_16 = PhotoImage(file='images/tank_red_16.png')
    
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
        global movement, bullets
        if shoot and bullets>0:
            bullets -= 1
            last_time_shooted = time.time()
            shooted = True
        elif shooted:
            current_time = time.time()
            diff = current_time - last_time_shooted
            if diff >= 3:
                bullets = 3
                reload = True
                shooted = False
        pointer_position = (pointer_x, pointer_y)
        state = (pointer_position, movement, shoot, reload)
        try:
            conn.send(state)
        except :
            message = (([], []), 0, -1)
        try:
            message = conn.recv()
        except :
            message = (([], []), 0, -1)
        reload = False
        shoot = False
        draw_board(canvas, message)
    
    def repet_act():
        global shoot, shooted, last_time_shooted, reload
        global movement, bullets
        key = movement
        for i in range(15):
            if shoot and bullets>0:
                bullets -= 1
                last_time_shooted = time.time()
                shooted = True
            elif shooted:
                current_time = time.time()
                diff = current_time - last_time_shooted
                if diff >= 3:
                    bullets = 3
                    reload = True
                    shooted = False
            pointer_position = (pointer_x, pointer_y)
            state = (pointer_position, key, shoot, reload)
            try:
                conn.send(state)
            except :
                message = (([], []), 0, -1)
            try:
                message = conn.recv()
            except :
                message = (([], []), 0, -1)
            reload = False
            shoot = False
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
