---
layout: default
title: Montelukast
parent: Solo Predicción del Modelo (L5)
nav_order: 454
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Montelukast: nueva indicación predicha, Bronquitis (nivel de evidencia L5). Indicación original: No especificada en el registro (el texto aprobado solo dice \"MONTELUK…"
---

# Montelukast
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Montelukast: De Indicación No Detallada en el Registro a Bronquitis

## Resumen en Una Frase

Montelukast es un antagonista del receptor de cisteinil-leucotrienos (CysLT1). En Colombia solo figura un registro sanitario, hoy cancelado, cuyo texto de indicación se limita al nombre del fármaco. El modelo TxGNN predice que podría ser efectivo para **bronquitis**, con **17 ensayos clínicos** y **20 publicaciones** relacionados. Sin embargo, buena parte de esa evidencia se refiere a bronquiolitis y bronquiolitis obliterante, no a bronquitis en sentido estricto.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo dice "MONTELUKAST"). La literatura lo describe como fármaco para asma y rinitis alérgica |
| Nueva Indicación Predicha | Bronquitis |
| Puntaje de Predicción TxGNN | 99.95% |
| Nivel de Evidencia | L2 (un ensayo de Fase 3 completado; no hay dos ECA de Fase 3 completados) |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados (sin registro vigente) |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la literatura revisada, montelukast es un antagonista selectivo del receptor CysLT1. Bloquea los efectos de los leucotrienos, mediadores inflamatorios que provocan broncoconstricción, aumento de la secreción de moco y reclutamiento de eosinófilos.

La relación con la bronquitis es plausible. Los leucotrienos participan en la inflamación de la vía aérea inferior. Varios estudios exploran montelukast en cuadros cercanos: bronquiolitis viral en lactantes, bronquitis obstructiva recurrente en niños, bronquitis eosinofílica no asmática y bronquiolitis obliterante tras trasplante. La literatura señala que los leucotrienos cisteinílicos se liberan durante la infección por virus respiratorio sincitial (VRS), lo que respalda la hipótesis.

El puntaje del modelo debe leerse con cautela. La mayoría de los ensayos son sobre bronquiolitis, un cuadro distinto de la bronquitis. Además, la relevancia de los ensayos para esta indicación aún no ha sido evaluada.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00076973](https://clinicaltrials.gov/study/NCT00076973) | Fase 3 | Completado | 1125 | Dos dosis de montelukast (MK0476) vs. placebo para síntomas respiratorios de bronquiolitis por VRS en niños de 3 a 24 meses |
| [NCT00863317](https://clinicaltrials.gov/study/NCT00863317) | N/A | Completado | 141 | Montelukast diario vs. placebo, doble ciego, sobre la duración de la enfermedad aguda en lactantes con primera bronquiolitis |
| [NCT01370187](https://clinicaltrials.gov/study/NCT01370187) | N/A | Completado | 146 | Montelukast en bronquiolitis aguda y sibilancias posbronquiolitis en lactantes de 3 a 12 meses |
| [NCT00524693](https://clinicaltrials.gov/study/NCT00524693) | N/A | Completado | 51 | Montelukast vs. placebo en bronquiolitis aguda por VRS: evolución clínica y perfil de citoquinas |
| [NCT04613180](https://clinicaltrials.gov/study/NCT04613180) | Fase 4 | Desconocido | 100 | Eficacia de montelukast para tratar y prevenir la bronquitis obstructiva recurrente en niños de 1 a 7 años |
| [NCT01121016](https://clinicaltrials.gov/study/NCT01121016) | Fase 4 | Desconocido | 63 | Montelukast añadido a budesonida inhalada en bronquitis eosinofílica no asmática (tos crónica/subaguda), doble ciego |
| [NCT00394160](https://clinicaltrials.gov/study/NCT00394160) | Fase 2 | Completado | 12 | Seguridad y perfil plasmático de montelukast en gránulos en lactantes de 1 a 3 meses con bronquiolitis |
| [NCT00656058](https://clinicaltrials.gov/study/NCT00656058) | Fase 2 | Completado | 25 | Montelukast para bronquiolitis obliterante tras trasplante de progenitores hematopoyéticos, en niños y adultos |
| [NCT01307462](https://clinicaltrials.gov/study/NCT01307462) | Fase 2 | Completado | 36 | Combinación fluticasona, azitromicina y montelukast en bronquiolitis obliterante tras trasplante de células madre |
| [NCT01211509](https://clinicaltrials.gov/study/NCT01211509) | Fase 4 | Completado | 30 | Montelukast vs. placebo para frenar el síndrome de bronquiolitis obliterante tras trasplante pulmonar |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [25773054](https://pubmed.ncbi.nlm.nih.gov/25773054/) | 2015 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Evalúa los inhibidores de leucotrienos, como montelukast, en bronquiolitis de lactantes y niños pequeños |
| [24118637](https://pubmed.ncbi.nlm.nih.gov/24118637/) | 2014 | Revisión sistemática | Pediatr Allergy Immunol | Eficacia de montelukast para prevenir sibilancias tras bronquiolitis por VRS |
| [25563311](https://pubmed.ncbi.nlm.nih.gov/25563311/) | 2015 | Estudio clínico | Chin Med J | Montelukast añadido a budesonida en bronquitis eosinofílica no asmática: efecto sobre inflamación de la vía aérea, tos y calidad de vida |
| [29704475](https://pubmed.ncbi.nlm.nih.gov/29704475/) | 2018 | Guía/Panel de expertos | Chest | Revisiones sistemáticas sobre tratamientos de la tos crónica posterior a bronquiolitis viral aguda en niños |
| [38504551](https://pubmed.ncbi.nlm.nih.gov/38504551/) | 2024 | Revisión | Ther Adv Respir Dis | Potencial terapéutico y posibles mecanismos de montelukast en bronquiolitis obliterante tras trasplante pulmonar y de progenitores hematopoyéticos |
| [38485149](https://pubmed.ncbi.nlm.nih.gov/38485149/) | 2024 | Guía de práctica clínica | Eur Respir J | Guías ERS/EBMT para el tratamiento de la enfermedad de injerto contra huésped crónica pulmonar en adultos |
| [40926299](https://pubmed.ncbi.nlm.nih.gov/40926299/) | 2025 | Consenso | Br J Haematol | Consenso de Taiwán sobre diagnóstico, vigilancia y manejo de la enfermedad de injerto contra huésped crónica pulmonar |
| [30038355](https://pubmed.ncbi.nlm.nih.gov/30038355/) | 2019 | Revisión | Bone Marrow Transplant | Retos diagnósticos y terapéuticos del síndrome de bronquiolitis obliterante |
| [28545478](https://pubmed.ncbi.nlm.nih.gov/28545478/) | 2017 | Preclínico (ratas) | J Cardiothorac Surg | Papel de LTB4 y montelukast en la bronquiolitis obliterante asociada a trasplante |
| [14766663](https://pubmed.ncbi.nlm.nih.gov/14766663/) | 2004 | Comentario | Am J Respir Crit Care Med | Comentario sobre montelukast en bronquiolitis por VRS |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20190806 (cancelado) | BONVENT® | Tableta masticable | Solo consta el nombre "MONTELUKAST", sin texto de indicación |

Fabricante: TECNOFAR TQ S.A.S. No hay registros vigentes para este fármaco.

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: se identificaron 100 interacciones. Las de nivel moderado incluyen dexametasona, metronidazol, miconazol, nateglinida, nitisinona y troglitazona. Otras interacciones listadas tienen nivel sin clasificar, entre ellas calcitriol, fentermina, pantoprazol, glimepirida, mesalazina, doxiciclina, clotrimazol, acarbosa, morfina, metformina, omeprazol, rosiglitazona, lansoprazol y sucralfato.
- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: el grafo de conocimiento del modelo asocia el fármaco con trastorno de ansiedad, trastorno neurótico, trastorno distímico, ansiedad, síndrome hipereosinofílico y vasculitis cutánea. Esto debe verificarse con fuentes clínicas.
- **Señal neuropsiquiátrica**: la literatura incluida señala que la FDA emitió en 2020 una advertencia en recuadro negro por eventos neuropsiquiátricos. Los estudios de cohorte y las revisiones sistemáticas citados en los datos compilados examinan este riesgo, también en niños.

Consultar el prospecto para las advertencias y contraindicaciones oficiales, que no están disponibles en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Existe un ensayo de Fase 3 completado con gran muestra (n=1125), pero evalúa bronquiolitis por VRS en lactantes, no bronquitis, y los datos disponibles no muestran sus resultados. El resto son estudios pequeños de Fase 2 o 4 y revisiones, con relevancia aún por evaluar. Además, no hay registro sanitario vigente en Colombia y no se pudo revisar la información de seguridad del prospecto, lo cual impide avanzar al tamizaje de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del registro en INVIMA (advertencias y contraindicaciones oficiales).
- Obtener los datos del mecanismo de acción desde DrugBank.
- Definir con precisión la indicación objetivo (bronquitis aguda, bronquitis obstructiva recurrente en niños, bronquitis eosinofílica o bronquiolitis) y revisar los resultados publicados de NCT00076973 y de la revisión Cochrane de 2015.
- Evaluar la relevancia de cada ensayo y publicación para la indicación elegida.
- Elaborar un plan de monitoreo neuropsiquiátrico, sobre todo si la población objetivo son niños.
- Aclarar la situación regulatoria: no hay registro vigente en Colombia.
- Como referencia, en los datos compilados otras predicciones tienen mayor respaldo: asma (L1, Proceed with Guardrails) y eccema atópico (L1, Research Question).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

