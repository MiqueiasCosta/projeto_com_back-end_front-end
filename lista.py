from funcoes import anumber
import json
from tkinter import *






list_of_goals = []
def create_list():
        writes = ''
        goals = enty_of_append.get()
        if goals =='':
            writes = 'Digite letras!'
            return writes
        elif goals.isdigit():
            writes = 'Digite apenas letras!'
            return writes
        elif goals.isdecimal():
            writes = 'Digite apenas letras!'
            return writes
        elif anumber.isfloat(goals) == True:
            writes = ' Digite apenas letras!'
            return writes
        elif goals in list_of_goals:
            writes = 'Esta meta já foi adicionada'
            return writes
        else:
            list_of_goals.append(goals)
            go_to_json = {
                 
                "list_of_goals": list_of_goals
                }
            with open("data.json","w") as file_json:
                json.dump(go_to_json,file_json)
            writes = True
            return writes
def resp():
    list_  = create_list()#resultado da função
    enty_of_append.delete(0,END)
    if list_ == True:
        list__ = '\n'.join(list_of_goals)#lista com separação de linhas 
        return list_of_window.config(text=list__)
    else:
        return list_of_window.config(text=list_)


def finish():
    if len(list_of_goals) > 0:
            window.destroy()
            from hora_data import play_of_window
            play_of_window()
    else:
        list_of_window.config(text='Adicione algo a lista de meta para finalizar')

window = Tk()
#configuração da janela
window.geometry('700x700')
window.title(f'Lista de Metas')

#Imagens adicionadas
img_bg_ = PhotoImage(master=window,file="img_1\\Adicione metas.png")
img_bt = PhotoImage(master=window,file="img_1\\Adicionar.png")
img_bt_finish = PhotoImage(master=window,file="img_1\\finalizar1.png")

#fundo
label_bg = Label(window,image=img_bg_)
label_bg.pack()


#testo da lista
list_of_window = Label(window,background='#d9d9d9')
list_of_window.place(relx=0.08,rely=0.55,relwidth=0.83,relheight=0.18)

#input
enty_of_append = Entry(window,border=4,justify='center',font=("Helvetica",20))
enty_of_append.place(relx=0.04,rely=0.39,width=639,height=48)

#botao de adicionar
button_of_append = Button(window,image=img_bt,border=3, command=resp)
button_of_append.place(relx=0.19,rely=0.78,width=141,height=70)

#botao de finalizar a lista
button_of_finish = Button(window,border=3,image=img_bt_finish,command=finish)
button_of_finish.place(relx=0.59,rely=0.78,width=141,height=70)


def listing_():
    window.mainloop()

listing_()