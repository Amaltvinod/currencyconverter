from tkinter import *
from tkinter import messagebox
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


img1 = ImageTk.PhotoImage(Image.open("info1.jpg").resize((20,20),Image.ANTIALIAS))


def info():
    messagebox.showinfo('For Reference','USD-US DOLLAR\nINR-Indian Rupee\nEUR-Euro\nJPY-Japanese yen\nCAD-Canadian dollar\nAUD-Australian dollar\nYER-Yemeni rial\nNZD-New Zealand dollar\nCHF-Swiss franc\nSEK-Swedish krona' )

info_button = Button(window,image = img1,borderwidth = 0,command = info)
info_button.place(x=550,y=220)

def conversion():
    amount1.configure(state='normal')
    amount1.delete(0,END)
   
    try:
        r=requests.get('https://api.exchangerate-api.com/v4/latest/USD',timeout=10)
        re=r.json()
        record=re['rates']
        if(amount.get() == '0' or amount.get() == ''):
            messagebox.showerror('INVALID INPUT','Amount not passed' )
        currency_from=clicked1.get()
        currency_to=clicked2.get()
        if(len(amount.get())>0):
            value=float(amount.get())
            if(currency_from!='USD'):
                value=(value / record[currency_from])
            a = StringVar
            if(currency_to == 'USD'):
                a = '$'
            
            elif(currency_to == 'INR'):
                a = '₹'
           
            elif(currency_to == 'EUR'):
                a = '€'
          
            elif(currency_to == 'JPY'):
                a = '¥'
       
            elif(currency_to == 'CAD'):
                a = '$'
          
            elif(currency_to == 'AUD'):
                a = '$'
              
            elif(currency_to == 'YER'):
                a = '﷼'
           
            elif(currency_to == 'NZD'):
                a = '$'
           
            elif(currency_to == 'CUP'):
                a = '₱'
              
            else:
                a = '₩'
         
            value=(round(value* record[currency_to],4))
            value= '{:,}'.format(value)
            amount1.insert(0,"{} ".format(a) + ' '+ str(value))  
        
    except requests.exceptions.ConnectTimeout:
        messagebox.showerror('CONNECTION ERROR','No Internet Connection')
    except requests.exceptions.ConnectionError:
        messagebox.showerror('CONNECTION ERROR','No Internet Connection')

    except requests.exceptions.HTTPError:
        messagebox.showerror('CONNECTION ERROR','No Internet Connection')
    finally:
        amount1.configure(state='readonly')
        
        
        
           
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
            "CUP",
            "KRW"
            ]

label1 = Label(window,text = "Amount : ",bg="#FFFFFF").place(x=250,y=180)

amount = Entry(window,borderwidth=5)
amount.place(x=400,y=180)


label2 = Label(window,text = "Convert From : ",bg="#FFFFFF").place(x=250,y=220)

clicked1 = StringVar()
clicked1.set("USD")

dropfrom = OptionMenu(window,clicked1,*options,)
dropfrom.config(width = 14)
dropfrom.pack()
dropfrom.place(x=400,y=215)


label3 = Label(window,text = "Convert To : ",bg="#FFFFFF").place(x=250,y=270)
clicked2 = StringVar()
clicked2.set("INR")

dropto = OptionMenu(window,clicked2,*options)
dropto.config(width = 14)
dropto.pack()
dropto.place(x=400,y=265)


label4 = Label(window,text = "Converted Amount : ",bg="#FFFFFF").place(x=250,y=315)
amount1 = Entry(window,borderwidth=5,state='readonly')
amount1.place(x=400,y=317)

def clear_text():
    amount.delete(0,END)
    amount1.configure(state='normal')
    amount1.delete(0,END)
    amount1.configure(state='readonly')
    
clrButton=Button(window,text="Clear", command=clear_text).place(x=450,y=350)





window.mainloop()

