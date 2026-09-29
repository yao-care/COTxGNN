---
layout: default
title: Avelumab
parent: Solo Predicción del Modelo (L5)
nav_order: 67
evidence_level: L5
indication_count: 10
---

# Avelumab
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

# Avelumab: De Indicación No Especificada en el Registro a Tumor Asociado al Herpesvirus Humano 8

## Resumen en Una Frase

Avelumab es un anticuerpo anti-PD-L1 comercializado en Colombia como BAVENCIO®. El registro sanitario solo indica "AVELUMAB" y no detalla la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **tumores asociados al herpesvirus humano 8** (como el sarcoma de Kaposi), pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. La predicción se basa solo en el modelo computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo dice "AVELUMAB") |
| Nueva Indicación Predicha | Tumor asociado al herpesvirus humano 8 |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 2 (ambos con el mismo número, 20131917) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, avelumab es un anticuerpo anti-PD-L1, es decir, una inmunoterapia que bloquea el eje PD-1/PD-L1 para reactivar la respuesta inmune contra las células tumorales.

La hipótesis mecanística es que el agotamiento inmunológico por el eje PD-1/PD-L1 es plausible en tumores causados por virus, como el sarcoma de Kaposi. En ese escenario, bloquear PD-L1 podría restaurar la respuesta inmune contra el tumor.

Esta relación es solo una inferencia general. No se suministraron ensayos, literatura ni datos de expresión de PD-L1 para este tumor, y la similitud con la indicación original no se pudo evaluar. La predicción se apoya únicamente en el puntaje del grafo de conocimiento.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20131917 | BAVENCIO® (MERCK S.A.) | Solución para infusión | AVELUMAB (sin texto de indicación detallado) |

El Evidence Pack lista dos registros con el mismo número y los mismos datos, por lo que aquí se muestra una sola vez.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (anticuerpo anti-PD-L1) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto (99.97%), pero es solo computacional (L5), sin ensayos ni literatura, y la indicación aprobada localmente no está detallada. No hay base suficiente para avanzar.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA (advertencias y contraindicaciones) para poder hacer el tamizaje de seguridad.
- Consultar el mecanismo de acción en DrugBank.
- Buscar ensayos clínicos y literatura sobre avelumab en sarcoma de Kaposi y otros tumores asociados a HHV-8.
- Reunir datos de expresión de PD-L1 en estos tumores.
- Como referencia, otras predicciones del mismo Evidence Pack tienen un vínculo más plausible: el carcinoma urotelial de uretra prostática (L4) y el carcinoma de células transicionales sarcomatoide de pelvis renal (L3). Pueden ser candidatas más prometedoras para priorizar.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

