import pygame
import random


class Sonido():

    #Definiendo Sonido de Fondo
    def musica_fondo():
        #Lista de musicas
        musicas = ["donovan_sunshine_superman.WAV", "ELO_mr_blue_sky.WAV", "eminem_superman.WAV", "mortal_kombat_theme.WAV", "Sexo.WAV"]
        
        #Seleccionando una musica de fondo al azar
        musica_seleccionada = random.choice(musicas)

        pygame.mixer.music.load("src/views/sound/sonidos_fondo/{}".format(musica_seleccionada))
        return pygame.mixer.music.play(-1)

    def sonido_golpear():
        #Selecccionando musica de golpear
        golpear_sonido = pygame.mixer.Sound("src/views/sound/sonidos_golpe/golpe_normal.wav")
        return golpear_sonido.play(1)

    def sonido_patear():
        #Selecccionando musica de golpear
        patear_sonido = pygame.mixer.Sound("src/views/sound/sonidos_golpe/patada.wav")
        return patear_sonido.play(1)


    def pasar():
        return null