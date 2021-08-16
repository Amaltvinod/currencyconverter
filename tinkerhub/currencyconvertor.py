from tkinter import *
from PIL import Image,ImageTk
import requests

window = Tk()
window.title("CurrencyConverter")
window.geometry("%dx%d+0+0" % (window.winfo_screenwidth(), window.winfo_screenheight()))


img = ImageTk.PhotoImage(Image.open("images.png"))
label = Label(window,image=img)
label.image = img
label.place(x=200,y=0)

convert_button = Button(window,text="CONVERT",fg="white",bg="grey",font=('Sans-serif',10,'bold'),borderwidth=2)
convert_button.place(x=550,y=180)

options = [
            "US Dollar (USD)",
            "Indian Rupee (RUP)",
            "Euro (EUR)",
            "Japanese Yen (JPY)",
            "Canadian Dollar (CAD)",
            "Australian Dollar(AUD)",
            "Chinese Renminbi (CNH)",
            "New Zealand Dollar(NZD)",
            "Swiss Franc (CHF)",
            "Swedish Krona(SEK)"
        ]

label1 = Label(window,text = "Amount : ").place(x=250,y=180)
amount = Entry(window,borderwidth=5)
amount.place(x=400,y=180)

label2 = Label(window,text = "Convert From : ").place(x=250,y=220)
clicked1 = StringVar()
clicked1.set("US Dollar (USD)")
dropfrom = OptionMenu(window,clicked1,*options)
dropfrom.pack()
dropfrom.place(x=400,y=215)

label3 = Label(window,text = "Convert To : ").place(x=250,y=270)
clicked2 = StringVar()
clicked2.set("Indian Rupee (RUP)")
dropto = OptionMenu(window,clicked2,*options)
dropto.pack()
dropto.place(x=400,y=265)

label4 = Label(window,text = "Converted Amount : ").place(x=250,y=315)
amount = Entry(window,borderwidth=5)
amount.place(x=400,y=317)


window.mainloop()
