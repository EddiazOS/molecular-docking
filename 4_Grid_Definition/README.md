## Definición del Grid Box para 6QE1–HYW

- El centro del grid se definió como el centro de masa del ligando co-cristalizado HYW en la estructura 6QE1, obtenido en PyMOL con:
  - `select lig, resn HYW`
  - `print cmd.get_centerofmass("lig")`

Coordenadas usadas:
- center_x = Xc
- center_y = Yc
- center_z = Zc

Tamaño del grid:
- size_x = 20 Å
- size_y = 20 Å
- size_z = 20 Å

Justificación:
- Un cubo de 20 Å de lado es suficiente para cubrir el bolsillo de unión de p38α alrededor de HYW y permitir pequeñas variaciones en la posición del ligando durante el docking.
