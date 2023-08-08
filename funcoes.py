'''
Este arquivo nos traz três funções e um objeto class:
    . O objeto anumber():
        Este objeto tem uma função dentro dele, onde esta função pega todos os argumentos de uma string qualquer e analisa se nessa string tem algum caractere que existe em uma lista que esta na própria função,
        retornando True se na string existir algun dos caracteres da lista e False caso não.


    .A função negative_number(a,b,c):
        Dentro desta função ela analisa os três parametros que são pedidos por "a,b,c", checando um por um para saber se á um valor negativo dentre estes parametros, retornando False caso tenha algun valor negativo
        nos parametros ou True se nenhum dos parametros forem negativos.


    .A função checking():

'''




class anumber():
    def isfloat(*args):
        numb = [')','(','*','¨','%','!','@','$','#','&','=','-',',','.','´´','0','1','2','3','4','5','6','7','8','9','10']
        for number in args:
            if number in numb:
                return True
        else:
            return False


def negative_number(a,b,c):
    if a < 0 :
        return False
    elif b < 0:
        return False
    elif c < 0:
        return False
    else:
        return True
    





def checking():
    try:
        with open("data.json","r+") as file_json:
            if file_json.read().strip() == '':
                return True
            else:
                return '++'
        
    except FileNotFoundError:
        with open("data.json","w") as file_json:
            return False


















# def comparing_values(a,b):
#     if a > b:
#         return True 
#     elif b > a:
#         return False
#     elif a == b:
#         return f'=='
#     else:
#         return f'[ERRO]Desconhecido'




# def ifs(a,b):
#     with open("data.json","r") as file:
#         database = json.load(file)
#         end_alarm = int(database["end_alarm"][0]),int(database["end_alarm"][1]),int(database["end_alarm"][2])
#     if comparing_values(a[2],b[2]) == '==':
#         if comparing_values(a[1],b[1]) == '==':
#             if comparing_values(a[0],b[0]) == False:
#                 return f'Faltam apenas {b[0]- a[0]} dias para o fim do alarme.'
#             elif comparing_values(a[0],b[0]) == True:
#                 return f'Faltam apenas {a[0]- b[0]} dias para o fim do alarme.'
#             else:
#                 return f'Hoje é o ultimo dia espero que tenha evoluido bastante nas suas metas.'
#         elif comparing_values(a[1],b[1]) == False:
#             return f'Seu alarme acabará {end_alarm}.'
#     elif comparing_values(a[2],b[2]) == False:
#         return f'Seu alarme acabará {end_alarm}'    
#     else:
#         return '+'
    
# def more_and_less(a,b):
#     a = a
#     b = b
#     if a>b:
#         c = a-b
#         return c
#     elif b>a:
#         d = b-a
#         return d
#     else:
#         return '[ERRO]Desconhecido'

    
# def during_over_30(a,b):
#     c = a
#     count = 0
#     while c >= b:
#         c -= b
#         count +=1
#     return count
# 1
# def less_of_30(a):
#     d = a
#     while d >30:
#         d -=30
#     return d



# def checking_datetime():
#     try:
#         with open("data.json","r") as file:
#             data = json.load(file)
#         if 'alarm_time' in data:
#             if 'end_alarm' in data:
#                 return True
#         else:
#             return False
#     except:
#         return 'aa'