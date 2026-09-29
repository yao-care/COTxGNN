---
layout: default
title: Cabozantinib
parent: Solo Predicción del Modelo (L5)
nav_order: 106
evidence_level: L5
indication_count: 10
---

# Cabozantinib
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

# Cabozantinib: De Indicación Original No Especificada a Liposarcoma

## Resumen en Una Frase

Cabozantinib es un inhibidor multiquinasa oral (VEGFR2, MET, AXL, RET) que está comercializado en Colombia, pero el registro sanitario solo indica el nombre del principio activo y no el texto de su indicación.
El modelo TxGNN predice que podría ser efectivo para **liposarcoma**,
con **1 ensayo clínico** (Fase 2, sin resultados) y **1 publicación** (Fase 1) que respaldan por ahora esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro solo dice "CABOZANTINIB") |
| Nueva Indicación Predicha | Liposarcoma |
| Puntaje de Predicción TxGNN | 99.83% |
| Nivel de Evidencia | L3 (según el Evidence Pack; no hay ECA completados) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 18 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Cabozantinib es un inhibidor de tirosina quinasas que actúa sobre VEGFR2, MET, AXL y RET. Esas vías participan en la angiogénesis, el crecimiento tumoral y la migración celular. No hay un campo detallado de mecanismo de acción en los datos recibidos, así que esta descripción proviene de la justificación del propio Evidence Pack.

La indicación original no está documentada en los datos. Aun así, el fármaco ya se usa en oncología (por ejemplo, en carcinoma renal avanzado, según otras predicciones del paquete). Su actividad antiangiogénica y sobre MET/AXL es plausible en sarcomas de tejidos blandos, y el liposarcoma pertenece a ese grupo.

No hay un mecanismo específico documentado para liposarcoma. El respaldo actual es indirecto y viene de estudios en sarcoma de tejidos blandos en general.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT05836571](https://clinicaltrials.gov/study/NCT05836571) | Fase 2 | Activo, sin reclutar | 66 | ECA que compara ipilimumab + nivolumab solos frente a su combinación con cabozantinib en sarcoma de tejidos blandos avanzado. No se incluye el liposarcoma de forma específica y aún no hay resultados. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [41770651](https://pubmed.ncbi.nlm.nih.gov/41770651/) | 2026 | Ensayo Fase 1 | American Journal of Clinical Oncology | Evalúa la seguridad de cabozantinib neoadyuvante con radioterapia concurrente en sarcomas de tejidos blandos de extremidades. Parte de la preocupación por el riesgo de fístula o perforación. |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20172869 | CABOMETYX 40 MG (IPSEN PHARMA) | Tableta recubierta | Solo figura "CABOZANTINIB"; sin texto de indicación |
| 20172869 | CABOMETYX 20 MG (IPSEN PHARMA) | Tableta recubierta | Solo figura "CABOZANTINIB"; sin texto de indicación |

Los 18 registros totales incluyen entradas repetidas del mismo número de registro. Aquí se muestran solo las presentaciones distintas.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor multiquinasa) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Advertencia desde la literatura**: el estudio de Fase 1 con radioterapia concurrente señala que existe preocupación por el riesgo de fístula o perforación. Esa combinación requiere vigilancia estrecha.
- No se encontraron interacciones farmacológicas en la consulta realizada.

Para el resto de advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Solo hay un ensayo de Fase 2 aún sin resultados y un estudio de Fase 1 de seguridad, ambos en sarcoma de tejidos blandos en general y no en liposarcoma específico. Con esto no se puede sostener un uso en liposarcoma.

**Para avanzar se necesita:**
- Resultados del ensayo NCT05836571, en particular los datos del subgrupo de liposarcoma.
- Datos preclínicos o mecanísticos específicos de liposarcoma (MET, AXL, VEGFR).
- El texto de indicaciones y las advertencias del prospecto de INVIMA, más el mecanismo de acción desde DrugBank.
- Un plan de seguridad si se combina con radioterapia (riesgo de fístula o perforación).

Como referencia, otras predicciones del mismo paquete tienen más respaldo. El carcinoma renal tiene evidencia L1 con ECA de Fase 3 y uso ya establecido. El carcinoma renal de células no claras sin clasificar tiene evidencia L2 con varios ensayos de Fase 2. Conviene evaluarlas como candidatas de mayor prioridad.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

