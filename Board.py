from Automaton2D import Automaton2D
from FileManager import FileManager
import pygame
import numpy as np
import time
import sys


class Board:
    def __init__(self, automaton):
        # Valores definidos por el usuario
        self.automaton = Automaton2D()
        self.automaton = automaton
        self.cells_y = automaton.iterations  # Numero de filas
        self.cells_x = automaton.size  # NUmero de columnas (iteraciones)
        self.state = []

        # Tamaño de las celdas del lienzo
        self.cell_width = 1000
        self.cell_height = 600

        # Colores
        self.background_color = 25, 25, 25
        self.cell_color = 255, 255, 255
        self.death_cell_color = 128, 128, 128

        # Otros valores por defecto
        self.max_width = 50  # Tamaño maximo de las filas
        self.current_row = 0  # Fila que estamos pintando actualmente
        self.file_manager = FileManager()

        # tamaño de celdas en el eje x
        self.sizeX = self.cell_width / self.cells_x
        self.sizeY = self.cell_height / self.cells_y

        # Desplegar la pantalla de pygame
        pygame.init()
        pygame.display.set_caption('Automata celular ' + str(self.automaton.rule))
        self.screen = pygame.display.set_mode((self.cell_width, self.cell_height))
        self.screen.fill(self.background_color)  # pintar fondo

    def run(self):

        self.state = self.automaton.state

        paused = False
        finished = False

        self.file_manager.delete(self.automaton.rule, "regla")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                # Despausar la ejecucion con una tecla
                if event.type == pygame.KEYDOWN:
                    paused = False

            # Simulacion en proceso
            if not paused:
                # colorear el fondo, limpiar la pantalla
                time.sleep(0.1)

                # No ha terminado las iteraciones
                if not finished:
                    if self.current_row >= 1:
                        # Guardar en el archivo
                        self.file_manager.write_new_line(self.automaton.rule, "regla", self.state)

                        # Nuevo estado
                        self.automaton.new_state()

                    self.state = self.automaton.state

                    # Dibujo de la cuadricula
                    for x in range(0, self.cells_x):
                        self.draw_polygon(x, self.current_row, self.state, 1)

                    # mostrar los cambios en la pantalla
                    pygame.display.flip()

                    # Terminar el programa
                    if self.current_row >= self.cells_y:
                        # Guardar en el archivo la ultima linea
                        # self.file_manager.write_new_line(self.automaton.rule, "automata", self.state)

                        finished = True

                    # Para que el usuario defina su patron inicial
                    if self.current_row <= 0:
                        paused = True

                    self.current_row += 1

            # Dibujando el patron inicial
            if paused:
                # vector que indica cual de las 3 teclas del mouse se presionó
                mouse_click = pygame.mouse.get_pressed()

                if sum(mouse_click) > 0:
                    # posicion del mouse
                    posX, posY = pygame.mouse.get_pos()

                    # celda que selecciona el mouse
                    celX, celY = int(np.floor(posX / self.sizeX)), int(np.floor(posY / self.sizeY))

                    # Validamos que se eligió la primera fila
                    if celY == 0:
                        # click izquierdo
                        if (mouse_click[0] == 1):
                            self.automaton.state[celX] = 1

                        # click derecho
                        if (mouse_click[2] == 1):
                            self.automaton.state[celX] = 0

                        self.draw_polygon(celX, celY, self.automaton.state, 0)

                        # mostrar los cambios en la pantalla
                        pygame.display.flip()

    # dibujar un poligono en la cuadricula
    def draw_polygon(self, x, y, game_state_info, fill):
        # dibijamos el poligono de la celula
        polygon_info = [((x)     * self.sizeX, (y)     * self.sizeY),
                        ((x + 1) * self.sizeX, (y)     * self.sizeY),
                        ((x + 1) * self.sizeX, (y + 1) * self.sizeY),
                        ((x)     * self.sizeX, (y + 1) * self.sizeY)]

        if game_state_info[x] == 0:
            pygame.draw.polygon(self.screen, self.death_cell_color, polygon_info, fill)
        else:
            pygame.draw.polygon(self.screen, self.cell_color, polygon_info, 0)
