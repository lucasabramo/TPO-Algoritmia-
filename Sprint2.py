'''TP ABM- Mundial de Futbol
Contexto general
Se necesita un sistema para administrar informacion de un Mundial. El desarrollo se
realizara en etapas. En cada sprint se agregará funcionalidad nueva sobre lo ya
construido, por lo tanto el código deberá estar organizado en funciones y preparado para
crecer.
El trabajo se realizará en 3 sprints y una entrega final.
Sprint 1 - Gestion de selecciones
En esta primera etapa se deberá desarrollar un sistema que permita administrar las
selecciones participantes.
Cada selección tendrá:
· Código de selección.
. Nombre del país.
. Grupo al que pertenece.
· Cantidad de partidos jugados.
. Goles a favor.
· Goles en contra.
El sistema deberá presentar un menú de opciones inicialmente:
Alta de selección
Ingresar una nueva selección validando que:
· El código sea positivo. El código no esté repetido.
. El nombre no debe contener numeros.
· El grupo sea una letra entre A y H. Permitir una sola letra.
. Los puntos y goles no sean negativos.
Modificacion de seleccion
permitir modificar los datos de una seleccion en particular. No se permite el cambio de Grupo.
Baja de selección
Eliminar una seleccion existente. No se podra eliminar una seleccion si ya posee partidos jugados.
Listado general
Mostrar todas las selecciones por el momento sin orden alguno, incluyendo:
IdInterno | Código | País | Grupo | Partidos Jugados | GF | GC'''

#DATOS
idinterno=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
codigos_seleccion=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115]
selecciones=["Uruguay","Argentina","Estados Unidos","Chile","Mexico","Brasil","Paraguay","Peru","Bolivia","Francia","Rumania","Belgica","Yugoslavia","España","Italia"]
paises_mundial =  [
    # América del Sur
    "Argentina", "Bolivia", "Brasil", "Chile", "Colombia", "Ecuador", "Paraguay", "Peru", "Uruguay", "Venezuela",

    # América del Norte, Central y Caribe
    "Antigua Y Barbuda", "Bahamas", "Barbados", "Belice", "Bermudas", "Canada", "Costa Rica", "Cuba", "Curazao", "Dominica", 
    "El Salvador", "Estados Unidos", "Granada", "Guatemala", "Guyana", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", 
    "Panama", "Puerto Rico", "Republica Dominicana", "San Cristobal Y Nieves", "San Vicente Y Las Granadinas", "Santa Lucia", "Surinam", "Trinidad Y Tobago",
    "Anguila", "Aruba", "Islas Caiman", "Islas Turcas Y Caicos", "Islas Virgenes Britanicas", "Islas Virgenes De Los Estados Unidos", "Montserrat",

    # Europa 
    "Albania", "Alemania", "Alemania Democratica", "Andorra", "Armenia", "Austria", "Azerbaiyan", "Belgica", "Bielorrusia", "Bosnia Herzegovina", 
    "Bulgaria", "Checoslovaquia", "Chipre", "Ciudad Del Vaticano", "Croacia", "Dinamarca", "Escocia", "Eslovaquia", "Eslovenia", "España", "Estonia", 
    "Finlandia", "Francia", "Gales", "Georgia", "Gibraltar", "Grecia", "Hungria", "Inglaterra", "Irlanda", "Irlanda Del Norte", 
    "Islandia", "Islas Feroe", "Israel", "Italia", "Kazajistan", "Kosovo", "Letonia", "Liechtenstein", "Lituania", "Luxemburgo", "Macedonia Del Norte", 
    "Malta", "Moldavia", "Monaco", "Montenegro", "Noruega", "Paises Bajos", "Polonia", "Portugal", "Reino Unido", "Republica Checa", "Rumania", "Rusia", 
    "San Marino", "Serbia", "Suecia", "Suiza", "Turquia", "Ucrania", "Union Sovietica", "Yugoslavia",

    # África 
    "Angola", "Argelia", "Benin", "Botsuana", "Burkina Faso", "Burundi", "Cabo Verde", "Camerun", "Chad", "Comoras", 
    "Congo", "Costa De Marfil", "Egipto", "Eritrea", "Esuatini", "Etiopia", "Gabon", "Gambia", "Ghana", "Guinea", 
    "Guinea Ecuatorial", "Guinea-Bisau", "Kenia", "Lesoto", "Liberia", "Libia", "Madagascar", "Malaui", "Mali", "Marruecos", 
    "Mauricio", "Mauritania", "Mozambique", "Namibia", "Niger", "Nigeria", "Republica Centroafricana", "Republica Democratica Del Congo", 
    "Ruanda", "Santo Tome Y Principe", "Senegal", "Seychelles", "Sierra Leona", "Somalia", "Sudafrica", "Sudan", "Sudan Del Sur", "Tanzania", "Togo", 
    "Tunez", "Uganda", "Yibuti", "Zaire", "Zambia", "Zimbabue",

    # Asia
    "Afganistan", "Arabia Saudita", "Australia", "Bahrein", "Bangladesh",  "Birmania", "Brunei", "Butan", "Camboya", "China", "Corea Del Norte", 
    "Corea Del Sur", "Emiratos Arabes Unidos", "Filipinas", "Guam", "Hong Kong", "India", "Indonesia", "Irak", "Iran", "Japon", 
    "Jordania", "Kirguistan", "Kuwait", "Laos", "Libano", "Macao", "Malasia", "Maldivas", "Mongolia", "Nepal", 
    "Oman", "Pakistan", "Palestina", "Qatar", "Singapur", "Siria", "Sri Lanka", "Tailandia", "Taiwan", "Tayikistan", "Timor Oriental", 
    "Turkmenistan", "Uzbekistan", "Vietnam", "Yemen",

    # Oceanía 
    "Fiyi", "Islas Cook", "Islas Marshall", "Islas Salomon", "Kiribati", "Micronesia", "Nauru", "Nueva Caledonia", "Nueva Zelanda", "Palaos", 
    "Papua Nueva Guinea", "Samoa", "Samoa Americana", "Tahiti", "Tonga", "Tuvalu", "Vanuatu"

    #Explicacion de la lista de los paises del mundial:
    '''Decidimos hacer una lista con todos los paises reconocidos actualmente para que cuando el usuario inserte el nombre de una seleccion, se valide que sea un pais participante del mundial o un pais que ya no este anotado.
    dejando de lado a propósito países que ya no existen o que cambiaron de nombre, como Yugoslavia, Checoslovaquia, Unión Soviética, Zaire, etc.
    tambien dejando de lado a propósito a los paises que no son reconocidos por la FIFA, como Kosovo, Gibraltar, etc.'''
    
]

grupo=["C","A","D","A","A","B","D","C","B","A","C","D","B","H","H"]
partidos_jugados=[4,5,3,3,3,2,2,2,2,3,2,2,3,0,0]
goles_a_favor=[15,18,7,5,4,5,1,1,0,4,3,0,7,0,0]
goles_en_contra=[3,9,8,3,13,3,4,4,8,5,5,5,7,0,0]

#FUNCIONES
#MUESTRA OPCIONES DEL MENU
#Autor: Lucas Abramo
def opciones_menu():
    print("1: Alta de seleccion")
    print("2: Modificacion de seleccion")
    print("3: Baja de seleccion")
    print("4: Listado general")
    print("5: Busqueda por codigo")
    print("6: Orden por goles a favor")
    print("7: Orden por goles en contra")
    print("8: Reporte filtrado por grupo")
    print("9: Salir")
# FUNCION LISTADO 
# Autor: Lucas Abramo
def listado():
    i = 0
    print(f"{'Idinterno':<10} | {'Codigo':<7} | {'Pais':<20} | {'Grupo':<6} | {'Partidos Jugados':<17} | {'GF':<4} | {'GC':<4}")
    print("-" * 87)
    while i < len(selecciones):
        print(f"{idinterno[i]:<10} | {codigos_seleccion[i]:<7} | {selecciones[i]:<20} | {grupo[i]:<6} | {partidos_jugados[i]:<17} | {goles_a_favor[i]:<4} | {goles_en_contra[i]:<4}")
        i += 1
    print("-" * 87)
    
#FUNCION ALTA DE SELECCION
# Autor: Gael Terrado 
def alta_seleccion():
    print ("\n --ALTA DE SELECCION--")
    #--CODIGO DE LA SELECCION--
    codigo=int(input("Ingrese el codigo de la seleccion: "))
    while codigo<=0 or codigo in codigos_seleccion or len(str(codigo)) != 3:
        print("Codigo invalido. Debe ser un numero positivo de 3 digitos y no repetido.")
        codigo=int(input("Ingrese el codigo de la seleccion: "))

    #--NOMBRE DEL PAIS--
    nombre=input("Ingrese el nombre de la seleccion: ").strip().title()
    while nombre not in paises_mundial or nombre in selecciones:
        print("Nombre invalido. Debe ser una seleccion participante del mundial o un pais que ya no este anotado.")
        nombre=input("Ingrese el nombre de la seleccion: ").strip().title() 
        
    #--GRUPO AL QUE PERTENECE--
    letra=input("Ingrese al grupo que pertenece la seleccion (grupo entre la A-H):").upper()
    while letra not in ['A','B','C','D','E','F','G','H']:
        print("Grupo invalido. Debe ser una letra entre A y H.")
        letra=input("Ingrese al grupo que pertenece la seleccion (grupo entre la A-H):").upper()

    #--CANTIDAD DE PARTIDOS JUGADOS--
    partidosJugados=int(input("Ingrese la cantidad de partidos jugados de la seleccion: "))
    while partidosJugados<0:
        print ("Cantidad de partidos jugados invalido. No puede ser un numero negativo.")
        partidosJugados=int(input("Ingrese la cantidad de partidos jugados de la seleccion: "))

    #--GOLES A FAVOR--
    gf=int(input("ingrese la cantidad de goles a favor de la seleccion:"))
    while gf<0:
        print("Cantidad de goles a favor invalida. No puede ser un numero negativo.")
        gf=int(input("ingrese la cantidad de goles a favor de la seleccion:"))

    #--GOLES EN CONTRA--
    gc=int(input("ingrese la cantidad de goles en contra de la seleccion:"))
    while gc<0:
        print("Cantidad de goles en contra invalida. No puede ser un numero negativo.")
        gc=int(input("ingrese la cantidad de goles en contra de la seleccion:"))

    #--AGREGAR LOS DATOS A LAS LISTAS--
    idinterno.append(idinterno[-1]+1)
    codigos_seleccion.append(codigo)
    selecciones.append(nombre)
    grupo.append(letra)
    partidos_jugados.append(partidosJugados)
    goles_a_favor.append(gf)
    goles_en_contra.append(gc)

#FUNCION MODIFICACION DE SELECCION
# Autor: Thiago Santervas
def modificacion_seleccion():
    print("\n-- MODIFICACION DE SELECCION --")
    codigo_buscar = int(input("Ingrese el codigo de la seleccion que desea modificar: "))
    #Buscamos en que posicion de la lista se encuentra el codigo ingresado
    posicion= -1
    i=0
    while i < len(codigos_seleccion):
        if codigos_seleccion[i] == codigo_buscar:
            posicion = i
        i += 1
    #Si el codigo no se encuentra, se muestra un mensaje de error
    if posicion == -1:
        print("Codigo no encontrado.")
    else: 
        print(f"Modificando el equipo: {selecciones[posicion]}")
        #Modificamos el nombre del pais
        nuevo_pais= input("Nuevo nombre de la seleccion(pais): ").upper().strip().title() 
        es_pais_valido = False
        esta_repetido = False
        #  Comprobamos si el nuevo país existe en paises_mundial 
        r= 0 
        while r < len(paises_mundial):
            if paises_mundial[r] == nuevo_pais:
                es_pais_valido = True
            r += 1
        #  Comprobamos si el nuevo país ya esta registrado en selecciones
        r= 0 
        while r < len(selecciones):
            if selecciones[r] == nuevo_pais and r != posicion:
                esta_repetido = True
            r += 1
        #si no es un pais valido o ya esta registrado, se muestra un mensaje de error
        while es_pais_valido == False or esta_repetido == True:
            print("Nombre inválido o ya anotado en otra selección. Debe ser un país válido.")
            nuevo_pais= input("Nuevo nombre de la seleccion(pais): ").upper().strip().title()
            # Volvemos a chequear los datos ingresados
            es_pais_valido = False
            esta_repetido = False
        
            r= 0
            while r < len(paises_mundial):
                if paises_mundial[r] == nuevo_pais:
                    es_pais_valido = True
                r += 1
            r= 0
            while r < len(selecciones):
                if selecciones[r] == nuevo_pais and r != posicion:
                    esta_repetido = True
                r += 1
        # Cuando pasa el filtro, guardamos el cambio
        selecciones[posicion] = nuevo_pais
        print("Nombre de la seleccion modificado correctamente.")

        #modificacion de partidos jugados
        nuevo_partidos_jugados = int(input("Nueva cantidad de partidos jugados: "))
        while nuevo_partidos_jugados < 0:
            print("Cantidad de partidos jugados invalida. No puede ser un numero negativo.")
            nuevo_partidos_jugados = int(input("Nueva cantidad de partidos jugados: "))
        partidos_jugados[posicion] = nuevo_partidos_jugados
        print("Cantidad de partidos jugados modificada correctamente.")

        #modificacion de goles a favor
        nuevo_gf = int(input("Nueva cantidad de goles a favor: "))
        while nuevo_gf < 0:
            print("Cantidad de goles a favor invalida. No puede ser un numero negativo.")
            nuevo_gf = int(input("Nueva cantidad de goles a favor: "))
        goles_a_favor[posicion] = nuevo_gf
        print("Cantidad de goles a favor modificada correctamente.")

        #modificacion de goles en contra
        nuevo_gc = int(input("Nueva cantidad de goles en contra: "))
        while nuevo_gc < 0:
            print("Cantidad de goles en contra invalida. No puede ser un numero negativo.")
            nuevo_gc = int(input("Nueva cantidad de goles en contra: "))
        goles_en_contra[posicion] = nuevo_gc
        print("Cantidad de goles en contra modificada correctamente.")

    print ("-" * 50)


#FUNCION BAJA DE SELECCION
# Autor: Thiago Santervas
def baja_seleccion():
    print("\n--BAJA DE SELECCION--")
    codigo_buscar = int(input("Ingrese el codigo de la seleccion que desea eliminar: "))

    #Buscamos en que posicion de la lista se encuentra el codigo ingresado
    posicion =-1
    i=0
    while i < len(codigos_seleccion):
        if codigos_seleccion[i] == codigo_buscar:
            posicion = i
        i += 1
        #validamos si se puede borrar
    if posicion == -1:
        print("El codigo ingresado no existe")
    else:
        #si ya jugo partidos(mayo a 0); No se borra
        if partidos_jugados[posicion] > 0:
            print("No se puede eliminar la seleccion porque ya posee partidos jugados.")
        else:
            #Si tiene 0 partidos, lo borramos de todas las listas
            #Listas vacias temporales
            nuevo_id = []
            nuevo_codigo = []
            nuevo_pais = []
            nuevo_grupo = []
            nuevo_partidos = []
            nuevo_gf = []
            nuevo_gc = []
            r = 0
            nuevo_id_contador = 1 #contador para asignar nuevos idinternos de forma consecutiva
            while r < len(codigos_seleccion):
                if r != posicion: #si no es la posicion a eliminar, se agrega a las nuevas listas
                    nuevo_id.append(nuevo_id_contador)
                    nuevo_codigo.append(codigos_seleccion[r])
                    nuevo_pais.append(selecciones[r])
                    nuevo_grupo.append(grupo[r])
                    nuevo_partidos.append(partidos_jugados[r])
                    nuevo_gf.append(goles_a_favor[r])
                    nuevo_gc.append(goles_en_contra[r])
                    nuevo_id_contador += 1
                r += 1

            # Vaciamos las listas originales de afuera usando un while
            #Reemplazamos las listas originales por las nuevas listas sin la seleccion eliminada
            # Borramos el primer elemento hasta que queden vacías
            while len(codigos_seleccion) > 0:
                codigos_seleccion[:] = []
                selecciones[:] = []
                grupo[:] = []
                partidos_jugados[:] = []
                goles_a_favor[:] = []
                goles_en_contra[:] = []
                idinterno[:] = []  

            # Volvemos a pasar los datos guardados a las listas originales usando .append()
            # De esta forma modificamos las variables originales directamente
            k = 0
            while k < len(nuevo_codigo):
                idinterno.append(nuevo_id[k])
                codigos_seleccion.append(nuevo_codigo[k])
                selecciones.append(nuevo_pais[k])
                grupo.append(nuevo_grupo[k])
                partidos_jugados.append(nuevo_partidos[k])
                goles_a_favor.append(nuevo_gf[k])
                goles_en_contra.append(nuevo_gc[k])
                k += 1
            print("Seleccion eliminada correctamente.")

# FUNCION BUSQUEDA POR CODIGO
# Autor: Lucas Abramo   
def busqueda_por_codigo():
    print("\n--BUSQUEDA POR CODIGO--")
    busqueda=int(input("Ingrese un codigo para buscar el pais: "))
    posicion=-1
    i=0
    while i<len(codigos_seleccion):
        if codigos_seleccion[i]==busqueda:
            posicion=i
        i+=1
    if posicion==-1: 
        print("El pais no fue encontrado")
    else: 
        print("La seleccion fue encontrada")   
        print ("-" * 87) 
        print(f"{'Idinterno':<10} | {'Codigo':<7} | {'Pais':<22} | {'Grupo':<6} | {'Partidos Jugados':<20} | {'GF':<4} | {'GC':<4}")
        print(f"{idinterno[posicion]:<10} | {codigos_seleccion[posicion]:<7} | {selecciones[posicion]:<22} | {grupo[posicion]:<6} | {partidos_jugados[posicion]:<20} | {goles_a_favor[posicion]:<4} | {goles_en_contra[posicion]:<4}")
        print ("-" * 87)


#funcion orden por goles a favor (metodo burbuja)
#Autor: Gael Terrrado
def orden_goles_a_favor():
    print ("\n--ORDEN POR GOLES A FAVOR--")
    for i in range (0, len(goles_a_favor)-1):
        for j in range (i + 1, len(goles_a_favor)):
            if goles_a_favor[j] > goles_a_favor[i]:
                aux = goles_a_favor[j]
                goles_a_favor[j] = goles_a_favor[i]
                goles_a_favor[i] = aux
                #ordenamos las otras listas para que no se pierda la relacion entre los datos
                aux = idinterno[i]
                idinterno[i] = idinterno[j]
                idinterno[j] = aux
                
                aux = codigos_seleccion[i]
                codigos_seleccion[i] = codigos_seleccion[j]
                codigos_seleccion[j] = aux

                aux = selecciones[i]
                selecciones[i] = selecciones[j]
                selecciones[j] = aux

                aux = grupo[i]
                grupo[i] = grupo[j]
                grupo[j] = aux

                aux = partidos_jugados[i]
                partidos_jugados[i] = partidos_jugados[j]
                partidos_jugados[j] = aux

                aux = goles_en_contra[i]
                goles_en_contra[i] = goles_en_contra[j]
                goles_en_contra[j] = aux
    print("Listado ordenado por goles a favor:")
    listado()

#Funcion orden por goles en contra (metodo seleccion)
#Autor: Gael Terrado
def orden_goles_en_contra():
    print ("\n--ORDEN POR GOLES EN CONTRA--")
    for i in range (0, len(goles_en_contra)-1):
        posicion_menor = i
        for j in range (i + 1, len(goles_en_contra)):
            if goles_en_contra[j] > goles_en_contra[posicion_menor]:
                posicion_menor = j
        #intercambiamos el menor con el primer elemento del subarreglo
        aux = goles_en_contra[i]
        goles_en_contra[i] = goles_en_contra[posicion_menor]
        goles_en_contra[posicion_menor] = aux
        #ordenamos las otras listas para que no se pierda la relacion entre los datos
        aux = idinterno[i]
        idinterno[i] = idinterno[posicion_menor]
        idinterno[posicion_menor] = aux

        aux = codigos_seleccion[i]
        codigos_seleccion[i] = codigos_seleccion[posicion_menor]
        codigos_seleccion[posicion_menor] = aux

        aux = selecciones[i]
        selecciones[i] = selecciones[posicion_menor]    
        selecciones[posicion_menor] = aux

        aux = grupo[i]
        grupo[i] = grupo[posicion_menor]
        grupo[posicion_menor] = aux

        aux = partidos_jugados[i]
        partidos_jugados[i] = partidos_jugados[posicion_menor]
        partidos_jugados[posicion_menor] = aux

        aux = goles_a_favor[i]
        goles_a_favor[i] = goles_a_favor[posicion_menor]
        goles_a_favor[posicion_menor] = aux
    print("Listado ordenado por goles en contra:")
    listado()

# Funcion reporte filtrado por grupo 
# Autor: Thiago Santervas
def reporte_filtrado_grupo():
    print("\n-- REPORTE FILTRADO POR GRUPO --")
    
    # 1. Pedimos el grupo avisando que sea en mayúscula
    grupo_buscar = input("Ingrese la letra del grupo a consultar: ").upper()
    
    # Validamos que sea un grupo válido (De la A a la H)
    while grupo_buscar != "A" and grupo_buscar != "B" and grupo_buscar != "C" and grupo_buscar != "D" and grupo_buscar != "E" and grupo_buscar != "F" and grupo_buscar != "G" and grupo_buscar != "H":
        print("Grupo inválido. Debe ser una sola letra entre A y H.")
        grupo_buscar = input("Ingrese la letra del grupo a consultar: ").upper()
         
    print("\nSELECCIONES ENCONTRADAS:")
    print("-" * 87)
    print(f"{'Idinterno':<10} | {'Codigo':<7} | {'Pais':<22} | {'Grupo':<6} | {'Partidos Jugados':<20} | {'GF':<4} | {'GC':<4}")
    print("-" * 87)
    
    # 2. Mostrar únicamente las selecciones de ese grupo
    i = 0
    cantidad_encontrados = 0 
    
    while i < len(grupo):
        if grupo[i] == grupo_buscar:
            print(f"{idinterno[i]:<10} | {codigos_seleccion[i]:<7} | {selecciones[i]:<22} | {grupo[i]:<6} | {partidos_jugados[i]:<20} | {goles_a_favor[i]:<4} | {goles_en_contra[i]:<4}")
            cantidad_encontrados = cantidad_encontrados + 1
        i = i + 1

        
    # 3. Informar si no se encontraron selecciones en ese grupo
    if cantidad_encontrados == 0:
        print("No se encontraron selecciones registradas para el grupo seleccionado.")
    
    print (cantidad_encontrados, "selecciones encontradas en el grupo", grupo_buscar)
    print("-" * 87)

#PROGRAMA PRINCIPAL
# Autor: Lucas Abramo
def main():
    eleccion=0
    while eleccion!=9:
        print("\n--MENU DE OPCIONES--")
        opciones_menu()
        eleccion=int(input("Seleccion una opcion: "))
        print("-" * 20)
        if eleccion==1:
             alta_seleccion()
        elif eleccion==2:
            modificacion_seleccion()
        elif eleccion==3:
            baja_seleccion()
        elif eleccion==4:
            listado()
        elif eleccion==5:
            busqueda_por_codigo()
        elif eleccion==6:
            orden_goles_a_favor()
        elif eleccion==7:
            orden_goles_en_contra()
        elif eleccion==8:
            reporte_filtrado_grupo()
        else:
            print("Adios, gracias")
main() 