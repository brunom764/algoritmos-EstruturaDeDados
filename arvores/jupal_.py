class NodeAVL:
    def __init__(self, num):
        self.value = num
        self.left = None
        self.right = None
        self.height = 1


class Jupal:

    # Infos AVL
    def minimum(self, no):  # return min
        if no is None or no.left is None:
            return no
        else:
            return self.minimum(no.left)

    def maximum(self, no):  # return max
        if no is None or no.right is None:
            return no
        else:
            return self.maximum(no.right)

    def getHeight(self, no):  # return valor da altura
        if no is None:
            return 0
        else:
            return no.height

    def updateHeight(self, no):
        return 1 + max(self.getHeight(no.left), self.getHeight(no.right))

    # Balanceamento
    def isBalance(self, no):  # Return coeficeinte de balanceamento
        if no is None:
            return 0
        else:
            return self.getHeight(no.left) - self.getHeight(no.right)

    def balanceInsert(self, balanceCoe, root, value):
        if balanceCoe > 1 and root.left.value > value:  # esq -> dir
            return self.rotateRight(root)
        if balanceCoe < -1 and value > root.right.value:  # dir -> esq
            return self.rotateLeft(root)
        if balanceCoe > 1 and value > root.left.value:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)
        if balanceCoe < -1 and value < root.right.value:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return None

    def balanceDelete(self, balanceCoe, no):
        if balanceCoe > 1 and self.isBalance(no.left) >= 0:
            return self.rotateRight(no)
        if balanceCoe < -1 and self.isBalance(no.right) <= 0:
            return self.rotateLeft(no)
        if balanceCoe > 1 and self.isBalance(no.left) < 0:
            no.left = self.rotateLeft(no.left)
            return self.rotateRight(no)
        if balanceCoe < -1 and self.isBalance(no.right) > 0:
            no.right = self.rotateRight(no.right)
            return self.rotateLeft(no)

    # Rotações
    def rotateRight(self, no):  # Rotaçao direita e return "raiz"
        newNo = no.left
        oldNo = newNo.right
        newNo.right = no
        no.left = oldNo
        # Atualizar alturas
        no.height = 1 + max(self.getHeight(no.left), self.getHeight(no.right))
        newNo.height = 1 + max(self.getHeight(newNo.left), self.getHeight(newNo.right))
        return newNo

    def rotateLeft(self, no):  # Rotaçao esq e return "raiz"
        newNo = no.right
        oldNo = newNo.left
        newNo.left = no
        no.right = oldNo
        # Atualizar alturas
        no.height = 1 + max(self.getHeight(no.left), self.getHeight(no.right))
        newNo.height = 1 + max(self.getHeight(newNo.left), self.getHeight(newNo.right))
        return newNo

    # Busca
    def find(self, value, root):
        if root is None or root.value == value:  # nó encontrado ou fim da árvore
            return root
        elif value < root.value:  # busca na subárvore esquerda
            return self.find(value, root.left)
        else:  # se o valor for maior que o valor do nó atual, busca na subárvore direita
            return self.find(value, root.right)

    # Inserir
    def insert(self, value, root, loops=1):
        if root is None:  # Cria No
            return NodeAVL(value)
        elif value <= root.value:  # procurando onde por
            root.left = self.insert(value, root.left, loops + 1)
        elif value > root.value:
            root.right = self.insert(value, root.right, loops + 1)

        # altura
        try:
            root.height = self.updateHeight(root)
        except TypeError:  # Correçao de bug
            root.height = loops

        # balanceamento
        balanceCoe = self.isBalance(root)  # int
        balanceRoot = self.balanceInsert(balanceCoe, root, value)
        if balanceRoot:
            return balanceRoot

        return root

    # Remover
    def delete(self, value, no):
        if no is None:
            return no

        elif value < no.value:  # buscar No
            no.left = self.delete(value, no.left)
        elif value > no.value:
            no.right = self.delete(value, no.right)
        else:
            if no.left is None:  # valor a dir, vira o no "raiz"
                switchNo = no.right
                no = None  # deleta
                return switchNo
            elif no.right is None:  # valor a esq, vira o no "raiz"
                switchNo = no.left
                no = None  # deleta
                return switchNo
            minNo = self.minimum(no.right)  # Nó mínimo da subárvore direita
            no.value = minNo.value  # No min assume o valor do no que deve ser deletado
            no.right = self.delete(minNo.value, no.right)  # deleta No´ minimo
        if no is None:
            return no

        # Altura
        no.height = self.updateHeight(no)

        # balanceamento
        balanceCoe = self.isBalance(no)  # int
        balanceRoot = self.balanceDelete(balanceCoe, no)
        if balanceRoot:
            return balanceRoot

        return no

    # Print da AVL & desafio I
    def exib(self, root):
        nos = []  # lista de Nos
        self.collectNos(root, nos)
        for i, no in enumerate(nos):  # printa lista
            if i == len(nos) - 1:  # sem espaço (Ultimo)
                print(no.value, end='')
            else:
                print(no.value, end=' ')  # com espaço(  tds ate o penultimo)

    def collectNos(self, root, nos):
        if root is not None:
            self.collectNos(root.left, nos)
            nos.append(root)  # add a lista
            self.collectNos(root.right, nos)

    # Desafio II
    def exibSemiRoot(self, value, root):
        semiRoot = self.find(value, root)
        if semiRoot is not None:
            if semiRoot.left is not None and semiRoot.right is not None:
                print(f'{semiRoot.value} tocou para {semiRoot.left.value} que cruzou para {semiRoot.right.value}.')
            elif semiRoot.left is not None:
                print(f'{semiRoot.value} tocou para {semiRoot.left.value}.')
            elif semiRoot.right is not None:
                print(f'{semiRoot.value} tocou para {semiRoot.right.value}.')
            else:
                print(f'{semiRoot.value} errou o passe.')
        else:
            print('ARVORE VAZIA')



# Parte principal
jupal = Jupal()
root = None
end = False
jupaL = []

while not end:
    request = input().split()

    if request[0] == 'INSERIR':
        add = True
        if root is not None:
            if root.value == request[1]:
                add = False
            elif jupal.find(request[1],root) == root:
                add = False
        if add:
            jupaL.append(request[1])
            root = jupal.insert(request[1], root)
            print(f'{request[1]} INSERIDO')

    elif request[0] == 'DELETAR':
        rem = False
        if root is not None:
            if root.value == request[1]:
                rem = True
            elif jupal.find(request[1], root) != root and jupal.find(request[1], root) is not None:
                rem = True
        if rem:
            jupaL.remove(request[1])
            root = jupal.delete(request[1], root)
            print(f'{request[1]} DELETADO')
        else:
            print(f'{request[1]} NAO ENCONTRADO')

    elif request[0] == 'MINIMO':
        min = jupal.minimum(root)
        if min is None:
            print('ARVORE VAZIA')
        else:
            print(f'MENOR: {min.value}')

    elif request[0] == 'MAXIMO':
        if len(jupaL) == 0:
            print('ARVORE VAZIA')
        else:
            maxi = max(jupaL)
            print(f'MAIOR: {maxi}')

    elif request[0] == 'ALTURA':
        alt = jupal.getHeight(root)
        print(f'ALTURA: {alt}')

    elif request[0] == 'VER' and request[1] in jupaL:  # desafio II
        jupal.exibSemiRoot(request[1], root)

    elif request[0] == 'VER' and len(request) == 1:  # desafio I
        if root is not None:
            jupal.exib(root)
            print('')
        else:
            print('ARVORE VAZIA')

    elif request[0] == 'FIM':
        if root is not None:
            jupal.exib(root)
        else:
            print('ARVORE VAZIA')
        end = True