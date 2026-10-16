---
layout: default
title: Norfloxacin
parent: Solo Predicción del Modelo (L5)
nav_order: 473
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
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

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Norfloxacino: De Norfloxacina (indicación no detallada en el registro) a Hiperamilasemia

## Resumen en Una Frase

Norfloxacino es un antibacteriano de la familia de las fluoroquinolonas, registrado en Colombia bajo el nombre "Norfloxacina", sin que el registro detalle la indicación específica.
El modelo TxGNN predice que podría ser efectivo para **hiperamilasemia**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, por lo que se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Norfloxacina (el registro sanitario no detalla la indicación) |
| Nueva Indicación Predicha | Hiperamilasemia |
| Puntaje de Predicción TxGNN | 99.70% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 4 (todos cancelados) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, norfloxacino es una fluoroquinolona antibacteriana que inhibe la ADN girasa y la topoisomerasa IV bacterianas, y su uso establecido está en infecciones bacterianas (principalmente urinarias).

La hiperamilasemia es un hallazgo de laboratorio (elevación de la amilasa en sangre), no una enfermedad infecciosa. No se identifica un vínculo mecanístico claro entre la inhibición de la ADN girasa y la corrección de este hallazgo. El puntaje alto del modelo proviene de patrones del grafo de conocimiento y no de evidencia biológica o clínica.

Por lo tanto, la predicción debe considerarse exploratoria. Otras predicciones del modelo para este fármaco (por ejemplo, síndrome de hiperviscosidad policlonal, analbuminemia congénita o esclerodermia difusa) tampoco cuentan con respaldo mecanístico. La única con plausibilidad biológica es la peste septicémica, una infección bacteriana sensible a fluoroquinolonas, aunque con evidencia solo preclínica e indirecta.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para hiperamilasemia.

## Información de Mercado en Colombia

Los cuatro registros sanitarios están cancelados; actualmente no hay productos vigentes con norfloxacino.

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
La predicción para hiperamilasemia es solo del modelo (L5), sin ensayos ni literatura, y sin vínculo mecanístico plausible. Además, el fármaco no tiene registros vigentes en Colombia y presenta un perfil de seguridad con numerosas contraindicaciones potenciales.

**Para avanzar se necesita:**
- Evidencia clínica o preclínica que relacione norfloxacino con la hiperamilasemia
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones oficiales)
- Evaluar si otra indicación predicha, como la peste septicémica, merece una investigación específica, considerando que otras fluoroquinolonas están mejor respaldadas
- Aclarar la situación regulatoria, ya que todos los registros están cancelados
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

