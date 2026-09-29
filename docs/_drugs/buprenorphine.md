---
layout: default
title: Buprenorphine
parent: Evidencia Moderada (L3-L4)
nav_order: 102
evidence_level: L4
indication_count: 6
---

# Buprenorphine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **6** 
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

# Buprenorfina: De Dolor Severo y Dependencia de Opioides a Porfiria Aguda Intermitente

## Resumen en Una Frase

La buprenorfina es un opioide sintético utilizado para tratar el dolor severo y la dependencia de opioides. El registro sanitario colombiano solo indica el nombre del principio activo, y el uso clínico proviene de la base farmacológica de la consulta.
El modelo TxGNN predice que podría ser efectiva para la **porfiria aguda intermitente**, pero hay **0 ensayos clínicos** y solo **1 publicación** (un reporte de caso sobre manejo anestésico, no sobre tratamiento de la enfermedad).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | "BUPRENORFINA" según el registro (solo nombra el principio activo, sin indicación explícita). Según la farmacología: dolor severo y dependencia de opioides |
| Nueva Indicación Predicha | Porfiria aguda intermitente |
| Puntaje de Predicción TxGNN | 99.41% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Lo que sí se conoce por la base farmacológica es que la buprenorfina actúa sobre los receptores opioides μ (gen OPRM1) y κ (gen OPRK1). Su eficacia en dolor severo y dependencia de opioides está establecida.

Sin embargo, no existe un mecanismo terapéutico demostrado que conecte la buprenorfina con la porfiria aguda intermitente. La única publicación disponible describe el manejo anestésico de una paciente con esta enfermedad. Muestra un uso perioperatorio, no un tratamiento de la porfiria.

El puntaje alto de TxGNN proviene de la proximidad en el grafo de conocimiento y no está respaldado por evidencia clínica. La predicción debe tomarse como una hipótesis de investigación y no como una señal de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [8301837](https://pubmed.ncbi.nlm.nih.gov/8301837/) | 1993 | Reporte de caso | Masui (Japanese Journal of Anesthesiology) | Manejo anestésico de una mujer de 40 años con sospecha de porfiria aguda intermitente, operada por un tumor maligno de ovario (histerectomía radical modificada). Es un reporte perioperatorio, no un estudio de tratamiento de la enfermedad |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19967654 | TRANSTEC® 70 MCG / H (GRUNENTHAL GMBH.) | Solución para uso transdérmico (parche) | BUPRENORFINA (sin indicación detallada en el registro) |

Nota: los 5 registros recibidos corresponden al mismo producto y al mismo número de registro, por lo que se presentan una sola vez. El total reportado es de 20 registros.

## Consideraciones de Seguridad

- **Porfiria y medicamentos**: la seguridad de los fármacos en porfiria debe verificarse por separado, porque algunos agentes pueden desencadenar crisis agudas. Esta verificación es indispensable antes de considerar cualquier uso en esta enfermedad.

Para el resto de la información de seguridad (advertencias, contraindicaciones e interacciones farmacológicas), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje de TxGNN es alto (99.41%), pero no hay ensayos clínicos y la única publicación es un reporte de caso anestésico sin valor terapéutico. Además, no existe un mecanismo plausible identificado. La evidencia se clasifica como L4.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) de buprenorfina y una hipótesis mecanística concreta hacia la porfiria aguda intermitente
- Revisión de la seguridad de buprenorfina en porfiria (riesgo de desencadenar crisis agudas)
- Advertencias y contraindicaciones del prospecto de INVIMA
- Evidencia preclínica o clínica que evalúe buprenorfina como tratamiento de la porfiria

Las otras cinco indicaciones predichas (discinesia orolingual-facial-bucal, trastorno de tics crónico, punta-onda continua durante el sueño, temblores benignos del lactante y enfermedad extrapiramidal y del movimiento) tienen evidencia L4 o L5 y tampoco justifican avanzar por ahora.

*Este informe es solo para investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

