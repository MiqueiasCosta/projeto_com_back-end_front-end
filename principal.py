from funcoes import anumber,negative_number
import json
from tkinter import *
from datetime import datetime






with open("data.json","r+") as file:
    database = json.load(file)



datetime__ = datetime.now()


new_hour = ''
new_date = '' 

actual_day = int(datetime__.day),int(datetime__.month),int(datetime__.year)
def append():  
    choice = etry_all.get()
    writes = ''
    if choice.isdigit():
        writes =  'Por favor digite apenas letras.'
        return writes
    elif choice == '':
        writes =  'Por favor digite apenas letras.'
        return writes
    elif anumber.isfloat(choice) == True:
        writes = 'Por favor digite apenas letras.'
        return writes
    else:
        database["list_of_goals"].append(choice)
        with open("data.json", "w")as file:
            json.dump(database,file)
        return True

def remove():
    choice = etry_all.get()
    write = ''
    if not choice.isdigit():
        write = 'Para remover digite apenas o numero da meta que deseja remover.'
        return write
    elif int(choice) > len(database["list_of_goals"]):
        write = 'Numero maior do que os que tem na lista.'
    else:
        database["list_of_goals"].pop(int(choice))
        with open("data.json", "w")as file:
            json.dump(database,file)
        return True

def change_alarm():
    choice = etry_all.get()
    write = ''
    if not choice.isdigit():
        write = 'Digite apenas numeros para alterar o alarme.EXEMPLO: 10 HRS'
        return write
    elif int(choice) > 23:
        write = 'O maximo para se alterar o alarme é até 23 horas.'
        return write
    elif int(choice) <= 0:
        write = 'Por favor coloque um numero maior.'
        return write
    else:
        global new_hour
        new_hour = choice
        database["alarm_time"] = int(new_hour)
        with open("data.json", "w")as file:
            json.dump(database,file)
        return True

def change_date_of_end():
    choice = etry_all.get()
    write = ''
    if len(choice) ==  0:
        write = 'Digite algo para colocarmos no banco de dados.'
        return write
    elif not ',' in choice:
        write = 'Dige a data neste formato. 10,7,2023'
        return write
    convertion = choice.split(',')
    day = convertion[0]
    month = convertion[1]
    year = convertion[2]
    if not day.isdigit():
        write = 'Digite apenas numeros por favor!'
        return write
    elif not month.isdigit():
        write = 'Digite apenas numeros por favor!'
        return write
    elif not year.isdigit():
        write = 'Digite apenas numeros por favor!'
        return write
    elif negative_number(int(day),int(month),int(year)) == False:
        write = 'Nenhum numero pode ser negativo!'
        return write
    else:
        if int(day) >30:
            write = 'O maximo que você pode colocar é 30 dias.'
            return write
        elif int(month) >12:
            write = 'O ano só tem 12 meses.'
            return write
        elif int(year) < actual_day[2]:
            write  = 'Ano invalido.'
            return write
        else:
            nd = int(day),int(month),int(year)
            global new_date 
            new_date = nd
            database["end_alarm"] = new_date
            with open("data.json", "w")as file:
                json.dump(database,file)
            return True

def add():
    a = append()
    lb_error.config(text='')
    lb_error.config(text='')
    etry_all.delete(0,END)
    if a == True:
        list_box_goals.delete(0,END)
        for value,item in enumerate(database["list_of_goals"],start=0):
            list_box_goals.insert(END, f'{value}- {item}')
    else:
        lb_error.config(text=a)

def remove2():
    a = remove()
    lb_error.config(text='')
    etry_all.delete(0,END)
    if a == True:
        list_box_goals.delete(0,END)
        for value,item in enumerate(database["list_of_goals"],start=0):
            list_box_goals.insert(END, f'{value}- {item}')
    else:
        lb_error.config(text=a)
        

def change_hour():
    a = change_alarm()
    
    lb_error.config(text='')
    etry_all.delete(0,END)
    if a == True:
        lb_time_alarme.config(text=database["alarm_time"])        
    else:
        lb_error.config(text=a)

def change_date():
    a = change_date_of_end()
    lb_error.config(text='')
    etry_all.delete(0,END)
    if a == True:
        lb_date.config(text=database["end_alarm"])
    else:
        lb_error.config(text=a)
     

    



CAMINHO_DA_IMAGEM = 'C:\\Users\\mique\\OneDrive\\Área de Trabalho\\Aplicativo super foco\\img'

principal = Tk()
 #configuração da janela
principal.geometry('800x800')
principal.title(f'Super Foco')
principal.resizable(False,False)

        
img_bg = PhotoImage(master=principal,file=f'{CAMINHO_DA_IMAGEM}\\pagina_1.png')
img_button_add = PhotoImage(file=f'{CAMINHO_DA_IMAGEM}\\adicionar_lista.png')
img_button_remove = PhotoImage(file=f'{CAMINHO_DA_IMAGEM}\\remover_lista.png')
img_button_time = PhotoImage(file=f'{CAMINHO_DA_IMAGEM}\\alterar_horario.png')
img_button_alarm = PhotoImage(file=f'{CAMINHO_DA_IMAGEM}\\alterar_data.png')

#background
bg= Label(principal,image=img_bg)
bg.pack()

#label hora e data 
lb_time_alarme = Label(principal)
lb_time_alarme.place(relx=0.25,rely=0.13,width=100,height=50)
lb_time_alarme.config(text= database["alarm_time"])

lb_date = Label(principal)
lb_date.place(relx=0.76,rely=0.13,width=100,height=50)
lb_date.config(text=database["end_alarm"])

#botao adicionar
bt_add = Button(principal,border=3,image=img_button_add, command=add)
bt_add.place(relx=0.10,rely=0.33,width=100,height=50)

#botao remover
bt_remove = Button(principal,border=3,image=img_button_remove,command=remove2)
bt_remove.place(relx=0.27,rely=0.33,width=100,height=50)

#botao alterar hora do alarme
bt_time = Button(principal,border=3,image=img_button_time, command=change_hour)
bt_time.place(relx=0.60,rely=0.33,width=100,height=50)

#botao alterar data do fim do alarme
bt_end_alarm = Button(principal,border=3,image=img_button_alarm,command=change_date)
bt_end_alarm.place(relx=0.77,rely=0.33,width=100,height=50)

#entry input
etry_all  = Entry(principal,justify='center')
etry_all.place(relx=0.03,rely=0.43,width=752,height=49)

#LABEL DE ERROS 
lb_error = Label(principal,background='#d9d9d9')
lb_error.place(relx=0.03,rely=0.50,width=752,height=19)


#Barra de rolagem 
bar_scroll = Scrollbar(principal,)
bar_scroll.place(relx=0.949, rely=0.53,width=23,height=350)

# # list box com as metas da lista
list_box_goals = Listbox(principal,selectmode=SINGLE, yscrollcommand=bar_scroll.set,font=("Arial",18))
list_box_goals.place(relx=0.03,rely=0.53,width=732,height=350)
bar_scroll.config(command=list_box_goals.yview)
for value,item in enumerate(database["list_of_goals"],start=0):
    list_box_goals.insert(END, f'{value}- {item}')

def loop():
    principal.mainloop()
