from tkinter import *
import wc
import worky_data_base as wdb


"""
Basic functions application Worky
"""
Login = 'Shock'
counter_dst = 12345
counter_odo = 12345678
worky_display = wc.Display()
button_aplication = wc.Buttons()
button_aplication.button_start()
button_aplication.button_stop()
button_aplication.button_null()
worky = wdb.Counter(Login, counter_dst, counter_odo)
worky.update()
worky_display.window.mainloop()