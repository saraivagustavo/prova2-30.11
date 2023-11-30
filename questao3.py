'''Faça um programa, em Python 3.x, que receba strings e, a partir de uma função, escreva uma nova STRING com as vogais (de forma não repetida) na ordem em que aparecem na string.  A condição de parada é quando for informada uma string vazia ("").'''

def f_selecionavogal(string):
    novo = ""
    ultimo_caractere = ""
    for i in range(len(string)):
        if(string[i] == 'A' or string[i] == 'E' or string[i] == 'I' or string[i] == 'O' or string[i] == 'U'):
            if(string[i] != ultimo_caractere):
                novo += string[i]
                ultimo_caractere = string[i]
    return novo
    
    
def main():
    #declaração de variáveis
    string = str("")
    #entrada de dados
    string = input().upper()
    #processamento e saída de dados
    while(string != ""):
        print(f'{f_selecionavogal(string)}')
        string = input().upper()
    return 0
    
if __name__ == "__main__":
    main()