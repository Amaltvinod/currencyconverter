from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import requests

window = Tk()
window.title("CurrencyConverter")
window.geometry("%dx%d+0+0" % (window.winfo_screenwidth(), window.winfo_screenheight()))
window.iconbitmap("icon.ico")
window.configure(bg="#FFFFFF")


def resize_image(event):
    new_width = event.width
    new_height = event.height
    image5 = copy_of_image.resize((new_width, new_height))
    photo5 = ImageTk.PhotoImage(image5)


image5 = Image.open("window_background1.jpeg")
copy_of_image = image5.copy()
photo5 = ImageTk.PhotoImage(image5)
label4 = ttk.Label(window, image = photo5)
label4.bind('<Configure>', resize_image)
label4.pack(fill=BOTH, expand = YES)

img = ImageTk.PhotoImage(Image.open("title_img.jpg").resize((900,185),Image.ANTIALIAS))
label = Label(window,image=img,borderwidth =0)
label.image = img
label.place(x=200,y=0,)





img1 = ImageTk.PhotoImage(Image.open("info1.jpg").resize((20,20),Image.ANTIALIAS))


def info():
    messagebox.showinfo('For Reference','USD-US Dollar\nINR-Indian Rupee\nEUR-Euro\nJPY-Japanese yen\nCAD-Canadian dollar\nAUD-Australian dollar\nYER-Yemeni rial\nNZD New-Zealand dollar\nCUP-Cuban Peso\nKRW-South Korean Won' )

info_button = Button(window,image = img1,borderwidth = 0,command = info)
info_button.place(x=600,y=225)

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




convert_button =Button(window,text="CONVERT",bg="black",fg="#ffffff",padx=8,pady=3,borderwidth=2,command=conversion)
convert_button.place(x=600,y=175)
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

label1 = Label(window,text = "Amount : ",bg="#0188c4",fg="#ffffff").place(x=250,y=175)

amount = Entry(window,borderwidth=5)
amount.config(width=17)
amount.place(x=400,y=170)


label2 = Label(window,text = "Convert From : ",bg="#0188c4",fg="#FFFFFF").place(x=250,y=220)

clicked1 = StringVar()
clicked1.set("USD")

dropfrom = OptionMenu(window,clicked1,*options,)
dropfrom.config(width = 12)
dropfrom.pack()
dropfrom.place(x=400,y=215)


label3 = Label(window,text = "Convert To : ",bg="#0188c4",fg="#FFFFFF").place(x=250,y=270)
clicked2 = StringVar()
clicked2.set("INR")

dropto = OptionMenu(window,clicked2,*options)
dropto.config(width = 12)
dropto.pack()
dropto.place(x=400,y=265)


label4 = Label(window,text = "Converted Amount : ",bg="#0188c4",fg="#ffffff").place(x=248,y=315)
amount1 = Entry(window,borderwidth=5,state='readonly')
amount1.config(width=17)
amount1.place(x=400,y=311)

def clear_text():
    amount.delete(0,END)
    amount1.configure(state='normal')
    amount1.delete(0,END)
    amount1.configure(state='readonly')
    
clrButton=Button(window,text="CLEAR",bg="black",fg="#ffffff",padx=8,pady=3,borderwidth=2, command=clear_text).place(x=437,y=354)





window.mainloop()

