from tkinter import *
from tkinter import messagebox
from tkinter import Tk, Label, StringVar,Toplevel

ventana_principal = Tk()

j=0

def calcular():
    for k in range(int(b.get())):
        
        for i in range(int(a.get())):
            c.create_rectangle(70+(80*i), 70+(50*k), 150+(80*i),120+(50*k), fill="green",outline="black")
            c.create_text(70+(80*i),70+(50*k),text="d")
            
            

        

        

a = StringVar()
b = StringVar()    
# titulo de la ventana
ventana_principal.title("Funciones")

# tamañan de la ventana
ventana_principal.geometry("600x800")

# deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

# color de fondo de la ventana
ventana_principal.config(bg= "black")
lb_a = Label(ventana_principal, text = "Parcial ")
lb_a.config(bg="black", fg="white", font=("Arial",20))
lb_a.place(x=20, y=60, width=115, height=30)

lb_a = Label(ventana_principal, text = "digite el numero de filas de la matriz: ")
lb_a.config(bg="black", fg="white", font=("Arial",16))
lb_a.place(x=35, y=120, width=350, height=60)

lb_x = Label(ventana_principal, text = "digite el numero de columnas:")
lb_x.config(bg="black", fg="white", font=("Arial",16))
lb_x.place(x=5, y=180, width=340, height=60)

entry_a = Entry(ventana_principal, textvariable=a)
entry_a.config(font=("Arial",20), justify=LEFT, fg="black")
entry_a.focus_set()
entry_a.place(x=390,y=130,width=115, height=30)

entry_b = Entry(ventana_principal, textvariable=b)
entry_b.config(font=("Arial",20), justify=LEFT, fg="black")
entry_b.focus_set()
entry_b.place(x=370,y=190,width=115, height=30)

bt_cuadratica = Button(ventana_principal, text="Calcular", command=calcular)
bt_cuadratica.place(x=80,y=250, width=100, height=30)

frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="purple", width=580, height=480)
frame_operaciones.place(x=10,y=300)


#creacion canvas
c = Canvas(ventana_principal, width=565, height=465)
c.place(x=15, y=305)


ventana_principal.mainloop()
