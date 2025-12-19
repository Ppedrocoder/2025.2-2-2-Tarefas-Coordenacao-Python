import threading
import time
import random
from threading import Semaphore, Lock

TAMANHO_BUFFER = 10          # Capacidade máxima do buffer
NUM_PRODUTORES = 2           # Número de threads produtoras
NUM_CONSUMIDORES = 2         # Número de threads consumidoras
NUM_ITENS_POR_THREAD = 10    # Quantos itens cada produtor/consumidor processa

buffer = []

itens_disponiveis = Semaphore(0)
espacos_vazios = Semaphore(TAMANHO_BUFFER)
lock = Lock()

produzido = 0
consumidor = 0
lock_contador = Lock()

def produtor(id_produtor):
    global produzido

    for i in range(NUM_ITENS_POR_THREAD):
        item = random.randint(1, 200)
        espacos_vazios.acquire()
        lock.acquire()
        try:
            buffer.append(item)
            with lock_contador:
                produzido+=1
            print(f'Produtor {id_produtor} produziu {item}, Buffer: {len(buffer):2d}/{TAMANHO_BUFFER} | {buffer}')
        finally:
            lock.release()
        itens_disponiveis.release()
        time.sleep(random.uniform(0.1, 0.5))