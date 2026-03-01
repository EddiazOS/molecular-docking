# Análisis de los resultados de docking 6QE1.

## A) Interpretación de afinidad.

El docking generó 9 poses con afinidades de entre -10.94 a -7.88 kcal, dentro de esta, la mejor pose, es la 1, mostrando una energía de -10.94 kcal7mol, lo que sufiere una unión favorable en el contexto de docking académico. 

## B) Convergencia y RMSD
Las poses 2 y 3 presentan una afinidad similar de -10.85 y -9.94 respectivamente, sin embargo los resultados de distancias relativas upper bound y low bound para la pose 2 dieron alejadas de rango aceptable > 2.0 A. Esto puede significar orientaciones relativas menos consistentes con la pose de mínima energía, mientras que en la pose 3, las distancias relativas se mantienen cerca del rango, lo cual indica a pensar un posible poso energético en común con la pose 1.

## C) Interacciones (HBonds, Hydrophobic)
En la inspección cualitativa en PyMOL, el núcleo aromático principal del ligando permanece ubicado dentro de un bolsillo hidrofóbico definido, mientras que los sustituyentes periféricos muestran mayor variabilidad orientacional. No se realizó todavía un conteo cuantitativo de puentes de hidrógeno, pero se observan contactos cercanos entre grupos polares del ligando y residuos del sitio activo.

## D) Limitaciones
Este análisis se basa en un único protocolo de docking rígido, sin considerar flexibilidad extensa de la proteína ni efectos explícitos de solvente. Además, no se ha comparado la pose predicha con una estructura cristalográfica real del complejo, por lo que las conclusiones son principalmente ilustrativas y adecuadas para fines académicos.