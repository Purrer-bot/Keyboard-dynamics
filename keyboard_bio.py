#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox as mb
from time import time
from PIL import Image, ImageTk
import db_conn


#Главное окно
root = Tk()
root.title("Клавиатурный почерк")
root.geometry("300x250")

#Окно регистрации
def registration_window():
    #Очищаем все и вся
    keyboard_array = []
    counter = 0
    dif_array = []
    # def_phrase = db_conn.get_random_message()
    changecounter.set("")
    correction.set("")
    #Начало работы
    register_window = Toplevel()
    register_window.title("Форма регистрации в системе для получения котика")
    register_window.grab_set()
    #*** Функции окна регистрации ***
    def check_counter(counter):
        global def_phrase
        global mean_deviation
        global ideal_array
        mean_ideal = 0
        mean_mean_deviation = 0
        username = name_box.get()
        if db_conn.check_username(username):
            correction.set("Такое имя уже существует")
            counter = 0
        if counter >= 5:
            # username = name_box.get()
            # if db_conn.check_username(username):
            #     correction.set("Такое имя уже существует")
            name.set(username)
            mb.showinfo("Ввод завершен","Данные записаны, вы зарегистрированы!")
            mean_ideal = sum(ideal_array) / len(ideal_array)
            mean_mean_deviation = sum(mean_deviation) / len(mean_deviation)
            phrase_id = db_conn.get_message_id(def_phrase)
            try:
                db_conn.insert_user(username, phrase_id, mean_ideal, mean_mean_deviation)
            except Exception as e:
                print("Ошибка записи ", e)
            #Все очищаем и опустошаем
            text_box.delete(0, END)
            name_box.delete(0, END)
            mean_deviation =[]
            ideal_array = []
            def_phrase = db_conn.get_random_message()
            register_window.grab_release()
            register_window.destroy()

    def prepare_text_box():
        text_box.delete(0, END)
        text_box.bind("<Key>", key)
        correction.set("")
        button_next.pack_forget()
        return

    def count_keyboard_dynamics(dif_array):
        global ideal_array
        global deviation_array
        global mean_deviation
        difference = 0
        for i in range(len(dif_array)):
            ideal_array.append(sum(dif_array)/len(dif_array))
        last_ideal = ideal_array[len(ideal_array) - 1]
        for i in range(len(dif_array)):
            difference += last_ideal - dif_array[i]
        deviation_array.append(difference / len(dif_array))
        mean_deviation.append(sum(deviation_array) / len(deviation_array))


    def spellcheck(def_phrase, dif_array):
        nonlocal counter
        print("Начинаю работу")
        phrase = text_box.get()
        if phrase == def_phrase:
            print("Сработало событие")
            # username = name_box.get()
            correction.set("Верно, записываем")
            text_box.unbind("<Key>")
            result = ' '.join(str(x) for x in dif_array)
            button_next.pack()
            count_keyboard_dynamics(dif_array)
            keyboard_array = []
            dif_array = []
            counter += 1
            check_counter(counter)
            remain_counter = 5 - counter
            changecounter.set("Введено : {}".format(remain_counter))
            return
        else:
            correction.set("Заново!")
            print("Сработало событие. Но неверно")
            return

    def key(event):
        # global keyboard_array
        nonlocal keyboard_array
        global def_phrase
        nonlocal dif_array
        global start_time
        if event.char == '\r':
            print("Оно вообще работает?")
            spellcheck(def_phrase, dif_array)
        print ("pressed", repr(event.char))
        end_time = time()
        diff = end_time - start_time
        keyboard_array.append(diff)
        print ("measured time:", end_time - start_time)
        if len(keyboard_array) >= 2:
            keystroke_diff = keyboard_array[len(keyboard_array)-1] - keyboard_array[len(keyboard_array) - 2]
            print("Diff:", keystroke_diff)
            dif_array.append(keystroke_diff)

    # ***Виджеты окна регистрации ***
    label_name = Label(register_window, text = 'Имя: ')
    name_box = Entry(register_window, textvariable = name)
    label_text = Label(register_window, text = 'Парольная фраза: ',)
    label_passprase = Label(register_window, text = def_phrase)
    text_box = Entry(register_window, textvariable = passphrase)
    label_correction = Label(register_window, textvariable = correction, fg = '#ff0000')
    label_counter = Label(register_window, textvariable = changecounter)
    button_next = Button(register_window, text = 'Еще раз!', command = prepare_text_box)

    # ***Размещение виджетов регистрации ***
    label_name.pack()
    name_box.pack()
    label_text.pack()
    text_box.pack()
    label_passprase.pack()
    label_correction.pack()
    label_counter.pack()
    name_box.focus_set()
    # ***Связывание счетчика нажатий ***
    text_box.bind("<Key>", key)

#Окно входа
def login_window():
    error = StringVar()
    error.set('')
    # log_name = "Pusheen"
    log_window = Toplevel()
    log_window.title("Вход")
    log_window.grab_set()
    # print("Log_name ",log_name)

    def diff_count():
        nonlocal df_array
        ideal = 0
        difference = 0
        for i in range(len(df_array)):
            ideal = sum(df_array)/len(df_array)
            difference += df_array[i] - ideal
        difference = difference / len(df_array)
        return difference, ideal

    def verification():
        global EPS_I
        global EPS_D
        err_mess = StringVar()
        # print("Ver ", name)
        login = log_box.get()
        password = pass_box.get()
        try:
            db_name, db_pid, db_ideal, db_diff = db_conn.get_user_info(login)
        except:
            error.set("Ошибка логина или парольной фразы, введите заново")
        if login == db_name and db_conn.get_message_id(password) == db_pid:
            difference, ideal = diff_count()
            print(EPS_I)
            print(abs(db_ideal - ideal ))
            print(EPS_D)
            print(abs(db_diff - difference))
            if abs(db_ideal - ideal )< EPS_I and abs(db_diff - difference) < EPS_D:
                print(difference)
                print(ideal)
                print(abs(db_ideal - ideal ))
                mb.showinfo("Вход в систему","Вы вошли в систему, ура!")
                log_box.delete(0, END)
                pass_box.delete(0, END)
                log_window.grab_release()
                log_window.destroy()
                create_after_window()
            else:
                error.set("Ошибка верификации почерка")
                pass_box.delete(0, END)
                pass_box.bind("<Key>", key_check)

    def key_check(event):
        global def_phrase
        nonlocal current_time
        nonlocal pass_array
        nonlocal df_array
        end_time = time()
        diff = end_time - current_time
        print("Diff ", diff)
        pass_array.append(diff)
        if len(pass_array) >= 2:
            keystroke_diff = pass_array[len(pass_array)-1] - pass_array[len(pass_array) - 2]
            df_array.append(keystroke_diff)
        if event.char == '\r':
            # phrase = pass_box.get()
            # if phrase == def_phrase:
            #     error.set("Пароль введен верно, можете пройти верификацию")
                pass_box.unbind("<Key>")
            # else:
            #     error.set("Ошибка ввода")

    def create_after_window():
        after_window = Toplevel()
        after_window.title("Система котика")
        after_window.grab_set()

        def logout():
            name.set('')
            after_window.grab_release()
            after_window.destroy()
            return

        image = Image.open("image.png")
        image = image.resize((250, 250), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        kitty_label = Label(after_window, image = photo, textvariable = 'Котик за хорошую работу, {}'.format(name))
        kitty_label.image = photo
        after_button = Button(after_window, text = "Разозлиться >_<", command = lambda:logout())
        kitty_label.pack()
        after_button.pack()

    #Виджеты входа
    log_label = Label(log_window, text = 'Логин')
    log_box = Entry(log_window)
    pass_label = Label(log_window, text = 'Парольная фраза')
    pass_box = Entry(log_window)
    log_button = Button(log_window, text = 'Вход', command = lambda: verification())
    error_label = Label(log_window, textvariable = error, fg = '#ff0000')

    #Размещение
    log_label.pack()
    log_box.pack()
    pass_label.pack()
    pass_box.pack()
    log_button.pack()
    error_label.pack()

    #Связываем счетчик и поле ввода
    current_time = time()
    pass_array = []
    df_array = []
    pass_box.bind("<Key>", key_check)


#Глобальные переменные и константы
start_time = 0
end_time = 0
name = StringVar()
passphrase = StringVar()
correction = StringVar()
changecounter = StringVar()
def_phrase = db_conn.get_random_message()
ideal_array = []
deviation_array = []
mean_deviation = []

#EPS_I = 0.05
EPS_I = 0.15
EPS_D = 0.0000000001
#Виджеты главного окна:
button_registration = Button(root, text = 'Регистрация', command = registration_window)
button_login = Button(root, text = 'Вход', command = login_window)

#Размещение виджетов главного окна
button_registration.pack()
button_login.pack()


#Прочее
# keyboard_array = []
start_time = time()

mainloop()
