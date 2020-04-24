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
    """
    Función que nos devuelve una copia de la cola.
    """
    p = []
    size = q.qsize()
    for i in range(size):
        ele = q.get()
        q.put(ele)
        p.append(ele)
    return p

def move_bullets(board_bullets, semaphore_bullets, board_tanks, semaphore_tanks, mapa):
    """
    Esta función coge la cola de las balas en el tablero y se asegura de que todas se muevan. Además, en caso de que impacten con un tanque
    se asegura de que ese tanque pierda una vida (llamando a tank_kill). Como vamos a modificar tanques y balas llamamos a ambos procedimientos.
    """
    while True:#Hay que poner un lock para que no mire siempre, solo cuando haya balas
        semaphore_bullets.acquire()
        nBullets = board_bullets.qsize()
        for i in range(nBullets):
            bullet = board_bullets.get()
            bullet_state = bullet.move(mapa)
            collision=False
            for key in board_tanks.keys():
                tank=board_tanks[key]
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
    """
    Elimina del tablero el tanque asociado a esa id.
    """
    print("board pop")
    board.pop(id[1])

def update_board(board_tanks, board_bullets, semaphore_bullets, semaphore_tanks, id, m):
    """
    Esta función se encarga de mover los tanques y poner los punteros hacia donde se está apuntando. También genera un objeto 'bullet' 
    si el tanque disparó (el usuario intentó disparar y pudo) y recarga si no.
    """
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

def serve_client(conn, id, beg, board_tanks, semaphore_tanks, board_bullets, semaphore_bullets, count, semaphore_count, mapa, position_ini, connected_players, semaphore_connected):
    """
    Función principal del servidor. Primero, selecciona un equipo aleatorio para el primer tanque y si el tanque que accede no es el primero,
    selecciona el equipo al que le falten jugadores hasta alcanzar la igualdad. Si ambos equipos tienen el mismo número de tanques (como mucho 3)
    los pone por orden (si el primer jugador fue al Equipo 1, el segundo necesariamente irá al Equipo 2).
    Luego recibe el input del jugador y actualiza el tablero en consecuencia. Si un tanque pierde todas sus vidas o el jugador se desconecta, es
    expulsado de la partida.
    """
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
    semaphore_connected.acquire()
    connected_players.value -= 1
    semaphore_connected.release()
    print ('connection', id, 'closed')

def connect(queue, beg, end, board_tanks, wait_semaphore,semaphore_tanks,board_bullets,semaphore_bullets, count, semaphore_count, mapa, position_ini, connected_players, semaphore_connected):
    """
    Proceso que mete a los clientes en la partida por orden de cola si hay hueco.
    """
    while True:
        m = end.poll(0)
        wait_semaphore.acquire()
        if connected_players.value<6 and queue.qsize()>0:
            semaphore_connected.acquire()
            connected_players.value += 1
            semaphore_connected.release()
            conn, last_accepted=queue.get()
            if type(m) == int:
                position_ini = m
            p = Process(target=serve_client, args=(conn, last_accepted, beg, board_tanks, semaphore_tanks, board_bullets, semaphore_bullets, count, semaphore_count, mapa, position_ini, connected_players, semaphore_connected))
            p.start()
        wait_semaphore.release()
        time.sleep(5)

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
    connected_players = Value('i',0)
    semaphore_connected = Lock()
    
    #Usamos Tkinter para poder elegir entre los dos mapas 
    
    root = Tk()
    root.title("New game")
    root.resizable(0, 0)
    root.iconbitmap("images/tank.ico")
    
    def opciones_mapa():
        """
        Función auxiliar a la ventana que nos deja escoger mapa y se asegura de que solo se escoja una opción.
        """
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
    foto = PhotoImage(file = "images/maps.png")
    Label(root, image = foto).pack()
    frame = Frame(root)
    frame.pack()
    Label(frame, text = "Elige el mapa", width = 60).pack()
    Checkbutton(frame, text = "Map 1", variable = map1, onvalue = 1, offvalue = 0, command=opciones_mapa).pack()
    Checkbutton(frame, text = "Map 2", variable = map2, onvalue = 1, offvalue = 0, command=opciones_mapa).pack()
    textoFinal= Label(frame)
    textoFinal.pack()
    
    def iniciate_map():
        """
        Análogamente a opciones_mapa, insta al cliente a seleccionar solo un mapa, pero esta vez impreso por consola.
        """
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
    q = Process(target=connect, args = (queue, beg, end, board_tanks, wait_semaphore,semaphore_tanks,board_bullets,semaphore_bullets, count, semaphore_count, mapa, position_ini, connected_players, semaphore_connected))
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


















