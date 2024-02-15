"""...."""
import sys
sys.path.append('./../')
import customtkinter as ctk
from  models.back import opratetion
import math
 
# Sets the appearance mode of the application
# "System" sets the appearance same as that of the system
ctk.set_appearance_mode("Dark")        
 
# Sets the color of the widgets
# Supported themes: green, dark-blue, blue
ctk.set_default_color_theme("blue")    
 
# Create App class
class App(ctk.CTk):
    op = opratetion()
    dis = ''
    
# Layout of the GUI will be written in the init itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
# Sets the title of our window to "App"
        self.title("Calclator")    
# Dimensions of the window will be 200x200
        self.geometry("300x450")
        #dispay_bourd
        self.displayBox = ctk.CTkTextbox(self, width=300, height=80, font=('Arial', 24))
        self.displayBox.grid(row=2, column=0, columnspan=5, padx=5, pady=10, sticky="nsew")
        # buttons
        self.b1 = ctk.CTkButton(self, text="1",width=50, height=50, font=('Arial', 15),command=lambda: self.updatescrean('1'))
        self.b1.grid(row=5, column=0, padx=0, pady=10)
        self.b2 = ctk.CTkButton(self, text="2",width=50, height=50, font=('Arial', 15), command= lambda:self.updatescrean('2'))
        self.b2.grid(row=5, column=1, padx=0, pady=10)
        self.b3 = ctk.CTkButton(self, text="3",width=50, height=50, font=('Arial', 15), command=lambda: self.updatescrean('3'))
        self.b3.grid(row=5, column=2, padx=0, pady=10)
        self.b4 = ctk.CTkButton(self, text="4",width=50, height=50, font=('Arial', 15), command=lambda: self.updatescrean('4'))
        self.b4.grid(row=6, column=0, padx=0, pady=10)
        self.b5 = ctk.CTkButton(self, text="5",width=50, height=50, font=('Arial', 15), command=lambda: self.updatescrean('5'))
        self.b5.grid(row=6, column=1, padx=0, pady=10)
        self.b6 = ctk.CTkButton(self, text="6",width=50, height=50, font=('Arial', 15), command=lambda: self.updatescrean('6'))
        self.b6.grid(row=6, column=2, padx=0, pady=10)
        self.b7 = ctk.CTkButton(self, text="7",width=50, height=50, font=('Arial', 15), command=lambda: self.updatescrean('7'))
        self.b7.grid(row=7, column=0, padx=0, pady=10)
        self.b8 = ctk.CTkButton(self, text="8",width=50, height=50, font=('Arial', 15), command=lambda: self.updatescrean('8'))
        self.b8.grid(row=7, column=1, padx=0, pady=10)
        self.b9 = ctk.CTkButton(self, text="9",width=50, height=50, font=('Arial', 15), command=lambda: self.updatescrean('9'))
        self.b9.grid(row=7, column=2, padx=0, pady=10)
        self.open = ctk.CTkButton(self, text="(",width=50, height=50, font=('Arial', 15), command=lambda: self.updatescrean('('))
        self.open.grid(row=8, column=0, padx=0, pady=10)
        self.b0 = ctk.CTkButton(self, text="0",width=50, height=50, font=('Arial', 15), command=lambda: self.updatescrean('0'))
        self.b0.grid(row=8, column=1, padx=0, pady=10)
        self.close = ctk.CTkButton(self, text=")",width=50, height=50, font=('Arial', 15), command=lambda: self.updatescrean(')'))
        self.close.grid(row=8, column=2, padx=0, pady=10)
        self.equle = ctk.CTkButton(self, text="=",width=50, height=50, font=('Arial', 15), command=lambda: self.display_res())
        self.equle.grid(row=9, column=0, padx=0, pady=10)
        self.plus = ctk.CTkButton(self, text="+",width=50, height=50, font=('Arial', 15), command=lambda: self.updatescrean('+'))
        self.plus.grid(row=7, column=3, padx=0, pady=10)
        self.mainuss = ctk.CTkButton(self, text="-",width=50, height=50, font=('Arial', 15), command=lambda: self.updatescrean('-'))
        self.mainuss.grid(row=8, column=3, padx=0, pady=10)
        self.dvide = ctk.CTkButton(self, text="/",width=50, height=50, font=('Arial', 15), command=lambda: self.updatescrean('/'))
        self.dvide.grid(row=9, column=1, padx=0, pady=10)
        self.mult = ctk.CTkButton(self, text="*",width=50, height=50, font=('Arial', 15), command=lambda: self.updatescrean('*'))
        self.mult.grid(row=9, column=2, padx=0, pady=10)
        self.pwer = ctk.CTkButton(self, text="^",width=50, height=50, font=('Arial', 15), command=lambda: self.updatescrean('**'))
        self.pwer.grid(row=9, column=3, padx=0, pady=10)
        self._pop = ctk.CTkButton(self, text="D",width=50, height=50, font=('Arial', 15), command=lambda: self.remove())
        self._pop.grid(row=5, column=3, padx=0, pady=10)
        self.cansel = ctk.CTkButton(self, text="C",width=50, height=50, font=('Arial', 15), command=lambda: self.clear())
        self.cansel.grid(row=6, column=3, padx=0, pady=10)
        

    def updatescrean(self,_input):
        if self.op.op == 'Error':
            self.op.op = ''
            self.dis = ''

        if _input == '**':
            self.dis = self.dis + '^'
        elif _input == '':
            return
        else:
            self.dis = self.dis + _input
        self.op.op += _input
        self.displayBox.delete(1.0, 'end')
        self.displayBox.insert(1.0, self.dis)
        
    def clear(self):
        self.dis = ''
        self.op.delet_all()
        self.displayBox.delete(1.0, 'end')
        self.displayBox.insert(1.0, self.dis)

    def remove(self):
        if self.dis != '':
            if self.op.op != 'Error':
                self.dis = self.dis[:-1]
                self.op.pop_last()
            else:
                self.clear()
    
        self.displayBox.delete(1.0, 'end')
        self.displayBox.insert(1.0, self.dis)

             
    def display_res(self):
        print('the dispay work')
        self.displayBox.delete(1.0, 'end')
        self.displayBox.insert(1.0, self.op.evalution())
        self.op.op = self.op.evalution()
        self.dis = self.op.op
