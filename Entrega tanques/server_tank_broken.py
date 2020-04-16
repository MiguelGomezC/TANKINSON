# -*- coding: utf-8 -*-
#test edit

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

import time
import random
import math

import tankClass

CANVAS_WIDTH = 250
CANVAS_HEIGHT = 500

def queue_copy(q):
    p = []
    size = q.qsize()
    for i in range(size):
        ele = q.get()
        q.put(ele)
        p.append(ele)
    return p

def move_bullets(board_bullets, semaphore_bullets, board_tanks):
    while True:#Hay que poner un lock para que no mire siempre, solo cuando haya balas
        #también habría que implementar choque con tanques
        semaphore_bullets.acquire()
        nBullets = board_bullets.qsize()
        for i in range(nBullets):
            bullet = board_bullets.get()
            bullet_state = bullet.move()
            collision=False
            for tank in board_tanks.keys():
               collision=bullet.impact(board_tanks[tank]) and bullet.get_team()!=board_tanks[tank].get_team()
                if collision:
                    break
            if bullet_state and not collision:
                board_bullets.put(bullet)
        semaphore_bullets.release()
        time.sleep(0.03)

def clear_client(board, id):
    print("board pop")
    board.pop(id[1])

def update_board(board_tanks, board_bullets, semaphore_bullets, id, m): #canvas size 500X250
    pointer_pos, movement, shoot = m
    tank = board_tanks[id[1]]
    tank.move(movement)
    tank.set_pointer(pointer_pos)
    semaphore_bullets.acquire()
    if shoot:
        bullet = tank.shoot()
        board_bullets.put(bullet)
    bullets_copy = queue_copy(board_bullets)
    semaphore_bullets.release()
    board_tanks[id[1]] = tank
    return (board_tanks.items(), bullets_copy)

def serve_client(conn, id, board_tanks, semaphore_tanks, board_bullets, semaphore_bullets, count, semaphore_count):
    value = random.random()
    semaphore_count.acquire()
    if count.value > 0:
        count.value -= 1
        semaphore_count.release()
        team = 0
    elif count.value < 0:
        count.value += 1
        semaphore_count.release()
        team = 1
    else:
        if value <= 0.5:
            count.value += 1
            semaphore_count.release()
            team = 1
        else:
            count.value -= 1
            semaphore_count.release()
            team = 0
    tank = tankClass.TankClass(team, id[1])
    board_tanks[id[1]] = tank
    while True:
        try:
            m = conn.recv()
        except EOFError:
            print('No receive, connection abruptly closed by client')
            break
        print ('received message:', m, 'from', id[1])
        
        semaphore_tanks.acquire()
        board_elements = update_board(board_tanks, board_bullets, semaphore_bullets, id, m)
        semaphore_tanks.release()
        answer = (board_elements, id[1])

        try:
            conn.send(answer)
        except IOError:
            print ('No send, connection abruptly closed by client')
            break
        time.sleep(0.01)

    semaphore_tanks.acquire()
    clear_client(board_tanks,id)
    semaphore_tanks.release()
    conn.close()
    print ('connection', id, 'closed')


if __name__ == '__main__':

    listener = Listener(address=('127.0.0.1', 6000), authkey=b'secret')
    print ('listener starting')
    
    manager = Manager()
    board_tanks = manager.dict()
    board_bullets = Queue()
    semaphore_tanks = Lock()
    semaphore_bullets = Lock()
    count = Value('i',0)
    semaphore_count = Lock()
    
    mb = Process(target=move_bullets, args=(board_bullets, semaphore_bullets,board_tanks))
    mb.start()

    while True:
        print ('accepting conexions')
        try:
            conn = listener.accept()                
            print ('connection accepted from', listener.last_accepted)
            p = Process(target=serve_client, args=(conn, listener.last_accepted, board_tanks, semaphore_tanks, board_bullets, semaphore_bullets, count, semaphore_count))
            p.start()
        except AuthenticationError:
            print ('Connection refused, incorrect password')

    listener.close()
    print ('end')









