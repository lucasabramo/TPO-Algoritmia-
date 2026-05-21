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
def opciones_menu():
    print("1: Alta de seleccion")
    print("2: Modificacion de seleccion")
    print("3: Baja de seleccion")
    print("4: Listado general")
    print("5: Salir")

def listado():
    i = 0
    print(f"{'Idinterno':<10} | {'Codigo':<7} | {'Pais':<20} | {'Grupo':<6} | {'Partidos Jugados':<17} | {'GF':<4} | {'GC':<4}")
    print("-" * 85)
    while i < len(selecciones):
        print(f"{idinterno[i]:<10} | {codigos_seleccion[i]:<7} | {selecciones[i]:<20} | {grupo[i]:<6} | {partidos_jugados[i]:<17} | {goles_a_favor[i]:<4} | {goles_en_contra[i]:<4}")
        i += 1
    print("-" * 85)
    
        
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


#PROGRAMA PRINCIPAL
def main():
    eleccion=0
    while eleccion!=5:
        print("\n--MENU DE OPCIONES--")
        opciones_menu()
        eleccion=int(input("Seleccion una opcion: "))
        print("-" * 20)
        print("")
        if eleccion==1:
             alta_seleccion()
        elif eleccion==2:
            pass
        elif eleccion==3:
            pass
        elif eleccion==4:
            listado()
        else:
            pass
main()