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
consumido = 0
lock_contador = Lock()

def produtor(id_produtor):
    global produzido

    for i in range(NUM_ITENS_POR_THREAD):
        item = random.randint(1, 100)
        try:
            espacos_vazios.acquire()
            lock.acquire()
            buffer.append(item)
            with lock_contador:
                produzido+=1
            print(f'Produtor {id_produtor} produziu {item:3d}, Buffer: {len(buffer):2d}/{TAMANHO_BUFFER} | {buffer} ')
        finally:
            lock.release()
        itens_disponiveis.release()
        time.sleep(random.uniform(0.1, 0.5))

def consumidor(id_consumidor):
    global consumido

    for i in range(NUM_ITENS_POR_THREAD):
        try:
            itens_disponiveis.acquire()
            lock.acquire()
            item = buffer.pop(0)
            with lock_contador:
                consumido+=1
            print(f'Consumidor {id_consumidor} consumiu {item:3d}, Buffer: {len(buffer):2d}/{TAMANHO_BUFFER} | {buffer}')
        finally:
            lock.release()
        espacos_vazios.release()
        time.sleep(random.uniform(0.1, 0.5))

def main():
    print(f"Configuração:")
    print(f" - Tamanho do buffer: {TAMANHO_BUFFER} - ")
    print(f" - Número de produtores: {NUM_PRODUTORES} - ")
    print(f" - Número de consumidores: {NUM_CONSUMIDORES} - ")
    print(f" - Itens por thread: {NUM_ITENS_POR_THREAD} - ")

    threads = []
    tempo_inicio = time.time()
    for i in range(NUM_PRODUTORES):
        thread = threading.Thread(target=produtor, args=(i,))
        threads.append(thread)
        thread.start()
    
    for i in range(NUM_CONSUMIDORES):
        thread = threading.Thread(target=consumidor, args=(i,))
        threads.append(thread)
        thread.start()
    
    for t in threads:
        t.join()
    tempo_total = time.time() - tempo_inicio
    print(f'Tempo total: {tempo_total}')
    esperado = NUM_PRODUTORES * NUM_ITENS_POR_THREAD
    print(f'Produzido: {produzido}')
    print(f'Consumido: {consumido}')
    if produzido == esperado and consumido == esperado:
        print("Execução feita corretamente")
    else:
        print(f"Esperado {esperado} itens, porém foram produzidos={produzido} e consumidos={consumido}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f" \n Erro na execução: {e}")