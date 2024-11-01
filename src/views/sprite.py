import pygame
import random

class Sprite():

    #Sprites Mincho
    mincho_normal = pygame.image.load("src/views/img/Personajes/Mincho/normal.PNG")
    mincho_golpe = pygame.image.load("src/views/img/Personajes/Mincho/golpe.png")
    mincho_patada = pygame.image.load("src/views/img/Personajes/Mincho/patada.png")

    #Sprites Roberth
    roberth_normal = pygame.image.load("src/views/img/Personajes/Roberth/normal.png")
    roberth_golpe = pygame.image.load("src/views/img/Personajes/Roberth/golpe.png")
    roberth_patada = pygame.image.load("src/views/img/Personajes/Roberth/patada.png")

    #Sprites Rodrigo
    rodrigo_normal = pygame.image.load("src/views/img/Personajes/Rodrigo/normal.png")
    rodrigo_golpe = pygame.image.load("src/views/img/Personajes/Rodrigo/golpe.png")
    rodrigo_patada = pygame.image.load("src/views/img/Personajes/Rodrigo/patada.png")

class Fondo():
    linea = pygame.image.load("src/views/img/Fondos/linea.PNG")
    generic = pygame.image.load("src/views/img/Fondos/generic.jpg")
    policlinico = pygame.image.load("src/views/img/Fondos/policlinico.jpg")
    hito = pygame.image.load("src/views/img/Fondos/hito.png")
    laguna = pygame.image.load("src/views/img/Fondos/laguna.png")
    muni = pygame.image.load("src/views/img/Fondos/Muni.png")
    skate = pygame.image.load("src/views/img/Fondos/Skate.png")
    mural = pygame.image.load("src/views/img/Fondos/mural.jpg")

    fondo_seleccionado = None

    @classmethod
    def Fondo_Choice(cls):

        #Listando los fondos
        fondos = [Fondo.linea, Fondo.generic, Fondo.policlinico, Fondo.hito, Fondo.laguna, Fondo.muni, Fondo.skate, Fondo.mural]

        if Fondo.fondo_seleccionado == None:
            Fondo.fondo_seleccionado = random.choice(fondos)

        return Fondo.fondo_seleccionado