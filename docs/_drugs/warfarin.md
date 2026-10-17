---
layout: default
title: Warfarin
parent: Evidencia Moderada (L3-L4)
nav_order: 666
evidence_level: L4
indication_count: 7
last_modified_at: 2026-10-14
description: "Warfarin: nueva indicación predicha, Deficiencia de cofactor 2 de la heparina (nivel de evidencia L4). Indicación original: WARFARINA"
monitor_inn: "warfarin"
predicted_indications: ["heparin cofactor 2 deficiency", "antithrombin deficiency type 2", "thrombophilia", "rheumatoid arthritis", "breast fibrocystic disease", "benign mammary dysplasia"]
---

# Warfarin
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **7** 
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

# Warfarina: De Warfarina (indicación sin detallar) a Deficiencia de Cofactor 2 de la Heparina

## Resumen en Una Frase

La warfarina es un anticoagulante oral antagonista de la vitamina K; en Colombia solo consta un registro sanitario (hoy cancelado) cuyo texto de indicación se limita al nombre del principio activo, sin describir un uso específico.
El modelo TxGNN predice que podría ser efectiva para **deficiencia de cofactor 2 de la heparina**, con **0 ensayos clínicos** y **3 publicaciones** (solo reportes de casos) que respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | WARFARINA (el registro no detalla una indicación clínica) |
| Nueva Indicación Predicha | Deficiencia de cofactor 2 de la heparina |
| Puntaje de Predicción TxGNN | 99.87% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo cancelado (sin registros vigentes) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la warfarina inhibe la enzima vitamina K epóxido reductasa, lo que reduce la síntesis de los factores de coagulación funcionales II, VII, IX y X.

La deficiencia de cofactor 2 de la heparina altera la inhibición de la trombina y favorece la trombosis. Reducir los factores dependientes de vitamina K es una vía plausible para controlar ese riesgo trombótico, y por eso la predicción tiene coherencia mecanística.

Sin embargo, la literatura disponible son solo reportes de casos y de familias con trombosis (1990-2001), que no demuestran eficacia comparativa de la warfarina. El puntaje alto de TxGNN refleja la estructura de la red de trombosis y no una validación clínica.

**Otras predicciones del modelo (todas en Hold):**

| Indicación predicha | Puntaje | Nivel | Comentario |
|------|------|------|------|
| Exceso de factor 5 con trombosis espontánea | 99.84% | L5 | Sin ensayos ni literatura; el factor V no depende de vitamina K, vínculo indirecto |
| Deficiencia de antitrombina tipo 2 | 99.84% | L4 | Un solo reporte de caso; los antagonistas de vitamina K son un enfoque estándar en trombofilia hereditaria, pero no se aportó evidencia directa |
| Trombofilia | 99.75% | L3 | Es la predicción con más respaldo: 1 ensayo Fase 3 relacionado y múltiples revisiones; recomendación del análisis: pregunta de investigación |
| Artritis reumatoide | 99.21% | L4 | Los ensayos usan warfarina solo como sustrato de prueba en estudios de interacciones; no hay vínculo terapéutico |
| Enfermedad fibroquística de la mama | 99.20% | L5 | Solo un reporte de interacción con danazol; sin mecanismo plausible |
| Displasia mamaria benigna | 99.10% | L5 | Misma entidad que la anterior; sin evidencia |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para deficiencia de cofactor 2 de la heparina.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [2214444](https://pubmed.ncbi.nlm.nih.gov/2214444/) | 1990 | Reporte de caso | Kyobu Geka | Trombosis del ventrículo derecho en una adolescente de 14 años con deficiencia familiar de cofactor II de la heparina; el trombo se extirpó quirúrgicamente |
| [2033902](https://pubmed.ncbi.nlm.nih.gov/2033902/) | 1991 | Reporte de caso | Nihon Kyobu Shikkan Gakkai Zasshi | Mujer de 48 años con trombosis venosa y embolia pulmonar recurrentes por deficiencia congénita de antitrombina, tratada con warfarina durante 7 años; luego se cambió a heparina |
| [11570053](https://pubmed.ncbi.nlm.nih.gov/11570053/) | 2001 | Reporte de caso (familia) | Journal of UOEH | Familia con trombosis múltiple desde la infancia; una hermana recibió warfarina, pero volvió a presentar trombosis venosa profunda a los 7 años |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20014730 | WARFAR5 MG. TABLETAS | Tableta | WARFARINA | Cancelado |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (TxGNN/PrimeKG; no provienen del prospecto):** hipertensión, insuficiencia y enfermedades hepáticas, colestasis, enfermedad de la vesícula biliar, insuficiencia cardíaca congestiva, hipotiroidismo, síndrome nefrótico, función renal alterada, trastornos psicóticos y mentales, enfermedades del tejido conectivo, óseas y del cartílago, abuso de sustancias, enfermedades de la coagulación sanguínea, hiperlipidemia, anemias (incluida la macrocítica) y enfermedad diarreica crónica.
- **Interacciones farmacológicas:** se registraron 865 interacciones. Las de nivel **mayor** incluidas en la muestra son con **ácido acetilsalicílico** y **metronidazol**. Hay además numerosas de nivel moderado (por ejemplo ranitidina, rabeprazol, doxiciclina, metformina, amoxicilina, bupropión, aprepitant, mesalazina y varios corticoides como hidrocortisona, dexametasona, betametasona, triamcinolona y budesonida) y de nivel menor (acarbosa, albiglutida, ácido ascórbico).
- **Consideraciones adicionales (de la literatura sobre trombofilia):** riesgo de necrosis cutánea inducida por warfarina (relacionada con deficiencia de proteína C/S), teratogenicidad en el embarazo y necesidad de monitorizar el INR.

Para advertencias y contraindicaciones del prospecto, consultar el prospecto del producto; esa información no estaba disponible en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal se apoya únicamente en tres reportes de casos antiguos, sin ensayos clínicos ni evidencia comparativa de eficacia. Además, el único registro sanitario en Colombia está cancelado y no hay datos de seguridad del prospecto, lo que impide avanzar al tamizaje de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), un vacío de datos bloqueante.
- Confirmar el mecanismo de acción desde DrugBank.
- Aclarar la situación regulatoria: ningún registro vigente de warfarina en los datos revisados, y la indicación registrada no es específica.
- Considerar priorizar la **trombofilia** (nivel L3) como pregunta de investigación, apoyada en el ensayo Fase 3 NCT00895505 (estado desconocido, sin resultados) y en las revisiones, con salvaguardas: tamizaje de proteína C/S, evitar el uso en embarazo y monitorización del INR.
- Para las demás indicaciones de TxGNN, buscar estudios clínicos específicos de eficacia; las asociaciones con artritis reumatoide y enfermedad fibroquística de la mama parecen reflejar coprescripción e interacciones, no beneficio terapéutico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

