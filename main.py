def etapa1(id):
    id = str(id)
    if len(id) == 1:
        return int(id)
    elif len(id) == 2:
        id = int(id[0]) + int(id[1])
        return int(id)
    elif len(id) == 3:
        id = list(id)
        id.append('0')
        id = sorted(id)
        a = [id[0], id[3]]
        b = [id[1], id[2]]
        a = ''.join(a)
        b = ''.join(b)
        a = int(a)
        b = int(b)
        c = a+b
        return c
    else:
        id = list(id)
        id = sorted(id)
        a = [id[0], id[3]]
        b = [id[1], id[2]]
        a = ''.join(a)
        b = ''.join(b)
        a = int(a)
        b = int(b)
        return a + b


def etapa2(votos):
    votos = list(votos)
    N = len(votos)
    lista_i = []
    for i in range(1,N+1):
        lista_i.append(i)
    lista_voto_n = []
    for y in lista_i:
        if y not in votos:
            lista_voto_n.append(y)
    return lista_voto_n

def etapa3(senha):
    senha = list(senha)
    x = 1
    y = []
    z = {}
    valido = True
    for i in senha:
        if i not in y:
            y.append(i)
            z[i] = 0
    for i in senha:
        if i in y:
            z[i] += 1
    for i in z:
        while x < len(y):
            if z[i] != z[y[x]]:
                valido = False
                break
            x += 1
    return valido


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
