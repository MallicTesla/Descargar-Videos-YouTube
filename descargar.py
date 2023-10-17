from pytube import YouTube, Playlist
from moviepy.editor import VideoFileClip, AudioFileClip

class DescargadorVideo ():
    def __init__(self, link, quiero, ruta_video, ruta_audio, final, lo_mejor, descarga_rapida, para):
        self.link = link
        self.quiero = quiero
        self.ruta_video = ruta_video
        self.ruta_audio = ruta_audio
        self.final = final
        self.lo_mejor = lo_mejor
        self.descarga_rapida = descarga_rapida
        self.para = para

        self.resolusiones = []
        self.resoluciones_videos = []
        self.titulos_resolusiones = []

        self.lista()

    # def lista (self, link, quiero, ruta_video, ruta_audio, final, lo_mejor, descarga_rapida):
    def lista (self):
        if self.link.lower().count("playlist") == 1:
            print ("playlist")
            self.links = Playlist (self.link)

            for self.listas in self.links.video_urls:
                print ("1")
                self.lista = YouTube (self.listas)

                # separador (lista, quiero, ruta_video, ruta_audio, final, lo_mejor, descarga_rapida)
                self.separador ()

        elif link.lower().count("playlist") == 0:
            print ("video")
            self.lista = YouTube (link)

            # separador (lista, quiero, ruta_video, ruta_audio, final, lo_mejor, descarga_rapida)
            self.separador ()

        else:
            print ("ninguna")


    # def separador (self, lista, quiero, ruta_video, ruta_audio, final, lo_mejor, descarga_rapida):
    def separador (self):
        self.titulo = self.lista.title

        self.video_completo = self.lista.streams.get_highest_resolution()
        print (self.video_completo)

        self.videos = self.lista.streams.order_by("resolution").desc().filter (type = "video")
        self.audios = self.lista.streams.order_by("abr").desc().filter (type = "audio")

        # print (self.videos)

        self.videos_quiero = self.videos.filter (resolution = self.quiero)

        # for video in videos :
        #     print ("todas ",video)
        # print ()
        # for audio in audios :
        #     print ("audios", audio)

        self.video = self.videos[0]
        self.audio = self.audios[0]

        # print (self.titulo)
        # print (f"video quiero {self.videos_quiero}")
        # print (f"video_completo.resolution {self.video_completo.resolution}")
        # print (f"primer video {self.video}")
        # print (f"primer audio {self.audio}")

        # descarga (video_completo, videos_quiero, video, audio, ruta_video, ruta_audio, final, lo_mejor, descarga_rapida, titulo)
        if self.para:
            print ("sigui")
            # self.descarga()

        elif self.para is False:
            print ("se paro")

            for self.video in self.videos :
                if self.video.resolution not in self.resolusiones :
                    self.resolusiones.append (self.video.resolution)

            self.resoluciones_str = '\n'.join (self.resolusiones)

            self.resoluciones_videos.append (f"{self.titulo}")
            self.resoluciones_videos.append (f"{self.resoluciones_str}")

        else:
            print ("else")


    def __str__(self):
        return f"{self.resoluciones_videos}"

    # def descarga (self, video_completo, videos_quiero, video, audio, ruta_video, ruta_audio, final, lo_mejor, descarga_rapida, titulo):
    def descarga (self):
        if self.descarga_rapida or self.video_completo.resolution is self.video.resolution or self.video_completo.resolution is self.videos_quiero[0].resolution:
            print ("descarga rapida", {self.video_completo})
            try:
                self.video_completo.download(self.final)

                print ("descarga completa")
            except:
                print ("fallo descarga")

        else:
            if self.lo_mejor and self.quiero == "":
                print (f"lo mejor {self.video}")
            else:
                self.video = self.videos_quiero [0]
                print (f"quiero {self.video}")

            try:
                self.video.download (self.ruta_video)
                self.audio.download (self.ruta_audio)

                print ("descarga completa")

                # fusionar (video, audio, ruta_video, ruta_audio, final, titulo)
                self.fusionar ()

            except:
                print ("fallo descarga")


    # def fusionar (self, video, audio, ruta_video, ruta_audio, final, titulo):
    def fusionar (self):
        try:
            self.video = VideoFileClip (f"{self.ruta_video}/{self.video.default_filename}")
            self.audio = AudioFileClip (f"{self.ruta_audio}/{self.audio.default_filename}")

            self.fusion = self.video.set_audio (self.audio)

            self.fusion.write_videofile (f"{self.final}\\{self.titulo}.mp4", codec="libx264", audio_codec="aac")

        except Exception as e:
            print ("Fallo la fusion", str(e))

        print (f"Proseso terminado")


class DescargadorMP3 ():
    def descargar_audio (self, link, ruta_audio):
        if link.lower().count("playlist") == 1:
            print ("playlist")
            links = Playlist (link)

            for listas in links.video_urls:
                print ("1")
                lista = YouTube (listas)

                # descarga (lista, ruta_audio)

        elif link.lower().count("playlist") == 0:
            print ("audio")
            lista = YouTube (link)

            # descarga_audio (lista, ruta_audio)

        else:
            print ("ninguna")

    def descarga_audio (self, lista, ruta_audio):
        audios = lista.streams.order_by("abr").desc().filter(type = "audio")

        # for audio in audios :
        #     print (f"audio {audio}")

        audio = audios[0]

        audio.download (ruta_audio)



# --------------------------------------------------------------------------------------------------------
# RUTAS DE DESTINO

ruta_video = "C:\\Users\\Mallic\\Downloads\\YouTube\\video"
ruta_audio = "C:\\Users\\Mallic\\Downloads\\YouTube\\audio"
final = "C:\\Users\\Mallic\\Downloads\\YouTube\\pronto"

# --------------------------------------------------------------------------------------------------------
# DESCARGAR AUDIO

# link = "https://www.youtube.com/watch?v=jEugr6x2_qc&ab_channel=Bizarro"
# link = "https://www.youtube.com/watch?v=GVkiFP71n_c&ab_channel=LaMomiadelHugo"

# descomenta esto para descargar audio y comenta el de DESCARGAR VIDEOS
# descargar_audio (link, ruta_audio)

# --------------------------------------------------------------------------------------------------------
# DESCARGAR VIDEOS

# link = "https://www.youtube.com/watch?v=8-bSHuiTSoM&ab_channel=DateunVlog" #1080
# link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley" #1080
# link = "https://www.youtube.com/watch?v=GVkiFP71n_c&ab_channel=LaMomiadelHugo" #720
# link = "https://www.youtube.com/watch?v=jEugr6x2_qc&ab_channel=Bizarro" # 2160
# link = "https://www.youtube.com/playlist?list=PL4vlU3dGym0bgQtk-MKvLFoouWHC9g7R6" #4
link = "youtube.com/playlist?list=PL4vlU3dGym0Z3ECP0QxmpylREWK9mPVM2" #2

lo_mejor = False
quiero = "1080p"

descarga_rapida = False

para = False

# descomenta esto para descargar videos y comenta el de DESCARGAR AUDIO
# lista (link, quiero, ruta_video, ruta_audio, final, lo_mejor, descarga_rapida)

# print (DescargadorVideo(link, quiero, ruta_video, ruta_audio, final, lo_mejor, descarga_rapida, para))

# funsionara = DescargadorVideo(link, quiero, ruta_video, ruta_audio, final, lo_mejor, descarga_rapida, para)
# print (f"funsionara {funsionara}")

# descargar_video.lista()

# --------------------------------------------------------------------------------------------------------
# DESCARGAR VIDEOS DE LISTA DE REPRODUCCION


# --------------------------------------------------------------------------------------------------------






