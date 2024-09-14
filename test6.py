import playsound


from diccionario import diccionario

from reproducir_traduccion import escuchar_traduccion

def normalizar_palabra(palabra):
    return palabra.strip().lower()

def detectar_idioma(palabra):
    palabra = normalizar_palabra(palabra)
    
    if palabra in diccionario:
        return "Kichwa", "Español", diccionario[palabra]
    
    for k, v in diccionario.items():
        if isinstance(v, list):
            if palabra in [x.lower() for x in v]:
                return "Español", "Kichwa", k
        else:
            if v.lower() == palabra:
                return "Español", "Kichwa", k
    
    return None, None, None

def realizar_traduccion():
    palabra = input("Introduce la palabra para traducir: ").strip()
    #return palabra
    
    if not palabra:
        print("Error: No has ingresado la palabra para traducir.")
        return
    
    idioma_origen, idioma_destino, traduccion = detectar_idioma(palabra)
    
    if traduccion:
        if isinstance(traduccion, list):
            traduccion = ', '.join(traduccion)
        print(f"La palabra se ingresó en {idioma_origen} y se tradujo a {idioma_destino}: {traduccion}")
    else:
        print("La palabra que ingresaste no se encuentra en nuestra base de datos.")

def mostrar_palabras_disponibles():
    palabras = "\n".join(sorted(diccionario.keys()))
    print(f"Palabras en Kichwa disponibles para traducir:\n\n{palabras}")

# MENÚ
while True:
    print("******************" "Menú:" "*******************")
    print("******************************************")
    print("*""1. Mostrar lista de palabras disponibles""*")
    print("*""2. Traducir palabra""                     *")
    print("*""3. Escuchar traducción""                  *")
    print("*""4. Salir""                                *")
    print("******************************************")
    
    opcion = input("Selecciona una opción (1/2/3/4): ").strip()
    
    if opcion == '1':  
        print("Opción 1 seleccionada")
        for i, palabra in enumerate(diccionario, start=1):
            print(f"{i}. {palabra}")
        while True:
            print("¿Quieres traducir una palabra?")
            print("1. Sí")
            print("2. No")
            seleccion = input("Selecciona una opción (1/2): ")
            print(diccionario)
            if seleccion == '1':
                realizar_traduccion()
                
                palabra=palabra

                print("¿Desea escuchar la traducción?")
                print("1. Sí")
                print("2. No")
                selec = input("Selecciona una opción (1/2): ")
                if selec == '1':
                    print (palabra)
                    escuchar_traduccion(palabra)
                elif selec == '2':
                    continue  
            elif seleccion == '2':
                break
    elif opcion == '2':
        print("Opción 2 seleccionada")
        realizar_traduccion()
    elif opcion == "3":
        print("Opción 3 seleccionada")
        palabra_a_escuchar = input("Introduce la palabra para escuchar su traducción: ").strip()
        escuchar_traduccion(palabra_a_escuchar)
    elif opcion == '4':
        print("Opción 4 seleccionada")
        print("Gracias por usar nuestro programa")
        print("Saliendo ...")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")
