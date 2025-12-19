"""
Template para o Problema do Produtor-Consumidor
================================================

INSTRUÇÕES:
Complete este template seguindo o checklist da atividade.
Preencha as seções marcadas com TODO.

Nome do Aluno: _______________________
Data: _______________________
"""

import threading
import time
import random
from threading import Semaphore, Lock

# ============================
# CONFIGURAÇÕES
# ============================

# Constantes já definidas para você
TAMANHO_BUFFER = 10          # Capacidade máxima do buffer
NUM_PRODUTORES = 2           # Número de threads produtoras
NUM_CONSUMIDORES = 2         # Número de threads consumidoras
NUM_ITENS_POR_THREAD = 10    # Quantos itens cada produtor/consumidor processa

# ============================
# ESTRUTURAS DE DADOS COMPARTILHADAS
# ============================

# Buffer já criado para você (lista vazia)
buffer = []

# TODO: Crie o semáforo para itens disponíveis (inicializado com 0)
# itens_disponiveis = ...

# TODO: Crie o semáforo para espaços vazios (inicializado com TAMANHO_BUFFER)
# espacos_vazios = ...

# TODO: Crie o lock para proteger o acesso ao buffer
# lock = ...

# ============================
# FUNÇÃO PRODUTOR
# ============================

def produtor(id_produtor):
    """
    Função executada por cada thread produtora.
    
    Args:
        id_produtor: Identificador único do produtor
    """
    # TODO: Implemente a função produtor
    # Dica: Use um loop para produzir NUM_ITENS_POR_THREAD itens
    
    for i in range(NUM_ITENS_POR_THREAD):
        # TODO: Gere um item aleatório
        # item = ...
        
        # TODO: Aguarde por um espaço vazio no buffer
        # Dica: Use espacos_vazios.acquire()
        
        # TODO: Adquira o lock para acessar o buffer
        # Dica: Use lock.acquire()
        
        try:
            # TODO: Adicione o item ao buffer
            
            # TODO: Exiba uma mensagem informando o que foi produzido
            # Exemplo: print(f"Produtor {id_produtor} produziu item {item}")
            pass
        finally:
            # TODO: Libere o lock
            # Dica: Use lock.release()
            pass
        
        # TODO: Sinalize que há um novo item disponível
        # Dica: Use itens_disponiveis.release()
        
        # TODO: Simule o tempo de produção
        # Dica: Use time.sleep(random.uniform(0.1, 0.5))
    
    print(f"Produtor {id_produtor} finalizou")

# ============================
# FUNÇÃO CONSUMIDOR
# ============================

def consumidor(id_consumidor):
    """
    Função executada por cada thread consumidora.
    
    Args:
        id_consumidor: Identificador único do consumidor
    """
    # TODO: Implemente a função consumidor
    # Dica: Use um loop para consumir NUM_ITENS_POR_THREAD itens
    
    for i in range(NUM_ITENS_POR_THREAD):
        # TODO: Aguarde por um item disponível no buffer
        # Dica: Use itens_disponiveis.acquire()
        
        # TODO: Adquira o lock para acessar o buffer
        # Dica: Use lock.acquire()
        
        try:
            # TODO: Remova o primeiro item do buffer
            # Dica: Use buffer.pop(0)
            # item = ...
            
            # TODO: Exiba uma mensagem informando o que foi consumido
            # Exemplo: print(f"Consumidor {id_consumidor} consumiu item {item}")
            pass
        finally:
            # TODO: Libere o lock
            # Dica: Use lock.release()
            pass
        
        # TODO: Sinalize que há um novo espaço vazio
        # Dica: Use espacos_vazios.release()
        
        # TODO: Simule o tempo de consumo
        # Dica: Use time.sleep(random.uniform(0.1, 0.5))
    
    print(f"Consumidor {id_consumidor} finalizou")

# ============================
# PROGRAMA PRINCIPAL
# ============================

def main():
    """
    Função principal que inicializa e gerencia todas as threads.
    """
    print("=" * 60)
    print("PROBLEMA DO PRODUTOR-CONSUMIDOR")
    print("=" * 60)
    print()
    
    # TODO: Crie uma lista para armazenar as threads
    threads = []
    
    # TODO: Crie e inicie as threads produtoras
    # Dica: Use um loop de 0 até NUM_PRODUTORES
    # Para cada iteração:
    #   - Crie uma thread: threading.Thread(target=produtor, args=(i,))
    #   - Adicione à lista de threads
    #   - Inicie a thread com .start()
    
    # TODO: Crie e inicie as threads consumidoras
    # Dica: Use um loop de 0 até NUM_CONSUMIDORES
    # Para cada iteração:
    #   - Crie uma thread: threading.Thread(target=consumidor, args=(i,))
    #   - Adicione à lista de threads
    #   - Inicie a thread com .start()
    
    # TODO: Aguarde todas as threads terminarem
    # Dica: Use um loop em todas as threads e chame .join()
    # for t in threads:
    #     t.join()
    
    print()
    print("=" * 60)
    print("Programa finalizado!")
    print("=" * 60)

# ============================
# PONTO DE ENTRADA
# ============================

if __name__ == "__main__":
    # TODO: Chame a função main()
    pass
