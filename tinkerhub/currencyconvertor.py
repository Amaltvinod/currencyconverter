from tkinter import *
from PIL import Image,ImageTk
import requests

window = Tk()
window.title("CurrencyConverter")
window.geometry("%dx%d+0+0" % (window.winfo_screenwidth(), window.winfo_screenheight()))
window.iconbitmap("icon.ico")
window.configure(bg="#FFFFFF")


img = ImageTk.PhotoImage(Image.open("images.png"))
label = Label(window,image=img)
label.image = img
label.place(x=200,y=0)

img2 = Image.open("convert_buttonb.jpeg")
resized=img2.resize((140,30),Image.ANTIALIAS)
new_image=ImageTk.PhotoImage(resized)


def conversion():
    amount1.delete(0,END)
    r=requests.get('https://api.exchangerate-api.com/v4/latest/USD')

    re=r.json()
    record=re['rates']
    currency_from=clicked1.get()    
    currency_to=clicked2.get()
  
    value=float(amount.get());
    if(currency_from!='USD'):
        value=(value / record[currency_from])

    value=(round(value* record[currency_to],4))
    amount1.insert(0,str(value))
    
convert_button =Button(window,image=new_image,borderwidth=0,command=conversion)
convert_button.place(x=550,y=176)
options = [
            "USD",
            "INR",
            "EUR",
            "JPY",
            "CAD",
            "AUD",
            "YER",
            "NZD",
            "CHF",
            "SEK"
        ]

label1 = Label(window,text = "Amount : ",bg="#FFFFFF").place(x=250,y=180)

amount = Entry(window,borderwidth=5)
amount.place(x=400,y=180)


label2 = Label(window,text = "Convert From : ",bg="#FFFFFF").place(x=250,y=220)

clicked1 = StringVar()
clicked1.set("USD")

dropfrom = OptionMenu(window,clicked1,*options,)
dropfrom.pack()
dropfrom.place(x=400,y=215)


label3 = Label(window,text = "Convert To : ",bg="#FFFFFF").place(x=250,y=270)
clicked2 = StringVar()
clicked2.set("INR")

dropto = OptionMenu(window,clicked2,*options)
dropto.pack()
dropto.place(x=400,y=265)


label4 = Label(window,text = "Converted Amount : ",bg="#FFFFFF").place(x=250,y=315)
amount1 = Entry(window,borderwidth=5)
amount1.place(x=400,y=317)

def clear_text():
    amount.delete(0,END)
    amount1.delete(0,END)
clrButton=Button(window,text="Clear", command=clear_text).place(x=450,y=350)





window.mainloop()
