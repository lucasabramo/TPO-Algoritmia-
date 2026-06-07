TPO - Introduccion a la Algoritmia 
Grupo 3
Alcance del Sprint 1
El sistema permite administrar las selecciones participantes del Mundial de Futbol de 1930. Las funcionalidades son: 
- Alta:Agregar una nueva seleccion validando que el pais exista, el codigo sea unico y positivo, el grupo sea una letra entre A y H, y que los goles y partidos no sean negativos.
- Modificacion: Modificar el nombre de una seleccion existente buscandola por codigo.
- Baja:Eliminar una seleccion existente, siempre que no tenga partidos jugados.
- Listado:Mostrar todas las selecciones con sus datos: IdInterno, Codigo, Pais, Grupo, Partidos Jugados, GF y GC.

Cada seleccion contiene:IdInterno, Codigo, Pais, Grupo, Partidos Jugados, Goles a Favor y Goles en Contra.

Alcance del Sprint 2 
Se incorporaron funcionalidades de consulta y analisis sobre las selecciones cargadas:
- Busqueda por codigo: Busqueda secuencial que muestra todos los datos de la seleccion encontrada o informa si no existe.
- Orden por goles a favor: Listado ordenado de mayor a menor usando el metodo Burbuja. No utiliza sort() ni sorted()
- Reporte filtrado por grupo: Muestra solo las selecciones del grupo ingresado (A-H), con validacion y conteo de resultados.

Creditos adicionales opcionales
- Orden por goles en contra: Listado ordenado de mayor a menor usando el metodo Selecccion.
- Reporte por partidos jugados: Muestra las selecciones con mas partidos jugados que un numero ingresado por el usuario.
- Contador de selecciones por grupo: Incluido dentro del reporte filtrado por grupo, informa la cantidad de selecciones encontradas en el grupo consultado.

URL del repositorio
https://github.com/lucasabramo/TPO-Algoritmia-