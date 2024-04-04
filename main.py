def menu():
    print("1-Numero Secreto \n")
    escolha = input("Escolha um trabalho!")
    match escolha:
        case 1:
            jogoDoNumeroSecreto()

def jogoDoNumeroSecreto():
    import random

    numeroSecreto = random.randint(1,100)
    tentativa = 0
    while True:
        numero = int(input("Digite um número: "))
        if numero == numeroSecreto:
            print("Parabéns você descobriu o número secreto!")
            print(f'Com um total de {tentativa} tentativas!')
            break
        elif numero < numeroSecreto:
            print("O numero é maior!")
        else:
            print("O número é menor!")
        tentativa = tentativa + 1

# menu()
jogoDoNumeroSecreto()