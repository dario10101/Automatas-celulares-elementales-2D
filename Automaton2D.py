import numpy as np


class Automaton2D:

    def __init__(self, rule=30, size=40, iterations=20):
        # Valores por defecto
        self.min_rule = 0
        self.max_rule = 255
        self.min_size = 3
        self.max_size = 200
        self.min_iterations = 1
        self.max_iterations = 100
        self.error = ""

        # Valores definidos por el usuario
        self.rule = rule
        self.size = size
        self.iterations = iterations
        self.state = []

        # Vector de regla
        self.rule_array = np.zeros(8)

    def create(self):
        # Tamaño del lattice fuera de rango
        if self.size < self.min_size or self.size > self.max_size:
            self.error += "Tamaño del mapa fuera de rango (" + str(self.min_size) + "-" + str(self.max_size) + ")"
            return False

        # Numero de regla invalido
        if self.rule < self.min_rule or self.rule > self.max_rule:
            self.error += "Regla fuera del rango valido (" + str(self.min_rule) + "-" + str(self.max_rule) + ")"
            return False

        # NUmero de iteraciones no valido
        if self.iterations < self.min_iterations or self.iterations > self.max_iterations:
            self.error += "Numero de iteraciones no valido (" + str(self.min_iterations) + "-" + str(self.max_iterations) + ")"
            return False

        # Crear estado inicial vacio
        self.state = np.zeros(self.size)
        """
        self.state = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
                        ,0,0,0,0,0,0,0,0,0
                        ,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
                        ,0,0,0,0,0,0,0,0,0]
        """
        
        # Crear las normas de la regla definida
        self.create_rule_array()

        return True

    # Convertir la regla definida en su respectivo arreglo de 8 posiciones
    def create_rule_array(self):
        # Convertir numero decimal a binario en arreglo de 1 o 0
        rule_array_aux = list((bin(self.rule)))
        rule_array_aux.pop(0)
        rule_array_aux.pop(0)

        # Configurar el arreglo que define la regla
        dif = len(self.rule_array) - len(rule_array_aux)
        for i in range(0, len(rule_array_aux)):
            self.rule_array[i+dif] = int(rule_array_aux[i])

    def change_state(self, position, value):
        if position < self.size:
            self.state[position] = value

    # Aplicar nuevo estado
    def new_state(self):
        state_aux = np.copy(self.state)
        for index in range(0, len(state_aux)):
            # defino la situacion de la celda segun sus vecinos
            rule_array_index = self.find_rule_index(index)

            # asigno el nuevo estado
            new_index_state = self.rule_array[rule_array_index]
            state_aux[index] = new_index_state

        self.state = np.copy(state_aux)

    # Encuentra que posicion del arreglo de la regla debe aplicar
    def find_rule_index(self, state_position):
        left = state_position - 1
        rigth = state_position + 1

        # Frontera infinita
        if left < 0:
            left = self.size - 1
        if rigth >= self.size:
            rigth = 0

        rule_array_index = int(self.state[rigth] + (self.state[state_position] * 2) + (self.state[left] * 4))
        rule_array_index = len(self.rule_array) - rule_array_index - 1
        return rule_array_index



