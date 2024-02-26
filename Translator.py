from tkinter import*
from tkinter import ttk,messagebox
import tkinter as tk 
import googletrans
from googletrans import Translator 
from PIL import Image,ImageTk


root=Tk()
root.title('Translator')
root.geometry('1000x400')#translator logo
img= Image.open('D:/Python/1.png')
photo = ImageTk.PhotoImage(img)
root.iconphoto(True , photo)

def label_change():
   c=combo1.get()
   c1=combo2.get()
   label1.configure(text=c)
   label2.configure(text=c1)
   root.after(1000,label_change)

def translate_now():
   text_=text1.get(1.0,END)
   t1=Translator()
   trans_text=t1.translate(text_,src=combo1.get(),des=combo2.get())
   trans_text=trans_text.text
   text2.delete(1.0,END)
   text2.insert(END,trans_text)




#list of languages 
language= googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()

#first combo with grid
combo1=ttk.Combobox(root,values=languageV,font='TimesNewRoman 14',state='r')
combo1.grid(row = 0, column = 0, padx = 25,pady=25,)
combo1.set('English')
label1=Label(root,text='ENGLISH',font='TimesNewRoman 30 bold',bg='white',width=12,bd=5,relief=GROOVE)
label1.place(x=5,y=50)



#first frame and text inside 
F =Frame(root,bg="Black")
F.place(height=210, width=250, x=20, y=120)
F.config(bg="Black")
text1=Text(F,font='TimesNewRoman 20',bg='white',relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=250,height=210)

#fisrt scollbar 
scrollbar1=Scrollbar(F)
scrollbar1.pack(side='right',fill='y')
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#seconf combo 
combo2=ttk.Combobox(root,values=languageV,font='TimesNewRoman 14',state='r')
combo2.grid(row = 0, column = 1, padx = 300, pady=25)
combo2.set('Select')

label2=Label(root,text='ENGLISH',font='TimesNewRoman 30 bold',bg='white',width=12,bd=5,relief=GROOVE)
label2.place(x=560,y=50)

#second frame with text inside 
F1 =Frame(root,bg="Black")
F1.place(height=210, width=250, x=590, y=120)
F1.config(bg="Black")
text2=Text(F1,font='TimesNewRoman 20',bg='white',relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=250,height=210)
scrollbar2=Scrollbar(F1)
scrollbar2.pack(side='right',fill='y')
scrollbar2.configure(command=text2.yview)
text1.configure(yscrollcommand=scrollbar2.set)
#translate_button
translate=Button(root,text='Translate',font='TimesNewRoman 20',activebackground='white',cursor='hand2',bd=1,width=10,height=2,bg='black',fg='white',command=translate_now)
translate.place(x=350,y=250)

label_change()
root.configure(bg='white')
root.mainloop()
