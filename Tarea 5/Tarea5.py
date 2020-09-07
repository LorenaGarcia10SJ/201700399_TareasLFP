a='___servidor1'
b= '3servidor'


def AFD(entrada):
    estado= 0
    for i in range(len(entrada)):
        if estado==0:
            if entrada[i]=='_':
                estado = 1
        elif estado==1:
            if entrada[i]=='_':
                estado= 3
            elif estado=='S':
                estado=4
            else:
                print("Cadena incorrecta")   
                return   
        elif estado==2:
            if entrada[i]=="S":
                estado=4
            elif entrada[i]=='1':
                estado=4 
            else:
                print("Cadena incorrecta")
                return     
        elif estado==3:
            if entrada[i]=='1':
                estado=4
            else:
                estado=3
                print("Cadena incorrecta")
                return    
        elif estado==4: 
            if entrada[i]=='':
                estado=4
                print('Cadena Correcta')
                return
        
    print("Cadena incorrecta")
    
AFD(a)
AFD(b)   




             
        


