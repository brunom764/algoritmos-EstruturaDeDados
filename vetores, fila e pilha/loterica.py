class No:
    def __init__(self, nome, valor):
        self.valor = (nome, float(valor))
        self.prev = None
        self.next = None


class Fila:
    def __init__(self):
        self.head = None
        self.tail = None
        self.tamanho = 0
        self.caixa = 0

    def len(self):
        return self.tamanho

    def naFila(self, nome, valor):  # Entrada na fila
        clienteNovo = No(nome, valor)
        if self.tamanho == 0:
            self.head = clienteNovo
            self.tail = clienteNovo
        else:
            self.tail.next = clienteNovo
            clienteNovo.prev = self.tail
            self.tail = clienteNovo
        self.tamanho += 1

    def metadeFila(self, tamanho):  # descobrir o valor da metade
        if tamanho % 2 != 0:  # impar
            metade = (tamanho + 1) // 2
        else:
            metade = tamanho // 2
        return metade

    def mudaFila(self):  # Cheia -> Vazia
        if self == fila2:  # fila 1 cheia
            metade = self.metadeFila(fila1.len())
            for i in range(metade):
                ultimoNo = fila1.tail
                ultimoNoValor = fila1.tail.valor
                fila2.naFila(ultimoNoValor[0], ultimoNoValor[1])  # Ultimo fila1 -> fila 2
                fila1.tail = fila1.tail.prev  # Novo Ultimo fila 1
                self.tamanho += 1
                fila1.tamanho -= 1

        elif self == fila1:  # fila 2 cheia
            metade = self.metadeFila(fila2.len())
            for i in range(metade):
                ultimoNo = fila2.tail
                ultimoNoValor = fila2.tail.valor
                fila1.naFila(ultimoNoValor[0], ultimoNoValor[1])
                fila2.tail = fila2.tail.prev
                self.tamanho += 1
                fila2.tamanho -= 1

    def proximo(self, fila):  # Remoção da fila
        if self.tamanho == 0:
            self.mudaFila()  # Fila cheia p/ Lista Vazia
        valor = self.head.valor
        self.head = self.head.next
        self.tamanho -= 1
        self.caixa += valor[1]
        if self.tamanho == 0:
            self.tail = None
        print(f"{valor[0]} foi chamado para o caixa {fila}")

    def total(self):  # Valor do caixa
        return self.caixa


# parte principal
fila1 = Fila()
fila2 = Fila()
end = False

while not end:
    comando = input().split()
    if comando[0] == 'ENTROU:':
        if comando[2] == '1':
            fila1.naFila(comando[1], comando[3])
        elif comando[2] == '2':
            fila2.naFila(comando[1], comando[3])
        print(f"{comando[1]} entrou na fila {comando[2]}")

    elif comando[0] == 'PROXIMO:':
        if fila1.len() + fila2.len() == 0:  # evitar runtime error
            comando[0] = 'FIM'
        elif fila1.len() + fila2.len() == 1:  # Ajuste para o final do case 2
            if comando[1] == '1':
                if fila1.len() == 0:
                    fila1.naFila(fila2.tail.value[0], fila2.tail.value[1])
                fila1.proximo(comando[1])
            elif comando[1] == '2':
                if fila2.len() == 0:
                    fila2.naFila(fila1.tail.value[0], fila1.tail.value[1])
                fila2.proximo(comando[1])
        else:
            if comando[1] == '1':
                fila1.proximo(comando[1])
            elif comando[1] == '2':
                fila2.proximo(comando[1])

    elif comando[0] == 'FIM':
        caixa1 = fila1.total()
        caixa2 = fila2.total()
        print(f"Caixa 1: R$ {caixa1:.2f}, Caixa 2: R$ {caixa2:.2f}")
        end = True


