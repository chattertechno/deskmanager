from tkinter import *

app = Tk()
# PART 1
part_text = StringVar()
part_label = Label(app, text='Part name', font=('bold', 14), pady=20)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

# Customer
customer_text = StringVar()
customer_label = Label(app, text='Customer', font=('bold', 14))
customer_label.grid(row=0, column=2, sticky=W)
customer_entry = Entry(app, textvariable=part_text)
customer_entry.grid(row=0, column=3)

# PART 3
retailer_text = StringVar()
retailer_label = Label(app, text='Retailer', font=('bold', 14))
retailer_label.grid(row=1, column=0, sticky=W)
retailer_entry = Entry(app, textvariable=part_text)
retailer_entry.grid(row=1, column=1)

# PART 4
price_text = StringVar()
price_label = Label(app, text='Price', font=('bold', 14))
price_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(app, textvariable=part_text)
price_entry.grid(row=1, column=3)


app.title('Desk manager')
app.geometry('700x350')

app.mainloop()