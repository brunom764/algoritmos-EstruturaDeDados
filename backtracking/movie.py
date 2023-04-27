class Cinema:
    def __init__(self, n):
        self.n = n
        self.subgrupos = []
        self.possibilidades = []

    def possibSala(self):
        def backtrack(tamanhoAtual, subgrupoAtual):
            if sum(subgrupoAtual) == self.n:
                self.possibilidades.append(subgrupoAtual[:])
                return    # fim da recursão

            for i in range(tamanhoAtual, self.n - sum(subgrupoAtual) + 1):
                subgrupoAtual.append(i)
                backtrack(i, subgrupoAtual)
                subgrupoAtual.pop()

        backtrack(1, self.subgrupos)

    def output(self):
        self.possibSala()
        print(f"Uma sessão com {self.n} pessoas pode ter sua audiência nos seguintes subgrupos:")
        for p in self.possibilidades:
            print(p)

# Parte principal
n = int(input())
cinema = Cinema(n)
cinema.output()

