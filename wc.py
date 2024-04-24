from tkinter import *
import time
import datetime
from PIL import Image, ImageDraw, ImageFont, ImageTk
import worky_data_base as wdb
import function as func
from tkinter import Menu


"""
This is class for worky
"""

class Display():
    """
    This is basic class of Worky, which displays Worky's Display
    """
    Login = 'Shock'
    counter_dst = 12345
    counter_odo = 12345678
    counter_data = wdb.Counter('Shock', 0, 0)
    counter = counter_data.download()
    counter_data.close()
    counter_1 = func.repack_download_counter(counter)
    Login, counter_dst, counter_odo = func.repack_download_counter(counter)
    window = Tk()
    window.title('Воркометр 2.5')
    window.geometry('372x180')
    foneimage = ImageTk.PhotoImage\
        (Image.open('d:\Python\Desktop\worky_v_2_5\emplate\media\image\worky.jpg'))
    fonelabel = Label(window, image=foneimage)
    fonelabel.place(x=0, y=0)
    textodometr = func.integer_to_string(counter_odo, 8)
    textdistance = func.integer_to_string(counter_dst, 5)
    textlogin = Login
    loginlabel = Label(fonelabel, text=textlogin, font=('Roboto Bold', 12))
    loginlabel.place(x=5, y=100)
    odometrlabel = Label(fonelabel, text=textodometr[0:6], font=('Roboto Bold', 13))
    odometrlabel.place(x=156, y=108)
    distancelabel = Label(fonelabel, text=textdistance[0:3], font=('Roboto Bold', 12))
    distancelabel.place(x=166, y=67)
    distancefloatlabel = Label(fonelabel, text=textdistance[3], font=('Roboto Bold', 12))
    distancefloatlabel.place(x=196, y=67)
    distancefloatlabel.configure(fg='red')
    indication = Label(fonelabel, text='Stop', fg='red', bg='black', font=('Roboto Bold', 20))
    indication.place(x=3, y=130)
    status = 1
    generalframe = Frame(master=window, bg='limegreen')
    generalframe.pack()


class Comand(Display):
    """
    This is class for work is command button aplication
    """
    @staticmethod
    def command_button_start_1():
        Display.status = 0

    @staticmethod
    def command_button_start():
        while True:
            Display.indication.configure(text='STOP', fg='red')
            counter_data = wdb.Counter('Shock', 0, 0)
            counter = counter_data.download()
            counter_data.close()
            Login, counter_dst, counter_odo  = func.repack_download_counter(counter)
            Display.Login = Login
            counter_odo = func.integer_to_string(counter_odo, 8)
            counter_dst = func.integer_to_string(counter_dst, 5)
            Display.odometrlabel.configure(text=counter_odo[0:6])
            Display.distancelabel.configure(text=counter_dst[0:3])
            Display.distancefloatlabel.configure(text=counter_dst[3])
            inte_odometr = func.string_to_integer(counter_odo)
            inte_distance = func.string_to_integer(counter_dst)
            Display.loginlabel.configure(text=Login)
            while Display.status == 0:
                Display.indication.configure(text='DRIVE', fg='green')
                Display.loginlabel.configure(text=Login)
                inte_odometr += 1
                inte_distance += 1
                inte_distance = func.big_number(inte_distance, 100000)
                inte_odometr = func.big_number(inte_odometr, 100000000)
                str_odometr = func.integer_to_string(inte_odometr, 8)
                str_distance = func.integer_to_string(inte_distance, 5)
                Display.odometrlabel.configure(text=str_odometr[0:6])
                Display.distancelabel.configure(text=str_distance[0:3])
                Display.distancefloatlabel.configure(text=str_distance[3])
                counter_data_1 = wdb.Counter(Display.Login, inte_distance, inte_odometr)
                counter_data_1.update()
                counter_data_1.close()
                inte_odometr = func.string_to_integer(str_odometr)
                inte_distance = func.string_to_integer(str_distance)
                time.sleep(1)

    @staticmethod
    def command_button_stop():
        Display.status = 1
        Display.indication.configure(text='STOP', fg='red')
        counter_data = wdb.Counter('Shock', 0, 0)
        counter = counter_data.download()
        counter_data.close()
        Login, counter_dst, counter_odo = func.repack_download_counter(counter)
        Login = Login+'+'
        counter_data_reserve = wdb.Counter(Login, counter_dst, counter_odo)
        counter_data_reserve.update()
        counter_data_reserve.close()

    @staticmethod
    def command_button_null():
        counter_data = wdb.Counter('Shock', 0, 0)
        counter = counter_data.download()
        counter_data.close()
        Login, counter_dst, counter_odo = func.repack_download_counter(counter)
        counter_data_new = wdb.Counter(Login, 0, counter_odo)
        counter_data_new.update()
        counter_data_new.close()

    @staticmethod
    def reserve_load():
        counter_data = wdb.Counter('Shock', 0, 0)
        counter = counter_data.download()
        #counter_data.close()
        Login, counter_dst, counter_odo = func.repack_download_counter(counter)
        Login = Login+'+'
        counter_data_new = wdb.Counter(Login, counter_dst, counter_odo)
        counter_data = counter_data_new.download()
        counter_data_new.close()
        Login, counter_dst, counter_odo = func.repack_download_counter(counter_data)
        Login = func.reserv_load_save(Login)
        counter_data_new_save = wdb.Counter(Login, counter_dst, counter_odo)
        counter_data_new_save.update()
        counter_data_new_save.close()

    @staticmethod
    def clickexit():
        Display.window.destroy()


class Buttons(Display):
    """
    This is class do it work button
    """
    @staticmethod
    def button_start():
        button_start = Button(
            Display.fonelabel, text='D', fg='green', font=('Roboto Bold', 16),
            command=Comand.command_button_start_1
                              )
        button_start.place(x=330, y=10)

    @staticmethod
    def button_stop():
        button_stop = Button(
            Display.fonelabel, text='S', fg='red', font=('Roboto Bold', 16),
            command=Comand.command_button_stop
                             )
        button_stop.place(x=330, y=60)

    @staticmethod
    def button_null():
        button_null = Button(
            Display.fonelabel, text='0', fg='black', font=('Roboto Bold', 16),
            command=Comand.command_button_null
                             )
        button_null.place(x=330, y=110)


class MenuSettings(Display):
    """
    This is class for menu worky
    """
    menu = Menu(Display.fonelabel)
    new_item = Menu(menu, tearoff=0)
    new_item.add_command(label='Drive', command=Comand.command_button_start_1)
    new_item.add_command(label='Stop', command=Comand.command_button_stop)
    new_item.add_command(label='Null', command=Comand.command_button_null)
    new_item.add_command(label='Reserve Load', command=Comand.reserve_load)
    new_item.add_command(label='Exit', command=Comand.clickexit)
    menu.add_cascade(label='file', menu=new_item)
    Display.window.config(menu=menu)