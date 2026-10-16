---
layout: default
title: Chlorambucil
parent: Evidencia Moderada (L3-L4)
nav_order: 150
evidence_level: L4
indication_count: 8
last_modified_at: 2026-10-14
description: "Chlorambucil: nueva indicación predicha, Leucemia linfocítica crónica/linfoma linfocítico pequeño de centro pr… (nivel de evidencia L4). Indicación original: Clorambucilo"
---

# Chlorambucil
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **8** 
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

# Clorambucilo: De Clorambucilo (indicación registrada sin detalle) a Leucemia Linfocítica Crónica/Linfoma Linfocítico Pequeño de Centro Pregerminal

## Resumen en Una Frase

Clorambucilo es un agente alquilante (mostaza nitrogenada) registrado en Colombia bajo el nombre Leukeran, cuyo registro sanitario solo indica el nombre del principio activo como indicación.
El modelo TxGNN predice que podría ser efectivo para **leucemia linfocítica crónica/linfoma linfocítico pequeño de centro pregerminal (IGHV no mutado)**, pero **no hay ensayos clínicos** y solo **1 publicación** (una revisión de 2003) que respalde esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Clorambucilo (el registro no detalla la indicación; se usa en neoplasias hematológicas) |
| Nueva Indicación Predicha | Leucemia linfocítica crónica/linfoma linfocítico pequeño de centro pregerminal |
| Puntaje de Predicción TxGNN | 99.72% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registro vigente) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este reporte. Según la información conocida, clorambucilo es un agente alquilante tipo mostaza nitrogenada que daña el ADN de las células en proliferación, y tiene un uso establecido desde hace décadas en la leucemia linfocítica crónica (LLC) y el linfoma linfocítico pequeño (LLP).

El subtipo predicho (IGHV no mutado, de tipo pregerminal) es un subconjunto molecular de la LLC/LLP. Por ello, la actividad del fármaco es plausible por extensión, y el puntaje alto probablemente refleja la cercanía entre estas enfermedades en la ontología. En la práctica, este caso es más un subtipo de una enfermedad ya tratada con el fármaco que un verdadero reposicionamiento.

Conviene tener en cuenta que los estándares actuales (inhibidores de BTK y de BCL2) han desplazado al clorambucilo, en especial en la enfermedad con IGHV no mutado. La única publicación disponible es una revisión de 2003 sobre un enfoque adaptado al riesgo, sin datos específicos de clorambucilo en este subtipo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [12577769](https://pubmed.ncbi.nlm.nih.gov/12577769/) | 2003 | Revisión | Nederlands tijdschrift voor geneeskunde | Describe la LLC como la leucemia más frecuente en Occidente, no tan indolente como se pensaba, con dos subtipos (pregerminal y de centro germinal) que justifican un enfoque adaptado al riesgo. No aporta datos específicos de clorambucilo. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 46264 (cancelado) | Leukeran Tabletas Recubiertas 2 mg | Tableta recubierta | CLORAMBUCIL |

Fabricante: Aspen Labs S.A. de C.V. (México). No hay registros vigentes.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (agente alquilante, mostaza nitrogenada) |
| Riesgo de Mielosupresión | Alto. Las contraindicaciones del grafo de conocimiento incluyen neutropenia, trombocitopenia, leucopenia, anemia, agranulocitosis y linfopenia. |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, plaquetas, función hepática y renal |
| Protección en Manejo | Seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Contraindicaciones o condiciones de precaución (según el grafo de conocimiento, no según el prospecto):** epilepsia, trombocitopenia, síndrome nefrótico (incluidas las formas familiar y de lesiones mínimas), neutropenia, agranulocitosis, anemia (incluida la macrocítica), enfermedad pulmonar intersticial, fibrosis pulmonar, daño hepático inducido por fármacos, leucopenia, linfopenia y leucemias agudas (incluidas las de fenotipo mixto o linaje ambiguo).
- **Interacciones farmacológicas:** se identificaron 167 interacciones. Entre las listadas con mayor gravedad están **deferiprona** (Mayor) y **samario (153Sm) lexidronam** (Mayor). Hay interacciones de nivel Moderado con anfotericina B (y sus formulaciones lipídicas), palifermina, cloruro de estroncio Sr-89, mercaptopurina, roflumilast y cloranfenicol. Levofloxacino es de nivel Menor. Otras (mesalazina, omeprazol, prednisona, prednisolona, simvastatina, warfarina, levotiroxina) tienen nivel no clasificado.
- **Riesgo de segundas neoplasias:** la literatura asociada señala este riesgo con los alquilantes.

Para las advertencias formales se debe consultar el prospecto, que no estuvo disponible en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en la proximidad ontológica con la LLC/LLP, con una única revisión de 2003 y sin ensayos clínicos. Además, el clorambucilo ha sido desplazado por terapias dirigidas en este subtipo, y en Colombia no hay ningún registro vigente. No es un reposicionamiento genuino, sino un subtipo de una indicación ya conocida.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), una brecha de datos que bloquea el análisis de seguridad.
- Completar los datos de mecanismo de acción desde DrugBank.
- Buscar evidencia clínica específica en LLC con IGHV no mutado, comparando con los tratamientos actuales (inhibidores de BTK/BCL2).
- Confirmar la situación regulatoria, dado que el único registro está cancelado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

