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
paises_mundial = [ "Uruguay", "Argentina", "Brasil", "Chile", "Paraguay", "Peru", "Bolivia", "Ecuador", "Colombia", "Venezuela",
    # América del Norte y Central
    "Mexico", "Estados Unidos", "Cuba", "Haiti", "El Salvador", "Honduras", "Costa Rica", "Canada", "Trinidad y Tobago", "Jamaica", "Panama",
    # Europa
    "Francia", "Alemania", "Italia", "España", "Inglaterra", "Portugal", "Holanda", "Belgica", "Suecia", "Suiza", "Dinamarca", "Noruega",
    "Polonia", "Checoslovaquia", "Yugoslavia", "Rumania", "Hungria", "Austria", "Escocia", "Irlanda del Norte", "Irlanda", "Gales",
    "Bulgaria", "Rusia", "Ucrania", "Croacia", "Serbia", "Eslovenia","Grecia", "Turquia", "Republica Checa", "Eslovaquia", "Bosnia Herzegovina", "Islandia", "Finlandia", "Letonia", "Albania", "Estonia",
    # África
    "Marruecos", "Argelia", "Tunez", "Egipto", "Nigeria", "Camerun","Sudafrica", "Senegal", "Ghana", "Costa de Marfil", "Angola","Togo", "Zaire", "Zambia", "Congo",
    # Asia
    "Corea del Sur", "Japon", "Arabia Saudita", "Iran", "Irak", "Kuwait","China", "Indonesia",
    # Oceanía
    "Australia", "Nueva Zelanda",]
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
        opciones_menu()
        eleccion=int(input("Seleccion una opcion: "))
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