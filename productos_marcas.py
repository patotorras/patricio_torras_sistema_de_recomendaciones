from recomendaciones import analizar_recomendaciones    


lista_productos = []
productos_disponibles = ["leche", "dulce de leche", "manteca", "queso blanco", "queso cremoso", "yogur", "crema"]
marcas_disponibles_leche = ["la serenisima", "armonia", "tregar"]
marcas_disponibles_dulce_de_leche = ["la serenisima", "ilolay", "vacalin"]
marcas_disponibles_manteca = ["la serenisima", "milkaut", "tonadita"]
marcas_disponibles_queso_blanco = ["la serenisima", "la paulina", "tonadita"]
marcas_disponibles_queso_cremoso = ["la serenisima", "la paulina", "veronica"]
marcas_disponibles_yogur = ["la serenisima", "ilolay", "milkaut"]
marcas_disponibles_crema = ["la serenisima", "tonadita", "vacalin"]

def imprimir_lista(productos_disponibles):
    """Función para imprimir la lista de productos disponibles.
    Args:        productos_disponibles (list): Lista de productos disponibles.
    Returns:        None
    """
    for producto in productos_disponibles:
        print(f"{producto}\n")
 

def validar_producto_ingresado(producto_ingresado, productos_disponibles):
    """Función para validar si el producto ingresado es válido.
    Args:        producto_ingresado (str): Producto ingresado por el usuario.
    Returns:        bool: True si el producto es válido, False en caso contrario.
    """
    
    for producto in productos_disponibles:
        if producto == producto_ingresado:
            return True 
    
    return False



def generar_lista_productos():
    """Función para generar una lista de productos ingresados por el usuario.
    Args:        None
    Returns:        list: Lista de productos ingresados por el usuario.
    """
    lista_productos = []
    
    while True:
        producto = input("Ingrese un producto (o 'fin' para terminar): ")
        
        if producto == "fin":
            break  
        
        if producto != "" and validar_producto_ingresado(producto, productos_disponibles):
            lista_productos.append(producto)
        else:
            print("Producto inválido. Ingrese un producto válido o 'fin'.")
    
    print(f"Lista de productos ingresados: {lista_productos}")      
    return lista_productos 


def elegir_marcas_producto(producto):
    """"Función para que el usuario seleccione la marca de cada producto ingresado.
    Args:        producto (str): Producto para el cual se seleccionará la marca.
    Returns:        str: Producto con la marca seleccionada."""
    
    lista_con_marcas = []
    if producto == "leche":
        print(f"Marcas disponibles para leche: {marcas_disponibles_leche}")
        marca_leche = input("Ingrese la marca de leche: ")
        lista_con_marcas.append("leche" + "_" + marca_leche)
        return producto + "_" + marca_leche
    elif producto == "dulce de leche":
        print(f"Marcas disponibles para dulce de leche: {marcas_disponibles_dulce_de_leche}")
        marca_dulce_de_leche = input("Ingrese la marca de dulce de leche: ")
        lista_con_marcas.append("dulce_de_leche" + "_" + marca_dulce_de_leche)
        return producto + "_" + marca_dulce_de_leche
    elif producto == "manteca":
        print(f"Marcas disponibles para manteca: {marcas_disponibles_manteca}")
        marca_manteca = input("Ingrese la marca de manteca: ")
        lista_con_marcas.append("manteca" + "_" + marca_manteca)
        return producto + "_" + marca_manteca
    elif producto == "queso blanco":
        print(f"Marcas disponibles para queso blanco: {marcas_disponibles_queso_blanco}")
        queso_blanco = input("Ingrese la marca de queso blanco: ")
        lista_con_marcas.append("queso_blanco" + "_" + queso_blanco)
        return producto + "_" + queso_blanco
    elif producto == "queso cremoso":
        print(f"Marcas disponibles para queso cremoso: {marcas_disponibles_queso_cremoso}")
        marca_queso_cremoso = input("Ingrese la marca de queso cremoso: ")
        lista_con_marcas.append("queso_cremoso" + "_" + marca_queso_cremoso)
        return producto + "_" + marca_queso_cremoso
    elif producto == "yogur":
        print(f"Marcas disponibles para yogur: {marcas_disponibles_yogur}")
        marca_yogur = input("Ingrese la marca de yogur: ")
        lista_con_marcas.append("yogur" + "_" + marca_yogur)
        return producto + "_" + marca_yogur
    elif producto == "crema":
        print(f"Marcas disponibles para crema: {marcas_disponibles_crema}")
        marca_crema = input("Ingrese la marca de crema: ")
        lista_con_marcas.append("crema" + "_" + marca_crema)
        return producto + "_" + marca_crema
    else:
        return []


 
def obtener_catalogo_completo():
    """Función para obtener un catálogo completo de productos con marcas disponibles.
    Args:        None
    Returns:        list: Lista de todos los productos disponibles con marcas."""
    
    catalogo = []
    
    
    for marca in marcas_disponibles_leche: catalogo.append(f"leche_{marca}")
    for marca in marcas_disponibles_dulce_de_leche: catalogo.append(f"dulce de leche_{marca}")
    for marca in marcas_disponibles_manteca: catalogo.append(f"manteca_{marca}")
    for marca in marcas_disponibles_queso_blanco: catalogo.append(f"queso blanco_{marca}")
    for marca in marcas_disponibles_queso_cremoso: catalogo.append(f"queso cremoso_{marca}")
    for marca in marcas_disponibles_yogur: catalogo.append(f"yogur_{marca}")
    for marca in marcas_disponibles_crema: catalogo.append(f"crema_{marca}")
    
    return catalogo
    
    
def obtener_datos_usuario():

    """Función para obtener los datos del usuario, hoy solo el nombre y la lista de productos con marcas seleccionadas.
    Args:        None
    Returns:        list: Lista con el nombre del usuario y la lista de productos con marcas seleccionadas."""
    
    nombre = input("Ingrese su nombre: ")
    print(f"---Seleccione productos para {nombre} ---")
    imprimir_lista(productos_disponibles)
    lista_base = generar_lista_productos()
    
    lista_con_marcas = []
    for p in lista_base:
        seleccion = elegir_marcas_producto(p)
        lista_con_marcas.append(seleccion)
    
    
    return   [nombre, lista_con_marcas]



def calcular_porcentaje_serenisima(lista_con_marcas):
    """"Función para calcular el porcentaje de productos de "la serenisima" en la lista de compras del usuario.
    Args:        lista_con_marcas (list): Lista de productos con marcas seleccionadas por el usuario.
    Returns:        float: Porcentaje de productos de "la serenisima" en la lista de compras del usuario."""
    
    total = len(lista_con_marcas)
    if total == 0:
        print("No se seleccionaron productos.")
        return 0.0
        
    contador_serenisima = 0
    
    for item in lista_con_marcas:
        if "la serenisima" in item.lower():
            contador_serenisima += 1
    
    porcentaje = (contador_serenisima / total) * 100
    
    print("-" * 30)
    print(f"Total de productos: {total}")
    print(f"Productos de primeras marcas: {contador_serenisima} ")
    print(f"Porcentaje: {porcentaje:.2f}%")
    print("-" * 30)
    
    return porcentaje 


def recomendar_productos_inteligentes(compras, pct, catalogo):
    """Función para recomendar productos inteligentes basados en el perfil de consumo del usuario.
    Args:        compras (list): Lista de productos con marcas seleccionadas por el usuario.
        pct (float): Porcentaje de productos de "la serenisima" en la lista de compras del usuario.
        catalogo (list): Lista de todos los productos disponibles.
    Returns:        list: Lista de productos recomendados."""
    
    recomendaciones = []
    es_fan_serenisima = pct >= 50
    
    for item in catalogo:
        if item not in compras:
            tiene_serenisima = "la serenisima" in item.lower()
            
           
            if es_fan_serenisima and tiene_serenisima:
                recomendaciones.append(item)
            elif not es_fan_serenisima and not tiene_serenisima:
                recomendaciones.append(item)
    return recomendaciones


def analizar_recomendaciones(u1, u2, pct1, pct2):
    """Función para analizar las recomendaciones basadas en los perfiles de consumo de dos usuarios.
    Args:        u1 (list): Lista con el nombre del primer usuario y su lista de productos con marcas seleccionadas.
        u2 (list): Lista con el nombre del segundo usuario y su lista de productos con marcas seleccionadas.
        pct1 (float): Porcentaje de productos de "la serenisima" en la lista de compras del primer usuario.
        pct2 (float): Porcentaje de productos de "la serenisima" en la lista de compras del segundo usuario.
    Returns:        None    """
    nombre1, compras1 = u1
    nombre2, compras2 = u2
    catalogo = obtener_catalogo_completo()
    
    comunes = []
    for item in compras1:
        if item in compras2 and item not in comunes:
            comunes.append(item)
        
    exclusivos1 = []
    for item in compras1:
        if item not in compras2 and item not in exclusivos1:
            exclusivos1.append(item)
        
    exclusivos2 = []
    for item in compras2:
        if item not in compras1 and item not in exclusivos2:
            exclusivos2.append(item)
            
    print("\n--- ANÁLISIS ---")
    print(f"Productos en común: {comunes}")
    print(f"Exclusivos de {nombre1}: {exclusivos1}")
    print(f"Exclusivos de {nombre2}: {exclusivos2}")
    
    print("\n--- RECOMENDACIONES POR PERFIL DE CONSUMO (Basado en tus gustos) ---")
    
    rec1 = recomendar_productos_inteligentes(compras1, pct1, catalogo)
    print(f"Para {nombre1}: Te sugerimos probar: {rec1}")
    
    rec2 = recomendar_productos_inteligentes(compras2, pct2, catalogo)
    print(f"Para {nombre2}: Te sugerimos probar: {rec2}")

    print("\n--- RECOMENDACIONES COLABORATIVAS (Basado en lo que compraron otros usuario) ---")
    # Si Usuario 2 compró algo que Usuario 1 no tiene, se lo recomendamos a Usuario 1
    if exclusivos2:
        print(f"Para {nombre1}: {nombre2} compró estos productos que te podrían gustar: {exclusivos2}")
    else:
        print(f"Para {nombre1}: No hay productos nuevos que {nombre2} haya comprado que tú no tengas.")

    if exclusivos1:
        print(f"Para {nombre2}: {nombre1} compró estos productos que te podrían gustar: {exclusivos1}")
    else:
        print(f"Para {nombre2}: No hay productos nuevos que {nombre1} haya comprado que tú no tengas.")