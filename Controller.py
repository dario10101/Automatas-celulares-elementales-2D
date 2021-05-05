from Board import Board
from Automaton2D import Automaton2D



class Controller:

    def __init__(self):
        self.my_automaton = 0
        self.my_board = 0

    def start(self):
        print("\n-----------------------------------------------------------------------")
        print("Automatas celulares elementales. Por:")
        print("Ruben Dario Dorado Cordoba\n")
        rule_number = self.read_integer_console("Digite el numero de la regla: ")
        aut_number = self.read_integer_console("Digite el tamaño del lattice: ")
        iteration_number = self.read_integer_console("Digite el numero de iteraciones: ")

        self.my_automaton = Automaton2D(rule_number, aut_number, iteration_number)

        # Parametros corerctos
        if self.my_automaton.create():
            print("\n - Ahora, podra dibujar el estado inicial en la primera linea de la pantalla.")
            print(" - Click izquierdo activa una celda y click derecho la desactiva")
            print(" - Presione Enter cuando termine de dibujar el estado inicial")
            input("\nPresione Enter para continuar ...")

            # Crear e iniciar el tablero
            self.my_board = Board(self.my_automaton)
            self.my_board.run()
        else:
            print("\nerror: " + self.my_automaton.error + "\n")

        print("Programa finalizado.")

    def read_integer_console(self, message):
        value = input(message)
        while not value.isnumeric():
            value = input("Error: debe ser un numero, mayor que cero.\n" + message)
        return int(value)





