n = int(input('Informe o numero: '))
antecessor = n - 1
sucessor = n + 1

print(f'Seu antecessor eh {antecessor} e seu sucessor eh {sucessor}')

dobro = 2 * n
triplo = 3 * n
quad = n ** 2

print(f'Seu numero eh {n}, seu dobro eh {dobro}, seu triplo eh {triplo} e seu quadrado eh {quad}')

notaT = float(input('Nota do teste: '))
notaP = float(input('Nota da prova: '))
media = (notaT + notaP) / 2

print(f'A media de seu teste e sua prova sera de: {media}')
