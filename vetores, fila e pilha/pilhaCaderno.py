# Resumo do problema: Confira se todas as frentes (F) tem seus devidos versos (V) em uma ordem satisfatória.
# Toda frente precisa ter um verso depois dela, não necessariamente imediatamente após, mas eventualmente.
# Nenhum verso pode aparecer sem que uma frente tenha o antecedido em algum momento.
# E, atenção, uma pilha que tem a mesma quantidade de frentes e versos NÃO está necessariamente correta.
#
# OBS: Strings vazias devem ser consideradas corretas.
#
# Input
#
# A única linha de entrada é composta por uma string, que corresponde a pilha de capas manuseada pelo funcionário.
# A string é uma sequência de letras sem espaços ou vírgulas então elas, como VFVFFFVVFVFV.
#
# Output
#
# Você deve produzir uma única linha de saída com a expressão “Correto.”
# caso a pilha seja bem formada, e “Incorreto, devido a capa na posição X.” caso contrário,
# onde X é a posição da primeira capa que interfere na integridade do caderno.



def pilhaCheck(pilha):
    f = 0
    for i, capa in enumerate(pilha):
        if capa == 'V':
            if f == 0:
                return f"Incorreto, devido a capa na posição {i + 1}."
            else:
                f -= 1
        elif capa == 'F':
            f += 1
    if f == 0:
      return "Correto."
    else:
      for i in range(len(pilha) - 1, -1, -1):
        if pilha[i] == 'F':
          f -= 1
          if f == 0:
            return f"Incorreto, devido a capa na posição {i + 1}."


cadernos = input()

tdOk = pilhaCheck(cadernos)
print(tdOk)


