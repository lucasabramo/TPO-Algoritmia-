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
#PROGRAMA PRINCIPAL
def main():
    eleccion=0
    while eleccion!=5:
        opciones_menu()
        eleccion=int(input("Seleccion una opcion: "))
        if eleccion==1:
            pass
        elif eleccion==2:
            pass
        elif eleccion==3:
            pass
        elif eleccion==4:
            listado()
        else:
            pass
main()()