---
layout: default
title: Etonogestrel
parent: Solo Predicción del Modelo (L5)
nav_order: 269
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Etonogestrel: nueva indicación predicha, Amenorrea (nivel de evidencia L5). Indicación original: Progestágeno + estrógeno"
monitor_inn: "ETONOGESTREL"
predicted_indications: ["amenorrhea (disease)", "breast fibrocystic disease", "blunt duct adenosis of breast", "apocrine adenosis of breast", "benign mammary dysplasia"]
---

# Etonogestrel
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Etonogestrel: De Progestágeno+Estrógeno a Amenorrea
{: .text-alpha }

## Resumen en Una Frase

Etonogestrel es un progestágeno que en Colombia contó con un registro sanitario como sistema de liberación (anillo), clasificado como "progestágeno+estrógeno".
El modelo TxGNN predice que podría ser efectivo para **amenorrea**, pero actualmente hay **0 ensayos clínicos** y **1 publicación** (sin relación real con el tema) que respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Progestágeno + estrógeno |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 0.9984 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, etonogestrel es un progestágeno que suprime la ovulación y adelgaza el endometrio. Su uso como anticonceptivo hormonal está documentado.

La amenorrea es un efecto bien conocido de los progestágenos, por lo que la asociación es biológicamente plausible. Sin embargo, la amenorrea es un **patrón de sangrado resultante del efecto del fármaco**, no una enfermedad que el fármaco trate. El puntaje alto del modelo probablemente refleja esta asociación y no una verdadera indicación terapéutica.

La única publicación vinculada (PMID 33430924) trata sobre BIO101 en COVID-19 y no guarda relación con etonogestrel ni con amenorrea; parece una coincidencia espuria.

Otras predicciones del modelo (todas con evidencia L5, sin ensayos ni literatura): enfermedad fibroquística de la mama (99.61%), adenosis de conductos romos (99.29%), adenosis apocrina (99.29%) y displasia mamaria benigna (99.21%). Su base es una hipótesis teórica de antagonismo de la proliferación mamaria inducida por estrógenos, y la dirección del efecto es incierta, ya que los anticonceptivos hormonales pueden empeorar o mejorar los síntomas mamarios.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33430924](https://pubmed.ncbi.nlm.nih.gov/33430924/) | 2021 | ECA (protocolo) | Trials | Protocolo de estudio de BIO101 para prevenir el deterioro respiratorio en COVID-19. No guarda relación con etonogestrel ni amenorrea. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20128300 (cancelado) | EXELRING ® | Sistemas de liberación | Progestágeno+Estrógeno |

---

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento** (relaciones fármaco-enfermedad del modelo, no texto de prospecto): hipertensión, epilepsia, trastornos de ansiedad, porfiria, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, lupus eritematoso sistémico, asma, diabetes mellitus y cetoacidosis diabética, hipertrigliceridemia, hiperlipidemia, carcinoma de mama femenino, tromboflebitis, migraña, enfermedad coronaria y obesidad.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total; las principales listadas son de nivel moderado e incluyen antidiabéticos (acarbosa, metformina, glimepirida, clorpropamida, inhibidores de SGLT2 como canagliflozina, dapagliflozina y empagliflozina, inhibidores de DPP-4 como alogliptina y saxagliptina, agonistas de GLP-1 como albiglutida, dulaglutida y semaglutida, e insulinas), además de aprepitant, claritromicina y linaclotida.

Para el resto de la información de seguridad, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (L5): no hay ensayos clínicos, la única publicación es irrelevante y la amenorrea es un efecto del fármaco, no una enfermedad a tratar. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Replantear si la amenorrea es una indicación terapéutica válida o solo un efecto esperado del fármaco.
- Obtener el prospecto de INVIMA para completar advertencias y contraindicaciones (bloqueante para el tamizaje de seguridad).
- Obtener datos del mecanismo de acción desde DrugBank.
- Buscar literatura y ensayos clínicos realmente relacionados con etonogestrel en las condiciones predichas (por ejemplo, enfermedad mamaria benigna).
- Evaluar la compatibilidad de vía de administración y la situación regulatoria actual, dado que el registro está cancelado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

