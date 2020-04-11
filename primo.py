def EsPrimo(valor):
    if(valor <= 1):
        return False;
    for i in range(2, valor, 1):
        if (valor%i == 0):
            return False;
    return True;
n = input()
a = EsPrimo(int(n));
print(a);
