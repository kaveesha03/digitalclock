import tkinter as ui
import time

window = ui.Tk()

def update_clock():

 hour=time.strftime('%I')
 minute=time.strftime('%M')
 second=time.strftime('%S')
 meridian=time.strftime('%p')
 dtime=hour+':'+minute+':'+second+':'+meridian
 digital_clock_lbl.config(text=dtime)
 digital_clock_lbl.after(1000,update_clock)


digital_clock_lbl = ui.Label(window , text="00:00:00",font='italics 82 bold')


digital_clock_lbl.pack()


update_clock()


window.mainloop()


