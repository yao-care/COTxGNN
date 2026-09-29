---
layout: default
title: Albendazole
parent: Evidencia Alta (L1-L2)
nav_order: 31
evidence_level: L2
indication_count: 3
---

# Albendazole
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **3** 
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

# Albendazol: De Antihelmíntico (registro sin indicación específica) a Equinococosis Alveolar

## Resumen en Una Frase

Albendazol es un antiparasitario benzimidazólico que en Colombia se comercializa como tabletas y suspensión oral. Los registros sanitarios solo consignan el nombre del principio activo y no detallan la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para la **equinococosis alveolar**, con **5 ensayos clínicos** relacionados (1 de Fase 2 completado y específico de la enfermedad) y **ninguna publicación** recuperada para esta indicación.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro solo indica "ALBENDAZOL") |
| Nueva Indicación Predicha | Equinococosis alveolar |
| Puntaje de Predicción TxGNN | 99,97 % |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según el conocimiento farmacológico general, albendazol se une a la beta-tubulina del parásito, bloquea la polimerización de los microtúbulos y reduce la captación de glucosa. Esto lo hace parasitostático frente a las metacéstodas de *Echinococcus multilocularis*, es decir, frena el crecimiento del parásito pero no lo elimina.

La equinococosis alveolar es una infección por larvas de cestodos, y albendazol ya es un antihelmíntico de amplio espectro contra estadios larvarios de cestodos. Por eso esta predicción está más cerca de un uso ya establecido en las guías que de un reposicionamiento novedoso. Además, la enfermedad no tratada tiene una letalidad cercana al 100 % en 10 a 15 años, y las opciones son la cirugía (posible solo en 30 a 40 % de los casos) o el tratamiento con benzimidazoles.

La evidencia específica de la enfermedad es limitada: un solo ensayo de Fase 2 completado, sin resultados publicados, y ninguna literatura recuperada para esta indicación.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT07182305](https://clinicaltrials.gov/study/NCT07182305) | Fase 2 | Completado | 194 | Albendazol en equinococosis alveolar en etapa temprana, en un nuevo foco de Kirguistán (2017-2023). Coincidencia directa de fármaco y enfermedad. No hay resultados publicados, por lo que la magnitud del efecto no está verificada. |
| [NCT02876146](https://clinicaltrials.gov/study/NCT02876146) | NA | Completado | 50 | Estudio prospectivo EchinoVISTA: viabilidad del parásito y marcadores de seguimiento en pacientes con equinococosis alveolar hepática tratados con albendazol. Apoya el monitoreo de la respuesta, no la eficacia. |
| [NCT06483880](https://clinicaltrials.gov/study/NCT06483880) | NA | Desconocido | 24 | ECA pequeño de albendazol adyuvante tras resección de quiste hidatídico pulmonar frente a placebo. Es equinococosis quística, una enfermedad relacionada pero distinta: apoyo indirecto. |
| [NCT05824442](https://clinicaltrials.gov/study/NCT05824442) | NA | Reclutando | 43 | Evaluación de una PCR cuantitativa múltiple para diagnosticar equinococosis. Sin evidencia terapéutica. |
| [NCT07176598](https://clinicaltrials.gov/study/NCT07176598) | N/A | Completado | 1 | Reporte de caso de quiste hidatídico intramuscular en el deltoides. No es equinococosis alveolar y no aporta evidencia de eficacia. |

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

Hay 20 registros de licencias. La mayoría son entradas duplicadas del mismo registro sanitario, por lo que se muestran solo los registros únicos.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19973311 | ALBENDAZOL 200 MG TABLETA (PENTACOOP S.A.) | Tableta | ALBENDAZOL (sin texto de indicación) |
| 20119849 | ALBENDAZOL 2% SUSPENSIÓN (COOPIDROGAS) | Suspensión oral | ALBENDAZOL (sin texto de indicación) |

También hay presentaciones de tableta recubierta por vía oral.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay un ensayo de Fase 2 completado (n=194) en la enfermedad exacta y el mecanismo es plausible. Albendazol ya se usa clínicamente en equinococosis. Aun así, no hay resultados publicados ni literatura recuperada, por lo que el nivel de evidencia se mantiene en L2.

**Para avanzar se necesita:**
- Obtener los resultados del ensayo NCT07182305 para confirmar la magnitud del efecto.
- Confirmar el etiquetado regulatorio en Colombia, porque los registros de INVIMA no detallan la indicación aprobada.
- Descargar y revisar el prospecto de INVIMA para completar advertencias y contraindicaciones.
- Completar los datos del mecanismo de acción consultando la API de DrugBank.
- Vigilar la función hepática y el hemograma durante tratamientos prolongados.
- Realizar una búsqueda dirigida de literatura sobre equinococosis alveolar.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

