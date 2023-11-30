'''Faça um programa solicite um tipo de entrada para o usuário:
1) TEXTO
2) NÚMERO
3) SAIR
Caso o usuário escolha o tipo 1- Texto, verifique se o mesmo é um PALÍNDROMO.
Caso o usuário escolha o tipo 2 - Número, verifique se o mesmo é uma CAPICUA.
Caso o usuário escolha o tipo 3 - Sair, saia da repetição informando quantos tipo texto e quantos tipo número foram escolhidos pelo usuário
INSTRUÇÕES:
1) Para o tipo TEXTO é permitido utilizar os recursos de STRINGS, aprendidos em aula para resolução
2) Para o tipo NÚMERO é obrigatório utilizar os recursos matemáticos para verificar se o número é CAPICUA. A utilização de recursos de STRING anulará a resolução'''

def f_palindromo(palavra):
    #declaração de variáveis
    inverso = ""
    #processamento e saída de dados
    for i in palavra:
        if(i != " "):
            inverso += i
    palavra_sem_espacos = inverso
    #inverte a palavra sem espacos
    inverso = palavra_sem_espacos[::-1]
    if(palavra_sem_espacos == inverso):
        print(f'{palavra} É PALÍNDROMO')
    else:
        print(f'{palavra} NÃO É PALÍNDROMO')

def f_tamanho(x):
    #declaração de variáveis
    tamanho = int(0)
    tamanho = 0 #inicialização da variável acumuladora
    #processamento e saída de dados
    while(x > 0):
        x = x // 10
        tamanho += 1
    return tamanho
    
def f_inverter(y):
    #declaração de variáveis
    n_invertido = int(0)
    potencia = int(0)
    resto = int(0)
    n_invertido = 0 #inicialização da variável acumuladora
    #descobrir o tamanho do número (processamento e saída de dados)
    potencia = f_tamanho(y) - 1
    while(y > 0):
        resto = y % 10
        n_invertido += resto * 10 ** potencia
        y = y // 10
        potencia -= 1
    return n_invertido
    
def f_capicua(x):
    if(x == f_inverter(x) and x >= 10):
        return True
    return False

def main():
    cont_palavra = 0
    cont_numero = 0
    flag = True
    while(flag):
        opcao = int(input())
        if(opcao == 1):
            palavra = input().upper()
            f_palindromo(palavra)
            cont_palavra += 1
        if(opcao == 2):
            numero = int(input())
            if(f_capicua(numero)):
                print(f'{numero} É CAPICUA')
            else:
                print(f'{numero} NÃO É CAPICUA')
            cont_numero += 1
        if(opcao != 1 and opcao != 2 and opcao != 3):
            print('VALOR INVÁLIDO. DIGITE 1, 2 OU 3')
        if(opcao == 3):
            flag = False
            print(f'TIPO TEXTO = {cont_palavra}')
            print(f'TIPO NUMÉRICO = {cont_numero}')
        
    return 0
    
if __name__ == "__main__":
    main()