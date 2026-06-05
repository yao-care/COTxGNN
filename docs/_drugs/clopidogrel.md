---
layout: default
title: Clopidogrel
parent: 僅模型預測 (L5)
nav_order: 90
evidence_level: L5
indication_count: 8
---

# Clopidogrel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Clopidogrel: De Enfermedad Cardiovascular Ateroesclerótica a Migraña con Aura de Tronco Cerebral

## Resumen en Una Frase

Clopidogrel es un inhibidor irreversible del receptor plaquetario P2Y12, ampliamente utilizado a nivel mundial para la prevención de eventos aterotrombóticos en síndrome coronario agudo, ictus isquémico y enfermedad arterial periférica, aunque actualmente no cuenta con registro sanitario en Colombia. El modelo TxGNN predice que podría ser efectivo para la **migraña con aura de tronco cerebral**, con **0 ensayos clínicos específicos** y **16 publicaciones** que actualmente respaldan esta dirección. La evidencia disponible proviene principalmente de estudios observacionales y un ensayo piloto aleatorizado, todos ellos en pacientes con foramen oval permeable (FOP), lo que sugiere un subgrupo específico de beneficio potencial.

---

## Resumen Rápido

| Ítem | Contenido |
|------|------|
| Indicación Original | Prevención de eventos aterotrombóticos (síndrome coronario agudo, ictus isquémico, enfermedad arterial periférica) |
| Nueva Indicación Predicha | Migraña con aura de tronco cerebral |
| Puntaje de Predicción TxGNN | 99.44% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Aunque los datos formales de mecanismo de acción no están disponibles en este Evidence Pack, Clopidogrel es una tienopiridina cuyo perfil farmacológico está bien caracterizado en la literatura científica: inhibe de forma irreversible el receptor P2Y12 en las plaquetas, bloqueando la agregación inducida por ADP y reduciendo la liberación plaquetaria de serotonina (5-HT), tromboxano A₂ y otros mediadores vasoactivos.

La migraña con aura de tronco cerebral (anteriormente denominada migraña basilar) involucra mecanismos de depresión cortical propagada a nivel del tronco encefálico (BS-CSD) y alteraciones en la vasculatura de la arteria basilar. En pacientes con foramen oval permeable (FOP), los microémbolos del circuito venoso pueden eludir el filtro pulmonar y activar directamente los núcleos trigeminales del tronco cerebral, desencadenando el fenómeno de aura y la cefalea. Al reducir la activación plaquetaria y la liberación de mediadores vasoactivos, Clopidogrel podría interrumpir este mecanismo de disparo en el subgrupo de pacientes con FOP significativo como factor contribuyente.

No obstante, la conexión mecanística tiene límites claros: la migraña con aura de tronco cerebral también involucra canalopatías iónicas (gen *CACNA1A*) y alteraciones en el umbral de CSD que no son modificables por agentes antiplaquetarios. El beneficio potencial de Clopidogrel estaría restringido al subgrupo con shunt derecha-izquierda demostrado, y no aplica a la población general de migrañosos con aura basilar de origen primario.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos registrados específicamente para la indicación de migraña con aura de tronco cerebral.

> **Contexto clínico**: Los ensayos clínicos con Clopidogrel en el espectro de la migraña están registrados bajo la categoría más amplia de "migraña" (Rank 2 de este informe), donde existe evidencia de mayor jerarquía, incluyendo el ensayo completado CANOA (NCT00799045, N=220, Fase 4) y el ensayo en curso COMPETE (NCT05546320, N=1.000, Fase 4).

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Revisión Sistemática | *Headache* | Explora la evidencia disponible sobre el rol de los antitrombóticos como medicación preventiva de migraña; incluye análisis de clopidogrel |
| [26908949](https://pubmed.ncbi.nlm.nih.gov/26908949/) | 2016 | ECA | *European Heart Journal* | Ensayo PRIMA: cierre percutáneo de FOP vs tratamiento médico en migraña con aura refractaria; clopidogrel como componente del brazo de cierre |
| [24836213](https://pubmed.ncbi.nlm.nih.gov/24836213/) | 2014 | ECA Piloto | *Cephalalgia* | Clopidogrel como tratamiento profiláctico de migraña: primer ensayo piloto aleatorizado controlado con este fármaco en población migrañosa general |
| [32848048](https://pubmed.ncbi.nlm.nih.gov/32848048/) | 2020 | Cohorte Observacional | *J Investig Med* | Clopidogrel 75 mg/día añadido al régimen profiláctico existente por 3–6 meses en migrañosos refractarios con FOP; FOP presente en 56.8% de los pacientes |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Observacional | *Heart* | Clopidogrel reduce migraña con aura tras cierre transcatéter de FOP y comunicación interauricular (CIA); primer reporte que vincula clopidogrel con reducción de migraña con aura |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | Piloto Abierto | *Neurology* | Estudio TRACTOR: ticagrelor (otro inhibidor P2Y12) reproduce efectos similares a clopidogrel en migraña refractaria con FOP, reforzando el papel del eje P2Y12 |
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Cohorte Retrospectiva | *Neurology* | Revisión retrospectiva de tienopiridinas (clopidogrel y prasugrel) en migrañosos con FOP; reporta reducción de frecuencia de ataques en subgrupo respondedor |
| [24770421](https://pubmed.ncbi.nlm.nih.gov/24770421/) | 2014 | Revisión Retrospectiva | *Cephalalgia* | Clopidogrel como terapia primaria en migrañosos con shunt derecha-izquierda; vincula activación plaquetaria y embolización paradójica con la fisiopatología de la migraña con aura |
| [15966922](https://pubmed.ncbi.nlm.nih.gov/15966922/) | 2005 | Serie de Casos | *J Interv Cardiol* | Migraña intensa en 5/13 pacientes tras cierre percutáneo de CIA; alivio casi inmediato con 300 mg de clopidogrel, sugiriendo rol mediado por plaquetas |
| [22992406](https://pubmed.ncbi.nlm.nih.gov/22992406/) | 2012 | Caso Clínico | *Cephalalgia* | Migraña de novo tras cierre de CIA; antiagregantes plaquetarios incluyendo clopidogrel asociados a mejoría de síntomas migrañosos post-procedimiento |

---

## Información de Mercado en Colombia

Clopidogrel **no cuenta con registros sanitarios INVIMA activos** a la fecha de corte de este informe (2026-06-04). No está comercializado en Colombia bajo ninguna forma farmacéutica ni concentración disponible en el mercado local.

> **Nota para la estrategia regulatoria**: Dado que Clopidogrel es un fármaco esencial de amplio uso global con múltiples aprobaciones internacionales (FDA, EMA, entre otras), la ruta regulatoria para su introducción al mercado colombiano deberá iniciarse desde el proceso de registro ante INVIMA, lo que representa un prerrequisito para cualquier aplicación clínica o estudio local.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación específica de migraña con aura de tronco cerebral no cuenta con ensayos clínicos directos registrados, y la evidencia disponible (16 publicaciones, predominantemente observacionales, en su mayoría en el contexto de FOP/CIA) corresponde a un nivel L3 que no es suficiente para respaldar una estrategia de reposicionamiento formal e independiente en esta subpoblación. Adicionalmente, Clopidogrel no está registrado en Colombia, lo que añade una barrera regulatoria significativa antes de cualquier aplicación clínica.

> **Recomendación paralela**: La indicación de **migraña (general)** — Rank 2 de este informe — alcanza nivel de evidencia L2 con la recomendación "Proceed with Guardrails", respaldada por el ensayo completado CANOA (JAMA y JAMA Cardiology) y el ensayo en curso COMPETE (N=1.000). Esta indicación más amplia representa la estrategia prioritaria de exploración.

**Para avanzar se necesita:**
- Consultar DrugBank API para obtener datos formales de mecanismo de acción (MOA) — remediación DG002
- Obtener y analizar el prospecto oficial (PDF INVIMA o FDA/EMA) para completar advertencias, contraindicaciones e interacciones farmacológicas — remediación DG001
- Iniciar proceso de registro sanitario ante INVIMA como prerrequisito regulatorio colombiano
- Diseñar protocolo de ensayo clínico específico en migraña con aura de tronco cerebral con confirmación de FOP mediante ecocardiografía con contraste
- Considerar estrategia conjunta con la indicación de migraña general (Rank 2) para mayor eficiencia regulatoria y clínica
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

