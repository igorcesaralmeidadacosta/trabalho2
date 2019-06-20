#Questão 2
def main():
    cont = 0
    while(cont==0):
        op=input('Deseja criptografar(1) ou descriptografar(2)? Digite o numero da opção: ')
        if(op=='1'):
            print('Para criptografar, insira cada digito do inteiro de 4 digitos separadamente:')

            vet = [1,2,3,4]
            vet[0] = int(input('Insira o 1º dígito: '))
            vet[1] = int(input('Insira o 2º dígito: '))
            vet[2] = int(input('Insira o 3º dígito: '))
            vet[3] = int(input('Insira o 4º dígito: '))

            vet[0] = vet[0] + 6
            vet[1] = vet[1] + 6
            vet[2] = vet[2] + 6
            vet[3] = vet[3] + 6

            vet[0] = vet[0] % 10
            vet[1] = vet[1] % 10
            vet[2] = vet[2] % 10
            vet[3] = vet[3] % 10

            troca = vet[0]
            vet[0] = vet[2]
            vet[2] = troca

            troca = vet[1]
            vet[1] = vet[3]
            vet[3] = troca

            print('\nO número criptografado é: ',vet,'\n')
            
        if(op=='2'):
            print('Para descriptografar, insira cada digito do inteiro de 4 digitos criptografado separadamente:')

            vet = [1,2,3,4]
            vet[0] = int(input('Insira o 1º dígito: '))
            vet[1] = int(input('Insira o 2º dígito: '))
            vet[2] = int(input('Insira o 3º dígito: '))
            vet[3] = int(input('Insira o 4º dígito: '))

            troca = vet[2]
            vet[2] = vet[0]
            vet[0] = troca

            troca = vet[3]
            vet[3] = vet[1]
            vet[1] = troca

            if(vet[0]>=6):
                vet[0] = vet[0]-6
            else:
                vet[0] = (10+vet[0])-6

            if(vet[1]>=6):
                vet[1] = vet[1]-6
            else:
                vet[1] = (10+vet[1])-6

            if(vet[2]>=6):
                vet[2] = vet[2]-6
            else:
                vet[2] = (10+vet[2])-6

            if(vet[3]>=6):
                vet[3] = vet[3]-6
            else:
                vet[3] = (10+vet[3])-6

            print('\nO número descriptografado é: ',vet,'\n')

        if(op != '1' and op!= '2'):
            print('Você digitou uma opção inexistente!')
        k = 0
        while(k == 0):
            contx = input('Deseja executar novamente? Digite "s" para sim e "n" para não: ')
            if(contx == 's'):
                cont == 0
                k = 10
            if(contx == 'n'):
                cont = 10
                k = 10

main()
