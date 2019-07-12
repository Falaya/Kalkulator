#kalkulator 0.1
#Wyświetlacz na 10 liczb, dodawanie, odejmowanie, mnożenie i dzielenie.

from tkinter import *

class Application(Frame):
    """Ramka od kalkulatora."""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Tworzenie przycisków i wyświetlacza."""
        self.wyswietlacz = Text(self, width = 30, height = 5, wrap = WORD)
        self.secret_txt.grid(row = 1, column = 1, columnspan = 2, sticky = W)
        
        

root = Tk()
root.title("Kalkulator")
root.geometry("800x600")

root.mainloop()
