---
layout: default
title: Clioquinol
parent: Evidencia Moderada (L3-L4)
nav_order: 131
evidence_level: L4
indication_count: 7
---

# Clioquinol
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **7** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Clioquinol: De Betametasona y Antibióticos (combinación tópica) a Candidiasis Cutánea

## Resumen en Una Frase

Clioquinol es un antimicrobiano tópico que en Colombia se comercializa en cremas combinadas con corticoide y antibióticos, como la crema tópica BETAGEN (betametasona y antibióticos).
El modelo TxGNN predice que podría ser efectivo para la **candidiasis cutánea**, pero **no hay ensayos clínicos registrados** y solo hay **6 publicaciones**, antiguas (1965-1988) e indirectas.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Betametasona y antibióticos (combinación tópica) |
| Nueva Indicación Predicha | Candidiasis cutánea |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, el clioquinol es un antimicrobiano tópico con actividad antifúngica. Se le atribuye una acción quelante de metales y de tipo ionóforo, pero esto es una inferencia y no un dato confirmado en la información recibida. Mecanísticamente podría ser aplicable a la candidiasis cutánea.

En las indicaciones aprobadas en Colombia, el clioquinol aparece dentro de combinaciones de corticoide con antibióticos, es decir, para dermatosis inflamatorias con componente infeccioso. La candidiasis cutánea es una infección superficial de la piel, por lo que la distancia clínica con el uso actual es corta. Aun así, la literatura solo evalúa el clioquinol dentro de cremas combinadas. Algunas combinaciones citadas contienen otro antifúngico (anfotericina, nistatina, tolnaftato), y no se puede aislar la contribución propia del clioquinol.

El puntaje alto de TxGNN (0.998) es solo una predicción. La evidencia es antigua, indirecta y sin ensayos registrados. Además, el clioquinol sistémico tiene antecedentes de neurotoxicidad (SMON), por lo que cualquier uso debería limitarse a la vía tópica.

De las demás indicaciones predichas, la más coherente mecanísticamente es la **micosis superficial** (L4). Su evidencia también es débil: un estudio preclínico de 2021 y un reporte clínico de 1958. Las predicciones de tiña profunda, granuloma de Majocchi e infecciones ectotrix/endotrix (L5) no tienen evidencia y normalmente requieren tratamiento sistémico. En la predicción de dermatofitosis de cuero cabelludo o barba, las 20 publicaciones recuperadas son falsos positivos por palabras clave y no aportan respaldo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [6459255](https://pubmed.ncbi.nlm.nih.gov/6459255/) | 1981 | ECA comparativo | J Int Med Res | Dos cremas de corticoide con antimicrobianos (una con clioquinol) en 154 pacientes, 67 con candidiasis cutánea; respuestas terapéuticas equivalentes. El contenido de clioquinol no está verificado en el resumen. |
| [128475](https://pubmed.ncbi.nlm.nih.gov/128475/) | 1975 | Estudio clínico doble ciego | Dermatologica | Crema de corticoide con clioquinol (3%) en 430 pacientes con dermatosis con infección bacteriana secundaria; mejor resultado que cada componente solo y que el placebo. No evalúa candidiasis. |
| [155507](https://pubmed.ncbi.nlm.nih.gov/155507/) | 1979 | Evaluación clínica | Curr Med Res Opin | Una crema con anfotericina logró respuesta excelente en 95% de 40 pacientes con candidiasis cutánea. El control (yodoclorhidroxiquina-hidrocortisona) alcanzó 43%. Indirecto: el fármaco probado no contiene clioquinol. |
| [136333](https://pubmed.ncbi.nlm.nih.gov/136333/) | 1976 | Evaluación clínica | Curr Ther Res | Evaluación de una combinación de corticoide con antifúngico. Sin resumen disponible; evidencia indirecta. |
| [4220930](https://pubmed.ncbi.nlm.nih.gov/4220930/) | 1965 | Reporte observacional | Z Haut Geschlechtskr | Papel de las levaduras en la acrodermatitis enteropática. Relación indirecta con el clioquinol. |
| [2978600](https://pubmed.ncbi.nlm.nih.gov/2978600/) | 1988 | Estudio in vitro | Przegl Dermatol | Aditivos de jabones frente a cepas de *Candida albicans*, para prevención de infección ocupacional. Indirecto. |

## Información de Mercado en Colombia

Los cinco registros del paquete corresponden al mismo registro sanitario, repetido; se muestra una sola vez. El paquete indica 20 registros en total, pero no detalla los demás.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19972065 | BETAGEN CREMA TOPICA | Crema tópica | Betametasona y antibióticos |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque el puntaje de TxGNN es alto y la candidiasis cutánea es una infección superficial compatible con el uso tópico, no hay ensayos registrados. La literatura es antigua e indirecta, y no permite aislar el efecto del clioquinol frente a otros antifúngicos o corticoides de las combinaciones. El paquete de evidencia tampoco incluye datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener del prospecto de INVIMA las advertencias y contraindicaciones (brecha de seguridad bloqueante).
- Confirmar el mecanismo de acción en DrugBank.
- Revisar el texto completo de los estudios de 1975-1981 para verificar el contenido de clioquinol y la respuesta específica en candidiasis.
- Buscar estudios in vitro o clínicos con clioquinol solo, frente a *Candida*.
- Limitar cualquier evaluación a la vía tópica, por el antecedente de neurotoxicidad sistémica (SMON).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

