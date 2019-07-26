import tkinter as tk

HEIGHT = 200
WIDTH = 400

root = tk.Tk()
root.title("ai2Project")
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#FAD4CC')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label = tk.Label(frame, text="Voter's ID Registration", bg='#FAD4CC', font=40)
label.pack()

button1 = tk.Button(frame, text="Start", font=40, height = 1, width = 10)
button1.pack(padx=10, pady=20, side=tk.LEFT)

button2 = tk.Button(frame, text="Reprint", font=40, height = 1, width = 10)
button2.pack(padx=15, pady=20, side=tk.RIGHT)

button3 = tk.Button(frame, text="End", font=40, height = 1, width = 10)
button3.pack(padx=15, pady=25, side=tk.RIGHT)

root.mainloop()



