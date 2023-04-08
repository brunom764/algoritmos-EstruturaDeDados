class Graph:

    def __init__(self, users):
        self.graph = [[] for _ in range(users)]  # grafo vazio
        self.visList = [0] * users

    def controller(self, users, conex):
        self.add(conex)
        for i in range(users):
            visited = [0] * users
            self.search(i, visited)
            self.visList[i] = sum(visited)    # N° de nós alcançáveis a partir do i nó

        return self.visList

    def add(self, conex):
        for x, y in conex:   # (1,7)  ->  (0,6)
            self.graph[x - 1].append(y - 1)
            self.graph[y - 1].append(x - 1)

    def search(self, x, visited):    # busca em profundidade
        visited[x] = 1
        for y in self.graph[x]:
            if not visited[y]:
                self.search(y, visited)


graph = []
output = ''
users, numConexs = input().split()
news = Graph(int(users))

for i in range(int(numConexs)):
    conex = [int(x) for x in input().split()]
    graph.append(conex)

result = news.controller(int(users), graph)
for num in result:
    output += str(num) + ' '
print(output.rstrip())
