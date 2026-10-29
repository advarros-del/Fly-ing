# AGENTS.md — Fly-in

Instrucciones permanentes para trabajar en este proyecto.

## Forma de trabajo

1. **Proyecto de aprendizaje.** Ayudar a entender el problema, las decisiones
   de diseño y el funcionamiento del programa. Guiar antes de dar soluciones
   completas.
2. **Solo mostrar código cuando se pida explícitamente.** Si el usuario no
   solicita código, explicar con conceptos, pasos y ejemplos no ejecutables.
3. **No dar información no solicitada.** No anticipar diagnósticos, soluciones
   ni opiniones técnicas que el usuario no haya pedido.
4. **Revisar antes de actuar.** Comprobar el contexto del proyecto y el
   enunciado antes de proponer o realizar cambios.
5. **El usuario decide el siguiente paso.** Al comenzar una sesión, resumir
   solo el contexto necesario y esperar la tarea concreta.
6. **Comprensión y responsabilidad.** Cualquier código generado o modificado
   debe poder explicarse y defenderse durante la evaluación y la revisión por
   pares.
7. **Idioma.** Responder siempre en español, salvo que el usuario pida otro
   idioma. El `README.md` del proyecto debe escribirse en inglés, tal como
   exige el enunciado.

## Flujo diario

- Al empezar desde este directorio, leer `AGENTS.md`, `README.md` si existe y
  consultar `flyin.pdf` cuando haga falta confirmar un requisito.
- No crear ni actualizar un archivo de progreso salvo que el usuario lo pida
  expresamente.
- Antes de modificar algo, explicar brevemente qué se va a cambiar cuando la
  decisión pueda afectar al diseño.
- Al terminar, indicar qué se ha hecho y qué comprobaciones se han ejecutado,
  sin añadir información no solicitada.

## Reglas técnicas del proyecto

- Usar Python 3.10 o posterior.
- Mantener el proyecto completamente orientado a objetos.
- No usar librerías que implementen lógica de grafos, como `networkx` o
  `graphlib`.
- Mantener tipado completo y validar con `mypy`.
- Cumplir `flake8` y documentar funciones y clases con docstrings PEP 257.
- Gestionar errores de forma explícita y usar context managers para recursos.
- Incluir un `Makefile` con, como mínimo, `install`, `run`, `debug`, `clean` y
  `lint`.
- Añadir pruebas para el parser, las reglas de ocupación, las capacidades,
  los movimientos restringidos y los casos límite.
- Respetar el formato de entrada y salida del enunciado. Los errores de
  parsing deben indicar la línea y la causa.

## Contexto funcional

Fly-in simula el desplazamiento de varios drones desde un `start_hub` hasta un
`end_hub` en una red de zonas conectadas. El objetivo es llevar todos los
drones en el menor número posible de turnos, respetando:

- capacidades de las zonas (`max_drones`);
- capacidades de las conexiones (`max_link_capacity`);
- zonas bloqueadas, restringidas y prioritarias;
- movimientos de coste uno o dos turnos;
- ocupación, salidas simultáneas y esperas;
- prevención de conflictos y bloqueos;
- distribución de drones entre varias rutas.

La solución debe incluir parser, representación del grafo sin librerías
prohibidas, búsqueda o planificación de rutas, motor de simulación, salida
paso a paso y representación visual mediante terminal o interfaz gráfica.

