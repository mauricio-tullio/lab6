def agregar_categoria(categorias: set, nueva_categoria: str) -> set:
    categorias.add(nueva_categoria)
    return categorias


def registrar_libro(inventario: dict, isbn: str, titulo: str, autor: str, categoria: str, categorias: set) -> tuple:
    
    info_libro = (titulo, autor, categoria)
    inventario[isbn] = info_libro
    categorias = agregar_categoria(categorias, categoria)
    return inventario, categorias


def registrar_usuario(usuarios: dict, id_usuario: str, nombre: str) -> dict:
    usuarios[id_usuario] = {"nombre": nombre, "libros_prestados": []}
    return usuarios


def prestar_libro(
    isbn: str, id_usuario: str, inventario: dict, usuarios: dict) -> dict:
    
    if isbn not in inventario:
        raise ValueError(
            f"El libro con ISBN '{isbn}' no se encuentra en el inventario."
        )

    if id_usuario not in usuarios:
        raise ValueError(
            f"El usuario con ID '{id_usuario}' no está registrado."
        )

    usuarios[id_usuario]["libros_prestados"].append(isbn)
    del inventario[isbn]

    return usuarios