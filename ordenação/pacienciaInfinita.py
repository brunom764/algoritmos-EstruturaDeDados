def bubbleSort(lst, actions=float('inf')):  # OK
    comp, trocas = 0, 0
    n = len(lst)
    for i in range(n):
        for j in range(n - i - 1):
            comp += 1
            if comp + trocas >= actions:
                return comp, trocas, lst
            if lst[j] > lst[j + 1]:  # compara
                lst[j], lst[j + 1] = lst[j + 1], lst[j]  # troca
                trocas += 1
    return comp, trocas, lst


def selectionSort(lst, actions=float('inf')):  # OK
    comp = 0
    trocas = 0

    for i in range(len(lst)):
        min_index = i

        for j in range(i + 1, len(lst)):
            comp += 1
            if comp + trocas >= actions:
                return comp, trocas, lst
            if lst[j] < lst[min_index]:
                min_index = j

        if i != min_index:
            trocas += 1
            lst[i], lst[min_index] = lst[min_index], lst[i]

    return comp, trocas, lst


def insertionSort(lst, actions=float('inf')):
    comp = 0
    trocas = 0
    for i in range(1, len(lst)):
        chave = lst[i]
        j = i - 1
        while j >= 0 and chave < lst[j]:
            comp += 1
            if comp + trocas >= actions:
                return comp, trocas, lst

            lst[j + 1] = lst[j]
            j -= 1
            trocas += 1

            if comp + trocas >= actions:
                return comp, trocas, lst

        if j >= 0:
            comp += 1

        lst[j + 1] = chave

    return comp, trocas, lst


def shellSort(lst, actions=float('inf')):
    n = len(lst)
    comp = 0
    trocas = 0
    intervalo = n // 2
    while intervalo > 0:
        for i in range(intervalo, n):
            temp = lst[i]
            j = i
            while j >= intervalo and lst[j - intervalo] > temp:
                comp += 1
                if comp + trocas >= actions:
                    return comp, trocas, lst

                lst[j] = lst[j - intervalo]
                j -= intervalo
                trocas += 1
                if comp + trocas >= actions:
                    return comp, trocas, lst

            if j >= intervalo:
                comp += 1

            lst[j] = temp

        intervalo //= 2
    return comp, trocas, lst


def quicksort(A, lo, hi):
    global compQS, trocasQS
    if lo >= 0 and hi >= 0 and lo < hi:
        p = partition(A, lo, hi)
        quicksort(A, lo, p)
        quicksort(A, p + 1, hi)


def partition(A, lo, hi):
    global compQS, trocasQS
    pivot = A[(hi + lo) // 2]
    i = lo
    j = hi
    while True:
        if i >= j:
            trocasQS += 1
            return j
        while A[i] < pivot:
            i += 1
            compQS += 1
        while A[j] > pivot:
            j -= 1
            compQS += 1
        if i < j:
            A[i], A[j] = A[j], A[i]
            trocasQS += 1


def outputBook1(lista):
    list2 = lista.copy()
    list3 = lista.copy()
    list4 = lista.copy()
    list5 = lista.copy()

    comp, t, _ = bubbleSort(lista)
    cr7 = comp + t
    outresult('Caça-Rato', comp, t)

    comp, t, _ = selectionSort(list2)
    grafa = comp + t
    outresult('Grafite', comp, t)

    comp, t, _ = insertionSort(list3)
    lac = comp + t
    outresult('Lacraia', comp, t)

    comp, t, _ = shellSort(list4)
    riva = comp + t
    outresult('Rivaldo', comp, t)

    quicksort(list5, 0, len(list5) - 1)
    toni = compQS + trocasQS
    outresult('Toninho', compQS, trocasQS)

    names = ['Caça-Rato', 'Grafite', 'Lacraia', 'Rivaldo', 'Toninho']
    resul = [cr7, grafa, lac, riva, toni]
    mini = min(resul)
    index = resul.index(mini)
    print('-VENCEDOR DA RODADA-')
    print(f'O vencedor da rodada é {names[index]}, com {mini} ações.')

    return index, mini


def outresult(name, comp, t):
    print(f'{name} ordena a lista com {comp} comparações e {t} trocas.')


def outputBook2(lst, actions, index):
    print('-Toninho está a dormir...-')
    print('Os outros estagiários retornam as seguintes listas com essa quantidade de ações:')
    list22 = lst.copy()
    list32 = lst.copy()
    list42 = lst.copy()
    list52 = lst.copy()

    if index != 0:
        x, y, newLst = bubbleSort(list22, actions)
        print(f'Com {actions} ações, Caça-Rato ordena a lista assim: {newLst}')

    if index != 1:
        x, y, newLst = selectionSort(list32, actions)
        print(f'Com {actions} ações, Grafite ordena a lista assim: {newLst}')

    if index != 2:
        x, y, newLst = insertionSort(list42, actions)
        print(f'Com {actions} ações, Lacraia ordena a lista assim: {newLst}')

    if index != 3:
        x, y, newLst = shellSort(list52, actions)
        print(f'Com {actions} ações, Rivaldo ordena a lista assim: {newLst}')


compQS = 0
trocasQS = 0
listNums = [int(x) for x in input().split()]
secondList = listNums.copy()
index, action = outputBook1(listNums)
outputBook2(secondList, action, index)