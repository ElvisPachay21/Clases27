# declarar el diccionario

opciones = {
    "izquierda": "Te encontraste con un dragón", 
    "derecha": "Encontraste un tesoro",
    "adelante": "Caíste en el pozo"
}

eleccion = input("Estás en un cruce. ¿Quieres ir a la derecha, izquierda o adelante?: ").strip().lower()

if eleccion in opciones:
    print("Respuesta: ", opciones[eleccion])
else:
    print("Opción equivocada")
