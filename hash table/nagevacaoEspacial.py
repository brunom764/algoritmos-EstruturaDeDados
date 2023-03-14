#Imagine que você é um cientista espacial encarregado de organizar o armazenamento de dados em uma nave espacial gigantesca. Sua missão é garantir que as informações sejam acessadas rapidamente em caso de emergência. Para isso, você decide aplicar seus conhecimentos em algoritmos e estruturas de dados para organizar o centro de dados da nave.

#A quantidade de espaço disponível na nave irá variar de acordo com o tipo de nave, mas uma coisa é certa - cada espaço pode armazenar apenas um conjunto de dados. Você receberá códigos que representam os dados e terá que distribuí-los de acordo com a seguinte lógica:

#X mod N

#Onde X é o código do dado e N é o número de espaços disponíveis no centro de dados da nave. Se um espaço já estiver ocupado, você precisará desenvolver um programa que possa encontrar um novo espaço para armazenar os dados.

#Sua missão é garantir que os dados na nave espacial estejam armazenados e gerenciados de forma eficiente, para que a nave possa atender suas necessidades de missão com rapidez e precisão.

#COMANDOS:

#ADD X -> Adiciona o código do dado X ao seu espaço de memoria correspondente.
#SCH D -> Eventualmente você poderá consultar se um dado foi adicionado a memória, para isso você receberá o dado D para consulta.
#CAP M -> Você poderá fazer consultas sobre o armazenamento daquele endereço de memória, para isso você receberá M representando o número de memória que precisará informar sua disponibilidade armazenamento.
#Input

#Inicialmente teremos um valor N, o N informará a quantidade de espaços de memoria que o data center tem.

#N

#Logo em seguida, será dado um C informando quantos comandos serão executados.

#C

#Após isso, seguem C linhas com as operações "ADD X", "CAP M" ou "SEARCH D".

#Comando 1

#Comando 2

#...

#Comando C

#Output

#Quando o dado é adicionado, você deverá imprimir o número da posição da memória no data center: " E: E".

#Quando quiser saber consultar se um dado já se encontra armazenado (comando SCH) você devera imprimir "NE" (Quando não for encontrado) ou "E: E" (O endereço que foi encontrado).

#Quando quiser saber consultar um espaço de memoria (comando CAP) você deverá imprimir, "D"(Se estiver disponível para armazenar) ou "A: D" (O dado no endereço).

#Quando o Data center não tiver mais nenhum endereço de memória disponível, você deverá imprimir "Toda memoria utilizada" e será finalizado o programa.




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


