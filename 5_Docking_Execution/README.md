## Ejecución de AutoDock Vina para el complejo 6QE1–HYW

La simulación de docking se realizó utilizando AutoDock Vina (versión 7ac2999-mod) con el siguiente comando, ejecutado desde la carpeta `5_Docking_Execution`:

```bash
vina --config ../4_Grid_Definition/outputs/config.txt \
     --out outputs/out.pdbqt > outputs/docking.log

### Resultados de afinidad de Vina

A continuación se resumen las afinidades de unión y los valores de RMSD reportados por Vina para los nueve modos generados:

| Modo | Afinidad (kcal/mol) | RMSD l.b. (Å) | RMSD u.b. (Å) |
|------|----------------------|---------------|---------------|
| 1    | -10.94               | 0.00          | 0.00          |
| 2    | -10.85               | 1.41          | 4.12          |
| 3    | -9.94                | 1.43          | 2.28          |
| 4    | -9.12                | 6.24          | 8.82          |
| 5    | -9.11                | 1.49          | 2.33          |
| 6    | -9.08                | 6.80          | 8.73          |
| 7    | -8.92                | 3.98          | 10.31         |
| 8    | -7.98                | 3.98          | 10.46         |
| 9    | -7.88                | 5.15          | 10.68         |

### Selección de la pose representativa

- La mejor energía de unión se obtuvo para el **modo 1** (-10.94 kcal/mol), que se tomó como pose principal.  
- Los modos 2 y 3 presentan afinidades similares y valores de RMSD bajos respecto al modo 1, lo que sugiere una familia de conformaciones relacionadas.  
- En la inspección visual en PyMOL, el núcleo aromático primidil–fenil del ligando se mantiene anclado en el bolsillo en los modos 1 y 3, mientras que otras poses muestran orientaciones menos consistentes con el sitio de unión esperado.

Para análisis posteriores, se guardó el complejo proteína–ligando correspondiente al modo 1 en:

- `5_Docking_Execution/outputs/6QE1_HYW_best1.pdb`
