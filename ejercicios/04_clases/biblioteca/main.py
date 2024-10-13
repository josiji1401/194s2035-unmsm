class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"El libro '{libro.titulo}' del autor '{libro.autor}' ha sido añadido a la biblioteca '{self.nombre}'")

    def remover_libro(self, libro):
        for c_libro in self.libros:
            if c_libro.titulo == libro.titulo and c_libro.autor == libro.autor:
                self.libros.remove(c_libro)
                return f"Se ha prestado el libro '{libro.titulo}' del autor '{libro.autor}' ahora mismo"
        return f"Error: El libro '{libro.titulo}' del autor '{libro.autor}' no se encuentra en la estantería '{self.nombre}'"

    def buscar_libros(self, cadena_busqueda):
        resultados = []
        cadena_busqueda = cadena_busqueda.lower()
        for libro in self.libros:
            if cadena_busqueda in libro.titulo.lower() or cadena_busqueda in libro.autor.lower():
                resultados.append(libro)

        for libro in resultados:
            print(f"Título: {libro.titulo}, Autor: {libro.autor}")
        
        return resultados

#
        
