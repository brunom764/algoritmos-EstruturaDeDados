def merge(leftHalf, rightHalf):
    # Combina duas listas ordenadas em uma lista ordenada
    result = []
    i = j = 0
    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] <= rightHalf[j]:
            result.append(leftHalf[i])
            i += 1
        else:
            result.append(rightHalf[j])
            j += 1
    # Adiciona os elementos restantes da lista que não foi completamente percorrida
    result += leftHalf[i:]
    result += rightHalf[j:]
    return result


def medCalc(salary1, salary2):
    # agrupar as 2 listas em uma única lsita ordenada
    salary = merge(salary1, salary2)

    # Calcular a mediana
    length = len(salary)
    if length % 2 == 0:
        med = (salary[length // 2 - 1] + salary[length // 2]) / 2
    else:
        med = salary[length // 2]

    # output
    return f'O salário sugerido por Juba na primeira negociação será de {med:.2f} mil reais.'


salarySport = [int(x) for x in input().split()]
salaryFuture = [int(x) for x in input().split()]


resul = medCalc(salarySport, salaryFuture)
print(resul)