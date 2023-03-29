class Wolfman:

    def __init__(self, lista, const):
        self.array = lista
        self.const = const

    def controller(self):
        count = 0
        while self.array:  #loop ate lista vazia
            maxValue, minValue = self.heapMinMax()  #ordena e recebe os values
            k = self.calculaK(maxValue, minValue)   # descobrir K
            self.array.remove(maxValue)  #remover maior
            if k > 0:
                self.array = self.array + [k]  #add K
            count += 1
        print(f'{count} rodadas, partindo para a próxima!')

    def heapMinMax(self):
        n = len(self.array)
        maxV = float('-inf')   #-infinite (tds os valores possiveis serão maiores)
        minV = float('inf')   #+inifinito (tds os valores possiveis serão menores)

        # Extrai os elementos da heap um de cada vez
        for i in range(n - 1, -1, -1):
            # Move a raiz atual para o final
            self.array[0], self.array[i] = self.array[i], self.array[0]

            # Atualiza o valor máximo e mínimo
            if self.array[i] > maxV:
                maxV = self.array[i]
            if self.array[i] < minV:
                minV = self.array[i]

        return maxV, minV


    def calculaK(self, maxV, minV):
        if not self.array:  #evitar indexError
            return 0
        k = maxV - abs(minV * self.const)
        return k



listNums = [int(x) for x in input().split()]
constan = int(input())

wolfman = Wolfman(listNums, constan)
wolfman.controller()






