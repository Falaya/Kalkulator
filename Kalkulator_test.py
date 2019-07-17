#kalkulator 1.7
#Wyświetlacz na 10 liczb, dodawanie, odejmowanie, mnożenie i dzielenie.
#Po wprowadzeniu znaku innego niż liczba kalkulator przechowuje liczbę w pamięci i zeruje wyświetlacz

from tkinter import *

class Application(Frame):
    """Ramka od kalkulatora."""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.znak = ""
        self.liczby = []

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
        self.wyswietlacz.grid(row = 3, column = 0, columnspan = 20, rowspan = 2, sticky = W)

        #Oddzielenie górnej krawędzi wyświetlacza od przycisków
        self.przerwa2 = Label(self,font=("Courier", 4) )
        self.przerwa2.grid(row = 5, column = 0, sticky = W)
        
        #Przycisk () - wstawienie obu nawiasów
        self.przycisk_nawiasy = Button(self, text = "( )", command = "Wstaw nawiasy")
        self.przycisk_nawiasy.grid(row = 6, column = 0, sticky = W)

        #Przycisk C - czyszczenie wszystkiego
        self.przycisk_C = Button(self, text = "C", command = self.usuwanie_C)
        self.przycisk_C.grid(row = 6, column = 1, sticky = W)

        #Przycisk <- - usuwanie ostatniego znaku
        self.przycisk_back = Button(self, text = "<--", command = self.usuwanie_back)
        self.przycisk_back.grid(row = 6, column = 2, sticky = W)
        
        #Przycisk / - dzielenie
        self.przycisk_dzielenie = Button(self, text = "/", command = self.dzielenie)
        self.przycisk_dzielenie.grid(row = 6, column = 3, sticky = W)
        
        #Oddzielenie przyciskow
        self.przerwa3 = Label(self,font=("Courier", 4) )
        self.przerwa3.grid(row = 7, column = 0, sticky = W)

        #Przycisk 1 - wprowadzenie liczby 1
        self.przycisk_1 = Button(self, text = "1", command = self.wprowadz_1)
        self.przycisk_1.grid(row = 8, column = 0, sticky = W)

        #Przycisk 2 - wprowadzenie liczby 2
        self.przycisk_2 = Button(self, text = "2", command = self.wprowadz_2)
        self.przycisk_2.grid(row = 8, column = 1, sticky = W)
       
        #Przycisk 3 - wprowadzenie liczby 3
        self.przycisk_3 = Button(self, text = "3", command = self.wprowadz_3)
        self.przycisk_3.grid(row = 8, column = 2, sticky = W)
        
        #Przycisk * - mnożenie
        self.przycisk_mnozenie = Button(self, text = "*", command = self.mnozenie)
        self.przycisk_mnozenie.grid(row = 8, column = 3, sticky = W)
        
        #Oddzielenie przyciskow
        self.przerwa4 = Label(self,font=("Courier", 4) )
        self.przerwa4.grid(row = 9, column = 0, sticky = W)

        #Przycisk 4 - wprowadzenie liczby 4
        self.przycisk_4 = Button(self, text = "4", command = self.wprowadz_4)
        self.przycisk_4.grid(row = 10, column = 0, sticky = W)

        #Przycisk 5 - wprowadzenie liczby 5
        self.przycisk_5 = Button(self, text = "5", command = self.wprowadz_5)
        self.przycisk_5.grid(row = 10, column = 1, sticky = W)

        #Przycisk 6 - wprowadzenie liczby 6
        self.przycisk_6 = Button(self, text = "6", command = self.wprowadz_6)
        self.przycisk_6.grid(row = 10, column = 2, sticky = W)
        
        #Przycisk - - odejmowanie
        self.przycisk_odejmowanie = Button(self, text = "-", command = self.odejmowanie)
        self.przycisk_odejmowanie.grid(row = 10, column = 3, sticky = W)
        
        #Oddzielenie przyciskow
        self.przerwa5 = Label(self,font=("Courier", 4) )
        self.przerwa5.grid(row = 11, column = 0, sticky = W)

        #Przycisk 7 - wprowadzenie liczby 7
        self.przycisk_7 = Button(self, text = "7", command = self.wprowadz_7)
        self.przycisk_7.grid(row = 12, column = 0, sticky = W)

        #Przycisk 8 - wprowadzenie liczby 8
        self.przycisk_8 = Button(self, text = "8", command = self.wprowadz_8)
        self.przycisk_8.grid(row = 12, column = 1, sticky = W)

        #Przycisk 9 - wprowadzenie liczby 9
        self.przycisk_9 = Button(self, text = "9", command = self.wprowadz_9)
        self.przycisk_9.grid(row = 12, column = 2, sticky = W)
        
        #Przycisk + - dodawanie
        self.przycisk_dodawanie = Button(self, text = "+", command = self.dodawanie)
        self.przycisk_dodawanie.grid(row = 12, column = 3, sticky = W)
        
        #Oddzielenie przyciskow
        self.przerwa6 = Label(self,font=("Courier", 4) )
        self.przerwa6.grid(row = 13, column = 0, sticky = W)
        
        #Przycisk +/- - zmiana znaku liczby w wyświetlaczu
        self.przycisk_dodawanie = Button(self, text = "+/-", command = "Wprowadź +/-")
        self.przycisk_dodawanie.grid(row = 14, column = 0, sticky = W)

        #Przycisk 0 - wprowadzenie liczby 0
        self.przycisk_0 = Button(self, text = "0", command = self.wprowadz_0)
        self.przycisk_0.grid(row = 14, column = 1, sticky = W)  

        #Przycisk . - stawianie kropki
        self.przycisk_kropka = Button(self, text = ".", command = self.wprowadz_kropka)
        self.przycisk_kropka.grid(row = 14, column = 2, sticky = W) 

        #Przycisk = - wykonanie operacji
        self.przycisk_rownasie = Button(self, text = "=", command = self.wynik)
        self.przycisk_rownasie.grid(row = 14, column = 3, sticky = W)   
        
    def usuwanie_C(self):
        """Usuwa wszystkie znaki z pamięci kalkulatora"""
        self.znak = ""
        self.liczby = []
        self.wyswietlacz.delete(0.0,END)
        
    def usuwanie_back(self):
        """Usuwa wszystkie znaki z pamięci kalkulatora"""
        dlugosc = len(self.znak) - 1
        self.znak = self.znak[:dlugosc]
        self.wyswietlacz.delete(0.0,END)
        self.wyswietlacz.insert(0.0,self.znak)        
        
    def dzielenie(self):
        """Wprowadź znak dzielenia"""
        self.liczby.append(self.znak)
        self.liczby.append("/")
        self.znak = ""
        self.wyswietlacz.delete(0.0,END)

    def wprowadz_1(self):
        """Wprowadź 1"""
        self.znak += "1"
        self.wyswietlacz.insert(END,1)
    
    def wprowadz_2(self):
        """Wprowadź 2"""
        self.znak += "2"
        self.wyswietlacz.insert(END,2)
        
    def wprowadz_3(self):
        """Wprowadź 3"""
        self.znak += "3"
        self.wyswietlacz.insert(END,3)
        
    def mnozenie(self):
        """Wprowadź znak mnożenia,"""
        self.liczby.append(self.znak)
        self.liczby.append("*")
        self.znak = ""
        self.wyswietlacz.delete(0.0,END)
        
    def wprowadz_4(self):
        """Wprowadź 4"""
        self.znak += "4"
        self.wyswietlacz.insert(END,4)
        
    def wprowadz_5(self):
        """Wprowadź 5"""
        self.znak += "5"
        self.wyswietlacz.insert(END,5)   
        
    def wprowadz_6(self):
        """Wprowadź 6"""
        self.znak += "6"
        self.wyswietlacz.insert(END,6)  
        
    def odejmowanie(self):
        """Wprowadź znak odejmowania"""
        self.liczby.append(self.znak)
        self.liczby.append("-")
        self.znak = ""
        self.wyswietlacz.delete(0.0,END)
        
    def wprowadz_7(self):
        """Wprowadź 7"""
        self.znak += "7"
        self.wyswietlacz.insert(END,7) 
        
    def wprowadz_8(self):
        """Wprowadź 8"""
        self.znak += "8"
        self.wyswietlacz.insert(END,8)  
        
    def wprowadz_9(self):
        """Wprowadź 9"""
        self.znak += "9"
        self.wyswietlacz.insert(END,9)   
        
    def dodawanie(self):
        """Wprowadź znak dodawania"""
        self.liczby.append(self.znak)
        self.liczby.append("+")
        self.znak = ""
        self.wyswietlacz.delete(0.0,END)
        
    def wprowadz_0(self):
        """Wprowadź 0"""
        self.znak += "0"
        self.wyswietlacz.insert(END,0)

    def wprowadz_kropka(self):
        """Wprowadź ."""
        self.znak += "."
        self.wyswietlacz.insert(END,".")        
        
    def wynik(self):
        self.liczby.append(self.znak)
        self.wyswietlacz.delete(0.0,END)
        wynik = 0
        for i in self.liczby:
            if i == "/":
                wynik /= float(self.liczby[self.liczby.index(i)+1])
                if wynik%1 == 0:
                    wynik = int(wynik)
                    self.wyswietlacz.insert(END, wynik)
                else:
                    self.wyswietlacz.insert(END, wynik)
            elif i == "*":
                wynik *= float(self.liczby[self.liczby.index(i)+1])
                if wynik%1 == 0:
                    wynik = int(wynik)
                    self.wyswietlacz.insert(END, wynik)
                else:
                    self.wyswietlacz.insert(END, wynik)

            elif i == "-":
                wynik -= float(self.liczby[self.liczby.index(i)+1])
                if wynik%1 == 0:
                    wynik = int(wynik)
                    self.wyswietlacz.insert(END, wynik)
                else:
                    self.wyswietlacz.insert(END, wynik)

            elif i == "+":
                wynik += float(self.liczby[self.liczby.index(i)+1])
                if wynik%1 == 0:
                    wynik = int(wynik)
                    self.wyswietlacz.insert(END, wynik)
                else:
                    self.wyswietlacz.insert(END, wynik)
 
            else:
                if self.liczby.index(i)== 0:
                    wynik += float(i)

        self.liczby = [wynik] 

root = Tk()
root.title("Kalkulator")
root.geometry("440x600")

app = Application(root)

root.mainloop()
