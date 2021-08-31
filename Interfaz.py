import tkinter as tk
from typing import Text
from tkinter import ttk
def pruebas(entrada):
    if entrada == True:
        print("Entro")
    else:
        print(False)
    
ventana  = tk.Tk()
ventana.title("Parcial Corte 1 ")
ventana.geometry('980x680')
ventana.configure(background = '#151934')

boton = ttk.Button(text = 'Aceptar',command = pruebas(True))
boton.place(x=50,y=50)

boton2 = ttk.Button(text = 'Rechazar',command = pruebas(False))
boton2.place(x=80,y=80)



ventana.mainloop()