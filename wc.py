from tkinter import *
import time
import datetime
from PIL import Image, ImageDraw, ImageFont, ImageTk
import worky_data_base as wdb
import function as func


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
    Login, counter_odo, counter_dst = func.repack_download_counter(counter)
    window = Tk()
    window.title('Воркометр 2.5')
    window.geometry('372x180')
    foneimage = ImageTk.PhotoImage\
        (Image.open('d:\Python\Desktop\worky_v_2_5\emplate\media\image\worky.jpg'))
    fonelabel = Label(window, image=foneimage)
    fonelabel.place(x=0, y=0)
    textodometr = str(counter_odo)
    textdistance = str(counter_dst)
    textlogin = Login
    loginlabel = Label(fonelabel, text=textlogin, font=('Roboto Bold', 12))
    loginlabel.place(x=5, y=100)
    odometrlabel = Label(fonelabel, text=textodometr[0:6], font=('Roboto Bold', 13))
    odometrlabel.place(x=156, y=108)
    distancelabel = Label(fonelabel, text=textdistance[0:3], font=('Roboto Bold', 12))
    distancelabel.place(x=166, y=67)
    distancefloatlabel = Label(fonelabel, text=textdistance[3], font=('Roboto Bold', 12))
    distancefloatlabel.place(x=195, y=67)
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
        #Display.indication.configure(text='DRIVE', fg='green')

    @staticmethod
    def command_button_start():
        while True:
            Display.indication.configure(text='STOP', fg='red')

            counter_data = wdb.Counter('Shock', 0, 0)
            counter = counter_data.download()
            counter_data.close()
            Login, counter_odo, counter_dst = func.repack_download_counter(counter)
            inte_odometr = func.string_to_integer(counter_odo)
            inte_distance = func.string_to_integer(counter_dst)
            #Display.textlogin.configure(text=Login)

            while Display.status == 0:
                Display.indication.configure(text='DRIVE', fg='green')
                inte_odometr += 1
                inte_distance += 1
                str_odometr = func.integer_to_string(inte_odometr, 8)
                str_distance = func.integer_to_string(inte_distance, 5)
                Display.odometrlabel.configure(text=str_odometr[0:6])
                Display.odometrlabel.place(x=156, y=108)
                Display.distancelabel.configure(text=str_distance[0:3])
                Display.distancelabel.place(x=166, y=67)
                Display.distancefloatlabel.configure(text=str_distance[3])
                Display.distancefloatlabel.place(x=195, y=67)
                counter_data_1 = wdb.Counter(Display.Login, inte_odometr, inte_distance)
                counter_data_1.update()
                counter_data_1.close()
                inte_odometr = func.string_to_integer(str_odometr)
                inte_distance = func.string_to_integer(str_distance)

                time.sleep(1)


    @staticmethod
    def command_button_stop():
        Display.status = 1
        Display.indication.configure(text='STOP', fg='red')





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
            Display.fonelabel, text='0', fg='black', font=('Roboto Bold', 16)
                             )
        button_null.place(x=330, y=110)