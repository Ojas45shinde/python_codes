import tkinter as tk
import time
from datetime import datetime

def digital_clock():
    current_time = datetime.now().strftime('%H:%M:%S')
    clock_label['text'] = current_time
    clock_label.after(1000, digital_clock)  


root = tk.Tk()
root.title("DIGITAL CLOCK")
root.geometry('250x100')

clock_label = tk.Label(root, font=('Helvetica', 46, 'bold'), bg='black', fg='white')
clock_label.pack(anchor='center')


digital_clock()

root.mainloop()
