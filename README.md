# Patrones_De_Dise-o_UNAB

#Ejercicio 1:
Investigar y documentar críticas a los patrones de diseño. Mencione ejemplos concretos.

#Ejercicio 2:
Seleccione 3 patrones de diseño e implementarlos en Python. Arme ejemplos concretos de uso. Lo ideal es
elegir un patrón de cada clasificación.

#Ejercicio 3:
Piense en 3 problemas habituales de su vida diaria en los cuales podría aplicar patrones de diseño.

#Ejercicio 4:
Los patrones de diseño suelen poseer distintos nombres o denominaciones. Busque y arme una tabla con
los posibles distintos nombres usados.

#Ejercicio 5:
¿Qué son los antipatrones de diseño? Ejemplifique algunos casos

1. Los patrones de diseño son fundamentales porque actúan como un catálogo de soluciones validadas por la experiencia de otros desarrolladores que sirven como una manera convencional de resolver problemas recurrentes, generando una lectura de codigo mas limpia y reforzando la aplicación de los principios de diseño orientado a objetos.
Sin embargo, más allá de lo mencionado en clase, existen críticas importantes sobre su aplicación:
  - Muchas veces aplicamos patrones de diseño a problemas sencillos complejizando soluciones de manera innecesaria 
  - A la hora de hacer Testing unitario algunos patrones ocultan dependencias o mantienen estados que dificultan aislar el código para testearlo de forma automatizada. (Muy normal en el patron Singleton)
  - Ya existen patrones de diseño integrados en lenguajes como Python (Iterator o ciertas funciones del Strategy) y al implementarlos es considerado unaperdida de tiempo y codigo innecesario

2. Archivo: Ejercicio_2.py

3. Situaciones reales en las que se aplica estos patrones:
   Por ej:
   - El Patron observer es aplicado a las notificaciones del celular de un grupo de wsp. O tambien a cuando en el bingo el que saca la bolilla la anuncia a todos
   - El Patron facthory method es aplicado cuando en un restaurante pedis una comida por su nombre e internamente en la cocina se crea el alimento
   - El Patron Decorator es aplicado cuando en el dia a dia hace frio y una persona se aplica una capa extra de abrigo

4.
Nombre clásico |	También puede aparecer como
---------------|------------------------------
Factory Method |	Factory
Observer	     |  Pub/Sub
Decorator      |	Wrapper
Facade         |	Front Interface
Strategy       |	Policy Pattern
Singleton      |	Single Instance
Adapter        |	Wrapper Adapter
Command        |	Action Object
Builder        |	Object Builder

5. Los antipatrones son soluciones con malas practicas que generan resoluciones a medias que crear problemas a futuro. Algunas son:
  - "El codigo spaggheti" Código desordenado, lleno de dependencias y lógica mezclada
  - Crear clases con demasiadas funciones
  - No reutilizar codigo
  - "Lava Flow": Código viejo que nadie entiende pero nadie se anima a borrar
