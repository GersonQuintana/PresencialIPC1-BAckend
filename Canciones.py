class Cancion:

    def __init__(self,nombre,artista,album,fecha,imagen,spotify,youtube):
        self.nombre = nombre
        self.artista = artista
        self.album = album
        self.imagen = imagen
        self.fecha = fecha
        self.spotify = spotify
        self.youtube = youtube

#METODOS - GET
    def getNombre(self):
        return self.nombre
    
    def getArtista(self):
        return self.artista
    
    def getAlbum(self):
        return self.album
    
    def getImagen(self):
        return self.imagen
    
    def getFecha(self):
        return self.fecha

    def getSpotify(self):
        return self.spotify
    
    def getYoutube(self):
        return self.youtube

#METODOS - SET
    def setNombre(self, nombre):
        self.nombre = nombre

    def setArtista(self, artista):
        self.artista = artista

    def setAlbum(self, album):
        self.album = album

    def setImagen(self, imagen):
        self.imagen = imagen

    def setFecha(self, fecha):
        self.fecha = fecha

    def setSpotify(self, spotify):
        self.spotify = spotify

    def setYoutube(self, youtube):
        self.youtube = youtube
    

    