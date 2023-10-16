import tkinter                       #   hhttps://recursospython.com/guias-y-manuales/caja-de-texto-entry-tkinter/
from tkinter import ttk

ventana = tkinter.Tk()

ventana.title("Descargas You Tuve")         #   Cambiar el nombre de la ventana
ventana.geometry("700x700")                 #   Configurar tamaño
ventana.resizable(1,1)                      #   para modificar manual mente el tamaño (para no modificarla(0,0)) (para modificarlo(1,1))
ventana.config(bg="#6e6969")                #   Cambiar color de fond el color en inglés o en formato hexadecima


ventana.columnconfigure (0, weight = 1)


# link------------------------------------------------------------------------------------------
txt_link = tkinter.Label(ventana,   text = "Link de Descarga",
                                    bg = "#6e6969",
                                    fg = "black",
                                    font="arial 15 ",)
txt_link.grid(column = 0, row = 1, pady = 5, padx = 5)

link_valor = tkinter.StringVar()

link_i = tkinter.Entry(ventana,     textvariable = link_valor,
                                    width = "75",
                                    font="arial 15 ",)
link_i.grid(column = 0, row = 2, pady = 5, padx = 5, columnspan=3)

def optener_link(boton):
    link = link_valor.get()
    try:
        if link != "":
            if boton == 1:
                print (1)
                link = link_valor.get()
                print (link)

            elif boton == 2:
                print (2)
                link = link_valor.get()
                print (link)

        else:
            print ("deves ingresar algun link")
            texto.set("Deves ingresar algun link")
    except:
        print ("Deve de ser un link valido")
        texto.set("Deve de ser un link valido")

# radio boton -----------------------------------------------------------------------------------
freim = tkinter.Frame (ventana, bg = "#6e6969",)
freim.grid (column = 0, row = 3, ipady= 40)

valor_radio = tkinter.IntVar()

def mostrar () :
    if valor_radio.get() == 1 :
        texto.set ("Descargar MP 3")
        calidad_i.config (state = "disabled")
        boton_1.config (state = "disabled")
        boton_2.config (state = "normal")

    elif valor_radio.get() == 2 :
        texto.set ("Descargar Video")
        calidad_i.config (state = "normal")
        boton_1.config (state = "normal")
        boton_2.config (state = "normal")

    elif valor_radio.get() == 3 :
        texto.set ("Descarga rapida")
        calidad_i.config (state = "disabled")
        boton_1.config (state = "normal")
        boton_2.config (state = "normal")


r1 = tkinter.Radiobutton(freim,     text = "MP 3",
                                    bg = "#999999",
                                    fg = "black",
                                    font = "arial 15",
                                    value = 1,
                                    variable = valor_radio,
                                    command=mostrar)
r1.pack(side="left", padx=5)

r2 = tkinter.Radiobutton(freim,     text = "Video",
                                    bg = "#999999",
                                    fg = "black",
                                    font = "arial 15",
                                    value = 2,
                                    variable = valor_radio,
                                    command=mostrar)
r2.pack(side="left", padx=5)

r3 = tkinter.Radiobutton(freim,     text = "Descarga rapida",
                                    bg = "#999999",
                                    fg = "black",
                                    font = "arial 15",
                                    value = 3,
                                    variable = valor_radio,
                                    command=mostrar)
r3.pack(side="left", padx=5)


# calidad --------------------------------------------------------------------------------------------------------------------------
freim_1 = tkinter.Frame (ventana, bg = "#6e6969",)
freim_1.grid (column = 0, row = 4, ipady= 20)

valor_resolusion = tkinter.StringVar()

calidad_t = tkinter.Label (freim_1, text = "Resolucion",
                                    bg = "#6e6969",
                                    fg = "black",
                                    font="arial 15 ",)
calidad_t.pack(side="left", padx=5)

calidad_i = tkinter.Entry(freim_1,  textvariable = valor_resolusion,
                                    width = "5",
                                    state = "disabled",
                                    font="arial 15 ",)
calidad_i.pack(side="left", padx=5)

calidad_t = tkinter.Label (freim_1, text = "p",
                                    bg = "#6e6969",
                                    fg = "black",
                                    font="arial 15 ",)
calidad_t.pack(side="left", padx=5)


# boton provar --------------------------------------------------------------------------------------------------------------------------
boton_1 = tkinter.Button(ventana,   text = "Resolusiones disponibles",
                                    width = "51",
                                    bg = "#999999",
                                    fg = "black",
                                    state = "disabled",
                                    command = lambda:optener_link (1),
                                    font = "arial 15",)
boton_1.grid (column = 0, row = 5)

# Texto de salida ------------------------------------------------------------------------------------------------------------------
freim_2 = tkinter.Frame (ventana,   bg = "#6e6969")
freim_2.grid (column = 0, row = 6, ipadx = 0, ipady= 0)

texto = tkinter.StringVar()
texto.set("Selecsionar un tipo de descarga")

txt_salida = tkinter.Label (freim_2,    textvariable = texto,
                                        font = "arial 15",
                                        bg = "#eeeeee",
                                        width= 51,
                                        height = 13,
                                        # justify="left",
                                        anchor="nw",
                                        )
txt_salida.pack(side="top", pady=20)


# Boton descarga ---------------------------------------------------------------------------------------------------------
def accion_descarga():
    optener_link (2)
    try:
        resolusion = valor_resolusion.get()
        resolusion_int = int (resolusion)

        comparar = 144, 240, 480, 720, 1080

        if resolusion_int in comparar:
            print (resolusion_int)

        else:
            texto.set (f"({resolusion}).No es un valor valido")
            print (f"({resolusion}).No es un valor valido")

    except:
        texto.set ("Solo se admiten numeros en la Resolucion")
        print ("Solo se admiten numeros en la Resolucion")

boton_2 = tkinter.Button(ventana,   text = "Descargar",
                                    width = "51",
                                    bg = "#999999",
                                    fg = "black",
                                    state = "disabled",
                                    command = accion_descarga,
                                    font = "arial 15",)
boton_2.grid (column = 0, row = 7)


ventana.mainloop()
