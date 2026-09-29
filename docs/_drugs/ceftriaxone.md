---
layout: default
title: Ceftriaxone
parent: Evidencia Moderada (L3-L4)
nav_order: 117
evidence_level: L4
indication_count: 7
---

# Ceftriaxone
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

# Ceftriaxona: De Infecciones Bacterianas a Hiperamilasemia

## Resumen en Una Frase

Ceftriaxona es un antibiótico betalactámico (cefalosporina de tercera generación), usado originalmente para tratar infecciones bacterianas.
El modelo TxGNN predice que podría ser efectivo para **hiperamilasemia**, pero **no hay ensayos clínicos** y solo hay **3 publicaciones**, ninguna de las cuales demuestra un beneficio terapéutico.
La predicción tiene un puntaje alto, pero no está respaldada por datos clínicos.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el campo solo dice «Ceftriaxona»); se asume uso antibacteriano |
| Nueva Indicación Predicha | Hiperamilasemia |
| Puntaje de Predicción TxGNN | 99.39% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, ceftriaxona es una cefalosporina bactericida con actividad contra patógenos comunes como *Streptococcus pneumoniae*, *Haemophilus influenzae* y varias enterobacterias. Su eficacia en infecciones bacterianas está bien establecida.

**Este caso no muestra una razón mecanística clara.** La hiperamilasemia es un hallazgo de laboratorio (amilasa sérica elevada), no una enfermedad que se trate directamente, y la ceftriaxona no tiene un efecto conocido sobre la amilasa. El puntaje alto del modelo no está respaldado por datos clínicos.

La única señal en la literatura es un estudio de 1999 sobre profilaxis con ceftriaxona tras papilosfinterotomía endoscópica. Es más plausible que el beneficio observado se deba a la prevención de infección biliar (colangitis) y no a una reducción de la amilasa. Además, el análisis del paquete señala que el lodo biliar y la pancreatitis son efectos adversos descritos de la ceftriaxona, lo que va en sentido contrario a la indicación predicha.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10458061](https://pubmed.ncbi.nlm.nih.gov/10458061/) | 1999 | Estudio clínico (diseño poco claro) | Bratislavske lekarske listy | 30 pacientes recibieron 1 g de ceftriaxona como profilaxis tras papilosfinterotomía endoscópica y se compararon con 30 sin antibiótico. Las bacterias biliares más frecuentes (*Pseudomonas aeruginosa*, *E. coli*) fueron sensibles a ceftriaxona. |
| [7522351](https://pubmed.ncbi.nlm.nih.gov/7522351/) | 1994 | Observacional (no relacionado con ceftriaxona) | Southern Medical Journal | 38 pacientes con hemorragia intracraneal: 25 tenían lipasa elevada y 17 también amilasa, sin pancreatitis. No evalúa ceftriaxona. |
| [36263834](https://pubmed.ncbi.nlm.nih.gov/36263834/) | 2023 | Reporte de caso | Rev Esp Enferm Dig | Síndrome de Weil (leptospirosis) con hemorragia digestiva alta por úlcera gástrica. Aporta poco a la hipótesis. |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20163214 | CEFTRINOX® 1000 MG POLVO ESTÉRIL PARA RECONSTITUIR (Nectar Lifesciences Limited) | Polvo estéril para reconstituir a solución inyectable | Solo figura «Ceftriaxona» (sin texto de indicación) |

El pack de evidencia lista cinco entradas idénticas del mismo registro 20163214. Aquí se muestra una sola. El total de registros reportado es 20.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni estudios que evalúen ceftriaxona para reducir la amilasa. La hiperamilasemia es un hallazgo de laboratorio, y la ceftriaxona se asocia a pancreatitis y lodo biliar. El puntaje de 99.39% es solo una predicción del modelo.

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de INVIMA (advertencias y contraindicaciones), que no está disponible en el pack.
- Completar el mecanismo de acción desde DrugBank.
- Confirmar la indicación original aprobada, ya que el registro solo muestra el nombre del principio activo.
- Antes de considerar esta indicación, definir si hay una pregunta clínica real detrás de la hiperamilasemia (p. ej., una enfermedad subyacente) y no solo un hallazgo de laboratorio.

**Nota adicional:** entre las otras predicciones del pack, *otitis media infecciosa* tiene mayor respaldo (nivel L1, «Proceed with Guardrails»). Es probable que sea un uso ya establecido y no un reposicionamiento, por lo que conviene evaluarla por separado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

