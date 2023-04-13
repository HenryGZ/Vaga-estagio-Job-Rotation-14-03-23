n = int(input('informe o numero que deseja verificar se está ou nao na sequencia:'))

ultimo = 1
penultimo = 1

while True:
    if n  == ultimo:
        print(f'o numero {n} está na sequencia')
        break 
    elif(n < ultimo):
        print(f'o numero {n} não está na sequencia')
        break
    else:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
