---
layout: default
title: Bleomycin
parent: Solo Predicción del Modelo (L5)
nav_order: 111
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Bleomycin: nueva indicación predicha, Neoplasia de la cola de caballo (cauda equina) (nivel de evidencia L5). Indicación original: No especificada en los registros (el texto aprobado solo indica \"Ble…"
monitor_inn: "bleomycin"
predicted_indications: ["cauda equina neoplasm", "adult astrocytic tumour", "reticulum cell sarcoma", "primary pulmonary lymphoma", "pulmonary blastoma", "well-differentiated fetal adenocarcinoma of the lung"]
---

# Bleomycin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Bleomicina: De Bleomicina (indicación no detallada en el registro) a Neoplasia de la Cola de Caballo
{: .text-alpha }

## Resumen en Una Frase

La bleomicina es un antineoplásico citotóxico cuyos registros sanitarios colombianos solo mencionan el nombre del principio activo, sin detallar la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para la **neoplasia de la cola de caballo (cauda equina)**, pero sin ensayos clínicos registrados y con **1 publicación** solo tangencialmente relacionada.
Se trata de una predicción sin respaldo clínico directo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en los registros (el texto aprobado solo indica "Bleomicina") |
| Nueva Indicación Predicha | Neoplasia de la cola de caballo (cauda equina) |
| Puntaje de Predicción TxGNN | 0.9930 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la bleomicina es un agente citotóxico que provoca roturas de las cadenas de ADN y se usa en tumores de células germinales y linfomas. Su eficacia en esas indicaciones está bien establecida, y mecanísticamente podría ser aplicable a otros tumores, aunque este vínculo no está demostrado para la nueva indicación.

La única publicación asociada trata sobre radioterapia en germinoma del sistema nervioso central (SNC) recidivado tras quimioterapia primaria con carboplatino, etopósido y bleomicina. Esto solo se relaciona de forma tangencial con una neoplasia de la cola de caballo: comparte la localización en el SNC y el uso de bleomicina en tumores germinales, pero no evalúa el fármaco en esta enfermedad.

En consecuencia, el puntaje alto del modelo es una predicción sin sustento clínico directo. Además, quedan sin resolver la penetración de la barrera hematoencefálica y la toxicidad pulmonar propia de la bleomicina.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9440744](https://pubmed.ncbi.nlm.nih.gov/9440744/) | 1998 | Cohorte (retrospectivo) | J Clin Oncol | Evalúa la radioterapia como rescate en germinoma del SNC recidivado tras quimioterapia primaria con carboplatino, etopósido y bleomicina (PEB). Relación solo tangencial con la neoplasia de la cola de caballo. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20259728 (cancelado) | BLENA® 15 UI | Polvo liofilizado para reconstituir a solución inyectable | Bleomicina |
| 20092577 (cancelado) | BLEOMICINA 15 UI | Polvo liofilizado | Bleomicina |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (agente que induce roturas en el ADN; familia de antibióticos antitumorales) |
| Riesgo de Mielosupresión | Bajo (la literatura señala un efecto relativamente ahorrador de médula ósea) |
| Clasificación de Emetogenicidad | Baja a moderada |
| Ítems de Monitoreo | Función pulmonar (toxicidad pulmonar limitante de dosis), hemograma, función hepática y renal, vigilancia de fiebre/reacciones agudas tras la primera dosis |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 205 interacciones potenciales. Entre las listadas figuran levofloxacino (menor) y, con nivel de gravedad no clasificado, pantoprazol, palonosetrón, lactulosa, aprepitant, morfina, omeprazol, lansoprazol, vancomicina, prednisona, hidrocortisona, manitol, cloruro de potasio, prednisolona, ranitidina, granisetrón, ondansetrón, famotidina, claritromicina y metoclopramida.
- **Toxicidad pulmonar**: la literatura asociada a otras indicaciones destaca la neumonitis intersticial y la toxicidad pulmonar por bleomicina como preocupación relevante, y también se describe hiperpirexia aguda.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo (nivel L5), sin ensayos clínicos y con una sola publicación tangencial. Además, no hay registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y análisis del vínculo mecanístico con la nueva indicación
- Obtener y analizar el prospecto (advertencias y contraindicaciones) para el tamizaje de seguridad
- Estudios preclínicos o clínicos específicos en tumores de la cola de caballo o del SNC, incluyendo penetración de la barrera hematoencefálica
- Evaluación de viabilidad regulatoria dado que los registros están cancelados

---

### Nota sobre otras indicaciones predichas

Entre las demás predicciones, el **sarcoma de células reticulares (linfoma no Hodgkin)** tiene mayor respaldo (nivel L1, con ensayos de Fase 3 completados como NCT00002565 y NCT00002835). Sin embargo, estos evalúan esquemas multifármaco, no se aísla la contribución de la bleomicina y el tratamiento estándar actual (R-CHOP) no la incluye, por lo que refleja uso histórico más que una señal clara de reposicionamiento. El **tumor astrocítico del adulto** presenta evidencia L3 limitada a estudios de Fase I y trabajos antiguos. Se recomienda evaluar estas alternativas si se desea priorizar según la solidez de la evidencia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

