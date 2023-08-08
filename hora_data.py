from funcoes import negative_number
from datetime import datetime
import json
from tkinter import *


# '''
# Já esta parte pega informações de data e hora para o usuario setar um alarme para foco.
# '''
end_of_day = []
alarm_time = []
change_window = False

def hour():
        hours_= entry_of_time.get()
        string_ = ''
        if hours_ == '':
            string_ = 'Digite algo para colocarmos no banco de dados.'
            return string_
        elif not hours_.isdigit():
            string_ = 'Digite apenas numeros.'
            return string_
        elif int(hours_) < 0:
            string_ = 'Numeros negativos não existem nas horas.'
        else:
            if int(hours_) > 23:
                string_ = 'Um dia só tem 23 horas.'
                return string_
            else:
                alarm_time.append(int(hours_))
                string_ = True
                return string_


def date():
        actual_day = datetime.now()
        day1 = int(actual_day.day),int(actual_day.month),int(actual_day.year)
        day_of_end = entry_of_days.get()
        write = ''
        convertion = day_of_end.split(',')
        day = convertion[0]
        month = convertion[1]
        year = convertion[2]
        if day_of_end == '':
            write = 'Digite algo para colocarmos no banco de dados.'
            return write
        if not day.isdigit():
             write = 'Digite apenas numeros por favor!'
             return write
        elif not month.isdigit():
            write = 'Digite apenas numeros por favor!'
            return write
        elif not year.isdigit():
            write = 'Digite apenas numeros por favor!'
            return write
        elif not ',' in day_of_end:
            write = 'Dige a data neste formato. EXEMPLO: 10,7,2023.'
            return write
        if negative_number(int(day),int(month),int(year)) == False:
            write = 'Nenhum numero pode ser negativo!'
            return write
        else:
            if int(day) >30:
                write = 'O maximo que você pode colocar é 30 dias.'
                return write
            elif int(month) >12:
                write = 'O ano só tem 12 meses.'
                return write
            elif int(year) < day1[2]:
                write  = 'Ano invalido.'
                return write
            else:
                nd = int(day),int(month),int(year)
                end_of_day.append(nd)
                return True




def resps():
    time = hour()
    date_ = date()
    label_of_error.config(text='')
    if time == True:
        if date_ == True:
            with open("data.json", "r") as file:
                data = json.load(file)
                data["alarm_time"] = alarm_time[0]
                data["end_alarm"] = end_of_day[0]
                with open("data.json", "w") as file:
                    json.dump(data,file)
                    window.destroy()
                    global change_window
                    change_window = True
                
        else:
            label_of_error.config(text=date_)
    else:
        label_of_error.config(text=time)





window = Tk()
 #configuração da janela
window.geometry('700x700')
window.title(f'Data e Hora')
window.resizable(False,False)

        
img_bg = PhotoImage(file='img\\pagina_data_hour.png')
img_button = PhotoImage(file='img\\botao_data_hour.png')
        
bg= Label(window,image=img_bg)
bg.pack()

#input de hora
entry_of_time = Entry(window,justify='center')
entry_of_time.place(relx=0.09,rely=0.28, width=140, height=40)

#input de dias
entry_of_days = Entry(window,justify='center')
entry_of_days.place(relx=0.09,rely=0.46, width=140, height=40)

#botao adcionar
bt_of_add = Button(window,image=img_button,border=3, command=resps)
bt_of_add.place(relx=0.42,rely=0.78,width=115, height=58)

# label se acontecer algum erro
label_of_error = Label(window, font=('Verdana',10),text='')
label_of_error.place(relx=0,rely=0.94,width=700,height=26)

def play_of_window():
    window.mainloop()


