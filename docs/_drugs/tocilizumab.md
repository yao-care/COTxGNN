---
layout: default
title: Tocilizumab
parent: 僅模型預測 (L5)
nav_order: 225
evidence_level: L5
indication_count: 10
---

# Tocilizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# TOCILIZUMAB: De Artritis Reumatoide a Espondilitis Anquilosante

## Resumen en Una Frase

Tocilizumab es un anticuerpo monoclonal humanizado anti-receptor de IL-6, aprobado internacionalmente para el tratamiento de la artritis reumatoide, la artritis idiopática juvenil y la arteritis de células gigantes, aunque actualmente no cuenta con registro sanitario en Colombia.
El modelo TxGNN predice que podría ser efectivo para **Espondilitis Anquilosante**,
con **9 ensayos clínicos** y **19 publicaciones** que actualmente informan esta dirección — incluyendo dos ensayos pivotales de Fase 3 terminados anticipadamente por insuficiencia de eficacia.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Artritis Reumatoide (aprobación internacional; sin registro en Colombia) |
| Nueva Indicación Predicha | Espondilitis Anquilosante |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el sistema. Según la información disponible en la literatura incluida en el paquete de evidencia, Tocilizumab es un anticuerpo monoclonal humanizado recombinante que actúa como antagonista del receptor de interleucina-6 (IL-6R). Bloquea de forma competitiva tanto el receptor de membrana como el receptor soluble de IL-6, inhibiendo la señalización downstream JAK-STAT3 y suprimiendo la producción de reactantes de fase aguda (PCR, fibrinógeno, amiloide sérico A). Esta acción explica su eficacia en enfermedades inflamatorias crónicas impulsadas por IL-6, como la artritis reumatoide y la arteritis de células gigantes.

La espondilitis anquilosante (EA) y la artritis reumatoide comparten la participación de la IL-6 como mediador de inflamación sistémica, degradación articular y activación de osteoclastos. En la EA, la IL-6 se encuentra elevada en suero y líquido sinovial, contribuye a la formación de sindesmofitos y media manifestaciones extraarticulares como la amiloidosis AA secundaria — un contexto en el que casos publicados confirman beneficio de TCZ (PMID 33981717). Esta superposición mecanística justifica que el modelo TxGNN asigne alta probabilidad a esta indicación.

Sin embargo, la EA axial está predominantemente impulsada por el eje IL-17/TNF, con una contribución de IL-6 secundaria y diferente en naturaleza respecto a la AR. Esta distinción fisiopatológica tiene consecuencias clínicas concretas y graves: los ensayos BUILDER-1 (NCT01209689, n=113) y BUILDER-2 (NCT01209702, n=306) — ambos estudios de Fase 3, aleatorizados, doble ciego y controlados con placebo — fueron terminados anticipadamente por insuficiencia de eficacia. La predicción TxGNN de alto puntaje refleja probablemente la proximidad en el grafo de conocimiento entre nodos de enfermedades reumatológicas con inflamación común, más que una señal real de eficacia clínica en la EA axial.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01209689](https://clinicaltrials.gov/study/NCT01209689) | Fase 3 | **Terminado** | 113 | BUILDER-1: TCZ (8 mg/kg o 4 mg/kg IV) vs placebo cada 4 semanas en EA con respuesta inadecuada a TNF; terminado anticipadamente por insuficiencia de eficacia — evidencia negativa pivotal |
| [NCT01209702](https://clinicaltrials.gov/study/NCT01209702) | Fase 2/3 | **Terminado** | 306 | BUILDER-2: TCZ vs placebo en EA naïve a TNF y con fallo a AINEs; terminado anticipadamente, confirmando señal de eficacia insuficiente en enfermedad axial |
| [NCT02569736](https://clinicaltrials.gov/study/NCT02569736) | N/A | Completado | 60 | Estudio mecanístico del efecto de TCZ en células T foliculares auxiliares (Tfh) in vivo e in vitro en pacientes con AR y EA; provee soporte mecanístico sobre la inhibición de la señalización IL-6 |
| [NCT05670301](https://clinicaltrials.gov/study/NCT05670301) | N/A | Reclutando | 2.500 | Estudio prospectivo multicéntrico flamenco de perfiles de citocinas en enfermedades inflamatorias sistémicas, incluyendo EA; diseño observacional longitudinal |
| [NCT07477795](https://clinicaltrials.gov/study/NCT07477795) | Fase 2 | No iniciado | 52 | RCT bayesiano prospectivo de secukinumab en arteritis de Takayasu severa activa; relevancia indirecta como ensayo emergente en vasculitis SpA-relacionada |
| [NCT01965132](https://clinicaltrials.gov/study/NCT01965132) | N/A | Reclutando | 10.000 | Registro nacional coreano de biológicos y terapias dirigidas en AR, EA y artritis psoriásica; datos de perfil de seguridad en vida real con TCZ |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [26986130](https://pubmed.ncbi.nlm.nih.gov/26986130/) | 2016 | Revisión Sistemática | Medicine | Meta-análisis en red bayesiana comparando todos los biológicos disponibles para EA; TCZ no demostró ventaja significativa sobre anti-TNF ni anti-IL-17 en criterios de valoración primarios |
| [29278210](https://pubmed.ncbi.nlm.nih.gov/29278210/) | 2018 | Revisión Sistemática | Clin Rheumatol | Meta-análisis cuantitativo del riesgo de infecciones graves con biológicos en EA y nr-axSpA; perfil de seguridad comparativo incluyendo TCZ en contexto de artritis axial |
| [23765873](https://pubmed.ncbi.nlm.nih.gov/23765873/) | 2014 | ECA (publicación) | Ann Rheum Dis | Resultados publicados de BUILDER-1 y BUILDER-2: evaluación de eficacia sintomática a corto plazo de TCZ en EA — los criterios de valoración primarios no fueron alcanzados en ninguno de los dos ensayos |
| [22452603](https://pubmed.ncbi.nlm.nih.gov/22452603/) | 2012 | Revisión | Inflamm Allergy Drug Targets | Revisión del antagonismo de IL-6 en EA; discute por qué la EA presenta respuesta limitada a TCZ pese al papel de IL-6 en su patogenia, señalando el predominio del eje IL-17 en la enfermedad axial |
| [21803631](https://pubmed.ncbi.nlm.nih.gov/21803631/) | 2011 | Revisión | Joint Bone Spine | Biológicos más allá de los antagonistas TNFα en EA; posiciona TCZ como alternativa exploratoria con fundamento mecanístico pero evidencia clínica limitada en el momento de publicación |
| [22450391](https://pubmed.ncbi.nlm.nih.gov/22450391/) | 2012 | Revisión | Curr Opin Rheumatol | Tratamiento de EA refractaria a inhibidores TNF; revisa nuevas clases farmacológicas incluyendo TCZ, con resultados considerados decepcionantes a la luz de los ensayos BUILDER |
| [33981717](https://pubmed.ncbi.nlm.nih.gov/33981717/) | 2021 | Reporte de Caso | Front Med | Dos casos de amiloidosis AA secundaria a EA tratados exitosamente con TCZ; documenta eficacia en complicaciones sistémicas IL-6-dependientes de la EA, subpoblación potencialmente respondedora |
| [28413099](https://pubmed.ncbi.nlm.nih.gov/28413099/) | 2017 | Revisión | Semin Arthritis Rheum | Optimización de segunda línea de biológicos en AR, AP y EA; TCZ posicionado como opción de segunda línea en EA con evidencia clínica mixta e insuficiente para recomendación generalizada |
| [31852268](https://pubmed.ncbi.nlm.nih.gov/31852268/) | 2020 | Cohorte | Expert Rev Clin Immunol | Riesgo de infección comparativo en artritis inflamatoria con biológicos vs no biológicos; perfil de seguridad relevante incluyendo TCZ en espectro de artritis inflamatoria |
| [20959960](https://pubmed.ncbi.nlm.nih.gov/20959960/) | 2011 | Revisión | Osteoporos Int | Efectos óseos sistémicos de biológicos en AR y EA; describe el impacto de la inhibición de IL-6 sobre la fragilidad ósea y el metabolismo óseo en enfermedades reumáticas crónicas |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Dos ensayos pivotales de Fase 3, aleatorizados, doble ciego y controlados con placebo (BUILDER-1, n=113; BUILDER-2, n=306) fueron terminados anticipadamente por insuficiencia de eficacia de tocilizumab en la espondilitis anquilosante axial. Esta evidencia negativa directa, publicada y confirmada en meta-análisis sistémicos, supera el alto puntaje predicho por TxGNN, que refleja proximidad en el grafo de conocimiento más que señal clínica real. La diferencia mecanística fundamental — EA axial impulsada por IL-17/TNF vs AR impulsada por IL-6 — explica el fracaso clínico observado.

**Para avanzar se necesita:**
- Identificar y caracterizar subgrupos de pacientes con EA que presenten predominio inflamatorio IL-6 (por ejemplo, EA con amiloidosis AA secundaria, manifestaciones extraarticulares severas o perfiles elevados de IL-6 sérica)
- Diseñar ensayos clínicos dirigidos específicamente a estas subpoblaciones, con biomarcadores de selección (IL-6 sérica, proteína amiloide A sérica)
- Obtener registro sanitario INVIMA en Colombia antes de cualquier iniciativa de reposicionamiento (actualmente no comercializado, 0 registros sanitarios)
- Completar ficha de mecanismo de acción (MOA) desde DrugBank para fundamentar análisis de relación mecanística completo
- Revisar información de seguridad del prospecto oficial para evaluar perfil de riesgo en la población colombiana objetivo
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

