from descargar import DescargadorVideo, DescargadorMP3

import tkinter                       #   hhttps://recursospython.com/guias-y-manuales/caja-de-texto-entry-tkinter/
from tkinter import ttk


class Inisio ():
    def __init__(self):

        self.ventana = tkinter.Tk()

        self.ventana.title("Descargas You Tuve")         #   Cambiar el nombre de la self.ventana
        self.ventana.geometry("700x700")                 #   Configurar tamaño
        self.ventana.resizable(1,1)                      #   para modificar manual mente el tamaño (para no modificarla(0,0)) (para modificarlo(1,1))
        self.ventana.config(bg="#6e6969")                #   Cambiar color de fond el color en inglés o en formato hexadecima

        self.ventana.columnconfigure (0, weight = 1)

# link------------------------------------------------------------------------------------------
        self.txt_link = tkinter.Label(self.ventana, text = "Link de Descarga",
                                                    bg = "#6e6969",
                                                    fg = "black",
                                                    font="arial 15 ",)
        self.txt_link.grid(column = 0, row = 1, pady = 5, padx = 5)

        self.link_valor = tkinter.StringVar()

        self.link_i = tkinter.Entry(self.ventana,   textvariable = self.link_valor,
                                                    width = "75",
                                                    font="arial 15 ",)
        self.link_i.grid(column = 0, row = 2, pady = 5, padx = 5, columnspan=3)

        def optener_link(boton):
            self.boton = boton
            # link = link_valor.get()
            try:
                if self.link != "":
                    if self.boton == 1:
                        print (1)
                        self.link = self.link_valor.get()
                        print (self.link)

                    elif self.boton == 2:
                        print (2)
                        self.link = self.link_valor.get()
                        print (self.link)

                else:
                    # print ("deves ingresar algun link")
                    self.texto.set("Deves ingresar algun link")
            except:
                print ("Deve de ser un link valido")
                self.texto.set("Deve de ser un link valido")

# radio boton -----------------------------------------------------------------------------------
        self.freim = tkinter.Frame (self.ventana, bg = "#6e6969",)
        self.freim.grid (column = 0, row = 3, ipady= 40)

        self.valor_radio = tkinter.IntVar()

        def mostrar () :
            if self.valor_radio.get() == 1 :
                self.texto.set ("Descargar MP 3")
                self.calidad_i.config (state = "disabled")
                self.boton_1.config (state = "disabled")
                self.boton_2.config (state = "normal")

            elif self.valor_radio.get() == 2 :
                self.texto.set ("Descargar Video")
                self.calidad_i.config (state = "normal")
                self.boton_1.config (state = "normal")
                self.boton_2.config (state = "normal")

            elif self.valor_radio.get() == 3 :
                self.texto.set ("Descarga rapida")
                self.calidad_i.config (state = "disabled")
                self.boton_1.config (state = "normal")
                self.boton_2.config (state = "normal")


        self.r1 = tkinter.Radiobutton(self.freim,   text = "MP 3",
                                                    bg = "#999999",
                                                    fg = "black",
                                                    font = "arial 15",
                                                    value = 1,
                                                    variable = self.valor_radio,
                                                    command=mostrar)
        self.r1.pack(side="left", padx=5)

        self.r2 = tkinter.Radiobutton(self.freim,   text = "Video",
                                                    bg = "#999999",
                                                    fg = "black",
                                                    font = "arial 15",
                                                    value = 2,
                                                    variable = self.valor_radio,
                                                    command=mostrar)
        self.r2.pack(side="left", padx=5)

        self.r3 = tkinter.Radiobutton(self.freim,   text = "Descarga rapida",
                                                    bg = "#999999",
                                                    fg = "black",
                                                    font = "arial 15",
                                                    value = 3,
                                                    variable = self.valor_radio,
                                                    command=mostrar)
        self.r3.pack(side="left", padx=5)


# calidad --------------------------------------------------------------------------------------------------------------------------
        self.freim_1 = tkinter.Frame (self.ventana, bg = "#6e6969",)
        self.freim_1.grid (column = 0, row = 4, ipady= 20)

        self.valor_resolusion = tkinter.StringVar()

        self.calidad_t = tkinter.Label (self.freim_1,   text = "Resolucion",
                                                        bg = "#6e6969",
                                                        fg = "black",
                                                        font="arial 15 ",)
        self.calidad_t.pack(side="left", padx=5)

        self.calidad_i = tkinter.Entry(self.freim_1,    textvariable = self.valor_resolusion,
                                                        width = "5",
                                                        state = "disabled",
                                                        font="arial 15 ",)
        self.calidad_i.pack(side="left", padx=5)

        self.calidad_t = tkinter.Label (self.freim_1,   text = "p",
                                                        bg = "#6e6969",
                                                        fg = "black",
                                                        font="arial 15 ",)
        self.calidad_t.pack(side="left", padx=5)


# boton provar --------------------------------------------------------------------------------------------------------------------------
        self.boton_1 = tkinter.Button(self.ventana, text = "Resolusiones disponibles",
                                                    width = "51",
                                                    bg = "#999999",
                                                    fg = "black",
                                                    state = "disabled",
                                                    command = lambda:optener_link (1),
                                                    font = "arial 15",)
        self.boton_1.grid (column = 0, row = 5)

# Texto de salida ------------------------------------------------------------------------------------------------------------------
        self.freim_2 = tkinter.Frame (self.ventana,   bg = "#6e6969")
        self.freim_2.grid (column = 0, row = 6, ipadx = 0, ipady= 0)

        self.texto = tkinter.StringVar()
        self.texto.set("Selecsionar un tipo de descarga")

        self.txt_salida = tkinter.Label (self.freim_2,  textvariable = self.texto,
                                                        font = "arial 15",
                                                        bg = "#eeeeee",
                                                        width= 51,
                                                        height = 13,
                                                        # justify="left",
                                                        anchor="nw",)
        self.txt_salida.pack(side="top", pady=20)


# Boton descarga ---------------------------------------------------------------------------------------------------------
        def accion_descarga():
            optener_link (2) #optengo el link
            try:
                self.resolusion = self.valor_resolusion.get()
                self.resolusion_int = int (self.resolusion)

                self.comparar = 144, 240, 480, 720, 1080

                if self.resolusion_int in self.comparar:
                    print (self.resolusion_int)

                    # DescargadorVideo(self.link, self.quiero, self.ruta_video, self.ruta_audio, self.final, self.lo_mejor, self.descarga_rapida, self.para)

                else:
                    self.texto.set (f"({self.resolusion}).No es un valor valido")
                    print (f"({self.resolusion}).No es un valor valido")

            except:
                self.texto.set ("Solo se admiten numeros en la Resolucion")
                print ("Solo se admiten numeros en la Resolucion")

        self.boton_2 = tkinter.Button(self.ventana, text = "Descargar",
                                                    width = "51",
                                                    bg = "#999999",
                                                    fg = "black",
                                                    state = "disabled",
                                                    command = accion_descarga,
                                                    font = "arial 15",)
        self.boton_2.grid (column = 0, row = 7)


        self.ventana.mainloop()
Inisio ()
# DescargadorVideo(link, quiero, ruta_video, ruta_audio, final, lo_mejor, descarga_rapida, para)