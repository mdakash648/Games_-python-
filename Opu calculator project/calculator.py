import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

# Style Controler
display_start_row = 0 
display_start_column = 0
columnspan = 3
padding_x = 10
out_dis_height = 50
out_dis_margin_y = 5
out_dis_border = 2
width = 120



button_height = int(width/6.6667)
btn_margin_y = int(width/10)
button_width = int((width/3)-15)
window=tk.Tk()
window.title('Claculator')
frame=tk.Frame(master=window,bg="skyblue",padx=padding_x)
frame.pack()
entry=tk.Entry(master=frame,relief=SUNKEN,borderwidth=out_dis_border,width=width)
entry.grid(row=display_start_row,column=display_start_column,columnspan=columnspan,ipady=out_dis_height,pady=out_dis_margin_y)



def myclick(number):
    entry.insert(tk.END,number)

def equal():
    try:
        y=str(eval(entry.get()))
        entry.delete(0,tk.END)
        entry.insert(0,y)
    except:
        tkinter.messagebox.showinfo("Error","Syntax Error")

def clear():
    entry.delete(0,tk.END)

button_1=tk.Button(master=frame,text='1',padx=20,pady=button_height,width=button_width,command=lambda:myclick(1))
button_1.grid(row=1,column=0,pady=btn_margin_y)
button_2=tk.Button(master=frame,text='2',padx=20,pady=button_height,width=button_width,command=lambda:myclick(2))
button_2.grid(row=1,column=1,pady=btn_margin_y)
button_3=tk.Button(master=frame,text='3',padx=20,pady=button_height,width=button_width,command=lambda:myclick(3))
button_3.grid(row=1,column=2,pady=btn_margin_y)
button_4=tk.Button(master=frame,text='4',padx=20,pady=button_height,width=button_width,command=lambda:myclick(4))
button_4.grid(row=2,column=0,pady=btn_margin_y)
button_5=tk.Button(master=frame,text='5',padx=20,pady=button_height,width=button_width,command=lambda:myclick(5))
button_5.grid(row=2,column=1,pady=btn_margin_y)
button_6=tk.Button(master=frame,text='6',padx=20,pady=button_height,width=button_width,command=lambda:myclick(6))
button_6.grid(row=2,column=2,pady=btn_margin_y)
button_7=tk.Button(master=frame,text='7',padx=20,pady=button_height,width=button_width,command=lambda:myclick(7))
button_7.grid(row=3,column=0,pady=btn_margin_y)
button_8=tk.Button(master=frame,text='8',padx=20,pady=button_height,width=button_width,command=lambda:myclick(8))
button_8.grid(row=3,column=1,pady=btn_margin_y)
button_9=tk.Button(master=frame,text='9',padx=20,pady=button_height,width=button_width,command=lambda:myclick(9))
button_9.grid(row=3,column=2,pady=btn_margin_y)
button_0=tk.Button(master=frame,text='0',padx=20,pady=button_height,width=button_width,command=lambda:myclick(0))
button_0.grid(row=4,column=1,pady=btn_margin_y)

button_add=tk.Button(master=frame,text="+",padx=20,pady=button_height,width=button_width,command=lambda:myclick('+'))
button_add.grid(row=5,column=0,pady=btn_margin_y)

button_subtract=tk.Button(master=frame,text="-",padx=20,pady=button_height,width=button_width,command=lambda:myclick('-'))
button_subtract.grid(row=5,column=1,pady=btn_margin_y)

button_multiply=tk.Button(master=frame,text="*",padx=20,pady=button_height,width=button_width,command=lambda:myclick('*'))
button_multiply.grid(row=5,column=2,pady=btn_margin_y)

button_div=tk.Button(master=frame,text="/",padx=20,pady=button_height,width=button_width,command=lambda:myclick('/'))
button_div.grid(row=6,column=0,pady=btn_margin_y)

button_clear=tk.Button(master=frame,text="clear",padx=20,pady=button_height,width=button_width+4,command=clear)
button_clear.grid(row=6,column=1,columnspan=2,pady=btn_margin_y)

button_equal=tk.Button(master=frame,text="=",padx=20,pady=button_height,width=button_width+3,command=equal)
button_equal.grid(row=7,column=0,columnspan=5,pady=btn_margin_y)

window.mainloop()
