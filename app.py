from tkinter import * 
from tkinter import messagebox

class App(Tk):
    def __init__(self):
        super().__init__()
        self.page()
    
    def page(self):

        self.data = {'A':'😀','B':'😃','C':'😄','D':'😁','E':"😆",'F':"😅",
        'G':'😂','H':'🤣','I':'😊','J':'😇','K':'🙂',
        'L':'🙃','M':'😉','N':'😌','O':'😍','P':'😘',
        'Q':'😗','R':'😙','S':'😚','T':'😋','U':'😛',
        'V':'😝','W':'😜','X':'🤪','Y':'🤨','Z':'🧐',
        'a':'🤓','b':'😎','c':'🤩','d':'😏','e':"😒",'f':"😞",
        'g':'😡','h':'🤬','i':'🤯','j':'😳','k':'😱',
        'l':'😨','m':'😰','n':'😥','o':'😓','p':'🤗',
        'q':'🤔','r':'🤭','s':'🤫','t':'😶','u':'💩',
        'v':'👻','w':'💀','x':'🎩','y':'👽','z':'👾',
        '1':'😽','2':'😺','3':'😸','4':'😹','5':"😻",'6':"😼",
        '7':'🎃','8':'🤡','9':'🖕','0':'👈'," ":" ",'':'',"?":'👌',"'":"🕶",
        ',':'👑','.':'👙'
        }

        self.geometry('700x400')
        self.configure(bg = 'cyan')
        self.title("အလုပ်မရှိတဲ့ အတွဲတွေအတွက်....")
        Label(self , text = 'အလုပ်မရှိတဲ့ အတွဲတွေအတွက်....' , 
              font =('Comic Sans Ms',19 , 'bold'),bg = 'cyan').pack()

        self.ent_var = StringVar()
        self.ent     = Entry(self , textvariable=self.ent_var , font=('Comic Sans Ms',18))
        self.ent.place(x = 200 , y=50)

        self.btn = Button(self , text = 'Txt_to_Emoji' , font = ('Helvetica' , 10) 
                          , padx=10 ,command = self.text_to_emoji )
        self.btn.place(x = 200 , y = 100)

        self.btn1 = Button(self , text = 'Emoji_to_Txt' , font = ('Helvetica' , 10) 
                          , padx=10 ,command = self.emoji_to_text )
        self.btn1.place(x = 400 , y = 100)
        
        self.F   = Frame(self)
        self.F.place(x = 150 , y = 150)

        self.bar = Scrollbar(self.F)
        self.bar.pack(side = RIGHT , fill = Y)

        self.txt_area = Text(self.F , height= 10 , width = 50 ,
                         font =('Helvetica') ,yscrollcommand=self.bar.set)
        
        self.txt_area.pack()
        self.bar.config(command = self.txt_area.yview)
        
    def text_to_emoji(self):
        try:
            self.txt_area.delete('1.0',END)
            self.txt_area.insert(INSERT,'Wait few seconds.....')
            
            txt = self.ent_var.get()
            m   = [self.data.get(i) for i in txt]
            self.txt_area.delete('1.0',END)
            self.txt_area.insert(INSERT,"".join(i for i in m))
            self.update_idletasks()
        except:
            messagebox.showerror('ERROR','Somthing Is Wrong\n Please check again')

    def emoji_to_text(self):
        try:
            self.txt_area.delete('1.0',END)
            txt = self.ent_var.get()
            m   = [list(self.data.keys())[list(self.data.values()).index(i)]for i in txt]
            # print("".join(i for i in m))
            self.txt_area.insert(INSERT , "".join(i for i in m))
        except:
            messagebox.showerror('Error','Somthing is wrong\n Please Check again')
       
    
if __name__ == "__main__":
    app = App()
    app.mainloop()