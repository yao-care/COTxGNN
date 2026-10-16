---
layout: default
title: Famotidine
parent: Evidencia Moderada (L3-L4)
nav_order: 277
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Famotidine: nueva indicación predicha, Reflujo duodenogástrico (nivel de evidencia L4). Indicación original: Famotidina"
---

# Famotidine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Famotidina: De Indicación Registrada (Famotidina) a Duodenogastric Reflux (Reflujo Duodenogástrico)

## Resumen en Una Frase

Famotidina es un antagonista de los receptores H2 de histamina, registrado en Colombia bajo el texto de indicación "famotidina" y usado clásicamente para reducir la acidez gástrica.
El modelo TxGNN predice que podría ser efectivo para **reflujo duodenogástrico**, pero **no hay ensayos clínicos registrados** y solo **2 publicaciones** de apoyo indirecto.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Famotidina (el registro sanitario solo indica el nombre del principio activo, sin detallar la indicación) |
| Nueva Indicación Predicha | Reflujo duodenogástrico |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la famotidina es un antagonista del receptor H2 (HRH2) que disminuye la secreción de ácido gástrico, y su eficacia en enfermedades relacionadas con la acidez está bien establecida.

La relación con el reflujo duodenogástrico es indirecta: reducir el ácido puede disminuir el daño de la mucosa asociado al reflujo, pero la famotidina no actúa directamente sobre el reflujo de bilis o de contenido duodenal. El puntaje alto del modelo parece reflejar la cercanía en la red de conocimiento con las enfermedades ulcerosas, más que evidencia clínica específica.

Cabe señalar que otras predicciones del modelo, como **enfermedad ulcerosa péptica** (L1), **úlcera gastroyeyunal** (L2) y **gastroduodenitis** (L3), tienen más evidencia, pero en su mayoría coinciden con el uso ya conocido de la famotidina y no constituyen reposicionamiento en sentido estricto. Este informe se centra en la predicción de mayor puntaje.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [12532466](https://pubmed.ncbi.nlm.nih.gov/12532466/) | 2003 | Estudio clínico (pacientes críticos; diseño poco claro) | World J Gastroenterol | Evalúa el efecto de la famotidina sobre el reflujo gastroesofágico y duodeno-gastro-esofágico en pacientes críticamente enfermos y explora posibles mecanismos |
| [16259441](https://pubmed.ncbi.nlm.nih.gov/16259441/) | 2004 | Revisión | Eksp Klin Gastroenterol | Eficacia de famotidina 20 mg dos veces al día en etapas tempranas de la enfermedad por reflujo gastroduodenal (artículo en ruso) |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19959810 | GASTRUM® 10 MG TABLETA (cancelado) | Tableta | FAMOTIDINA |
| 20249954 | PEPTOFAN® 40 MG (cancelado) | Tableta recubierta | FAMOTIDINA |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** el grafo de conocimiento del modelo asocia la famotidina con enfermedad renal, función renal alterada, nefrolitiasis, enfermedad hepática, enfermedad de la vesícula biliar, hipercalcemia, hiperparatiroidismo, sarcoidosis, estreñimiento, enfermedad diarreica y cáncer gástrico (incluidas sus variantes). Estas relaciones requieren verificación clínica; en particular, el cáncer gástrico sugiere cautela porque el alivio sintomático podría enmascarar una neoplasia.
- **Interacciones farmacológicas:** los datos solo muestran dianas farmacológicas (receptor H2 y TAS2R31), sin interacciones medicamentosas clínicas relevantes.

No se dispone de advertencias ni contraindicaciones del prospecto; consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en dos publicaciones indirectas y ningún ensayo clínico, y el mecanismo (supresión ácida) no actúa sobre el reflujo biliar o duodenal. Además, en Colombia solo existen registros cancelados, lo que limita la disponibilidad práctica.

**Para avanzar se necesita:**
- Datos del mecanismo de acción detallado y del prospecto (advertencias y contraindicaciones oficiales)
- Estudios controlados que evalúen la famotidina específicamente en reflujo duodenogástrico
- Confirmar la situación regulatoria y la disponibilidad actual del producto en Colombia
- Considerar priorizar indicaciones relacionadas con úlcera péptica solo si se busca documentar usos ya conocidos; en ese caso, la evidencia indica que la famotidina es inferior a los inhibidores de la bomba de protones para prevenir recurrencia de úlceras asociadas a aspirina
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

