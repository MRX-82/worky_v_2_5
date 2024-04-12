from tkinter import *
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
    worky = wdb.Counter(Login, counter_dst, counter_odo)
    display_data = worky.download()
    Login = display_data[0][0]
    counter_dst = func.integer_to_string(display_data[0][1], 5)
    counter_odo = func.integer_to_string(display_data[0][2], 8)
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
    pass


class Buttons(Display):
    """
    This is class do it work button
    """
    @staticmethod
    def button_start():
        button_start = Button(Display.fonelabel, text='D', fg='green', font=('Roboto Bold', 16)
                              )
        button_start.place(x=330, y=10)

    @staticmethod
    def button_stop():
        button_stop = Button(Display.fonelabel, text='S', fg='red', font=('Roboto Bold', 16)
                             )
        button_stop.place(x=330, y=60)

    @staticmethod
    def button_null():
        button_null = Button(Display.fonelabel, text='0', fg='black', font=('Roboto Bold', 16)
                             )
        button_null.place(x=330, y=110)