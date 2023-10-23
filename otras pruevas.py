# class Inisio ():
#     def __init__(self):
#         self.freim_2 = tkinter.Frame (self.ventana,   bg = "#6e6969",
#                                                         pady=15
#                                                         )
#         self.freim_2.grid (column = 0, row = 6)

#         # self.texto.set("Selecsionar un tipo de descarga")
#         self.entrada_texto = ("Selecsionar un tipo de descarga")
#         self.agregar_texto()
#         self.texto_salida = tkinter.Text(self.freim_2,  wrap=tkinter.WORD,
#                                                         font = "arial 15",
#                                                         state=tkinter.DISABLED,
#                                                         bg = "#eeeeee",
#                                                         height=14,
#                                                         width=51)
#         self.texto_salida.pack()

#     def agregar_texto(self):
#         texto = self.entrada_texto
#         texto_anterior = self.texto_salida.get("1.0", "end-1c")
#         texto_completo = f"{texto_anterior}\n{texto}"

#         self.texto_salida.config(state=tkinter.NORMAL) 
#         self.texto_salida.delete("1.0", "end")
#         self.texto_salida.insert("1.0", texto_completo)
#         self.texto_salida.config(state=tkinter.DISABLED)

# Inisio ()


class MiClaseSubscriptable:
    def __init__(self):
        self.datos = {}

    def __getitem__(self, key):
        return self.datos[key]

    def __setitem__(self, key, value):
        self.datos[key] = value

# Crear una instancia de la clase
mi_instancia = MiClaseSubscriptable()

# Asignar un valor a través de la subscripción
mi_instancia['clave'] = 'valor'

# Acceder al valor a través de la subscripción
print(mi_instancia['clave'])  # 