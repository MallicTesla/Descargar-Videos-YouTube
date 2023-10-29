from descargar import DescargadorVideo, DescargadorMP3

import tkinter                      #   hhttps://recursospython.com/guias-y-manuales/caja-de-texto-entry-tkinter/

from tkinter import ttk, filedialog


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

        self.url_link = tkinter.StringVar()

        self.link_i = tkinter.Entry(self.ventana,   textvariable = self.url_link,
                                                    width = "75",
                                                    font="arial 15 ",)
        self.link_i.grid(column = 0, row = 2, pady = 5, padx = 5, columnspan=3)


# radio boton -----------------------------------------------------------------------------------
        self.freim = tkinter.Frame (self.ventana, bg = "#6e6969",)
        self.freim.grid (column = 0, row = 3, ipady= 10)

        self.valor_radio = tkinter.IntVar()

        self.r1 = tkinter.Radiobutton(self.freim,   text = "MP 3",
                                                    bg = "#999999",
                                                    fg = "black",
                                                    font = "arial 15",
                                                    value = 1,
                                                    variable = self.valor_radio,
                                                    command=self.manejo_radio_boton)
        self.r1.pack(side="left", padx=5)

        self.r2 = tkinter.Radiobutton(self.freim,   text = "Video",
                                                    bg = "#999999",
                                                    fg = "black",
                                                    font = "arial 15",
                                                    value = 2,
                                                    variable = self.valor_radio,
                                                    command=self.manejo_radio_boton)
        self.r2.pack(side="left", padx=5)

        self.r3 = tkinter.Radiobutton(self.freim,   text = "Descarga rapida",
                                                    bg = "#999999",
                                                    fg = "black",
                                                    font = "arial 15",
                                                    value = 3,
                                                    variable = self.valor_radio,
                                                    command=self.manejo_radio_boton)
        self.r3.pack(side="left", padx=5)


# calidad --------------------------------------------------------------------------------------------------------------------------
        self.freim_1 = tkinter.Frame (self.ventana, bg = "#6e6969",)
        self.freim_1.grid (column = 0, row = 4, ipady= 10)

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
                                                    command = lambda:self.optener_link (1),
                                                    font = "arial 15",)
        self.boton_1.grid (column = 0, row = 5)


# Texto salida ------------------------------------------------------------------------------------------------------------------
        self.freim_2 = tkinter.Frame (self.ventana,   bg = "#6e6969",
                                                        pady=15)
        self.freim_2.grid (column = 0, row = 6)

        self.entrada_texto = ("Selecsionar un tipo de descarga")
        self.texto_salida = tkinter.Text(self.freim_2,  wrap=tkinter.WORD,
                                                        font = "arial 15",
                                                        state=tkinter.DISABLED,
                                                        bg = "#eeeeee",
                                                        height=14,
                                                        width=50)
        self.texto_salida.pack(side=tkinter.LEFT)

        scrollbar = tkinter.Scrollbar(self.freim_2, command=self.texto_salida.yview)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        self.texto_salida.config(yscrollcommand=scrollbar.set)

        self.agregar_texto()


# Boton descarga ---------------------------------------------------------------------------------------------------------
        self.boton_2 = tkinter.Button(self.ventana, text = "Descargar",
                                                    width = "51",
                                                    bg = "#999999",
                                                    fg = "black",
                                                    state = "disabled",
                                                    command = self.accion_descarga,
                                                    font = "arial 15",)
        self.boton_2.grid (column = 0, row = 7)


# rutas ---------------------------------------------------------------------------------------------------------
        def archivo ():
            tkinter.messagebox.showinfo("Info" , "Se creara una carpeta llamada descargas para guardar las descargas")
            self.ruta_descarga = filedialog.askdirectory()

        self.boton_3 = tkinter.Button(self.ventana, text = "Ruta de Descarga",
                                                    width = "51",
                                                    bg = "#999999",
                                                    fg = "black",
                                                    command = archivo,
                                                    font = "arial 15",)
        self.boton_3.grid (column = 0, row = 8, pady=20)


        self.ventana.mainloop()


# agregar texto---------------------------------------------------------------------------------------------------------
    def agregar_texto(self):
        texto = self.entrada_texto
        texto_anterior = self.texto_salida.get("1.0", "end-1c")
        texto_completo = f"{texto_anterior}\n{texto}"

        self.texto_salida.config(state=tkinter.NORMAL) 
        self.texto_salida.delete("1.0", "end")
        self.texto_salida.insert("1.0", texto_completo)
        self.texto_salida.config(state=tkinter.DISABLED)


# logica link---------------------------------------------------------------------------------------------------------------------------------
    def optener_link(self, boton):
        self.link = self.url_link.get()

        try:
            if self.link != "":
                if boton == 1:
                    resolusiones = DescargadorVideo(
                        self.link, quiero = False, ruta_video = False, ruta_audio = False, final = False, lo_mejor = False, descarga_rapida = False, solo_resolucion = False)

                    resolusiones = resolusiones.obtener_datos()

                    for resolusion in resolusiones:
                        res = str(resolusion['Resoluciones'])
                        res = res.replace("[", "").replace("]", "")

                        self.entrada_texto = f"{resolusion['Título']}\n{res}\n"
                        self.agregar_texto()

                elif boton == 2:
                    pass

            else:
                self.entrada_texto = "Deves ingresar algun link"
                self.agregar_texto()

        except:
            self.entrada_texto = "Deve de ser un link valido"
            self.agregar_texto()


# logica radio boton---------------------------------------------------------------------------------------------------------------------
    def manejo_radio_boton (self) :
        if self.valor_radio.get() == 1 :
            self.calidad_i.config (state = "disabled")
            self.boton_1.config (state = "disabled")
            self.boton_2.config (state = "normal")
            self.radio_boton = "Descargar MP 3"

            self.entrada_texto = "Descargar MP 3"

        elif self.valor_radio.get() == 2 :
            self.calidad_i.config (state = "normal")
            self.boton_1.config (state = "normal")
            self.boton_2.config (state = "normal")
            self.radio_boton = "Descargar Video"

            self.entrada_texto = "Descargar Video"

        elif self.valor_radio.get() == 3 :
            self.calidad_i.config (state = "disabled")
            self.boton_1.config (state = "normal")
            self.boton_2.config (state = "normal")
            self.radio_boton = "Descargar rapida"

            self.entrada_texto = "Descargar rapida \nNormalmente se descarga a 720p"

        self.agregar_texto()


# logica boton descargar----------------------------------------------------------------------------------------------------------------
    def accion_descarga(self):
        self.optener_link (2) #optengo el link

        try:
            if self.ruta_descarga != "" or None:
                print (self.ruta_descarga)

                if self.radio_boton == "Descargar MP 3":
                    print ("Descargar MP 3")

                elif self.radio_boton == "Descargar Video":
                    print ("Descargar Video")

                    try:
                        resolusion = self.valor_resolusion.get()
                        resolusion_int = int (resolusion)

                        self.comparar = 144, 240, 480, 720, 1080, 1440, 2160, 4320

                        if resolusion_int in self.comparar:

                            # DescargadorVideo(
                            # self.link, quiero = resolusion, ruta_video = False, ruta_audio = False, final = False, lo_mejor = False, descarga_rapida = True, solo_resolucion = False)
                            self.entrada_texto = "Finalizo la descarga"
                            self.agregar_texto()

                        else:
                            self.entrada_texto = f"({resolusion}).No es un valor valido"
                            self.agregar_texto()

                    except:
                        self.entrada_texto = "Solo se admiten numeros en la Resolucion"
                        self.agregar_texto()

                elif self.radio_boton == "Descargar rapida":
                    print ("Descargar rapida")
                    # DescargadorVideo(
                    #         self.link, quiero = False, ruta_video = False, ruta_audio = False, final = False, lo_mejor = False, descarga_rapida = True, solo_resolucion = False)

                    self.entrada_texto = "Finalizo la descarga"
                    self.agregar_texto()

        except:
            tkinter.messagebox.showinfo("ERROR" , "Deves de ingresar una ruta de descarg")
            self.entrada_texto = "Deves de ingresar una ruta de descarga"
            self.agregar_texto()


Inisio ()
# DescargadorVideo(link, quiero, ruta_video, ruta_audio, final, lo_mejor, descarga_rapida, solo_resolucion)

