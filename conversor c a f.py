import tkinter as tk

def celsius_to_fahrenheit():
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = celsius * 9 / 5 + 32
        result_label.config(text=f"{fahrenheit:.2f} °F")
    except ValueError:
        result_label.config(text="Introduce un número válido en Celsius.")

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(fahrenheit_entry.get())
        celsius = (fahrenheit - 32) * 5 / 9
        result_label.config(text=f"{celsius:.2f} °C")
    except ValueError:
        result_label.config(text="Introduce un número válido en Fahrenheit.")

# Creamos la ventana principal
window = tk.Tk()
window.title("Conversor de temperatura")

# Creamos los widgets de la interfaz
celsius_label = tk.Label(window, text="Celsius")
celsius_entry = tk.Entry(window)
fahrenheit_label = tk.Label(window, text="Fahrenheit")
fahrenheit_entry = tk.Entry(window)
to_fahrenheit_button = tk.Button(window, text="→ Fahrenheit", command=celsius_to_fahrenheit)
to_celsius_button = tk.Button(window, text="→ Celsius", command=fahrenheit_to_celsius)
result_label = tk.Label(window, text="Introduce una temperatura.")

# Añadimos los widgets a la ventana
celsius_label.grid(row=0, column=0)
celsius_entry.grid(row=0, column=1)
to_fahrenheit_button.grid(row=0, column=2)
fahrenheit_label.grid(row=1, column=0)
fahrenheit_entry.grid(row=1, column=1)
to_celsius_button.grid(row=1, column=2)
result_label.grid(row=2, columnspan=3)

# Iniciamos el bucle de eventos
window.mainloop()
