---
layout: default
title: Norfloxacin
parent: Solo Predicción del Modelo (L5)
nav_order: 473
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
description: "Norfloxacin: nueva indicación predicha, Hiperamilasemia (nivel de evidencia L5). Indicación original: Norfloxacina"
monitor_inn: "Norfloxacin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "punctate epithelial keratoconjunctivitis", "premalignant hematological system disease", "diffuse scleroderma", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
---

# Norfloxacin
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

## Norfloxacino: De Norfloxacina (indicación no detallada en el registro) a Hiperamilasemia
{: .text-alpha }

## Resumen en Una Frase

Norfloxacino es un antibacteriano de la familia de las fluoroquinolonas, registrado en Colombia bajo el nombre "Norfloxacina", sin que el registro detalle la indicación específica.
El modelo TxGNN predice que podría ser efectivo para **hiperamilasemia**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, por lo que se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Norfloxacina (el registro sanitario no detalla la indicación) |
| Nueva Indicación Predicha | Hiperamilasemia |
| Puntaje de Predicción TxGNN | 0.9970 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 11 de 11) |
| Número de Registros Sanitarios | 11 (vigentes: 11) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, norfloxacino es una fluoroquinolona antibacteriana que inhibe la ADN girasa y la topoisomerasa IV bacterianas, y su uso establecido está en infecciones bacterianas (principalmente urinarias).

La hiperamilasemia es un hallazgo de laboratorio (elevación de la amilasa en sangre), no una enfermedad infecciosa. No se identifica un vínculo mecanístico claro entre la inhibición de la ADN girasa y la corrección de este hallazgo. El puntaje alto proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

Por lo tanto, la predicción debe considerarse exploratoria. Otras predicciones del modelo para este fármaco (por ejemplo, síndrome de hiperviscosidad policlonal, analbuminemia congénita o esclerodermia difusa) tampoco cuentan con respaldo mecanístico. La única con plausibilidad biológica es la peste septicémica, una infección bacteriana sensible a fluoroquinolonas, aunque con evidencia solo preclínica e indirecta.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para hiperamilasemia.

<!-- review:begin co-lic-20261105-norfloxacin-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Los cuatro registros sanitarios están cancelados; actualmente no hay productos vigentes con norfloxacino." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 11 registros sanitarios (vigentes: 11); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-norfloxacin-1 -->

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 29749 | NORFLOXACINA 400MG (Tecnoquímicas) | Tableta cubierta (gragea) | Norfloxacina |
| 19942965 | UROTRIN® 400 MG Tabletas (Bioquifar) | Tableta recubierta | Norfloxacina |
| 20105055 | URODROL® (Bioquímico Pharma) | Cápsula dura | Norfloxacina |
| 19983228 | NORAFLOX® 400MG Tabletas (Laboratorios Best) | Tableta | Norfloxacina |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** síndrome de QT largo (incluido el familiar) y torsades de pointes; insuficiencia hepática, cirrosis y enfermedad hepática o de la vesícula biliar; enfermedad renal; epilepsia; trastornos de ansiedad, psicóticos y otros trastornos mentales; diabetes mellitus y cetoacidosis diabética; neuropatía periférica; tendinitis y otras afecciones del tejido conectivo; rabdomiólisis; trombocitopenia; anemia; deficiencia de potasio.
- **Interacciones farmacológicas:** se identificaron 100 interacciones. Entre las de nivel **mayor** figuran hidrocortisona, dexametasona, betametasona, triamcinolona (corticosteroides, con mayor riesgo de lesión tendinosa), bupropión y clorpropamida. Entre las de nivel **moderado** figuran antidiabéticos (acarbosa, metformina, pioglitazona, alogliptina, canagliflozina, albiglutida), famotidina, loperamida, ácido acetilsalicílico, balsalazida, bisacodilo y sales de calcio y potasio.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para hiperamilasemia es solo del modelo (L5), sin ensayos ni literatura, y sin vínculo mecanístico plausible. Además, presenta un perfil de seguridad con numerosas contraindicaciones potenciales.

<!-- review:begin co-lic-20261105-norfloxacin-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, el fármaco no tiene registros vigentes en Colombia y presenta un perfil de seguridad con numerosas contraindicaciones potenciales." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 11 registros sanitarios (vigentes: 11); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-norfloxacin-2 -->

**Para avanzar se necesita:**
- Evidencia clínica o preclínica que relacione norfloxacino con la hiperamilasemia
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones oficiales)
- Evaluar si otra indicación predicha, como la peste septicémica, merece una investigación específica, considerando que otras fluoroquinolonas están mejor respaldadas
- Confirmar la situación regulatoria: el medicamento está comercializado y cuenta con 11 licencias válidas

<!-- review:begin co-lic-20261112-norfloxacin-1 -->

> **Corrección de revisión (2026-11-12)**: Texto original: "4 licencias válidas" Corregido según los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-05): 11 registros sanitarios, de los cuales 11 vigentes. Las cifras actuales están en el Resumen rápido. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261112-norfloxacin-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Los cuatro registros sanitarios están cancelados; actualmente no hay productos vigentes con norfloxacino" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "el fármaco no tiene registros vigentes en Colombia y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-12 | Número de registros vigentes: 4 → 11 | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

