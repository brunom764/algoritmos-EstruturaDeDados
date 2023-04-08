class Graph():
    def __init__(self, followers, boost, idUser):
        self.idUser = int(idUser)
        self.views = followers[int(idUser)]
        self.boost = int(boost) + len(self.views)
        self.users = followers

    def controller(self):    # faz a bfs e retorna os users
        v1, v2 = self.bfs()
        self.views = v1 + v2
        return self.views

    def bfs(self):  #realiza a bfs
        visited = [False] * len(self.users)
        queue = [self.idUser]
        visited[self.idUser] = True
        trash = []   # itens apagados da queue, mas que foram atingidos

        while queue:
            current = queue.pop(0)
            trash.append(current)

            for neighbor in self.users[current]:
                if not visited[int(neighbor)]:
                    visited[int(neighbor)] = True
                    queue.append(int(neighbor))
                    self.boost -= 1
                if self.boost == 0:
                    return trash[1:], queue

        return trash[1:], queue


numUsers = int(input())
idUser = input()
boost = float(input()) // 5.25
graph = []

for i in range(numUsers):
    _, ids = input().split(':')
    followers = ids.split()
    graph.append(followers)

views = Graph(graph, boost, idUser)
output = views.controller()
for i in range(len(output)):
    output[i] = str(output[i])
print(output)
