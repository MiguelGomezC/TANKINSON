# -*- coding: utf-8 -*-

#Definimos el tablero, recurso en competencia
#Pensar en la estructura de datos... es quizás los más interesante
# del problema, la parte de conc/dist parece fácil.

#procesos que atienden a los clientes:
#recibe dato (id, movimiento, tecla)
#accede en EM al tablero y comprueba si come o es comido, actualiza posición
# y devuelve la ventana de tablero.
#envía de vuelta al cliente la ventana de tablero

from multiprocessing.connection import Listener
from multiprocessing import Process
from multiprocessing.connection import AuthenticationError
from multiprocessing import Lock
from multiprocessing import Manager
from multiprocessing import Queue
from multiprocessing import Value
from multiprocessing import Pipe
from tkinter import *

import time
import random


import tankClass


def queue_copy(q):
    p = []
    size = q.qsize()
    for i in range(size):
        ele = q.get()
        q.put(ele)
        p.append(ele)
    return p
"""
def move_bullets(board_bullets, semaphore_bullets, mapa):
    while True:#Hay que poner un lock para que no mire siempre, solo cuando haya balas
        #también habría que implementar choque con tanques
        semaphore_bullets.acquire()
        nBullets = board_bullets.qsize()
        for i in range(nBullets):
            bullet = board_bullets.get()
            bullet_state = bullet.move(mapa)
            if bullet_state:
                board_bullets.put(bullet)
        semaphore_bullets.release()
        time.sleep(0.03)

def move_bullets(board_bullets, semaphore_bullets, board_tanks, mapa):
    while True:#Hay que poner un lock para que no mire siempre, solo cuando haya balas
        #también habría que implementar choque con tanques
        semaphore_bullets.acquire()
        nBullets = board_bullets.qsize()
        for i in range(nBullets):
            bullet = board_bullets.get()
            bullet_state = bullet.move(mapa)
            collision = False
            for tank in board_tanks.keys():
                if bullet.close(board_tanks[tank]):
                    collision = bullet.impact(board_tanks[tank])
            if bullet_state and not collision:
                board_bullets.put(bullet)
        semaphore_bullets.release()
        time.sleep(0.01)
"""
def move_bullets(board_bullets, semaphore_bullets, board_tanks, semaphore_tanks, mapa):
    while True:#Hay que poner un lock para que no mire siempre, solo cuando haya balas
        #también habría que implementar choque con tanques
        semaphore_bullets.acquire()
        nBullets = board_bullets.qsize()
        for i in range(nBullets):
            bullet = board_bullets.get()
            bullet_state = bullet.move(mapa)
            collision=False
            for key in board_tanks.keys():
                tank=board_tanks[key]
                if bullet.close(tank):
                    collision=bullet.impact(tank) and bullet.get_team()!=tank.get_team()
                if collision:
                    semaphore_tanks.acquire()
                    tank.tank_kill()
                    board_tanks[key] = tank
                    semaphore_tanks.release()
                    break
            if bullet_state and not collision:
                board_bullets.put(bullet)
        semaphore_bullets.release()
        time.sleep(0.03)

def clear_client(board, id):
    print("board pop")
    board.pop(id[1])

def update_board(board_tanks, board_bullets, semaphore_bullets, semaphore_tanks, id, m): 
    pointer_pos, movement, shoot, reload = m
    semaphore_bullets.acquire()
    semaphore_tanks.acquire()
    tank = board_tanks[id[1]]
    tank.move(movement)
    tank.set_pointer(pointer_pos)
    if shoot:
        if tank.has_bullets():#Patch
            bullet = tank.shoot()
            board_bullets.put(bullet)
    elif reload:
        tank.reload()
    bullets_copy = queue_copy(board_bullets)
    board_tanks[id[1]] = tank
    semaphore_tanks.release()
    semaphore_bullets.release()
    return (board_tanks.items(), bullets_copy)

def serve_client(conn, id, beg, board_tanks, semaphore_tanks, board_bullets, semaphore_bullets, count, semaphore_count, mapa, position_ini):
    value = random.random()
    semaphore_count.acquire()
    if count.value > 0:
        count.value -= 1
        position_ini.value +=1
        pos_ini = position_ini.value
        semaphore_count.release()
        team = 0
    elif count.value < 0:
        count.value += 1
        position_ini.value +=1
        pos_ini = position_ini.value
        semaphore_count.release()
        team = 1
    else:
        if value <= 0.5:
            count.value += 1
            position_ini.value +=1
            pos_ini = position_ini.value
            semaphore_count.release()
            team = 1
        else:
            count.value -= 1
            position_ini.value +=1
            pos_ini = position_ini.value
            semaphore_count.release()
            team = 0
    tank = tankClass.TankClass(team, id[1], mapa, pos_ini)
    board_tanks[id[1]] = tank
    while True:
        try:
            m = conn.recv()
        except:
            print('No receive, connection abruptly closed by client')
            break
        print ('received message:', m, 'from', id[1])
        
      
        board_elements = update_board(board_tanks, board_bullets, semaphore_bullets, semaphore_tanks, id, m)
        if board_tanks[id[1]].tank_death():
            if board_tanks[id[1]].get_team()==0:
                semaphore_count.acquire()
                count.value += 1
                semaphore_count.release()
            else:
                semaphore_count.acquire()
                count.value -= 1
                semaphore_count.release()
            mapa = -1
            answer = (board_elements, id[1], mapa)
            try:
                conn.send(answer)
                break
            except IOError:
                print ('No send, connection abruptly closed by client')
                break
            print('tank',id,'is dead')
            
        answer = (board_elements, id[1], mapa)

        try:
            conn.send(answer)
        except IOError:
            print ('No send, connection abruptly closed by client')
            break
        time.sleep(0.01)

    semaphore_tanks.acquire()
    clear_client(board_tanks,id)
    beg.send(pos_ini)
    semaphore_tanks.release()
    conn.close()
    print ('connection', id, 'closed')

def connect(queue, beg, end, board_tanks, wait_semaphore,semaphore_tanks,board_bullets,semaphore_bullets, count, semaphore_count, mapa, position_ini):
    """
    Proceso que mete a los clientes en la partida por orden de cola si hay hueco
    """
    while True:
        m = end.poll(15)
        wait_semaphore.acquire()
        while len(board_tanks)<6 and queue.qsize()>0:
            conn, last_accepted=queue.get()
            if type(m) == int:
                position_ini = m
            p = Process(target=serve_client, args=(conn, last_accepted, beg, board_tanks, semaphore_tanks, board_bullets, semaphore_bullets, count, semaphore_count, mapa, position_ini))
            p.start()
        wait_semaphore.release()

if __name__ == '__main__':

    listener = Listener(address=('127.0.0.1', 6000), authkey=b'secret')
    print ('listener starting')
    
    manager = Manager()
    board_tanks = manager.dict()
    board_bullets = Queue()
    semaphore_tanks = Lock()
    semaphore_bullets = Lock()
    count = Value('i',0)
    position_ini = Value('i',0)
    semaphore_count = Lock()
    
    #Usamos Tkinter para poder elegir entre los dos mapas 
    
    root = Tk()
    root.title("New game")
    root.resizable(0, 0)
    root.iconbitmap("Tanque2.ico")
    
    def opciones_mapa():
        opcionEscogida = ""
    
        if (map1.get()==1 and map2.get()==0):
            opcionEscogida += " Map 1 "
            return  2
        elif (map2.get()==1 and map1.get()==0):
            opcionEscogida += " Map 2 "
            return 1
        elif (map2.get()==0 and map1.get()==0):
            opcionEscogida += " You have to choose a map "
        else:
            opcionEscogida += " Choose only one map "

        textoFinal.config(text= opcionEscogida)
    
    
    map1 = IntVar()
    map2 = IntVar()
    foto = PhotoImage(file = "mapita1.png")
    Label(root, image = foto).pack()
    frame = Frame(root)
    frame.pack()
    Label(frame, text = "Elige el mapa", width = 60).pack()
    Checkbutton(frame, text = "Map 1", variable = map1, onvalue = 1, offvalue = 0, command=opciones_mapa).pack()
    Checkbutton(frame, text = "Map 2", variable = map2, onvalue = 1, offvalue = 0, command=opciones_mapa).pack()
    textoFinal= Label(frame)
    textoFinal.pack()
    
    def iniciate_map():
        if map1.get() + map2.get() == 2:
            print("choose only one map")
        elif map1.get() + map2.get() == 0:
            print("you have to choose a map")
        else:
            print("map selected")
            root.destroy()
    
    #Cuando pulsemos Aceptar desaparecerá la ventana con las opciones 
    Button(root, text="Accept", command=iniciate_map).pack()
    root.mainloop()

    
    mapa = opciones_mapa()
    
    mb = Process(target=move_bullets, args=(board_bullets, semaphore_bullets, board_tanks, semaphore_tanks, mapa))
    mb.start()
    
    queue = Queue() #lista de espera
    wait_semaphore = Lock()
    end, beg = Pipe(False) #serve_client y el propio connect notifica cuando un usuario es derrotado y queda un sitio libre, y el proceso connect lo detecta.
    q = Process(target=connect, args = (queue, beg, end, board_tanks, wait_semaphore,semaphore_tanks,board_bullets,semaphore_bullets, count, semaphore_count, mapa, position_ini))
    q.start()
    while True:
        print ('accepting conexions')
        try:
            conn = listener.accept()
            print ('connection accepted from', listener.last_accepted)
            wait_semaphore.acquire()
            queue.put((conn, listener.last_accepted))
            beg.send('new user')
            wait_semaphore.release()
        except AuthenticationError:
            print ('Connection refused, incorrect password')
    listener.close()
    print ('end')


















