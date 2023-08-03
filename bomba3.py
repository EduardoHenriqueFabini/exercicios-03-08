end=" " # gera a sequencia com um espaço entre qualquer coisa

len = int(input("Digite o numero que deseja da sequencia de Fibonacci"))

vari1 = 0
vari2 = 1

print(vari1, vari2, end=" ")

len -= 2

while  vari2 <= len:
    print(vari1 + vari2, end=" ")

    temp = vari2
    vari2 = vari1+vari2
    vari1 = temp 

    len -=1