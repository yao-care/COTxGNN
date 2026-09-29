---
layout: default
title: Betamethasone
parent: Evidencia Alta (L1-L2)
nav_order: 88
evidence_level: L2
indication_count: 10
---

# Betamethasone
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **10** 
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

# Betametasona: De Betametasona y Antibióticos Tópicos a Alopecia Areata

## Resumen en Una Frase

La betametasona es un glucocorticoide sintético que en Colombia está registrado en cremas tópicas combinadas con antibióticos y antifúngicos. El modelo TxGNN predice que podría ser efectivo para **alopecia areata**, con **8 ensayos clínicos** y **20 publicaciones** que respaldan esta dirección. La evidencia directa más sólida es un ensayo de Fase 2 completado y varios ECA publicados.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Betametasona y antibióticos (crema tópica combinada) |
| Nueva Indicación Predicha | Alopecia areata |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el campo original de DrugBank. Según la información farmacológica disponible, la betametasona es un agonista del receptor de glucocorticoides (NR3C1) con actividad antiinflamatoria, antipruriginosa y vasoconstrictora. Se usa en dermatitis atópica, seborreica y de contacto, psoriasis y reacciones por picaduras.

La alopecia areata es una enfermedad autoinmune en la que los linfocitos T atacan el folículo piloso y rompen su privilegio inmunológico. Un corticoide potente puede suprimir esa respuesta inflamatoria e inmunitaria. Esto conecta su uso dermatológico actual, que es antiinflamatorio, con la nueva indicación.

Los corticoides ya son un tratamiento establecido para esta enfermedad. La betametasona se ha evaluado por vía tópica, intralesional, en microagujas y en minipulsos orales. Por eso la predicción tiene respaldo mecanístico y clínico, aunque el puntaje del modelo no es evidencia clínica por sí mismo.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06786689](https://clinicaltrials.gov/study/NCT06786689) | Fase 2 | Completado | 60 | Azatioprina semanal en pulso vs. minipulso oral de betametasona en alopecia areata moderada a grave. Evidencia directa para esta indicación y vía. |
| [NCT02350023](https://clinicaltrials.gov/study/NCT02350023) | Fase 4 | Completado | 50 | Estudio aleatorizado que compara latanoprost tópico con corticoide tópico en alopecia areata localizada. El corticoide es el comparador. |
| [NCT03535233](https://clinicaltrials.gov/study/NCT03535233) | Fase 4 | Completado | 40 | Minoxidil 5% más corticoide tópico potente vs. triamcinolona intralesional. No se confirma que el corticoide sea betametasona. |
| [NCT05803070](https://clinicaltrials.gov/study/NCT05803070) | N/A | Desconocido | 59 | Cetirizina tópica 1% vs. betametasona valerato 0.1% en alopecia areata localizada. La betametasona es el comparador. |
| [NCT06087796](https://clinicaltrials.gov/study/NCT06087796) | Fase 1 | Desconocido | 60 | Pentoxifilina y metformina tópicas vs. betametasona valerato 0.1% en alopecia areata en parches. La betametasona es el comparador activo. |
| [NCT07696585](https://clinicaltrials.gov/study/NCT07696585) | N/A | Aún no recluta | 60 | Metformina 30%, simvastatina 2% y betametasona valerato 0.1% tópicos en alopecia areata en parches. Aún sin resultados. |
| [NCT04207931](https://clinicaltrials.gov/study/NCT04207931) | Fase 4 | Reclutando | 250 | Alopecia cicatricial centrífuga central, que no es alopecia areata. Relevancia solo indirecta. |
| [NCT01111981](https://clinicaltrials.gov/study/NCT01111981) | Fase 4 | Desconocido | 30 | Espuma de clobetasol en alopecia cicatricial centrífuga central. Otro fármaco y otra enfermedad; relevancia solo de clase. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | Metaanálisis en red | Cochrane Database Syst Rev | Compara inmunosupresores, estimulantes del crecimiento capilar e inmunoterapia de contacto en alopecia areata. |
| [39393548](https://pubmed.ncbi.nlm.nih.gov/39393548/) | 2025 | ECA | J Am Acad Dermatol | Administración transdérmica de betametasona compuesta con microagujas, como alternativa a la inyección intralesional, que puede ser muy dolorosa. |
| [36257912](https://pubmed.ncbi.nlm.nih.gov/36257912/) | 2022 | ECA doble ciego | Dermatol Ther | Latanoprost vs. minoxidil, betametasona y sus combinaciones (6 grupos de 18 pacientes). |
| [34400956](https://pubmed.ncbi.nlm.nih.gov/34400956/) | 2021 | ECA doble ciego, con placebo | Iran J Pharm Res | Betametasona oral en pulso (3 mg semanales), metotrexato (15 mg semanales) y su combinación en 36 pacientes con alopecia areata grave. |
| [40510104](https://pubmed.ncbi.nlm.nih.gov/40510104/) | 2025 | ECA | Cureus | Ciclosporina oral vs. minipulsos de betametasona oral en 60 pacientes. |
| [32594786](https://pubmed.ncbi.nlm.nih.gov/32594786/) | 2022 | ECA intrapaciente | J Dermatol Treat | Betametasona intralesional vs. triamcinolona acetónido en alopecia areata localizada. |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Revisión | Dermatol Pract Concept | Eficacia, recaídas, efectos adversos y factores pronósticos de la terapia de pulsos con corticoides en alopecia areata. |
| [40519428](https://pubmed.ncbi.nlm.nih.gov/40519428/) | 2025 | Estudio clínico | Cureus | Eficacia y seguridad de minipulsos orales de betametasona en alopecia areata moderada a grave. |
| [38623137](https://pubmed.ncbi.nlm.nih.gov/38623137/) | 2024 | Estudio clínico comparativo | Cureus | Betametasona dipropionato tópica vs. minoxidil tópico (diseño no confirmado). |
| [31516138](https://pubmed.ncbi.nlm.nih.gov/31516138/) | 2019 | Estudio comparativo | Indian J Dermatol | Azatioprina semanal en pulso vs. minipulso oral de betametasona en alopecia areata moderada a grave. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20114683 | Betametasona + Clotrimazol 1% + Neomicina 0.5% (Aplicaciones Farmacéuticas AFAVEL S.A.S.) | Crema tópica | Betametasona y antibióticos |

Los 5 registros devueltos por la consulta corresponden al mismo registro sanitario. En total hay 20 registros, pero el resto no aparece en los datos recibidos.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: No se reportan interacciones fármaco-fármaco. El único registro es de tipo farmacológico: la betametasona actúa sobre el receptor de glucocorticoides (NR3C1).
- **Precauciones según las vías evaluadas**: vigilar atrofia cutánea con uso tópico y los efectos adversos sistémicos de los esteroides con la terapia oral en pulsos.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay un ensayo de Fase 2 completado, varios ensayos de Fase 4 completados y múltiples ECA publicados con betametasona en alopecia areata, lo que corresponde a un nivel de evidencia L2. No hay ningún ensayo de Fase 3 en los datos, y en varios estudios la betametasona es solo el comparador. Las otras 9 indicaciones predichas tienen evidencia mucho más débil (L4-L5) y quedan en Hold o como pregunta de investigación.

**Para avanzar se necesita:**
- Ensayos de Fase 3 o metaanálisis que comparen la betametasona con corticoides de referencia en alopecia areata.
- Definir la vía y el régimen (tópico, intralesional, minipulso oral), ya que los registros locales son solo cremas tópicas combinadas con antibióticos.
- Obtener del prospecto de INVIMA las advertencias y contraindicaciones, que no están en los datos actuales.
- Plan de monitoreo de seguridad: atrofia cutánea con uso tópico y efectos sistémicos con la terapia oral.
- Datos detallados del mecanismo de acción (MOA) desde DrugBank.

*Este resultado es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

