import tkinter as tk
from tkinter import *
""""CONSTANTS"""
C_HEIGHT = 400
C_WIDTH = 400
POS = 0.2
bgColor = "#a2a4a8"
root = tk.Tk()
root.title("DRIVING STATISTICS")
var1=IntVar()
var2=IntVar()
var3=IntVar()

canvas = tk.Canvas(root, height=C_HEIGHT , width=C_WIDTH,)
canvas.pack()
"""Functions"""
def confirm():
    date = str(dateEntry.get())
    location = str(locateEntry.get())
    duration = str(durEntry.get())
    tod1 = var1.get()
    tod2 = var2.get()
    tod3 = var3.get()
    def respond(msg):
        Top= tk.Toplevel(height=300, width=300)
        Top.title = "Sucess!"
        respondFrame = tk.Frame(Top)
        respondFrame.place(relheight=1, relwidth=1)
        respondLabel = tk.Label(respondFrame, text=msg)
        respondLabel.pack()
        respondButton = tk.Button(respondFrame, text="OK", command=lambda:Top.destroy())
        respondButton.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.2)
    if len(date) > 0 and len(location) > 0 and len(duration) > 0 and (tod1 == True) and (tod2 == False) and (tod3 == False):
        tod = "morning"
        msg = ("You drove at %s, \non %s, \nfor %s minute(s),\n in the %s!\nSuccessfully printed information to\nDrivingStatistics.txt!" %(location, date, duration, tod))
        txtMsg = ("You drove at %s, on %s, for %s minute(s), in the %s!\r\n" %(location, date, duration, tod))
        respond(msg)
        file=open("DrivingStatistics.txt", "a+")
        file.write(txtMsg)
        file.close()
    elif len(date) > 0 and len(location) > 0 and len(duration) > 0 and (tod1 == False) and (tod2 == True) and (tod3 == False):
        tod = "afternoon"
        msg = ("You drove at %s, \non %s, \nfor %s minute(s),\n in the %s!\nSuccessfully printed information to\nDrivingStatistics.txt!" %(location, date, duration, tod))
        txtMsg = ("You drove at %s, on %s, for %s minute(s), in the %s!\r\n" %(location, date, duration, tod))
        respond(msg)
        file=open("DrivingStatistics.txt", "a+")
        file.write(txtMsg)
        file.close()
    elif len(date) > 0 and len(location) > 0 and len(duration) > 0 and (tod1 == False) and (tod2 == False) and (tod3 == True):
        tod = "night"
        msg = ("You drove at %s, \non %s, \nfor %s minute(s),\n in the %s!\nSuccessfully printed information to\nDrivingStatistics.txt!" %(location, date, duration, tod))
        txtMsg = ("You drove at %s, on %s, for %s minute(s), in the %s!\r\n" %(location, date, duration, tod))
        respond(msg)
        file=open("DrivingStatistics.txt", "a+")
        file.write(txtMsg)
        file.close()
    else:
        msg = ("Either all fields were not filled,\nor too many checkboxes were selected.\nTry again!")
        respond(msg)
    dateEntry.delete(0, END)
    locateEntry.delete(0, END)
    durEntry.delete(0, END)


"""Date"""
dateFrame = tk.Frame(canvas)
dateFrame.place(relheight=0.2, relwidth= 1, rely=0)
dateLabel = tk.Label(dateFrame, text="Select a date (mm/dd/yyyy)")
dateLabel.place(relwidth=0.4, relx = 0.3, rely = 0.2)
dateEntry = tk.Entry(dateFrame, justify="center")
dateEntry.place(relwidth=0.5, relx=0.25, rely=0.7)
"""Location"""
locateFrame = tk.Frame(canvas)
locateFrame.place(relheight=0.2, relwidth = 1, rely = POS)
locLabel = tk.Label(locateFrame, text="Enter a Location")
locLabel.place(relwidth=0.4, relx = 0.3, rely = 0.2)
locateEntry = tk.Entry(locateFrame, justify="center")
locateEntry.place(relwidth=0.5, relx=0.25, rely=0.7)
"""Duration"""
durFrame = tk.Frame(canvas)
durFrame.place(relheight=0.2, relwidth=1, rely=POS*2)
durLabel = tk.Label(durFrame, text="Enter duration of drive (in minutes)")
durLabel.place(relwidth=0.7, relx = 0.15, rely = 0.2)
durEntry = tk.Entry(durFrame, justify="center")
durEntry.place(relwidth=0.5, relx=0.25, rely=0.7)
"""TimeofDay"""
todFrame = tk.Frame(canvas)
todFrame.place(relheight=0.2, relwidth=1, rely=POS*3 )
todLabel = tk.Label(todFrame, text="Select time of day")
todLabel.place(relwidth=0.7, relx=0.15, rely=0.2)
morning = tk.Checkbutton(todFrame, text="morning", variable=var1, onvalue=1, offvalue=0)
morning.place(relx=0.2, rely=0.7)
afternoon = tk.Checkbutton(todFrame, text="afternoon", variable=var2, onvalue=1, offvalue=0)
afternoon.place(relx=0.45, rely=0.7)
night = tk.Checkbutton(todFrame, text="night", variable=var3, onvalue=1, offvalue=0)
night.place(relx=0.7, rely=0.7)

"""enterButton"""
buttonFrame = tk.Frame(canvas)
buttonFrame.place(relheight=0.2, relwidth=1, rely=POS*4)
enterButton = tk.Button(buttonFrame, text="Confirm Data", justify="center"\
    ,command=lambda:confirm())
enterButton.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.25)


root.mainloop()
