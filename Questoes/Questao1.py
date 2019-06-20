def paramb(bte):
        mb = float(bte)/(1024*1024)
        return mb

def porcento(parcial,total):
    return ((parcial/total)*100)

def main():

    arquivo = open('usuarios.txt','r')
    base1 = arquivo.readlines()
    arquivo.close()

    arquivo = open ('relatorio.txt','w')
    arquivo.write('ACME Inc.               Uso do espaço em disco pelos usuarios\n')
    arquivo.write('-------------------------------------------------------------------------\n')
    arquivo.write('Nr.  Usuário        Espaço utilizado     % do uso\n')
    arquivo.close()

    name = ['a','b','c','d','e','f']
    number = [1,2,3,4,5,6]
    
    l1 = base1[0]
    (name[0],number[0]) = l1.split(' ',1)
    number[0] = float(number[0])

    l2 = base1[1]
    (name[1],number[1]) = l2.split(' ',1)
    number[1] = float(number[1])

    l3 = base1[2]
    (name[2],number[2]) = l3.split(' ',1)
    number[2] = float(number[2])

    l4 = base1[3]
    (name[3],number[3]) = l4.split(' ',1)
    number[3] = float(number[3])

    l5 = base1[4]
    (name[4],number[4]) = l5.split(' ',1)
    number[4] = float(number[4])

    l6 = base1[5]
    (name[5],number[5]) = l6.split(' ',1)
    number[5] = float(number[5])
  
    number[0] = round(paramb(number[0]),2)
    number[1] = round(paramb(number[1]),2)
    number[2] = round(paramb(number[2]),2)
    number[3] = round(paramb(number[3]),2)
    number[4] = round(paramb(number[4]),2)
    number[5] = round(paramb(number[5]),2)

    soma = number[0] + number[1] + number[2]+ number[3] + number[4] + number[5]
    media = round((soma/6),2)

    porcentagem = [(1,1),(1,1),(1,1),(1,1),(1,1),(1,1)]    
    porcentagem[0] = round(porcento(number[0],soma),2)
    porcentagem[1] = round(porcento(number[1],soma),2)
    porcentagem[2] = round(porcento(number[2],soma),2)
    porcentagem[3] = round(porcento(number[3],soma),2)
    porcentagem[4] = round(porcento(number[4],soma),2)
    porcentagem[5] = round(porcento(number[5],soma),2)

    x=0
    while(x<6):
        y=0
        arquivo = open('relatorio.txt','a')
        arquivo.write('\n')
        arquivo.write(str(x+1))
        arquivo.write('    ')
        arquivo.write(name[x])
        t = len(name[x])
        t = 15 - t
        while(y<t):
                arquivo.write(' ')
                y = y + 1
        y = 0
        arquivo.write(str(number[x]))
        arquivo.write(' MB')
        t = len(str(number[x]))
        t = 23 - t
        while(y<t):
                arquivo.write(' ')
                y = y + 1
        y = 0
        arquivo.write(str(porcentagem[x]))
        arquivo.write('%')
        x = x + 1

    arquivo.write('\n\nEspaço total ocupado: ')
    arquivo.write(str(soma))
    arquivo.write(' MB')
    arquivo.write('\nEspaço médio ocupado: ')
    arquivo.write(str(media))
    arquivo.write(' MB')
    arquivo.close()

        

    
main()
