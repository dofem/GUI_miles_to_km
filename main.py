from tkinter import *


def miles_to_km():
    value = float(miles_input.get())
    result = (value * 1.609)
    print(result)
    km_result.config(text=f"{result}")


window = Tk()
window.title("miles to km converter")
window.config(padx=20, pady=20)

equal_label = Label(text="is equal to", font=("Arial", 10, "bold"))
equal_label.grid(column=0, row=1)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

km_label = Label(text="km", font=("Arial", 8, "bold"))
km_label.grid(column=2, row=1)


km_result = Label(text=0)
km_result.grid(column=1, row=1)

miles_label = Label(text="miles", font=("Arial", 10, "bold"))
miles_label.grid(column=2, row=0)


button = Button(text="calculate", width=10, command=miles_to_km)
button.grid(column=1, row=2)


window.mainloop()