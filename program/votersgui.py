import tkinter as tk
from tkinter import messagebox
import recognizer as rec
import image_generator as ig
import populator
import db


HEIGHT = 200
WIDTH = 400


def gui():
    root = tk.Tk()
    root.title("ai2Project")
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    frame = tk.Frame(root, bg='#FAD4CC')
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    label = tk.Label(frame, text="Voter's ID Registration", bg='#FAD4CC', font=40)
    label.pack()

    start_button = tk.Button(frame, text="Start", font=40, height = 1, width = 10, command=start)
    start_button.pack(padx=10, pady=20, side=tk.LEFT)

    show_button = tk.Button(frame, text="Show History", font=40, height = 1, width = 10, command=show_history)
    show_button.pack(padx=15, pady=20, side=tk.RIGHT)

    # end_button = tk.Button(frame, text="End", font=40, height = 1, width = 10, command=end)
    # end_button.pack(padx=15, pady=25, side=tk.RIGHT)

    root.mainloop()


def start():
    values = populator.start()
    # save here!!!
    db.save(values)

def show_history():
    values = db.retrieve()
    if values:
        names = "\r\n".join([f"{v['first name']} {v['last name']}"  for v in values])
        messagebox.showinfo('User History', names)
    else:
        messagebox.showinfo('User History', 'No history yet.')



if __name__ == "__main__":
    gui()
