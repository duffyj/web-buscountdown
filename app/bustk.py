
from busdatareader import BusDataReader
import tkinter as tk

dbo = BusDataReader()
root = tk.Tk()
root.configure(background='black')
next_bus = tk.StringVar()
following_bus = tk.StringVar()

def to_text(b):
    return b[0] + "   " + str(b[2]) + "m"

def update_gui():
    filtered_results = dbo.get_data()

    # display if not empty
    if filtered_results:
       next_bus.set(to_text(filtered_results[0]))
       following_bus.set('\n'.join([to_text(b) for b in filtered_results[1:]]))
    root.after(5000, update_gui)

def main():

    root.wm_attributes("-topmost", 1)      #always on top

    next_lab = tk.Label(root, textvariable=next_bus,background='black',
                        foreground='blue', font='Ariak 70 bold')
    next_lab.pack()
    follow_lab = tk.Label(root, textvariable=following_bus, background='black',
                          foreground='lightblue', font='Arial 35')
    follow_lab.pack()

    update_gui()
    root.mainloop()


if __name__ == '__main__':
    main()

    
