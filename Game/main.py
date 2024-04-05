#!/usr/bin/env python3

import pygame

import pygame

# Dimensions de la fenêtre du jeu
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Couleurs
BLACK = (0, 0, 0)
RED = (255, 0, 0)

def main():
    # Initialisation de Pygame
    pygame.init()

    # Création de la fenêtre du jeu
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Explorer's Unity")

    # Chargement de l'image de la carte
    map_image = pygame.image.load("map.png")

    # Chargement de l'image du joueur
    player_image = pygame.image.load("player.png")

    # Position initiale du joueur
    player_x = 400
    player_y = 300

    # Vitesse de déplacement du joueur
    player_speed = 5

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Gestion des touches enfoncées pour le déplacement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed

        # Dessiner la carte
        screen.blit(map_image, (0, 0))

        # Dessiner le joueur
        screen.blit(player_image, (player_x, player_y))

        # Rafraîchir l'écran
        pygame.display.flip()

    # Quitter Pygame
    pygame.quit()

# Exécution de la fonction main
if __name__ == "__main__":
    main()