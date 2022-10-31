def etapa1(id):
    return 1000


def etapa2(votos):
    b = len(x)
    lista_i = []
    for i in range(1,b+1):
        lista_i.append(i)
    lista_voto_n = []
    for y in lista_i:
        if y not in x:
            lista_voto_n.append(y)
    return lista_voto_n


def etapa3(senha):
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


if __name__ == "__main__":
    if etapa1('1234') > 100:
        print('ID inválido')
        exit(1)
    if len(etapa2([1, 1])) > 0:
        print('Voto inválido')
        exit(1)
    if not etapa3('abba'):
        print('Senha inválida')
        exit(1)
