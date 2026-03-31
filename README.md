# COTxGNN - Colombia: Reposicionamiento de Medicamentos

[![Website](https://img.shields.io/badge/Website-cotxgnn.yao.care-blue)](https://cotxgnn.yao.care)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Predicciones de reposicionamiento de medicamentos (drug repurposing) para Colombia utilizando el modelo TxGNN.

## Aviso Legal

- Los resultados de este proyecto son solo para fines de investigacion y no constituyen consejo medico.
- Los candidatos a reposicionamiento de medicamentos requieren validacion clinica antes de su aplicacion.

## Resumen del Proyecto

| Elemento | Cantidad |
|----------|----------|
| **Informes de Medicamentos** | 420 |
| **Predicciones Totales** | 73,068,418 |

## Metodos de Prediccion

### Metodo de Grafo de Conocimiento (Knowledge Graph)
Consulta directa de relaciones farmaco-enfermedad en el grafo de conocimiento TxGNN, identificando candidatos potenciales para reposicionamiento basados en conexiones existentes en la red biomedica.

### Metodo de Aprendizaje Profundo (Deep Learning)
Utiliza el modelo de red neuronal preentrenado TxGNN para calcular puntuaciones de prediccion, evaluando la probabilidad de nuevas indicaciones terapeuticas para medicamentos aprobados.

## Enlaces

- Sitio Web: https://cotxgnn.yao.care
- Articulo TxGNN: https://doi.org/10.1038/s41591-023-02233-x
