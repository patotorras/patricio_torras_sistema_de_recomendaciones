from productos_marcas import obtener_datos_usuario, calcular_porcentaje_serenisima, analizar_recomendaciones
 
  

def menu():
    """Función principal para ejecutar el programa.
    Args:        None
    Returns:        None"""
    
    usuario1 = obtener_datos_usuario()
    pct1 = calcular_porcentaje_serenisima(usuario1[1])
    
    usuario2 = obtener_datos_usuario()
    pct2 = calcular_porcentaje_serenisima(usuario2[1])
    
    # Ahora sí pasamos los 4 argumentos
    analizar_recomendaciones(usuario1, usuario2, pct1, pct2)



if __name__ == "__main__":
    menu()

