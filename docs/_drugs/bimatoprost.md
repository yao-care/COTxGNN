---
layout: default
title: Bimatoprost
parent: Solo Predicción del Modelo (L5)
nav_order: 90
evidence_level: L5
indication_count: 10
---

# Bimatoprost
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Bimatoprost: De Glaucoma e Hipertensión Ocular a Síndrome Malformativo con Componente Dental y/o Periodontal

## Resumen en Una Frase

Bimatoprost es un análogo de prostamida, comercializado en solución oftálmica y usado originalmente para el glaucoma y la hipertensión ocular.
El modelo TxGNN predice que podría ser efectivo para **síndrome malformativo con componente dental y/o periodontal**,
pero hay **0 ensayos clínicos** y **20 publicaciones** sobre periodontitis en general, ninguna de las cuales menciona bimatoprost. Es una predicción basada solo en el grafo del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Bimatoprost (el registro de INVIMA solo indica el nombre del principio activo; según la literatura, glaucoma e hipertensión ocular) |
| Nueva Indicación Predicha | Síndrome malformativo con componente dental y/o periodontal |
| Puntaje de Predicción TxGNN | 99.997% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Bimatoprost es un análogo de prostamida que actúa como agonista del receptor FP. En el campo de mecanismo de acción del Evidence Pack no hay datos detallados. La descripción anterior proviene del análisis de la propia predicción.

No se identificó un vínculo mecanístico plausible entre este mecanismo y el síndrome malformativo con componente dental o periodontal. La literatura recuperada trata la periodontitis en general (relación con diabetes, microbiota, cirugía regenerativa, guías de tratamiento) y nunca menciona bimatoprost.

El puntaje alto (0.99997) refleja la estructura del grafo de conocimiento, no evidencia biológica ni clínica. Por eso conviene tratar esta predicción con mucha cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Ninguna de estas publicaciones estudia bimatoprost. Solo aportan contexto sobre la enfermedad periodontal.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35420698](https://pubmed.ncbi.nlm.nih.gov/35420698/) | 2022 | Revisión sistemática | Cochrane Database Syst Rev | Tratamiento de la periodontitis para el control glucémico en personas con diabetes |
| [35688447](https://pubmed.ncbi.nlm.nih.gov/35688447/) | 2022 | Guía | J Clin Periodontol | Guía de práctica clínica EFP S3 para el tratamiento de la periodontitis estadio IV |
| [22057194](https://pubmed.ncbi.nlm.nih.gov/22057194/) | 2012 | Revisión | Diabetologia | Relación bidireccional entre periodontitis y diabetes; la diabetes triplica aproximadamente la susceptibilidad |
| [37435999](https://pubmed.ncbi.nlm.nih.gov/37435999/) | 2023 | Revisión | Periodontology 2000 | Complicaciones y errores de tratamiento en cirugía periodontal regenerativa |
| [39233377](https://pubmed.ncbi.nlm.nih.gov/39233377/) | 2024 | Revisión | Periodontology 2000 | Sueño y salud periodontal; la apnea obstructiva como factor de riesgo emergente |
| [36883660](https://pubmed.ncbi.nlm.nih.gov/36883660/) | 2023 | Revisión | J Dent Res | Papel de los fibroblastos gingivales en la patogénesis de la periodontitis |
| [38907216](https://pubmed.ncbi.nlm.nih.gov/38907216/) | 2024 | Revisión | J Nanobiotechnology | Inmunoterapia de macrófagos mediada por biomateriales en periodontitis |
| [29193334](https://pubmed.ncbi.nlm.nih.gov/29193334/) | 2018 | Revisión | Periodontology 2000 | Comparación de tejidos blandos periimplantarios y periodontales en salud y enfermedad |
| [9495612](https://pubmed.ncbi.nlm.nih.gov/9495612/) | 1998 | Observacional | J Clin Periodontol | Complejos microbianos en la placa subgingival de 185 sujetos |

## Información de Mercado en Colombia

Los 5 registros listados en el Evidence Pack corresponden al mismo registro sanitario (los 20 registros totales no se detallan individualmente en los datos recibidos).

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19923968 | LUMIGAN ® SOLUCIÓN OFTÁLMICA (ABBVIE INC) | Solución oftálmica | BIMATOPROST (el registro no detalla la indicación) |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni literatura que vincule bimatoprost con esta indicación, y no se identificó un mecanismo plausible. El nivel de evidencia es L5, solo predicción del modelo.

**Para avanzar se necesita:**
- Un fundamento mecanístico que justifique la relación entre el agonismo FP/prostamida y la patología dental o periodontal
- Datos de mecanismo de acción y de seguridad (prospecto de INVIMA)

**Nota:** otras predicciones del mismo Evidence Pack tienen más respaldo, en particular **alopecia** (rango 8, nivel L2, Proceed with Guardrails), con varios ensayos de Fase 2 completados en alopecia androgenética. Se recomienda evaluarla por separado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

