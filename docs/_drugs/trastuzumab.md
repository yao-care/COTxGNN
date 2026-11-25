---
layout: default
title: Trastuzumab
parent: Solo Predicción del Modelo (L5)
nav_order: 637
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-25
monitor_inn: "TRASTUZUMAB"
predicted_indications: ["malignant cutaneous granular cell skin tumor", "ectomesenchymoma", "human herpesvirus 8-related tumor", "middle ear neuroendocrine tumor", "kidney pelvis sarcomatoid transitional cell carcinoma", "prostatic urethra urothelial carcinoma"]
description: "Trastuzumab: nueva indicación predicha, Malignant cutaneous granular cell skin tumor (nivel de evidencia L5). Indicación original: PERTUZUMAB Y TRASTUZUMAB"
---

# Trastuzumab
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

## Trastuzumab: Malignant cutaneous granular cell skin tumor
{: .text-alpha }

## Resumen en Una Frase

Trastuzumab es un anticuerpo monoclonal.
El modelo TxGNN predice que podría ser efectivo para el **subtipo de carcinoma de mama tipo normal (normal breast-like)**, pero solo hay **1 ensayo clínico** (aún sin reclutar, y de otro fármaco) y **1 publicación** (sobre morfología de otro subtipo) relacionados, por lo que la evidencia directa es prácticamente nula.

<!-- review:begin co-lic-20261105-trastuzumab-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Trastuzumab es un anticuerpo monoclonal que en Colombia contó con registros sanitarios para presentaciones de trastuzumab solo y en combinación con pertuzumab." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-trastuzumab-2 -->

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | PERTUZUMAB Y TRASTUZUMAB; TRASTUZUMAB |
| Nueva Indicación Predicha | Malignant cutaneous granular cell skin tumor |
| Puntaje de Predicción TxGNN | 0.9948 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 12 de 13) |
| Número de Registros Sanitarios | 13 (vigentes: 12) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Trastuzumab (traducción no oficial): «El protooncogén HER2 (o c-erbB2) codifica una proteína receptora transmembrana de 185 kDa, que está relacionada estructuralmente con el receptor del factor de crecimiento epidérmico. Se ha demostrado, tanto en ensayos in vitro como en animales, que los productos de trastuzumab inhiben la proliferación de células tumorales humanas que sobreexpresan HER2.» Texto original en inglés: "The HER2 (or c-erbB2) proto-oncogene encodes a transmembrane receptor protein of 185 kDa, which is structurally related to the epidermal growth factor receptor. Trastuzumab products have been shown, in both in vitro assays and in animals, to inhibit the proliferation of human tumor cells that overexpress HER2." ([DailyMed: Ogivri (trastuzumab-dkst) prescribing information, Biocon Biologics Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b6465b44-a6dd-f99c-d009-6851cf05169c), versión del 2026-06-26; consultado el 2026-11-19). Según la información conocida, trastuzumab es un anticuerpo dirigido contra el receptor HER2. Su eficacia en cáncer de mama HER2 positivo está bien establecida, y mecanísticamente podría ser aplicable a otros tumores de mama solo si estos dependen de HER2.

La relación con la nueva indicación es débil. El beneficio de trastuzumab depende del estado de HER2, no del subtipo molecular intrínseco. El subtipo "normal-like" es mayormente HER2 negativo y no es un grupo reconocido como sensible a trastuzumab. Por eso la predicción del modelo, aunque con puntaje alto, no cuenta con un respaldo mecanístico claro.

La evidencia disponible es solo indirecta. El único ensayo evalúa trastuzumab rezetecán (un conjugado anticuerpo-fármaco distinto) en cáncer de mama triple negativo, y el único artículo describe características morfológicas del subtipo basal-like.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT07669610](https://clinicaltrials.gov/study/NCT07669610) | Fase 3 | Aún no reclutando | 140 | Trastuzumab rezetecán con o sin bevacizumab como tratamiento de 1.ª a 3.ª línea en cáncer de mama triple negativo subtipo basal-like inmunosuprimido. Evalúa otro fármaco y no aporta datos de eficacia de trastuzumab ni del subtipo normal-like. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [19466513](https://pubmed.ncbi.nlm.nih.gov/19466513/) | 2009 | Cohorte | Breast Cancer (Tokyo) | Describe las características morfológicas y citopatológicas del carcinoma de mama subtipo basal-like, de curso agresivo y mal pronóstico. No evalúa trastuzumab ni el subtipo normal-like. |

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19903070 | HERCEPTIN ® POLVO LIOFILIZADO PARA INFUSION 440 MG | POLVO LIOFILIZADO PARA RECONSTITUIR A SOLUCION INYECTABLE | TRASTUZUMAB | Vigente |
| 20055046 | HERCEPTIN® SOLUCION INYECTABLE 600MG/5ML | SOLUCION INYECTABLE | TRASTUZUMAB | Vigente |
| 20130360 | HERTICAD® | POLVO LIOFILIZADO PARA RECONSTITUIR A SOLUCION INYECTABLE | TRASTUZUMAB | Vigente |
| 20142329 | OGIVRI® | POLVO LIOFILIZADO PARA RECONSTITUIR A SOLUCION INYECTABLE | TRASTUZUMAB | Vigente |
| 20143846 | BISINTEX | POLVO LIOFILIZADO PARA RECONSTITUIR A SOLUCION INYECTABLE | TRASTUZUMAB | Vigente |

Se muestran 5 de 13 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (anticuerpo monoclonal anti-HER2) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Función cardíaca (fracción de eyección del ventrículo izquierdo, LVEF); además, consultar el prospecto para hemograma y función hepática y renal |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registraron 94 interacciones; entre las más relevantes (se muestran 20):
  - **Mayores**: deferiprona, samario (153Sm) lexidronam, adalimumab y baricitinib.
  - **Moderadas**: warfarina, dicumarol, paclitaxel, zidovudina, cloranfenicol, azatioprina, alemtuzumab, anakinra, canakinumab, alefacept, palifermina, roflumilast, cloruro de estroncio Sr-89 y algunas vacunas (toxoide tetánico, ántrax).

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El respaldo para este subtipo es solo indirecto: un ensayo sin iniciar sobre otro fármaco y un artículo morfológico sobre otro subtipo. Además, el subtipo normal-like es mayormente HER2 negativo, por lo que no hay una base mecanística sólida.

<!-- review:begin co-lic-20261105-trastuzumab-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, el subtipo normal-like es mayormente HER2 negativo, por lo que no hay una base mecanística sólida. Los registros sanitarios locales están todos cancelados." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-trastuzumab-1 -->

**Para avanzar se necesita:**
- Demostrar con datos que existe una fracción HER2 positiva dentro del subtipo normal-like; sin esto, no hay base para avanzar.
- Datos detallados del mecanismo de acción.
- Verificar el estado actual de los registros sanitarios y la disponibilidad real del producto en Colombia.
- Revisar el prospecto de INVIMA para advertencias y contraindicaciones, que no estaban disponibles en los datos compilados.
- Tener en cuenta que otras predicciones del mismo fármaco, como el cáncer de mama HER2 positivo con receptor de progesterona positivo o negativo, tienen mucha más evidencia (incluido un ensayo de Fase 3 completado, NCT01275677). Sin embargo, corresponden en gran parte a un uso ya establecido y no a un reposicionamiento nuevo.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Los registros sanitarios locales están todos cancelados" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "que en Colombia contó con registros sanitarios para presentaciones de trastuzumab solo y en combinación con pertuzumab" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Ogivri (trastuzumab-dkst) prescribing information, Biocon Biologics Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b6465b44-a6dd-f99c-d009-6851cf05169c) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

