---
layout: default
title: Alteplase
parent: Solo Predicción del Modelo (L5)
nav_order: 42
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
description: "Alteplasa: nueva indicación predicha, Deficiencia de cofactor 2 de la heparina (nivel de evidencia L5). Indicación original: Alteplasa"
monitor_inn: "ALTEPLASE"
predicted_indications: ["heparin cofactor 2 deficiency", "congenital coronary artery anomaly", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "thrombophilia", "coronary stenosis"]
---

# Alteplase
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

## Alteplasa: De Indicación Registrada (Alteplasa) a Deficiencia de cofactor 2 de la heparina
{: .text-alpha }

## Resumen en Una Frase

Alteplasa es un activador del plasminógeno tisular recombinante (trombolítico), registrado en Colombia con el producto Actilyse 50 mg.
El modelo TxGNN predice que podría ser efectivo para **infarto de miocardio posteroinferior**, pero **no hay ensayos clínicos ni publicaciones** específicos para esta indicación que respalden la predicción.

<!-- review:begin co-lic-20261105-alteplase-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Alteplasa es un activador del plasminógeno tisular recombinante (trombolítico), registrado en Colombia con el producto Actilyse 50 mg, cuyo registro sanitario figura hoy como cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-alteplase-2 -->

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Alteplasa (el registro no detalla la indicación aprobada más allá del nombre del principio activo) |
| Nueva Indicación Predicha | Infarto de miocardio posteroinferior |
| Puntaje de Predicción TxGNN | 0.9972 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Clinical Pharmacology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Alteplase (traducción no oficial): «Alteplasa es una enzima (serina proteasa) que tiene la propiedad de convertir el plasminógeno en plasmina de forma potenciada por la fibrina. En ausencia de fibrina, produce una conversión limitada del plasminógeno. Alteplasa se une a la fibrina de un trombo y convierte el plasminógeno atrapado en plasmina, con lo que inicia la fibrinólisis local.» Texto original en inglés: "Alteplase is an enzyme (serine protease) that has the property of fibrin-enhanced conversion of plasminogen to plasmin. It produces limited conversion of plasminogen in the absence of fibrin. Alteplase binds to fibrin in a thrombus and converts the entrapped plasminogen to plasmin, thereby initiating local fibrinolysis." ([DailyMed: Cathflo Activase (alteplase) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=91ecdef2-95ff-42dd-a31c-c8a09cab3ad9), versión del 2026-01-20; consultado el 2026-11-19). Según el conocimiento farmacológico general, alteplasa es un activador del plasminógeno tisular recombinante: convierte el plasminógeno en plasmina, que disuelve la fibrina de los coágulos.

En el infarto de miocardio, la causa habitual es un trombo que ocluye una arteria coronaria. La disolución del trombo es, por tanto, un enfoque mecanísticamente coherente.

Un matiz importante: la trombólisis ya es una estrategia establecida en el infarto con elevación del ST en general. El infarto posteroinferior es probablemente un subtipo de un uso ya conocido y no un reposicionamiento genuino. El puntaje es solo una predicción computacional.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para infarto de miocardio posteroinferior.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación específica.

### Otras indicaciones predichas con evidencia (contexto)

Las siguientes predicciones secundarias sí cuentan con algo de evidencia, aunque mayormente indirecta:

| Indicación | Puntaje TxGNN | Nivel | Evidencia disponible |
|------|------|------|---------|
| Trombofilia | 0.9943 | L2 | 1 ensayo Fase 2 en reclutamiento ([NCT05540834](https://clinicaltrials.gov/study/NCT05540834), 70 participantes, tPA guiado por pruebas viscoelásticas en insuficiencia respiratoria aguda protrombótica) y numerosos reportes de caso |
| Estenosis coronaria | 0.9914 | L2 | Sin ensayos registrados. Incluye un ensayo aleatorizado doble ciego de alteplasa vs. placebo en dolor torácico en reposo ([8299637](https://pubmed.ncbi.nlm.nih.gov/8299637/), 1993) y un estudio en angina inestable ([8721695](https://pubmed.ncbi.nlm.nih.gov/8721695/), 1996) |

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 33103 | ACTILYSE 50 MG | POLVO LIOFILIZADO PARA RECONSTITUIR A SOLUCION INYECTABLE | ALTEPLASE | Vigente |

Se muestra el único registro sanitario de este principio activo en los datos del INVIMA, Código Único de Medicamentos.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

No se dispone de advertencias ni contraindicaciones del prospecto en los datos compilados. Debe consultarse el prospecto para esa información. Tampoco se identificaron contraindicaciones en el grafo de conocimiento.

- **Interacciones farmacológicas**: se identificaron 100 interacciones en total. Entre las revisadas:
  - **Mayores**: abciximab, fondaparinux, apixabán, acalabrutinib, anisindiona, deferasirox, ibritumomab tiuxetán y tositumomab. En su mayoría implican un riesgo aditivo de sangrado.
  - **Moderadas**: ácido acetilsalicílico, ibuprofeno, ketorolaco, fluvoxamina, fosinopril, ácido aminocaproico, aprotinina, fenfluramina, dexfenfluramina y sibutramina.
- Por su mecanismo, el sangrado es el riesgo central a vigilar, sobre todo en combinación con anticoagulantes y antiagregantes.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para el infarto posteroinferior carece de ensayos y literatura específicos (L5). Además, probablemente corresponde a un subtipo de un uso ya establecido de la trombólisis, y no a un reposicionamiento real.

<!-- review:begin co-lic-20261105-alteplase-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, probablemente corresponde a un subtipo de un uso ya establecido de la trombólisis, y no a un reposicionamiento real. El único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-alteplase-3 -->

**Para avanzar se necesita:**
- Aclarar si esta indicación aporta algo más allá de la trombólisis ya establecida en infarto con elevación del ST.
- Obtener el prospecto de INVIMA con advertencias y contraindicaciones, ya que su ausencia impide el análisis de seguridad.
- Completar los datos del mecanismo de acción (por ejemplo, desde DrugBank).
- Si se busca una línea con más potencial, evaluar la trombofilia (ensayo Fase 2 NCT05540834 en curso) o la estenosis coronaria, siempre con atención al riesgo de sangrado.

<!-- review:begin co-lic-20261031-alteplase-1 -->

> **Corrección de revisión (2026-10-31)**: Texto original: "Confirmar la situación regulatoria vigente de alteplasa en Colombia (registro cancelado) y la disponibilidad de otros productos. / Si se busca una línea con más potencial, evaluar la trombofilia (ensayo Fase 2 NCT05540834 en curso) o la estenosis coronaria, siempre con atención al riesgo de sangrado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-10-31. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261031-alteplase-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-10-31 | Eliminado: "Confirmar la situación regulatoria vigente de alteplasa en Colombia (registro cancelado) y la disponibilidad de otros productos" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "cuyo registro sanitario figura hoy como cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "El único registro sanitario en Colombia está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Cathflo Activase (alteplase) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=91ecdef2-95ff-42dd-a31c-c8a09cab3ad9) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

