from modelos_biblioteca import agregar_categoria, prestar_libro, registrar_libro, registrar_usuario

categorias = set()
inventario = {}
usuarios = {}

categorias = agregar_categoria(categorias, "Fantasía")
categorias = agregar_categoria(categorias, "Ciencia Ficción")
print("Categorías cargadas:", categorias)

inventario, categorias = registrar_libro(
    inventario=inventario,
    isbn="978-0140449136",
    titulo="La Odisea",
    autor="Homero",
    categoria="Clásicos",
    categorias=categorias,
)

inventario, categorias = registrar_libro(
    inventario=inventario,
    isbn="978-0747532699",
    titulo="Harry Potter",
    autor="J.K. Rowling",
    categoria="Fantasía",
    categorias=categorias,
)

print("Inventario:", inventario)
print("Categorías (se agregó 'Clásicos' automáticamente):", categorias)

print("\n--- Registrar Usuario ---")
usuarios = registrar_usuario(usuarios, "U001", "Mauricio Tullio")
usuarios = registrar_usuario(usuarios, "U002", "Ana Gómez")
print("Usuarios registrados:", usuarios)

print("\n--- Prestar Libro ---")
usuarios = prestar_libro("978-0747532699", "U001", inventario, usuarios)

print("Libros del usuario U001:", usuarios["U001"]["libros_prestados"])
print("Inventario actual:", inventario)

