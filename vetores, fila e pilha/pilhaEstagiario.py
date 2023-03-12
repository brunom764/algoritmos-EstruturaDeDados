# Nesse contexto, desenvolva uma função novaLocacao(pilha, codigo) que adiciona, em tempo O(n) o valor inteiro ‘codigo’
# na sua posição apropriada da pilha ‘pilha’ (vetor), se a pilha estiver ordenada.
# A função deve retornar um novo vetor com a nova locação adicionada.
# Mas, atenção, antes disso você deve executar uma função pilhaImaculada(pilha) que checa em tempo O(n) se ela estava
# na ordem certa, antes de fazer a inserção.
#
# Input
#
# A entrada do programa é composta por duas linhas.
# A primeira representa o vetor que se refere à pilha de solicitações, com números inteiros (códigos de locação)
# separados por vírgula e sem espaço, no formato a,b,c.
# A segunda linha é o código da nova locação, que é um inteiro simples
# que deverá ser inserido na lista, se esta estiver ordenada.
#
# Output
#
# Você deve produzir uma única linha de saída. Caso a pilha tenha sido encontrada ordenada e a
# nova solicitação tenha sido inserida nela, deve-se imprimir a nova pilha de solicitações,
# no mesmo formato da entrada (['a','b','c']). Caso a pilha tenha sido encontrada desordenada,
# imprima a expressão “A pilha está um caos.”.

def pilhaAcumulada(pilha):
    ord = False
    for i in range(len(pilha) - 1):
        if pilha[i] < pilha[i+1]:
            ord = True
        else:
            ord = False
            break
    return ord

def novaLocacao(pilha, cod):
    if cod < pilha[0]:
        pilha.insert(0, cod)
    elif cod > pilha[len(pilha) - 1]:
        pilha.insert(len(pilha), cod)
    else:
        for i in range(len(pilha) - 1):
            if cod > pilha[i] and cod < pilha[i+1]:
                pilha.insert(i+1, cod)
    return pilha


pilha = input().split(',')
ordem = pilhaAcumulada(pilha)
if not ordem:
    print('A pilha está um caos.')
else:
    data = input()
    pilha = novaLocacao(pilha, data)
    print(pilha)