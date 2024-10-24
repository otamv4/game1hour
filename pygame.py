import pygame
import sys

# Inicializar o Pygame
pygame.init()

# Configurações de tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo Plataforma POO com Pygame")

# Definir cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Classe Jogo
class Game:
    def __init__(self):
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Inicia o jogador no centro da tela
        self.clock = pygame.time.Clock()

    def run(self):
        # Loop principal do jogo
        while True:
            # Captura os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Obter teclas pressionadas
            keys = pygame.key.get_pressed()

            # Atualizar jogador
            self.player.update(keys)

            # Desenhar na tela
            screen.fill(WHITE)  # Limpa a tela
            # self.player.draw(screen)  # Desenha o jogador

            # Atualizar a tela
            pygame.display.flip()

            # Controlar o frame rate
            self.clock.tick(60)

# Inicializar e rodar o jogo
if __name__ == "__main__":
    game = Game()  # Cria o objeto jogo
    game.run()  # Inicia o loop do jogo