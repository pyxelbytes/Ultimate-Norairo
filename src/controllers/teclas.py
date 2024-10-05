import pygame
from ..views.vista import Vista


class Teclas():

    @classmethod
    def golpear(cls, personaje1,  personaje2, verificacion_golpear = False):
        personaje1.sprite = "normal" #para que vuelva a la normalidad, despues de golpear
        personaje2.sprite = "normal"

        #Golpes
        teclas = pygame.key.get_pressed() #Tecla presionada
        if teclas[pygame.K_q]:  # Golpe del jugador 1
            if verificacion_golpear:
                dano = personaje1.golpear(personaje2, verificacion_golpear)
                print(f"{personaje1.nombre} golpea a {personaje2.nombre} causando {dano} de daño.")
            else:
                dano = personaje1.golpear(personaje2, verificacion_golpear)

        if teclas[pygame.K_KP7]:  # Golpe del jugador 2
            if verificacion_golpear:
                dano = personaje2.golpear(personaje1, verificacion_golpear)
                print(f"{personaje2.nombre} golpea a {personaje1.nombre} causando {dano} de daño.")
            else:
                dano = personaje2.golpear(personaje1, verificacion_golpear)

    
    @classmethod
    def patear(cls, personaje1,  personaje2, verificacion_patear = False):
        #personaje1.sprite = "normal" #para que vuelva a la normalidad, despues de golpear
        #personaje2.sprite = "normal"

        #Patadas
        teclas = pygame.key.get_pressed() #Tecla presionada
        if teclas[pygame.K_e]:  # Golpe del jugador 1
            if verificacion_patear:
                dano = personaje1.patear(personaje2, verificacion_patear)
                print(f"{personaje1.nombre} patea a {personaje2.nombre} causando {dano} de daño.")
            else:
                dano = personaje1.patear(personaje2, verificacion_patear)
            
        if teclas[pygame.K_KP9]:  # Golpe del jugador 2
            if  verificacion_patear:
                dano = personaje2.patear(personaje1)
                print(f"{personaje2.nombre} patea a {personaje1.nombre} causando {dano} de daño.")
            else:
                dano = personaje2.patear(personaje1, verificacion_patear)


        


    @classmethod
    def mover(cls, personaje, ancho, player_1 = True):
        velocidad = 10
        mov_x = 0

        #movimientos
        teclas = pygame.key.get_pressed()
        if player_1:
            if teclas[pygame.K_d]:  # Mover hacia adelante
                mov_x = velocidad
                print(f"{personaje.nombre} se mueve hacia adelante")
            elif teclas[pygame.K_a]:  # Mover hacia atrás
                mov_x = -velocidad
                print(f"{personaje.nombre} se mueve hacia atrás")
        else:
            if teclas[pygame.K_KP6]:  # mover jugador jugador 1 hacia enfrente
                mov_x = velocidad
                print(f"{personaje.nombre} se mueve hacia entrente")
            if teclas[pygame.K_KP4]:  # mover jugador jugador 1 hacia atras
                mov_x -= velocidad
                print(f"{personaje.nombre} se mueve hacia atras")

        # Actualizar el movimiento del personaje
        personaje.mover(mov_x)

        # Limitar el movimiento dentro de la pantalla
        if player_1:

            if personaje.hitbox.left < 0:
                personaje.pos_x = 0
            if personaje.hitbox.right > ancho:
                personaje.pos_x = ancho - personaje.hitbox.width

        else:

            if personaje.hitbox.left + mov_x < 0:
                personaje.pos_x = 0
            
            if personaje.hitbox.right + mov_x > ancho:
                personaje.pos_x = ancho - personaje.hitbox.width

    
    @classmethod
    def saltar(cls, personaje, altitud = 60, player_1 = True):
        gravedad = 10
        altitud = 180
        mov_y = 0

        #movimientos
        teclas = pygame.key.get_pressed()
        if player_1:
            if teclas[pygame.K_w] and personaje.saltando == False :  # saltar
                mov_y -= altitud
                print(f"{personaje.nombre} salta hacia arriba, obviamente")
                personaje.saltando = True
        else:
            if teclas[pygame.K_KP8] and personaje.saltando == False:  # mover jugador jugador 1 hacia enfrente
                mov_y -= altitud
                print(f"{personaje.nombre} salta hacia arriba obviamente")
                personaje.saltando = True

        # Actualizar el movimiento del personaje
        personaje.saltar(mov_y + gravedad * 2) #saltar


        #Siempre en el suelo
        if personaje.hitbox.bottom >= 568:
            personaje.saltando = False
            personaje.pos_y = 388
            personaje.saltar(mov_y + gravedad)



