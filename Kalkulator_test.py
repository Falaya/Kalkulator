#kalkulator -0.1
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
        #Oddzielenie nazwy kalkulatora od górnej krawędzi okna głównego
        self.przerwa1 = Label(self,font=("Courier", 2) )
        self.przerwa1.grid(row = 0, column = 0, sticky = W)

        #Model kalulatora
        self.nazwa = Label(self, text = "STANIO 7260",font=("Courier", 18) )
        self.nazwa.grid(row = 1, column = 0, sticky = W)
        
        #Oddzielenie nazwy kalkulatora od górnej krawędzi wyświetlacza
        self.przerwa2 = Label(self,font=("Courier", 4) )
        self.przerwa2.grid(row = 2, column = 0, sticky = W)

        #Wyświetlacz
        self.wyswietlacz = Text(self, width = 11, height = 1, wrap = W, font=("Courier", 50))
        self.wyswietlacz.grid(row = 3, column = 0, columnspan = 2, rowspan = 2, sticky = W)

        #Oddzielenie górnej krawędzi wyświetlacza od przycisków
        self.przerwa2 = Label(self,font=("Courier", 4) )
        self.przerwa2.grid(row = 5, column = 0, sticky = W)

        #Przycisk C - czyszczenie wszystkiego

        #Przycisk <- - usuwanie ostatniego znaku

        #Przycisk 1 - wprowadzenie liczby 1

        #Przycisk 2 - wprowadzenie liczby 2
       
        #Przycisk 3 - wprowadzenie liczby 3

        #Przycisk 4 - wprowadzenie liczby 4

        #Przycisk 5 - wprowadzenie liczby 5

        #Przycisk 6 - wprowadzenie liczby 6

        #Przycisk 7 - wprowadzenie liczby 7

        #Przycisk 8 - wprowadzenie liczby 8

        #Przycisk 9 - wprowadzenie liczby 9

        #Przycisk 0 - wprowadzenie liczby 0

        #Przycisk +/- - zmiana znaku liczby w wyświetlaczu
        
        #Przycisk + - dodawanie

        #Przycisk - - odejmowanie

        #Przycisk * - mnożenie

        #Przycisk / - dzielenie

        #Przycisk . - stawianie kropki

        #Przycisk = - wykonanie operacji

        #Przycisk ( - wstawienie lewego nawiasu

        #Przycisk ) - wstawienie prawego nawiasu

        
root = Tk()
root.title("Kalkulator")
root.geometry("440x600")

app = Application(root)

root.mainloop()
