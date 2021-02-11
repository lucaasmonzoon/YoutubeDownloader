import tkinter as tk
from tkinter import tix
from pytube import YouTube

def show_entry_fields():
     print("URL ES %s" % (celda.get()))


def opciones():
    
    global ventana2
    ventana2=tk.Tk()
    calidad1=tk.Button(ventana2,text="360p", command=descargar_video360, width=0, height= 1)
    calidad2=tk.Button(ventana2,text="720p", command=descargar_video720, width=0, height= 1)
    calidad1.pack()
    calidad2.pack()
    
    ventana2.mainloop()


def descargar_video360():


    video=YouTube(celda.get())
    video.streams.get_by_resolution("360p").download()
    ventana.destroy()
    ventana2.destroy()
    

def descargar_video720():

    video=YouTube(celda.get())
    video.streams.get_by_resolution("720p").download()
    ventana.destroy()
    ventana2.destroy()
    
    

    
        


    

ventana = tk.Tk()

bienvenida = tk.Label(
    text="YOUTUBE DOWNLOADER",
    fg = "white",
    bg = "black",
    width = 40,
    height=2,
    
    )

mensaje1 = tk.Label(
    text= "Ingrese su URL debajo",
    fg="white",
    bg="black",
    width = 40,
    height=5,)

bienvenida.pack()
mensaje1.pack()


celda = tk.Entry(ventana, width = 40)
celda.pack()
boton1=tk.Button(ventana,text="DESCARGAR", command=opciones, width= 0, height= 1) 
boton1.pack()
          







ventana.mainloop()