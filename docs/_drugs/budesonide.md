---
layout: default
title: Budesonide
parent: Solo Predicción del Modelo (L5)
nav_order: 119
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Budesonide: nueva indicación predicha, Eccema atópico (nivel de evidencia L5). Indicación original: Formoterol y budesonida (combinación inhalada para enfermedad respira…"
monitor_inn: "Budesonide"
predicted_indications: ["atopic eczema", "bronchitis", "dermatitis, atopic", "polyp of vocal cord", "polyp of middle ear", "epulis", "fibroepithelial polyp", "uterine polyp", "polyp of frontal sinus", "polyp of external auditory canal"]
---

# Budesonide
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

## Budesonida: De Formoterol y Budesonida Inhalados (Enfermedad Respiratoria) a Eccema Atópico
{: .text-alpha }

## Resumen en Una Frase

La budesonida es un corticosteroide sintético que en Colombia se registró en productos inhalatorios (combinada con formoterol) y en espuma rectal.
El modelo TxGNN predice que podría ser efectiva para **eccema atópico**, pero hasta ahora hay **0 ensayos clínicos** y **20 publicaciones**, casi todas indirectas (alergia de contacto a corticosteroides, revisiones generales y un estudio preclínico de formulación), por lo que la señal sigue siendo básicamente una predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Formoterol y budesonida (combinación inhalada para enfermedad respiratoria) |
| Nueva Indicación Predicha | Eccema atópico |
| Puntaje de Predicción TxGNN | 0.9996 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 20) |
| Número de Registros Sanitarios | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Budesonide (traducción no oficial): «La budesonida es un corticosteroide antiinflamatorio que presenta una potente actividad glucocorticoide y una débil actividad mineralocorticoide. En modelos estándar in vitro y en animales, la budesonida tiene una afinidad por el receptor de glucocorticoides aproximadamente 200 veces mayor y una potencia antiinflamatoria tópica 1000 veces mayor que el cortisol (ensayo de edema auricular inducido por aceite de crotón en ratas).» Texto original en inglés: "Budesonide is an anti-inflammatory corticosteroid that exhibits potent glucocorticoid activity and weak mineralocorticoid activity. In standard in vitro and animal models, budesonide has approximately a 200-fold higher affinity for the glucocorticoid receptor and a 1000-fold higher topical anti-inflammatory potency than cortisol (rat croton oil ear edema assay)." ([DailyMed: Budesonide Inhalation Suspension (budesonide) prescribing information, Cipla USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c52c5382-1400-44b9-95be-a30e1cf706da), versión del 2026-06-10; consultado el 2026-11-19). Se sabe que la budesonida es un glucocorticoide: actúa principalmente sobre el receptor de glucocorticoides (NR3C1) y, en menor medida, sobre los receptores de mineralocorticoides (NR3C2) y de progesterona (PGR). Su acción antiinflamatoria e inmunosupresora está bien establecida en asma, EPOC, enfermedad de Crohn, colitis ulcerosa y esofagitis eosinofílica.

El eccema atópico es una enfermedad inflamatoria de la piel dominada por la inflamación tipo 2. Su tratamiento habitual incluye corticosteroides tópicos. Por eso es plausible que un glucocorticoide con efecto antiinflamatorio local pueda ser útil, y las publicaciones describen la budesonida como usada en terapia local de dermatitis atópica pediátrica.

Sin embargo, esta plausibilidad es teórica. La relación con la indicación original (enfermedad respiratoria inflamatoria) se basa en el mecanismo común de inflamación alérgica, no en datos clínicos directos en piel. Además, la literatura recuperada contiene advertencias: la budesonida figura como alérgeno de contacto y se describen efectos sistémicos de los corticosteroides en niños.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Se muestran las 10 publicaciones más relevantes de un total de 20 recuperadas. Ninguna demuestra eficacia de la budesonida en eccema atópico humano.

<!-- review:begin co-lic-20261105-budesonide-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Los tres registros sanitarios están cancelados; actualmente no hay productos de budesonida vigentes en este conjunto de datos." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-budesonide-1 -->

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21062310](https://pubmed.ncbi.nlm.nih.gov/21062310/) | 2010 | ECA (veterinario, perros) | J Vet Pharmacol Ther | Un acondicionador de budesonida al 0.025% (Barazone) redujo lesiones y prurito en perros con dermatitis atópica frente a placebo (29 animales). No es evidencia en humanos. |
| [38275852](https://pubmed.ncbi.nlm.nih.gov/38275852/) | 2024 | Estudio preclínico de formulación | Gels (Basel) | Nanopartículas de budesonida en hidrogel sensible al pH para terapia local de dermatitis atópica, con liberación mejorada en la lesión. Solo laboratorio. |
| [9496795](https://pubmed.ncbi.nlm.nih.gov/9496795/) | 1998 | Estudio abierto longitudinal | Pediatr Dermatol | En 14 niños con dermatitis atópica, se evaluó con knemometría si la budesonida tópica afecta el crecimiento a corto plazo. Es un estudio de seguridad, no de eficacia. |
| [16428071](https://pubmed.ncbi.nlm.nih.gov/16428071/) | 2006 | Estudio in vitro | Int Immunopharmacol | La budesonida, a diferencia del tacrolimus, modifica funciones inmunes de queratinocitos humanos normales, lo que sugiere efecto inmunosupresor local. |
| [31705907](https://pubmed.ncbi.nlm.nih.gov/31705907/) | 2020 | Revisión | J Allergy Clin Immunol | Terapias emergentes para esofagitis eosinofílica, incluidas formulaciones de esteroides deglutidos. Es una enfermedad distinta, de la misma familia atópica. |
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Revisión | Neuroimmunomodulation | Corticosteroides intranasales y supresión adrenal, relevante para el riesgo sistémico en enfermedades alérgicas. |
| [14616123](https://pubmed.ncbi.nlm.nih.gov/14616123/) | 2003 | Revisión | Allergy | Los glucocorticoides causan con frecuencia alergia de contacto retardada y, ocasionalmente, alergia inmediata. |
| [33931866](https://pubmed.ncbi.nlm.nih.gov/33931866/) | 2021 | Serie de pruebas de parche | Contact Dermatitis | La budesonida es el marcador de hipersensibilidad a corticosteroides en la serie basal europea; se observa una tendencia decreciente de alergia en dos décadas. |
| [9543750](https://pubmed.ncbi.nlm.nih.gov/9543750/) | 1997 | Revisión | Ned Tijdschr Geneeskd | La alergia de contacto a corticosteroides no es rara (hasta 6% en sospecha de dermatitis de contacto), sobre todo en pacientes con dermatitis atópica de larga data. |
| [37927648](https://pubmed.ncbi.nlm.nih.gov/37927648/) | 2023 | Reporte de caso | Cureus | Angioedema y urticaria por hipersensibilidad tipo I a un corticosteroide en un paciente con antecedentes de dermatitis atópica. |

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 1980184 | PULMICORT® 0.5 MG / ML | SUSPENSION PARA NEBULIZACION | BUDESONIDA | Vigente |
| 19906224 | B-CORT® 200 AEROSOL | AEROSOLES | BUDESONIDA | Vigente |
| 19908024 | BUDENOFALK® 3 MG CÁPSULAS | CAPSULA DURA | BUDESONIDA | Vigente |
| 19918906 | SYMBICORT TURBUHALER (R) 160/4.5/MCG/DOSIS | POLVO PARA INHALACION | FORMOTEROL Y BUDENOSINA | Vigente |
| 19932996 | AEROVIAL® CÁPSULA DURA PARA ADMINISTRAR POR INHALADOR | CAPSULA DURA | FORMOTEROL Y BUDENOSINA | Vigente |

Se muestran 5 de al menos 20 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes. Los datos de este informe solo incluyen parte de los registros.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento TxGNN (no provienen del prospecto):** hipertensión, epilepsia, enfermedad hepática, enfermedad de la vesícula biliar, hiperglucemia, sarampión, insuficiencia cardíaca congestiva, queratitis por herpes simple, hipopituitarismo y diversas deficiencias hormonales hipofisarias (incluidos hipogonadismo hipogonadotrópico, síndrome de Kallmann y síndrome de Sheehan), y algunos trastornos del ciclo de la urea (deficiencia de carbamoilfosfato sintetasa I, hiperargininemia, citrulinemia).
- **Señales de seguridad en la literatura revisada:**
  - Alergia de contacto a la budesonida y a otros corticosteroides, más frecuente en pacientes con dermatitis atópica.
  - Supresión del eje hipotálamo-hipófisis-adrenal con corticosteroides intranasales.
  - Efectos sobre el crecimiento y el recambio óseo en niños tratados con glucocorticoides tópicos.
- **Interacciones farmacológicas:** no se identificaron interacciones con otros fármacos. Solo se registran sus blancos farmacológicos (receptores de glucocorticoides, mineralocorticoides y progesterona).

Para advertencias y contraindicaciones oficiales, consultar el prospecto aprobado, que no estuvo disponible para este informe.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje de TxGNN es muy alto (0.9996), pero no hay ensayos clínicos y la literatura es indirecta: alergia de contacto, seguridad pediátrica y un único estudio preclínico de formulación. Además, existen señales de seguridad específicas (sensibilización de contacto, efectos sistémicos en niños) en esta población.

<!-- review:begin co-lic-20261105-budesonide-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, no hay registros vigentes de budesonida en Colombia y existen señales de seguridad específicas (sensibilización de contacto, efectos sistémicos en niños) en esta población." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-budesonide-2 -->

**Para avanzar se necesita:**
- Ensayos clínicos controlados (fase 2 o superior) de budesonida en dermatitis atópica, con una formulación dérmica definida y comparador activo (p. ej., otro corticosteroide tópico).
- Datos formales de mecanismo de acción y del prospecto (advertencias y contraindicaciones oficiales).
- Evaluación de seguridad dermatológica y pediátrica: sensibilización de contacto, absorción sistémica, supresión adrenal y crecimiento.
- Como referencia, otra indicación predicha para este fármaco, **bronquitis**, tiene mejor respaldo (nivel L2, con ensayos de fase 2 y 4 parcialmente indirectos) y podría priorizarse en una evaluación aparte.

<!-- review:begin co-lic-20261105-budesonide-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Análisis regulatorio: en Colombia no hay registros vigentes ni una formulación dérmica aprobada, por lo que se requeriría un nuevo registro o una vía de indicación nueva. / Como referencia, otra indicación predicha para este fármaco, **bronquitis**, tiene mejor respaldo (nivel L2, con ensayos de fase 2 y 4 parcialmente indirectos) y podría priorizarse en una evaluación aparte." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-budesonide-3 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Los tres registros sanitarios están cancelados; actualmente no hay productos de budesonida vigentes en este conjunto de datos" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "no hay registros vigentes de budesonida en Colombia y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Análisis regulatorio: en Colombia no hay registros vigentes ni una formulación dérmica aprobada, por lo que se requeriría un nuevo registro " | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Budesonide Inhalation Suspension (budesonide) prescribing information, Cipla USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c52c5382-1400-44b9-95be-a30e1cf706da) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

