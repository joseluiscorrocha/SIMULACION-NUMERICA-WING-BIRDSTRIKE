# SIMULACION-NUMERICA-Y-OPTIMIZACION-MULTIOBJETIVO-DE-UNA-SECCION-DE-ALA-ANTE-UN-IMPACTO-DE-AVE
Este proyecto trata sobre la simulación numérica y optimización multiobjetivo de una sección de ala ante un impacto de ave. El análisis estructural es parametrizado a través de Ábaqus, utilizando su librería para ejecutar scripts. Por otro lado se utilizan las librerías smt https://github.com/SMTorg/smt  para la construcción del modelo subrogado y pyswarms https://github.com/ljvmiranda921/pyswarms para la optimización.

A continuación, una breve descripción del uso de cada archivo.
- FEM_script: script principal para la creación del modelo en Ábaqus. Las variables de diseño son el espesor del revestimiento y el espesor de los larguerillos.
- FEM_script_angulo_impacto: script muy similar al anterior pero parametrizando el angulo de impacto en el modelo.
- FEM_script_impacto_envergadura: script muy similar al primero pero modificando la zona de impacto a lo largo de la envergadura.
- FEM_script_veloicdad: script muy similar al principal pero modificando la velocidad de impacto.
- postproceso_s: script de postproceso en abaqus para generar un report con las tensiones en el set de nodos del borde de ataque del modelo.
- postproceso_u_m_sdeg: script de postproceso en abaqus para generar reports de daño, desplazamiento y masa en el set de nodos en el borde de ataque del modelo.
- Representacion_datos_postproceso: script que coge los reports generados y genera las graficas correspondientes para representar las funciones objetivo.
- subrogado_y_optimizacion: script que no necesita ningun archivo extra para ejecutarse. Realiza la construccion del modelo subrogado con las funciones objetivo y los distintos casos de optimizacion propuestos en el trabajo de fin de grado.
