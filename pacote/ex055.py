print('Digite o peso de 5 pessoas: ')
maior = menor = 0

for i in range(0, 5):
    p = input('>')
    if i == 1:
        maior = menor = p
    if p > maior:
        maior = p
    if p < menor:
        menor =  p

print(f'''Pessoa mais pesada: {maior}
Pessoa mais leve: {menor}''')