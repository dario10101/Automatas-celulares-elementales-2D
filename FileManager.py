from os import remove
from os import mkdir
import os.path as path


class FileManager:

    def __init__(self):
        self.path = "resultados"

        # Crea el directorio donde se van a guardar resultados
        self.create_directory(self.path)

    def write_new_line(self, id, name, content):
        base_name = self.path + "/" + name + "_" + str(id) + ".txt"
        f = open(base_name, 'a')
        f.write(",".join([str(c) for c in content]) + "\n")
        f.close()

    def delete(self, id, name):
        base_name = self.path + "/" + name + "_" + str(id) + ".txt"

        if path.exists(base_name):
            remove(base_name)

    def create_directory(self, directorio):
        try:
            mkdir(directorio)
        except OSError:
            print("Directorio existente: %s" % directorio)
        else:
            print("Se ha creado el directorio: %s " % directorio)



