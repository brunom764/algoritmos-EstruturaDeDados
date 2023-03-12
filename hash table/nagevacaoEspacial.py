class HashTable:
    def __init__(self, num):
        self.size = num
        self.array = [None] * num

    def checkSize(self):
        return self.size

    def hash(self, value):
        return value % self.size

    def hashController(self, value):
        hashValue = self.hash(value)
        bucket = self.array[hashValue]

        # Tratamento colisões

        if bucket is None:
            # Se bucket vazio, return o índice atual
            return hashValue, bucket

        # Procura o value no bucket
        for i, (v, x) in enumerate(bucket):
            if v == value:
                return hashValue, bucket

        # Se não encontrou o value, procura o prox índice vazio na tabela
        for i in range(hashValue + 1, len(self.array) + hashValue):
            index = i % len(self.array)
            bucket = self.array[index]
            if bucket is None:
                self.array[index] = []  # cria uma nova lista vazia
                return index, self.array[index]

        # Se não encontrou nenhum índice vazio, return índice atual
        return hashValue, bucket

    def add(self, value):
        hashValue, bucket = self.hashController(value)

        if bucket is None:
            bucket = []
            self.array[hashValue] = bucket  # cria uma nova lista vazia

        findKey = False
        for index, box in enumerate(bucket):
            boxValue, boxHash = box
            if boxValue == value:  # verificar se o valor já existe
                findKey = True
                break

        if findKey:  # atualiza o elemento na cesta com o novo valor e o hash correspondente
            bucket[index] = (value, hashValue)
        else:  # add o novo valor a cesta
            bucket.append((value, hashValue))
        print(f'E: {hashValue}')

    def search(self, value):
        hashValue, bucket = self.hashController(value)

        if bucket is not None:
            for box in bucket:
                boxValue, boxHash = box
                if boxValue == value:
                    print(f'E: {hashValue}')
                    return

        print('NE')

    def cap(self, hashValue):
        bucket = self.array[hashValue]

        if bucket is not None:
            for box in bucket:
                boxValue, boxHash = box
                if boxHash == hashValue:  # o valor do registro é igual ao hash
                    print(f'A: {boxValue}')
                    return
        print('D')


num = int(input())
comandos = int(input())
nave = HashTable(num)

for i in range(comandos):
    request, number = input().split()

    if request == 'ADD':
        nave.add(int(number))

    elif request == 'SCH':
        nave.search(int(number))

    elif request == 'CAP':
        nave.cap(int(number))

    if nave.checkSize() == 0:  # Check endereço de memória disponível
        print('Toda memoria utilizada')
        break


