---
layout: default
title: Dexketoprofen
parent: Solo Predicción del Modelo (L5)
nav_order: 211
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
description: "Dexketoprofen: nueva indicación predicha, Tendinitis (nivel de evidencia L5). Indicación original: No detallada en el registro sanitario"
monitor_inn: "dexketoprofen"
predicted_indications: ["tendinitis", "fibromyalgia", "myositis fibrosa", "idiopathic granulomatous myositis", "rheumatoid arthritis", "migraine disorder", "headache disorder", "migraine with brainstem aura", "exostosis", "congenital hypotrichosis milia"]
---

# Dexketoprofen
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Dexketoprofeno: De Analgésico Antiinflamatorio (AINE) a Tendinitis
{: .text-alpha }

## Resumen en Una Frase

Dexketoprofeno es un antiinflamatorio no esteroideo (AINE) registrado en Colombia como analgésico oral, en solución y en tabletas recubiertas.
El modelo TxGNN predice que podría ser efectivo para **tendinitis**,
pero hoy solo hay **0 ensayos clínicos** y **1 publicación** indirecta que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No detallada en el registro sanitario (el texto registrado solo indica «Dexketoprofeno») |
| Nueva Indicación Predicha | Tendinitis |
| Puntaje de Predicción TxGNN | 0.9990 |
| Nivel de Evidencia | L5 (solo evidencia indirecta; no hay estudios directos en tendinitis) |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 9 de 9) |
| Número de Registros Sanitarios | 9 (vigentes: 9) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según lo conocido de la clase, dexketoprofeno es un AINE que inhibe las enzimas COX-1 y COX-2. Esto reduce la síntesis de prostaglandinas, mediadoras del dolor y la inflamación.

La tendinitis es una inflamación del tendón con dolor asociado, por lo que un efecto antiinflamatorio y analgésico por inhibición de COX es mecanísticamente plausible. Por eso la predicción tiene sentido biológico.

Sin embargo, la única publicación disponible estudió dolor musculoesquelético agudo no traumático en urgencias. La tendinitis se menciona allí solo como una de sus posibles causas. Es evidencia indirecta y no demuestra eficacia específica en tendinitis.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para tendinitis.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30744914](https://pubmed.ncbi.nlm.nih.gov/30744914/) | 2019 | ECA | The American Journal of Emergency Medicine | Compara dexketoprofeno intravenoso con paracetamol en el alivio del dolor musculoesquelético agudo no traumático en urgencias. Es evidencia indirecta, no específica de tendinitis. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20105211 | DEXKETOVITAE 25 MG/10ML | Solución oral | Dexketoprofeno | Vigente |
| 20103268 | DEXKETOVITAE® 25 MG comprimidos recubiertos | Tableta recubierta | Dexketoprofeno | Vigente |

Ambos registros pertenecen a GALENICUM HEALTH COLOMBIA S.A.S.

<!-- review:begin co-lic-20261105-dexketoprofen-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Ambos registros pertenecen a GALENICUM HEALTH COLOMBIA S.A.S. y no hay registros vigentes." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 9 registros sanitarios (vigentes: 9); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-dexketoprofen-1 -->

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

No se encontraron interacciones farmacológicas registradas en los datos compilados. Esto no equivale a ausencia de interacciones. Como con otros AINE, deben tenerse en cuenta los riesgos gastrointestinales, renales y cardiovasculares.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para tendinitis tiene un puntaje alto del modelo y un mecanismo plausible. Sin embargo, no hay ensayos clínicos y la única publicación es indirecta.

<!-- review:begin co-lic-20261105-dexketoprofen-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Sin embargo, no hay ensayos clínicos y la única publicación es indirecta. Además, los dos registros sanitarios en Colombia están cancelados." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 9 registros sanitarios (vigentes: 9); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-dexketoprofen-2 -->

**Para avanzar se necesita:**
- Estudios clínicos o revisiones que evalúen dexketoprofeno específicamente en tendinitis.
- Verificar la disponibilidad regulatoria.
- Obtener el prospecto de INVIMA con advertencias y contraindicaciones.
- Completar los datos del mecanismo de acción desde DrugBank.

<!-- review:begin co-lic-20261105-dexketoprofen-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Verificar la disponibilidad regulatoria, porque no hay registros vigentes en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 9 registros sanitarios (vigentes: 9); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-dexketoprofen-3 -->

**Nota adicional:** en los datos compilados, la indicación predicha con mayor respaldo es la **migraña** (puntaje TxGNN de 0.9987). Cuenta con 5 ensayos clínicos de Fase 4 y un metaanálisis de ECA, incluido un ensayo controlado con placebo (NCT02159547, n=224). Para ella la evidencia se clasificó como L1 con recomendación «Proceed with Guardrails», siempre que se verifique la disponibilidad regulatoria. Si se busca una línea de reposicionamiento con mayor sustento, conviene evaluarla como candidata prioritaria.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "y no hay registros vigentes" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Además, los dos registros sanitarios en Colombia están cancelados" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "porque no hay registros vigentes en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

