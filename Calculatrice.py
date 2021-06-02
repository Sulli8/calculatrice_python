from tkinter import *


window = Tk()
window.title("Mon application")
# Définir un icone :
window.iconbitmap("logo.ico")
# Personnaliser la couleur de l'arrière-plan de la fenêtre principale :
window.config(bg = "purple")
window.geometry("300x680")
v = StringVar()
listeCalculNombre = []
listeTypeCalcul = []
listeSomme = []

def buttonEvent0():
    listeCalculNombre.append(0)
    v.set(0)
def buttonEvent1():
    listeCalculNombre.append(1)
    v.set(1)
def buttonEvent2():
    listeCalculNombre.append(2)
    v.set(2)
def buttonEvent3():
    listeCalculNombre.append(3)
    v.set(3)
def buttonEvent4():
    listeCalculNombre.append(4)
    v.set(4)
def buttonEvent5():
    listeCalculNombre.append(5)
    v.set(5)
def buttonEvent6():
    listeCalculNombre.append(6)
    v.set(6)
def buttonEvent7():
    listeCalculNombre.append(7)
    v.set(7)
def buttonEvent8():
    listeCalculNombre.append(8)
    v.set(8)



def buttonEventPlus():
    listeTypeCalcul.append("+")
def buttonEventMultipli():
    listeTypeCalcul.append("*")
def buttonEventSoustrait():
    listeTypeCalcul.append("-")
def buttonEventEfface():
    listeCalculNombre.clear()
    listeTypeCalcul.clear()
    somme = 0
    print(listeCalculNombre)
    print(listeTypeCalcul)
    print('Effacé')
def buttonEventDestroy():
    window.destroy()
    
def buttonEventResult():
    somme = listeCalculNombre[0]
    if(listeTypeCalcul[len(listeTypeCalcul)-1] == "-"):
        somme = somme - listeCalculNombre[len(listeCalculNombre)-1]
    if(listeTypeCalcul[len(listeTypeCalcul)-1] == "+"):
        somme = somme  + listeCalculNombre[len(listeCalculNombre)-1]
    if(listeTypeCalcul[len(listeTypeCalcul)-1] == "*"):
        somme = somme * listeCalculNombre[len(listeCalculNombre)-1]
    print("Somme : ",somme)
    listeCalculNombre[0] = somme
    v.set(somme)
 
bouton = Button(window,text= 0,width=5,height=5,padx=10,pady=10,activebackground="yellow",command=buttonEvent0)
bouton.grid(row =1,column=0,pady=10,padx=10)

bouton = Button(window,text= 1,width=5,height=5,padx=10,pady=10,activebackground="yellow",command=buttonEvent1)
bouton.grid(row =1,column=1,pady=10,padx=10)

bouton = Button(window,text= 2,width=5,height=5,padx=10,pady=10,activebackground="yellow",command=buttonEvent2)
bouton.grid(row =1,column=2,pady=10,padx=10)


bouton = Button(window,text= 3,width=5,height=5,padx=10,pady=10,activebackground="yellow",command=buttonEvent3)
bouton.grid(row =2,column=0,pady=10,padx=10)


bouton = Button(window,text= 4,width=5,height=5,padx=10,pady=10,activebackground="yellow",command=buttonEvent4)
bouton.grid(row =2,column=1,pady=10,padx=10)


bouton = Button(window,text= 5,width=5,height=5,padx=10,pady=10,activebackground="yellow",command=buttonEvent5)
bouton.grid(row =2,column=2,pady=10,padx=10)

bouton = Button(window,text= 6,width=5,height=5,padx=10,pady=10,activebackground="yellow",command=buttonEvent6)
bouton.grid(row =3,column=0,pady=10,padx=10)

bouton = Button(window,text= 7,width=5,height=5,padx=10,pady=10,activebackground="yellow",command=buttonEvent7)
bouton.grid(row =3,column=1,pady=10,padx=10)

bouton = Button(window,text= 8,width=5,height=5,padx=10,pady=10,activebackground="yellow",command=buttonEvent8)
bouton.grid(row =3,column=2,pady=10,padx=10)


bouton = Button(window,text= "+",width=5,height=5,padx=10,pady=10,activebackground="yellow",command=buttonEventPlus)
bouton.grid(row =4,column=0,pady=10,padx=10)

bouton = Button(window,text= "-",width=5,height=5,padx=10,pady=10,activebackground="yellow",command=buttonEventSoustrait)
bouton.grid(row =4,column=1,pady=10,padx=10)

bouton = Button(window,text= "*",width=5,height=5,padx=10,pady=10,activebackground="yellow",command=buttonEventMultipli)
bouton.grid(row =4,column=2,pady=10,padx=10)

bouton = Button(window,text= "Q",bg='#A877BA',width=5,height=5,padx=10,pady=10,activebackground="yellow",command=buttonEventDestroy)
bouton.grid(row =5,column=0,pady=10,padx=10)


bouton = Button(window,text= "=",bg='#A877BA',width=5,height=5,padx=10,pady=10,activebackground="yellow",command=buttonEventResult)
bouton.grid(row =5,column=1,pady=10,padx=10)

bouton = Button(window,text= "C",bg='#A877BA',width=5,height=5,padx=10,pady=10,activebackground="red",command=buttonEventEfface)
bouton.grid(row =5,column=2,pady=10,padx=10)



nombre = Entry(window,width=5,textvariable=v)
nombre.focus_set()
nombre.grid(row = 0,column = 1,padx=10,pady=10)



window.mainloop()
