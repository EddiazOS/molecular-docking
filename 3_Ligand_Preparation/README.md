## Preparación del ligando HYW

- Ligando: HYW (inhibidor de p38 alpha en 6QE1)
- Fuente: RCSB PDB (https://www.rcsb.org/ligand/HYW)

### Descarga

Descargué el archivo SDF desde la página del ligando en RCSB y lo guardé como:
- `3_Ligand_Preparation/data/HYW.sdf`

### Conversión a PDBQT (ligando flexible)

Usé Open Babel para generar una conformación 3D, ajustar protonación a pH 7.4 y calcular cargas parciales de Gasteiger:

```bash
obabel 3_Ligand_Preparation/data/HYW.sdf \
  -O 3_Ligand_Preparation/outputs/HYW_prepared.pdbqt \
  -p 7.4 --gen3d --partialcharge gasteiger

