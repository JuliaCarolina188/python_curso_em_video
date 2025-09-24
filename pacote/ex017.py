from math import sqrt, pow

cateto1 = int(input('Digite a largura de um dos catetos: '))
cateto2 = int(input('Digite a do outro cateto: '))

hipotenusa = sqrt(cateto1**2 + cateto2**2)

print(f'A hipotenusa é igual a {hipotenusa}')