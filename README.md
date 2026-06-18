# TPO - Introduccion a la Algoritmia 
## Grupo 3

### Alcance del Sprint 1
El sistema permite administrar las selecciones participantes del Mundial de Futbol de 1930. Las funcionalidades son: 
* **Alta:** Agregar una nueva seleccion validando que el pais exista, el codigo sea unico y positivo, el grupo sea una letra entre A y H, y que los goles y partidos no sean negativos.
* **Modificacion:** Modificar el nombre de una seleccion existente buscandola por codigo.
* **Baja:** Eliminar una seleccion existente, siempre que no tenga partidos jugados.
* **Listado:** Mostrar todas las selecciones con sus datos: IdInterno, Codigo, Pais, Grupo, Partidos Jugados, GF y GC.

Cada seleccion contiene: IdInterno, Codigo, Pais, Grupo, Partidos Jugados, Goles a Favor y Goles en Contra.

---

### Alcance del Sprint 2 
Se incorporaron funcionalidades de consulta y analisis sobre las selecciones cargadas:
* **Busqueda por codigo:** Busqueda secuencial que muestra todos los datos de la seleccion encontrada o informa si no existe.
* **Orden por goles a favor:** Listado ordenado de mayor a menor usando el metodo Burbuja. No utiliza sort() ni sorted()
* **Reporte filtrado por grupo:** Muestra solo las selecciones del grupo ingresado (A-H), con validacion y conteo de resultados.

#### Creditos adicionales opcionales
* **Orden por goles en contra:** Listado ordenado de mayor a menor usando el metodo Selecccion.
* **Reporte por partidos jugados:** Muestra las selecciones con mas partidos jugados que un numero ingresado por el usuario.
* **Contador de selecciones por grupo:** Incluido dentro del reporte filtrado por grupo, informa la cantidad de selecciones encontradas en el grupo consultado.

---

### Alcance del Sprint 3
En esta etapa se realizó una reestructuración para eliminar el uso de variables globales y se añadieron herramientas matriciales:

* **Refactorización y Modularización Obligatoria:** 
  * Creación de las estructuras principales (idinterno, codigos_seleccion, selecciones, grupo, partidos_jugados, goles_a_favor, goles_en_contra) dentro de una función específica que las retorna.
  * El programa principal recibe estas estructuras y las envía por parámetro a todas las funciones que las requieran, garantizando que ninguna función dependa de variables globales.

* **Reutilización de Búsquedas:** Implementación de funciones de búsqueda secuencial propias y reutilizables que reciben parámetros y retornan la posición o un valor especial si no existe el elemento. Se prohíbe terminantemente el uso de los operadores in, not in y del método .index().

* **Reporte 1 (Reporte Matricial Grupo / Rendimiento Ofensivo):** Visualización tabular bidimensional utilizando una estructura de lista de listas (matriz). Clasifica las selecciones cruzando su Grupo (Filas A-H) con su nivel de rendimiento ofensivo (Columnas: Bajo [0-3], Medio [4-8], Alto [más de 8 goles]). Funciona incluso sin registros cargados.

* **Reporte 2 (Indicadores Estadísticos Generales):** Generación de métricas generales del torneo mediante recorridos manuales, acumuladores, contadores y comparaciones directas (sin funciones automáticas), validando el caso de listas vacías. Informa:
  * Cantidad total de selecciones registradas.
  * Total y promedio de goles a favor y total de goles en contra.
  * Selección con mayor cantidad de goles a favor y selección con menor cantidad de goles en contra.
  * Grupo con mayor cantidad de selecciones.
  * Cantidad de selecciones sin partidos disputados.

* **Reporte 3 (Reporte Filtrado por Grupo y Partidos Jugados):** Reporte tabular que aplica simultáneamente dos filtros validados provistos por el usuario: selección de grupo (A-H) y cantidad mínima de partidos jugados. Muestra las coincidencias, informa el total encontrado o advierte si no hay registros que cumplan las condiciones.

---

### URL del repositorio
https://github.com/lucasabramo/TPO-Algoritmia-