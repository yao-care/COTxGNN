---
layout: default
title: Rivaroxaban
parent: Solo Predicción del Modelo (L5)
nav_order: 348
evidence_level: L5
indication_count: 4
---

# Rivaroxaban
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Rivaroxabán: De Anticoagulante (indicación específica no registrada) a Artritis Reumatoide

## Resumen en Una Frase

Rivaroxabán es un anticoagulante oral, inhibidor directo del Factor Xa. El registro sanitario colombiano solo lista el nombre del principio activo, sin una indicación específica.
El modelo TxGNN predice que podría ser efectivo para **artritis reumatoide**, pero hay **0 ensayos clínicos** y **4 publicaciones** que no evalúan la eficacia del fármaco en esta enfermedad.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | RIVAROXABAN (el registro solo indica el nombre del principio activo, sin indicación específica) |
| Nueva Indicación Predicha | Artritis reumatoide |
| Puntaje de Predicción TxGNN | 99.57% |
| Nivel de Evidencia | L5 (solo predicción del modelo; el paquete de datos lo clasificó como L4, pero ningún estudio recuperado evalúa rivaroxabán en artritis reumatoide) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados en la base de datos. Según la información general conocida, rivaroxabán es un inhibidor directo del Factor Xa, y su uso está establecido en enfermedades tromboembólicas. Los datos de entrada no incluyen la indicación original ni el mecanismo, por lo que no se puede verificar el razonamiento del grafo de conocimiento detrás del puntaje.

El único vínculo plausible es el cruce entre coagulación e inflamación en las enfermedades autoinmunes. Una revisión sobre el ensayo de generación de trombina en enfermedades autoinmunes sugiere que estos pacientes tienen estados de hipercoagulabilidad y mayor riesgo cardiovascular. Esto es una hipótesis indirecta.

Ningún estudio recuperado muestra que rivaroxabán trate o modifique la artritis reumatoide. La literatura encontrada trata sobre tromboembolismo venoso, adherencia en fibrilación auricular y un caso perioperatorio. El puntaje alto del modelo es solo una predicción y no una prueba de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Revisión | JAMA | Diagnóstico y tratamiento del tromboembolismo venoso de miembros inferiores. Incidencia de trombosis venosa profunda de 88 a 112 por 100 000 personas-año. No trata la artritis reumatoide. |
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Revisión | La Revue de médecine interne | El ensayo de generación de trombina permite evaluar la hipercoagulabilidad en enfermedades autoinmunes. Es el único vínculo indirecto con el mecanismo, sin evaluar rivaroxabán. |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Cohorte | PloS one | Compara la adherencia a rivaroxabán frente a apixabán en fibrilación auricular no valvular. No es pertinente para artritis reumatoide. |
| [41918541](https://pubmed.ncbi.nlm.nih.gov/41918541/) | 2026 | Reporte de caso | Cureus | Infarto cerebral tromboembólico perioperatorio en una mujer de 88 años con fibrilación auricular que tomaba esteroides orales por artritis reumatoide. La artritis es solo una comorbilidad. |

## Información de Mercado en Colombia

Los cinco registros devueltos corresponden a un mismo registro sanitario, listado una sola vez. El total reportado es de 20 registros.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20233281 | RIVAROXABÁN 20MG TABLETAS RECUBIERTAS (American Generics S.A.S.) | Tableta recubierta | RIVAROXABAN (solo nombre del principio activo) |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (99.57%). No hay ensayos clínicos y ninguna publicación evalúa la eficacia de rivaroxabán en artritis reumatoide. Además, faltan los datos de indicación original, mecanismo y seguridad del prospecto.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones), un vacío que bloquea el tamizaje de seguridad.
- Obtener el mecanismo de acción desde DrugBank para evaluar el vínculo mecanístico.
- Buscar estudios preclínicos o clínicos que evalúen inhibidores del Factor Xa en artritis reumatoide.
- Evaluar el riesgo de sangrado en pacientes con artritis reumatoide que usan AINE o corticoides.

*Este informe es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

