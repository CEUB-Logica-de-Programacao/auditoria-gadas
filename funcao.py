# Etapa 2
listavotos = [4,3,2,7,8,2,3,1]
def verificacao_votos(x):
    b = len(x)
    lista_i = []
    for i in range(1,b+1):
        lista_i.append(i)
    lista_voto_n = []
    for y in lista_i:
        if y not in x:
            lista_voto_n.append(y)
    return lista_voto_n
print(verificacao_votos(listavotos))
#etapa 3
def senha():
    x = input('Senha: ')
    x = list(x)
    y = []
    z = {'*':0,}
    for i in x:
        if i not in y:
            y.append(i)
            z[i] = 0
    for i in x:
        if i in y:
            z[i] += 1
            z['*']+=1
    for i in z:
        if i == z['*']:
            continue
        else:
            return False
            break
print(senha())
