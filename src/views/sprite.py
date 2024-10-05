import pygame

class Sprite():

    #Sprites Mincho
    mincho_normal = pygame.image.load("src/views/img/Personajes/Mincho/normal.PNG")
    mincho_golpe = pygame.image.load("src/views/img/Personajes/Mincho/golpe.png")
    mincho_patada = pygame.image.load("src/views/img/Personajes/Mincho/patada.png")

    #Sprites Roberth
    roberth_normal = pygame.image.load("src/views/img/Personajes/Roberth/normal.png")
    roberth_golpe = pygame.image.load("src/views/img/Personajes/Roberth/golpe.png")
    roberth_patada = pygame.image.load("src/views/img/Personajes/Roberth/patada.png")

class Fondo():
    linea = pygame.image.load("src/views/img/Fondos/linea.PNG")
    generic = pygame.image.load("src/views/img/Fondos/generic.jpg")