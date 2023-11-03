import os
import shutil

from pytube import YouTube, Playlist
from moviepy.editor import VideoFileClip, AudioFileClip

class DescargadorVideo ():
    def __init__(self, link, quiero, ruta, lo_mejor, descarga_rapida, solo_resolucion):
        self.link = link
        self.quiero = quiero
        self.lo_mejor = lo_mejor
        self.descarga_rapida = descarga_rapida
        self.solo_resolucion = solo_resolucion
        self.ruta = ruta
        self.videos_quiero = False
        self.resolusiones = []
        self.resoluciones_videos = []
        self.titulos_resolusiones = []

        self.listado()


    def listado (self):
        if self.link.lower().count("playlist") == 1:
            links = Playlist (self.link)

            for listas in links.video_urls:
                self.lista = YouTube (listas)

                self.separador ()

        elif self.link.lower().count("playlist") == 0:
            self.lista = YouTube (self.link)

            self.separador ()


    def separador (self):
        self.titulo = self.lista.title

        self.video_completo = self.lista.streams.get_highest_resolution()

        self.videos = self.lista.streams.order_by("resolution").desc().filter (type = "video")
        self.audios = self.lista.streams.order_by("abr").desc().filter (type = "audio")

        self.videos_quiero = self.videos.filter (resolution = self.quiero + "p")

        self.video = self.videos[0]
        self.audio = self.audios[0]


        if self.solo_resolucion:
            for self.video_1 in self.videos :
                if self.video_1.resolution not in self.resolusiones:
                    self.resolusiones.append(self.video_1.resolution)

                    self.resoluciones_int = []
                    for self.resolusion in self.resolusiones:
                        self.resoluciones_int.append (int(self.resolusion.rstrip('p')))

                self.resoluciones_dict = {
                    "Título": self.titulo,
                    "Resoluciones": sorted (self.resoluciones_int, reverse=True)
                    }

            self.resoluciones_videos.append(self.resoluciones_dict)

        else:
            self.carpetas()
            self.descarga()


    def obtener_datos(self):
        return self.resoluciones_videos

    def __str__(self):
        return f"{self.resoluciones_videos}"


    def carpetas (self):
        nombre_principal = "/YouTube"
        ruta_principal = self.ruta + nombre_principal

        subcarpeta_1 = "Video"
        subcarpeta_2 = "Audio"

        if not os.path.exists(ruta_principal):
            os.makedirs(ruta_principal)

        ruta_subcarpeta_1 = os.path.join(ruta_principal, subcarpeta_1)
        if not os.path.exists(ruta_subcarpeta_1):
            os.makedirs(ruta_subcarpeta_1)

        ruta_subcarpeta_2 = os.path.join(ruta_principal, subcarpeta_2)
        if not os.path.exists(ruta_subcarpeta_2):
            os.makedirs(ruta_subcarpeta_2)

        self.ruta_video = ruta_principal + "/Video"
        self.ruta_audio = ruta_principal + "/Audio"
        self.final = ruta_principal

    def eliminar_carpeta (self):
        if os.path.exists(self.ruta_video):
            shutil.rmtree(self.ruta_video)

        if os.path.exists(self.ruta_audio):
            shutil.rmtree(self.ruta_audio)


    def descarga (self):
        son_iguales = False

        print ("que ese ", self.videos_quiero)
        if self.videos_quiero :
            print ("no")
            self.video = self.videos_quiero [0]

        else:
            print ("si")
            self.descarga_rapida = True

        for video_quiero in self.videos_quiero:
            if video_quiero.itag == self.video_completo.itag:
                son_iguales = True

        if self.descarga_rapida or son_iguales :
            try:
                self.video_completo.download(self.final)

                self.eliminar_carpeta()

            except:
                print ("fallo descarga")

        else:
            try:
                self.video.download (self.ruta_video)
                self.audio.download (self.ruta_audio)

                self.fusionar ()

            except:
                print ("fallo descarga")


    def fusionar (self):
        try:
            self.video = VideoFileClip (f"{self.ruta_video}/{self.video.default_filename}")
            self.audio = AudioFileClip (f"{self.ruta_audio}/{self.audio.default_filename}")

            self.fusion = self.video.set_audio (self.audio)

            self.fusion.write_videofile (f"{self.final}\\{self.titulo}.mp4", codec="libx264", audio_codec="aac")

            self.eliminar_carpeta()

        except Exception as e:
            print ("Fallo la fusion", str(e))


# --------------------------------------------------------------------------------------------------------
class DescargadorMP3 ():
    def __init__(self, link, ruta):
        self.link = link
        self.ruta = ruta

        self.carpetas()
        self.listado()

    def listado (self):
        if self.link.lower().count("playlist") == 1:
            print ("playlist")
            links = Playlist (self.link)

            for listas in links.video_urls:
                print ("1")
                self.lista = YouTube (listas)

                self.descarga_audio ()

        elif self.link.lower().count("playlist") == 0:
            print ("audio")
            self.lista = YouTube (self.link)

            self.descarga_audio ()

        else:
            print ("ninguna")

    def descarga_audio (self):
        audios = self.lista.streams.order_by("abr").desc().filter(type = "audio")

        audio = audios[0]

        audio.download (self.ruta_audio)
        print ("se descargo")

    def carpetas (self):
        nombre_principal = "/YouTube"
        ruta_principal = self.ruta + nombre_principal

        subcarpeta_1 = "MP 3"

        if not os.path.exists(ruta_principal):
            os.makedirs(ruta_principal)

        ruta_subcarpeta_1 = os.path.join(ruta_principal, subcarpeta_1)
        if not os.path.exists(ruta_subcarpeta_1):
            os.makedirs(ruta_subcarpeta_1)

        self.ruta_audio = ruta_principal + "/MP 3"




# link = "https://www.youtube.com/watch?v=8-bSHuiTSoM&ab_channel=DateunVlog" #1080
# link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley" #1080
# link = "https://www.youtube.com/watch?v=GVkiFP71n_c&ab_channel=LaMomiadelHugo" #720
# link = "https://www.youtube.com/watch?v=jEugr6x2_qc&ab_channel=Bizarro" # 2160
# link = "https://www.youtube.com/playlist?list=PL4vlU3dGym0bgQtk-MKvLFoouWHC9g7R6" #4
# link = "youtube.com/playlist?list=PL4vlU3dGym0Z3ECP0QxmpylREWK9mPVM2" #2