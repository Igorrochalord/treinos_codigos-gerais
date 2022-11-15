'''
cpf = 168.995.350-09
----------------------------------------------------------------
1*10 =10                #
6*9 = 54                #
8*8 = 64                #
9*7 = 63                #
9*6 = 54                #      
5*5 = 25                #
3*4 = 12                #
5*3 = 15                #
0*2 = 0                 #
TOTAL 297               #
                        #
11 - (297 %11) =11      #
11 >9=0                 #
DIGITO 1 - 0            #
                        #
343
11 - (343 %11) =11 #
DIGITO2=9                        #
                        #
                        #
                        #
                        #
                        #
            #
            #
            #
            #
            #
            #
            #
            #
            #
'''

while True:
    print("bem vindo ao meu cpf mania")
    cp=int(input('cpf: '))
    if cp > 11:
        print(f"cpf valido {cp}")
        break
    else:
        print(f"cpf invalido {cp}")

