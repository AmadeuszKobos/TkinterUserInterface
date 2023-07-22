import tkinter as tk

def on_button_click():
    entry_text = entry.get()
    label.config(text=entry_text)
    entry.delete(0, tk.END)

app = tk.Tk()
app.title("My app")

label = tk.Label(app, text="This is python user interface created with tkinter library")
label.pack()

entry = tk.Entry(app)
entry.pack()

button = tk.Button(app, text="Click here", command=on_button_click)
button.pack()

app.mainloop()