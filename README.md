Simulacion de los 255 automatas basicos de dos dimensiones.

Este este trabajo se busca entender el funcionamiento de los autómatas celulares de dos dimensiones, con dos posibles valores en sus estados, 0 o 1 (vivo o muerto), estudiando las reglas que se pueden aplicar para su funcionamiento, en una vecindad de una sola casilla de distancia, una a la izquierda, el centro (la misma casilla) y una posición a la derecha. Esta vecindad permite 8 posibles configuraciones para la vecindad. Luego, como existen dos estados posibles como resultado para cada vecindad, podemos definir 256 autómatas celulares (28 = 256), que se denominan autómatas celulares elementales.

Función de las clases:

-	Main: Es el punto de inicio de la aplicación, crea el controlador y lo inicia mediante su método start()
-	Controller: Se encarga de pedir los datos configurables por el usuario, como la regla, el tamaño y las iteraciones, luego crea el autómata de dos dimensiones y el tablero (Board), y comienza la ejecución de la simulación.
-	Automaton2D: Contiene el estado de un autómata de dos dimensiones, las reglas que se le van a aplicar para calcular un nuevo estado, entre otros parámetros.
-	Board: Se encarga de la visualización en pantalla de la simulación, haciendo uso de la librería Pygame, también permite al usuario representar un estado inicial, antes de empezar la simulación
-	FileManager: Se encarga de la escritura de datos en un archivo, la usa la clase Board para guardar cada estado en el proceso de simulación del autómata.

La aplicación se desarrolló en el lenguaje de programación Python, con la ayuda de la librería Pygame, que facilita la visualización en pantalla de figuras como polígonos, líneas, etc. En esta versión, la aplicación solicita por medio de la interfaz de consola el número de la regla que desea aplicar (numero entre 0 y 255), el tamaño del lattice o del mapa de dos dimensiones de nuestro autómata y el número de iteraciones, luego, mediante la interfaz gráfica puede seleccionar el estado inicial del autómata, posteriormente se realizará la simulación y se guardarán los resultados en un archivo con formato .txt.

Para ejecutar mediante la consola se ejecuta mediante el comando: 
<p>Python Main.py</p> 

Al abrir la pantalla de Pygame, podemos configurar el estado inicial con el mouse, dando click izquierdo para colocar en 1 (vivo) el estado de una celda y con click derecho se coloca en 0 (muerta), luego presionando Enter, se da inicio a la simulación.

Referencias:

Funcionamiento de los autómatas celulares de dos dimensiones y vecindad de una casilla:
https://mathworld.wolfram.com/ElementaryCellularAutomaton.html

Pygame, herramienta para dibujar en pantalla:
https://www.pygame.org/docs/

