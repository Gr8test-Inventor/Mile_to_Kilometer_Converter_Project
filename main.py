from tkinter import *

KILOMETER_CONVERSION = 1.60934
def m_to_km_converter():
    # print("I got clicked")
    miles_to_km = round(float(miles_entry.get()) * KILOMETER_CONVERSION, 2)
    value_Km_label.config(text= miles_to_km)


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width= 100, height= 100)
window.config(padx= 40, pady= 20)

# Button
calculate_button = Button(text="Calculate", command= m_to_km_converter)
calculate_button.grid(column= 1, row= 2)
calculate_button.config(padx= 10, pady= 10)

# Entry
miles_entry = Entry(width= 10)
miles_entry.insert(END, string="0")
miles_entry.grid(column= 1, row= 0)



# Labels
text_label = Label(text= "is equal to",)
text_label.grid(column= 0, row= 1)
text_label.config(padx=10, pady= 15)

miles_label = Label(text= "Miles",)
miles_label.grid(column= 2, row= 0)
miles_label.config(padx=10, pady= 10)

Km_label = Label(text= "Km",)
Km_label.grid(column= 2, row= 1)
Km_label.config(padx=10, pady= 20)


value_Km_label = Label(text= "0",)
value_Km_label.grid(column= 1, row= 1)

window.mainloop()