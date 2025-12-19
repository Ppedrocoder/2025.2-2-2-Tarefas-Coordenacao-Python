"""
Solução de Referência: Problema do Produtor-Consumidor
========================================================

Este programa demonstra a solução completa do problema clássico do produtor-consumidor
usando threads e semáforos em Python.

Conceitos Implementados:
- Threads para execução concorrente
- Semáforos para controlar espaços vazios e itens disponíveis
- Lock (mutex) para proteger a seção crítica
- Sincronização entre produtores e consumidores

Autor: Sistema de Ensino de Sistemas Operacionais
"""

import threading
import time
import random
from threading import Semaphore, Lock

# ============================
# CONFIGURAÇÕES
# ============================

TAMANHO_BUFFER = 10          # Capacidade máxima do buffer
NUM_PRODUTORES = 2           # Número de threads produtoras
NUM_CONSUMIDORES = 2         # Número de threads consumidoras
NUM_ITENS_POR_THREAD = 10    # Quantos itens cada produtor/consumidor processa

# ============================
# ESTRUTURAS DE DADOS COMPARTILHADAS
# ============================

buffer = []  # Buffer compartilhado (lista)

# Semáforo para contar itens disponíveis no buffer
# Inicializado com 0 porque o buffer começa vazio
itens_disponiveis = Semaphore(0)

# Semáforo para contar espaços vazios no buffer
# Inicializado com TAMANHO_BUFFER porque o buffer começa totalmente vazio
espacos_vazios = Semaphore(TAMANHO_BUFFER)

# Lock para proteger o acesso ao buffer (exclusão mútua)
lock = Lock()

# Contadores para estatísticas
total_produzido = 0
total_consumido = 0
lock_contadores = Lock()

# ============================
# FUNÇÃO PRODUTOR
# ============================

def produtor(id_produtor):
    """
    Função executada por cada thread produtora.
    
    O produtor:
    1. Gera um item (número aleatório)
    2. Aguarda por espaço vazio no buffer
    3. Adiciona o item ao buffer de forma segura (com lock)
    4. Sinaliza que há um novo item disponível
    
    Args:
        id_produtor: Identificador único do produtor
    """
    global total_produzido
    
    for i in range(NUM_ITENS_POR_THREAD):
        # Gera um item aleatório para produzir
        item = random.randint(1, 100)
        
        # Aguarda por um espaço vazio no buffer
        # Se o buffer estiver cheio, esta thread será bloqueada aqui
        espacos_vazios.acquire()
        
        # SEÇÃO CRÍTICA: acesso exclusivo ao buffer
        lock.acquire()
        try:
            # Adiciona o item ao buffer
            buffer.append(item)
            
            # Atualiza contador
            with lock_contadores:
                total_produzido += 1
            
            # Exibe mensagem informativa
            print(f"🟢 Produtor {id_produtor} produziu item {item:3d} | "
                  f"Buffer: {len(buffer):2d}/{TAMANHO_BUFFER} | {buffer}")
        finally:
            # IMPORTANTE: Sempre liberar o lock, mesmo se houver exceção
            lock.release()
        
        # Sinaliza que há um novo item disponível no buffer
        itens_disponiveis.release()
        
        # Simula o tempo de produção
        time.sleep(random.uniform(0.1, 0.5))
    
    print(f"✅ Produtor {id_produtor} finalizou (produziu {NUM_ITENS_POR_THREAD} itens)")

# ============================
# FUNÇÃO CONSUMIDOR
# ============================

def consumidor(id_consumidor):
    """
    Função executada por cada thread consumidora.
    
    O consumidor:
    1. Aguarda por um item disponível no buffer
    2. Remove o item do buffer de forma segura (com lock)
    3. Processa o item (simulado)
    4. Sinaliza que há um novo espaço vazio
    
    Args:
        id_consumidor: Identificador único do consumidor
    """
    global total_consumido
    
    for i in range(NUM_ITENS_POR_THREAD):
        # Aguarda por um item disponível no buffer
        # Se o buffer estiver vazio, esta thread será bloqueada aqui
        itens_disponiveis.acquire()
        
        # SEÇÃO CRÍTICA: acesso exclusivo ao buffer
        lock.acquire()
        try:
            # Remove o primeiro item do buffer (FIFO - First In, First Out)
            item = buffer.pop(0)
            
            # Atualiza contador
            with lock_contadores:
                total_consumido += 1
            
            # Exibe mensagem informativa
            print(f"🔵 Consumidor {id_consumidor} consumiu item {item:3d} | "
                  f"Buffer: {len(buffer):2d}/{TAMANHO_BUFFER} | {buffer}")
        finally:
            # IMPORTANTE: Sempre liberar o lock, mesmo se houver exceção
            lock.release()
        
        # Sinaliza que há um novo espaço vazio no buffer
        espacos_vazios.release()
        
        # Simula o tempo de consumo/processamento
        time.sleep(random.uniform(0.1, 0.5))
    
    print(f"✅ Consumidor {id_consumidor} finalizou (consumiu {NUM_ITENS_POR_THREAD} itens)")

# ============================
# PROGRAMA PRINCIPAL
# ============================

def main():
    """
    Função principal que inicializa e gerencia todas as threads.
    """
    print("=" * 80)
    print("PROBLEMA DO PRODUTOR-CONSUMIDOR")
    print("=" * 80)
    print(f"Configuração:")
    print(f"  - Tamanho do buffer: {TAMANHO_BUFFER}")
    print(f"  - Número de produtores: {NUM_PRODUTORES}")
    print(f"  - Número de consumidores: {NUM_CONSUMIDORES}")
    print(f"  - Itens por thread: {NUM_ITENS_POR_THREAD}")
    print("=" * 80)
    print()
    
    # Lista para armazenar todas as threads
    threads = []
    
    # Marca o tempo de início
    tempo_inicio = time.time()
    
    # Cria e inicia as threads produtoras
    print("🚀 Iniciando produtores...")
    for i in range(NUM_PRODUTORES):
        t = threading.Thread(target=produtor, args=(i,), name=f"Produtor-{i}")
        threads.append(t)
        t.start()
    
    # Cria e inicia as threads consumidoras
    print("🚀 Iniciando consumidores...")
    for i in range(NUM_CONSUMIDORES):
        t = threading.Thread(target=consumidor, args=(i,), name=f"Consumidor-{i}")
        threads.append(t)
        t.start()
    
    print()
    print("=" * 80)
    print("EXECUÇÃO EM ANDAMENTO...")
    print("=" * 80)
    print()
    
    # Aguarda todas as threads terminarem
    for t in threads:
        t.join()
    
    # Calcula o tempo total de execução
    tempo_total = time.time() - tempo_inicio
    
    # Exibe estatísticas finais
    print()
    print("=" * 80)
    print("ESTATÍSTICAS FINAIS")
    print("=" * 80)
    print(f"✅ Total de itens produzidos: {total_produzido}")
    print(f"✅ Total de itens consumidos: {total_consumido}")
    print(f"✅ Itens restantes no buffer: {len(buffer)}")
    print(f"⏱️  Tempo total de execução: {tempo_total:.2f} segundos")
    print("=" * 80)
    print()
    
    # Verificação de consistência
    esperado = NUM_PRODUTORES * NUM_ITENS_POR_THREAD
    if total_produzido == esperado and total_consumido == esperado:
        print("✅ SUCESSO: Todos os itens foram produzidos e consumidos corretamente!")
    else:
        print(f"⚠️  ATENÇÃO: Esperado {esperado} itens, mas produzidos={total_produzido}, consumidos={total_consumido}")

# ============================
# PONTO DE ENTRADA
# ============================

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Programa interrompido pelo usuário (Ctrl+C)")
    except Exception as e:
        print(f"\n\n❌ Erro durante a execução: {e}")
        import traceback
        traceback.print_exc()
