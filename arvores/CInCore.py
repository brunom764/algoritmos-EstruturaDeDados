class No:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class BinaryT:
    def __init__(self):
        self.root = None   # raiz

    def add(self, value, output=False):
        level = 0
        if not self.root:
            self.root = No(value)
        else:
            noNow = self.root
            dadNo = None  # pai
            while noNow:
                if value < noNow.value:  # esquerda
                    dadNo = noNow
                    noNow = noNow.left
                elif value > noNow.value:  # direita
                    dadNo = noNow
                    noNow = noNow.right
                else:
                    return
                level += 1
            if value < dadNo.value:  # esq
                dadNo.left = No(value)
                dadNo.left.parent = dadNo  # atribui o pai
            else:  # direita
                dadNo.right = No(value)
                dadNo.right.parent = dadNo  # atribui o pai
        if output:
            print(level)

    def search(self,value):
        noNow, dadNo = self.find(value, True)
        if noNow is not None:
            self.rotation(noNow, dadNo)

    def find(self, value, output=False):
        if self.root is None:
            return None, None
        noNow = self.root  # começar o loop pela raiz
        dadNo = self.root
        level = 0
        while noNow and noNow.value != value:  # busca
            dadNo = noNow
            if value < noNow.value:
                noNow = noNow.left
            elif value > noNow.value:
                noNow = noNow.right
            try:
                noNow.parent = dadNo  # atualiza o pai
            except:
                pass
            level += 1
        if noNow is None:
            if output:
                print(-1)
            return None, None
        if output:
            print(level)  # output do PL(antes da mudanca)
        return noNow, dadNo

    def rotation(self, noNow, dadNo):
        while dadNo is not None and self.root.value != noNow.value:
            dadNo = noNow.parent
            grandNo = dadNo.parent
            newRoot = None
            if grandNo is None:  # filho no 2° andar
                if noNow == dadNo.left:  # r
                    newRoot = self.rightRotate(dadNo)
                if noNow == dadNo.right:  # l
                    newRoot = self.leftRotate(dadNo)
            else:
                if dadNo == grandNo.left:  # pai ta na esq
                    if noNow == dadNo.left:  # r,r
                        newRoot = self.rightRotate(dadNo)
                        grandNo = self.rightRotate(grandNo)
                    else:  # l,r
                        newRoot = self.leftRotate(dadNo)
                        grandNo = self.rightRotate(grandNo)

                else:  # pai ta na dir
                    if noNow == dadNo.right:  #l,l
                        grandNo = self.leftRotate(grandNo)
                        newRoot = self.leftRotate(dadNo)
                    else:  #r,l
                        newRoot = self.rightRotate(dadNo)
                        grandNo = self.leftRotate(grandNo)

            noNow , dadNo = self.find(newRoot.value)

        # rotate left at node x
    def leftRotate(self, no):
        newRoot = no.right
        no.right = newRoot.left
        if newRoot.left != None:
            newRoot.left.parent = no

        newRoot.parent = no.parent
        if no.parent == None:
            self.root = newRoot
            self.root.parent = None
            newRoot.parent = None
        elif no == no.parent.left:
            no.parent.left = newRoot
        else:
            no.parent.right = newRoot
        newRoot.left = no
        no.parent = newRoot

        return newRoot

        # rotate right at node x
    def rightRotate(self, no):
        newRoot = no.left
        no.left = newRoot.right
        if newRoot.right != None:
            newRoot.right.parent = no

        newRoot.parent = no.parent
        if no.parent == None:
            self.root = newRoot
            self.root.parent = None
            newRoot.parent = None
        elif no == no.parent.right:
            no.parent.right = newRoot
        else:
            no.parent.left = newRoot

        newRoot.right = no
        no.parent = newRoot

        return newRoot

binaryT = BinaryT()
end = False

while not end:
    try:
        request = input().split()
        if request[0] == 'ADD':
            binaryT.add(int(request[1]), True)
        elif request[0] == 'SCH':
            binaryT.search(int(request[1]))
    except EOFError:
        end = True


