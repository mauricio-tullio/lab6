def parsear_producto(linea: str):
    """
    Entrada:
        linea: str con formato "codigo,nombre,precio,cantidad"
    Salida:
        dict: {"codigo" : codigo:str, "nombre" : nombre:str, "precio" : precio:float, "cantidad" : cantidad:int}
    """
    # Tu código empieza aquí. Recuerda eliminar el 'pass'
    if not isinstance(linea, str):
        raise ValueError("El parametro 'linea' debe ser un string.")

    partes = linea.split(",")
    if len(partes) != 4:
        raise ValueError(
            "La linea debe contener 4 elementos separados por coma."
        )

    codigo, nombre, precio, cantidad = [p.strip() for p in partes]

    if not codigo or not nombre:
        raise ValueError("El codigo y el nombre no pueden estar vacios.")

    try:
        precio = float(precio)
    except ValueError:
        raise ValueError(
            f"El precio '{precio}' no es un numero valido."
        )

    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")

    try:
        cantidad = int(cantidad)
    except ValueError:
        raise ValueError(
            f"La cantidad '{cantidad}' no es un entero valido."
        )

    if cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa.")

    return {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
    }


def resumen_de_producto(linea: str) -> str:
    """
    Entrada:
        linea: str con formato "codigo,nombre,precio,cantidad"
    Salida:
        str: "CODIGO - NOMBRE: $VALOR" (VALOR = precio*cantidad redondeado a 1 decimal)
    """
    # Tu código empieza aquí. Recuerda eliminar el 'pass'

    producto = parsear_producto(linea)
    valor = round(producto["precio"] * producto["cantidad"], 1)
    return f"{producto['codigo']} - {producto['nombre']}: ${valor}"

def _validar_lineas(lineas: list) -> None:
    if not isinstance(lineas, list) or not lineas:
        raise ValueError(
            "El parametro 'lineas' debe ser una lista y no puede estar vacia."
        )

    for linea in lineas:
        if not isinstance(linea, str):
            raise ValueError(
                f"El elemento '{linea}' no es una cadena de texto (str)."
            )
        
def resumen_de_lotes(lineas: list) -> list:
    """
    Entrada:
        lines: list de str, no vacía
    Salida:
        list de str con resúmenes por producto (usa resumen_de_producto)
    """
    # Tu código empieza aquí. Recuerda eliminar el 'pass'

    _validar_lineas(lineas)
    salida = []
    for linea in lineas:
        salida.append(resumen_de_producto(linea))
    return salida


def valor_de_lote(lineas: list) -> float:
    """
    Entrada:
        lineas: list de str, no vacía
    Salida:
        float: valor total (suma de precio*cantidad) redondeado a 1 decimal
    """
    # Tu código empieza aquí. Recuerda eliminar el 'pass'
    _validar_lineas(lineas)
    total = 0.0
    for linea in lineas:
        producto = parsear_producto(linea)
        total += producto["precio"] * producto["cantidad"]
    return round(total, 1)


def producto_maximo_valor(lineas: list) -> str:
    """
    Entrada:
        lineas: list de str, no vacía
    Salida:
        str: resumen del producto de mayor (precio*cantidad). En empate, el primero.
    """
    # Tu código empieza aquí. Recuerda eliminar el 'pass'
    _validar_lineas(lineas)

    primer_producto = parsear_producto(lineas[0])
    max_producto = primer_producto
    valor_max = primer_producto["precio"] * primer_producto["cantidad"]

    for linea in lineas[1:]:
        producto = parsear_producto(linea)
        valor_actual = producto["precio"] * producto["cantidad"]

        if valor_actual > valor_max:
            valor_max = valor_actual
            max_producto = producto

    valor_redondeado = round(valor_max, 1)
    return f"{max_producto['codigo']} - {max_producto['nombre']}: ${valor_redondeado}"


if __name__ == "__main__":
    products = [
        "P001,Lapiz,0.5,100",
        "P002,Cuaderno,1.25,50",
        "P003 , Borrador ,1.35 , 10"
    ]
    # ejemplos rápidos para visualizar (descomenta cuando implementes)
    print(resumen_de_producto(products[0]))       # "P001 - Lapiz: $50.0"
    print(resumen_de_lotes(products))             # ["P001 - ...", "P002 - ...", "P003 - ..."]
    print(valor_de_lote(products))                # 126.0
    print(producto_maximo_valor(products))        # "P002 - Cuaderno: $62.5"
