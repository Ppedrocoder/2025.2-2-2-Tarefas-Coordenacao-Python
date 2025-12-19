# Atividade Avaliativa: Problema do Produtor-Consumidor

## 🎯 Objetivos de Aprendizagem

Nesta atividade, você irá aprender:
- Como threads funcionam em Python
- Como resolver problemas de concorrência com semáforos
- O que é o problema clássico do produtor-consumidor
- Como sincronizar acesso a recursos compartilhados

## 📋 Descrição do Problema

O problema do produtor-consumidor é um clássico da programação concorrente. Imagine uma fábrica onde:
- **Produtores** criam itens e os colocam em um buffer (fila limitada)
- **Consumidores** retiram itens do buffer para processá-los
- O buffer tem capacidade limitada (ex: 10 itens)

### Desafios de Concorrência:
1. **Produtor não pode adicionar** se o buffer está cheio
2. **Consumidor não pode remover** se o buffer está vazio
3. **Produtor e consumidor não podem acessar o buffer simultaneamente** (condição de corrida)

## ✅ Checklist Passo a Passo

### Fase 1: Preparação (15 minutos)
- [ ] Criar arquivo `produtor_consumidor.py` ou usar o `template_produtor_consumidor.py`
- [ ] Importar bibliotecas necessárias: `threading`, `time`, `random`
- [ ] Importar `Semaphore` e `Lock` de `threading`
- [ ] Verificar as constantes já definidas: `TAMANHO_BUFFER`, `NUM_PRODUTORES`, `NUM_CONSUMIDORES`

### Fase 2: Estrutura de Dados (10 minutos)
- [ ] Verificar que o buffer (lista vazia) já está criado
- [ ] Criar um semáforo para controlar itens disponíveis: `itens_disponiveis = Semaphore(0)`
- [ ] Criar um semáforo para controlar espaços vazios: `espacos_vazios = Semaphore(TAMANHO_BUFFER)`
- [ ] Criar um lock (mutex) para proteger o acesso ao buffer: `lock = Lock()`

### Fase 3: Implementar a Função Produtor (20 minutos)
- [ ] Criar função `produtor(id_produtor)` que recebe o ID do produtor
- [ ] Criar loop infinito ou com número definido de iterações
- [ ] Gerar item aleatório (pode ser um número)
- [ ] **Antes de adicionar ao buffer:**
  - [ ] Aguardar por espaço vazio: `espacos_vazios.acquire()`
  - [ ] Adquirir o lock: `lock.acquire()`
- [ ] Adicionar item ao buffer
- [ ] Exibir mensagem: "Produtor X produziu item Y. Buffer: [conteúdo]"
- [ ] **Depois de adicionar:**
  - [ ] Liberar o lock: `lock.release()`
  - [ ] Sinalizar item disponível: `itens_disponiveis.release()`
- [ ] Simular tempo de produção: `time.sleep(random.uniform(0.1, 0.5))`

### Fase 4: Implementar a Função Consumidor (20 minutos)
- [ ] Criar função `consumidor(id_consumidor)` que recebe o ID do consumidor
- [ ] Criar loop infinito ou com número definido de iterações
- [ ] **Antes de remover do buffer:**
  - [ ] Aguardar por item disponível: `itens_disponiveis.acquire()`
  - [ ] Adquirir o lock: `lock.acquire()`
- [ ] Remover item do buffer (primeiro item da lista)
- [ ] Exibir mensagem: "Consumidor X consumiu item Y. Buffer: [conteúdo]"
- [ ] **Depois de remover:**
  - [ ] Liberar o lock: `lock.release()`
  - [ ] Sinalizar espaço vazio: `espacos_vazios.release()`
- [ ] Simular tempo de consumo: `time.sleep(random.uniform(0.1, 0.5))`

### Fase 5: Programa Principal (15 minutos)
- [ ] Criar função `main()` ou bloco `if __name__ == "__main__":`
- [ ] Criar lista para armazenar threads: `threads = []`
- [ ] Criar threads de produtores:
  - [ ] Loop de 0 até NUM_PRODUTORES
  - [ ] Criar thread: `t = threading.Thread(target=produtor, args=(i,))`
  - [ ] Adicionar à lista de threads
  - [ ] Iniciar thread: `t.start()`
- [ ] Criar threads de consumidores:
  - [ ] Loop de 0 até NUM_CONSUMIDORES
  - [ ] Criar thread: `t = threading.Thread(target=consumidor, args=(i,))`
  - [ ] Adicionar à lista de threads
  - [ ] Iniciar thread: `t.start()`
- [ ] Aguardar todas as threads terminarem:
  - [ ] Loop em todas as threads
  - [ ] Chamar `t.join()`

### Fase 6: Testes e Validação (20 minutos)
- [ ] Executar o programa e observar a saída
- [ ] Verificar se o buffer nunca excede o tamanho máximo
- [ ] Verificar se não há erros de índice (tentar remover de lista vazia)
- [ ] Observar se produtores e consumidores estão sincronizados
- [ ] Testar com diferentes números de produtores e consumidores
- [ ] Testar com diferentes tamanhos de buffer

### Fase 7: Melhorias (Opcional - 15 minutos)
- [ ] Adicionar condição de parada (ex: produzir/consumir N itens)
- [ ] Adicionar contador de itens produzidos/consumidos
- [ ] Exibir estatísticas ao final da execução
- [ ] Adicionar tratamento de exceções (try-except)
- [ ] Adicionar logs mais detalhados com timestamp

## 🧪 Como Testar

### Teste Básico
```bash
python produtor_consumidor.py
```

### Comportamentos Esperados:
1. ✅ Buffer nunca deve ter mais de 10 itens
2. ✅ Não deve haver erros de "list index out of range"
3. ✅ Mensagens de produtor e consumidor devem alternar de forma ordenada
4. ✅ O programa deve executar sem deadlocks (travamentos)

### Teste de Estresse:
- Aumentar `NUM_PRODUTORES = 5` e `NUM_CONSUMIDORES = 3`
- Diminuir `TAMANHO_BUFFER = 5`
- O programa ainda deve funcionar corretamente

## 📚 Conceitos Importantes

### Semáforos
Um semáforo é um contador que controla o acesso a recursos:
- `acquire()`: Decrementa o contador. Se for 0, bloqueia até que seja maior que 0
- `release()`: Incrementa o contador e desbloqueia uma thread esperando

### Lock (Mutex)
Um lock garante exclusão mútua:
- Apenas uma thread pode segurar o lock por vez
- Protege seções críticas do código (acesso ao buffer)

### Por que precisamos de 3 mecanismos?
- `espacos_vazios`: Garante que produtor não adiciona em buffer cheio
- `itens_disponiveis`: Garante que consumidor não remove de buffer vazio
- `lock`: Garante que apenas uma thread acessa o buffer por vez

## 🏆 Critérios de Avaliação

| Critério | Pontos |
|----------|--------|
| Implementação correta dos semáforos | 3.0 |
| Função produtor funcionando corretamente | 2.5 |
| Função consumidor funcionando corretamente | 2.5 |
| Sincronização correta (sem condições de corrida) | 1.5 |
| Código organizado e comentado | 0.5 |
| **Total** | **10.0** |

## 💡 Dicas

1. **Ordem importa**: Sempre adquira semáforos antes de locks para evitar deadlock
2. **Sempre libere**: Todo `acquire()` deve ter um `release()` correspondente
3. **Use try-finally**: Para garantir que locks sejam liberados mesmo com erros
4. **Teste incremental**: Teste primeiro com 1 produtor e 1 consumidor
5. **Debug com prints**: Use mensagens para entender o fluxo de execução

## 🔗 Recursos Adicionais

- [Documentação Python Threading](https://docs.python.org/3/library/threading.html)
- [Tutorial sobre Semáforos](https://realpython.com/intro-to-python-threading/)
- Consulte `template_produtor_consumidor.py` para estrutura inicial
- Consulte `solucao_produtor_consumidor.py` apenas após tentar resolver sozinho

## 🆘 Problemas Comuns

### "IndexError: list index out of range"
➡️ Você esqueceu de usar `itens_disponiveis.acquire()` antes de remover

### O programa trava (deadlock)
➡️ Verifique se você está chamando `release()` para todos os `acquire()`

### Buffer fica maior que o tamanho máximo
➡️ Você esqueceu de usar `espacos_vazios.acquire()` antes de adicionar

### Condição de corrida (mensagens estranhas)
➡️ Certifique-se de adquirir o lock antes de acessar o buffer

Boa sorte! 🚀
