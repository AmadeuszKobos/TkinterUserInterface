import tkinter as tk


def on_button_click():
    entry_text = entry.get()
    label.config(text=entry_text)
    entry.delete(0, tk.END)


app = tk.Tk()
app.geometry("400x300")
app.title("My app")

label = tk.Label(app, text="This is python user interface created with tkinter library")
label.pack(padx=20, pady=10)

entry = tk.Entry(app)
entry.pack(pady=10)

textbox = tk.Text(app, height=4, width=30)
textbox.pack()

button = tk.Button(app, text="Call", command=on_button_click)
button.pack()

button_frame = tk.Frame(app, pady=5)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)

btn1 = tk.Button(button_frame, text='1')
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(button_frame, text='2')
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(button_frame, text='3')
btn3.grid(row=0, column=2, sticky="WE") #second way for sticky param

btn1 = tk.Button(button_frame, text='4')
btn1.grid(row=1, column=0, sticky=tk.W+tk.E)

btn1 = tk.Button(button_frame, text='5')
btn1.grid(row=1, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(button_frame, text='6')
btn1.grid(row=1, column=2, sticky=tk.W+tk.E)

btn1 = tk.Button(button_frame, text='7')
btn1.grid(row=2, column=0, sticky=tk.W+tk.E)

btn1 = tk.Button(button_frame, text='8')
btn1.grid(row=2, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(button_frame, text='9')
btn1.grid(row=2, column=2, sticky=tk.W+tk.E)

button_frame.pack(fill='x')

app.mainloop()