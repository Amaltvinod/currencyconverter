from tkinter import *
from PIL import Image,ImageTk

window = Tk()
window.title("CurrencyConverter")
window.geometry("700x700")


photo = Image.open("currency.jpg")
img = ImageTk.PhotoImage(photo)
label = Label(window,image=img)
label.image = img
label.place(x=200,y=0)


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

label1 = Label(window,text = "Amount : ").place(x=130,y=180)
amount = Entry(window)
amount.place(x=230,y=180)

label2 = Label(window,text = "Convert From : ").place(x=130,y=220)
clicked1 = StringVar()
clicked1.set("US Dollar (USD)")
dropfrom = OptionMenu(window,clicked1,*options)
dropfrom.pack()
dropfrom.place(x=230,y=215)

label3 = Label(window,text = "Convert To : ").place(x=130,y=270)
clicked2 = StringVar()
clicked2.set("Indian Rupee (RUP)")
dropto = OptionMenu(window,clicked2,*options)
dropto.pack()
dropto.place(x=230,y=265)

label4 = Label(window,text = "Converted Amount : ").place(x=130,y=315)
amount = Entry(window)
amount.place(x=240,y=317)


window.mainloop()
