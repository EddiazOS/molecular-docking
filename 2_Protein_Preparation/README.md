## Preparación de la proteína (6QE1)

- Proteína: p38 alpha (MAPK14)
- Método experimental: X-RAY DIFFRACTION
- Resolución: 1.85 A
- Estado: holo (P38 alpha complex with AR117046 / HYW)

Paso realizados:
1. Creé la carpeta ´2_Protein_Preparation/data´
2. Descargué el archivo PDB con:
	- ´wget https://files.rcsb.org/download/6QE1.pdb´
3. Guardé el archivo en ´2_Protein_Preparation/data/6QE1.pdb´
4. Limpieza de proteína con:
	- grep "^ATOM" 6QE1.pdb > 6QE1_clean.pdb
5. Conversión a formato PDBQT con Obabel:
	- Se añadieron cargas parciales (Gasteiger) y tipos PDBQT
	- obabel 2_Protein_Preparation/outputs/6QE1_clean.pdb \
  		-O 2_Protein_Preparation/outputs/6QE1_prepared.pdbqt \
  		-xr --partialcharge gasteiger
	Archivo generado 
		6QE1_prepared.pdbqt
6 se verificó el número de átomos como:
	- grep "^ATOM" 2_Protein_Preparation/outputs/6QE1_prepared.pdbqt | wc -l
