class HashTableCPF:
    def __init__(self):
        self.array = [None] * 11

    def controller(self, cpf, magicNumber):
        cpfList = self.cpfListGenerate(cpf)  # formar uma lista de cpf multiplicados por 10
        cpfList = self.checkRepetida(cpfList)  # Modificar termos repetidos

        self.hashTable(cpfList, magicNumber)  # Formar a hashTable
        up = self.checkUp(magicNumber)   # Conferir se há dois termos que somados sejam iguais ao magic Number
        return up

    def cpfListGenerate(self, cpf):
        cpfList = []
        for i in range(11):
            cpfList.append(int(cpf[i]) * 10)

        return cpfList

    def checkRepetida(self, lista):  # Somar termos repertidos
        newLista = []
        newNewLista = []
        i = 0

        while i < len(lista):
            count = lista.count(lista[i])
            if count > 1:
                newLista.append(lista[i] * count)
            else:
                newLista.append(lista[i])
            i += 1

        for i in range(len(newLista)):
            if newLista[i] not in newNewLista:
                newNewLista.append(newLista[i])

        return newNewLista

    def hashTable(self, cpf, value):
        for i in range(len(cpf)):  # formar a hash Table
            index = int(cpf[i]) % len(self.array)
            if self.array[index] is None:
                self.array[index] = [cpf[i]]
            else:
                self.array[index].append(cpf[i])

    def checkUp(self, value):  # Busca por um "complemento" p/ cada elemento da lista na hash table
        for i in range(len(self.array)):
            if self.array[i] is not None:
                for elem in self.array[i]:
                    complement = int(value) - elem
                    index = complement % len(self.array)
                    if (self.array[index] is not None) and (complement in self.array[index]) and (complement != elem):
                        return 'UP Permission'

        return 'NOT Permission'


num = int(input())

for i in range(num):
    cpfClass = HashTableCPF()
    cpf, magicNumber = input().split()
    check = cpfClass.controller(cpf, magicNumber)
    print(check)
