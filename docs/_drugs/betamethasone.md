---
layout: default
title: Betamethasone
parent: Solo Predicción del Modelo (L5)
nav_order: 104
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Betamethasone: nueva indicación predicha, Alopecia areata (nivel de evidencia L5). Indicación original: Betametasona y antibióticos"
monitor_inn: "Betamethasone"
predicted_indications: ["alopecia areata", "alopecia mucinosa", "telogen effluvium", "Quinquaud's folliculitis decalvans", "alopecia antibody deficiency", "hereditary hypotrichosis with recurrent skin vesicles", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "atrichia with papular lesions", "idiopathic steroid-sensitive nephrotic syndrome", "sporadic idiopathic steroid-resistant nephrotic syndrome"]
---

# Betamethasone
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

# Betametasona: De Betametasona y Antibióticos (crema tópica) a Alopecia Areata

## Resumen en Una Frase

Betametasona es un glucocorticoide sintético, autorizado en Colombia en cremas tópicas combinadas con antibióticos (por ejemplo, betametasona + clotrimazol + neomicina).
El modelo TxGNN predice que podría ser efectivo para **alopecia areata**,
con **6 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Betametasona y antibióticos |
| Nueva Indicación Predicha | Alopecia areata |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L1 (con reservas; ver nota abajo) |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 4 (todos cancelados) |
| Decisión Recomendada | Proceed with Guardrails |

> **Nota sobre el nivel de evidencia:** el nivel L1 se basa en varios ensayos aleatorizados y un metaanálisis en red. Sin embargo, no se confirma en los datos compilados la existencia de dos ECA de Fase 3 completados, por lo que el nivel debe verificarse antes de la aprobación final. Los ensayos de Fase 2 y Fase 4 usan la betametasona sobre todo como comparador activo o en combinación.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información farmacológica conocida, la betametasona es un agonista del receptor de glucocorticoides (NR3C1) con actividad antiinflamatoria, antipruriginosa y vasoconstrictora. Se utiliza en dermatitis atópica, seborreica y de contacto, psoriasis y reacciones por picaduras.

La alopecia areata es una enfermedad autoinmune en la que se pierde el privilegio inmunitario del folículo piloso y se produce un ataque inflamatorio mediado por linfocitos T CD8+. La betametasona, al activar el receptor de glucocorticoides, inhibe citocinas proinflamatorias y puede frenar ese ataque inmunitario. Existen descripciones de uso tópico, intralesional y en minipulsos orales.

La relación con la indicación original es la inflamación cutánea tratable con corticoides. Aun así, la evidencia respalda a la betametasona como terapia activa o comparador establecido, no como un tratamiento nuevo demostrado superior.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06786689](https://clinicaltrials.gov/study/NCT06786689) | Fase 2 | Completado | 60 | Azatioprina semanal en pulsos vs. minipulsos orales de betametasona en alopecia areata moderada a grave |
| [NCT02350023](https://clinicaltrials.gov/study/NCT02350023) | Fase 4 | Completado | 50 | Latanoprost tópico vs. corticoide tópico (betametasona) en alopecia areata localizada |
| [NCT05803070](https://clinicaltrials.gov/study/NCT05803070) | N/A | Desconocido | 59 | Cetirizina tópica 1% vs. valerato de betametasona 0.1% en alopecia areata localizada |
| [NCT06087796](https://clinicaltrials.gov/study/NCT06087796) | Fase 1 | Desconocido | 60 | Pentoxifilina y metformina tópicas vs. valerato de betametasona 0.1% en alopecia areata en parches |
| [NCT07696585](https://clinicaltrials.gov/study/NCT07696585) | N/A | Aún no recluta | 60 | Metformina 30%, simvastatina 2% y valerato de betametasona 0.1% en alopecia areata en parches; sin resultados |
| [NCT04207931](https://clinicaltrials.gov/study/NCT04207931) | Fase 4 | Reclutando | 250 | Alopecia cicatricial centrífuga central (otra enfermedad); relación solo indirecta |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | Metaanálisis en red | Cochrane Database Syst Rev | Comparación de tratamientos (inmunosupresores, estimulantes del crecimiento, inmunoterapia de contacto) en alopecia areata |
| [39393548](https://pubmed.ncbi.nlm.nih.gov/39393548/) | 2025 | ECA | J Am Acad Dermatol | Administración transdérmica con microagujas de betametasona compuesta en alopecia areata |
| [28521549](https://pubmed.ncbi.nlm.nih.gov/28521549/) | 2018 | ECA | J Dermatol Treat | Latanoprost tópico vs. minoxidil y valerato de betametasona |
| [36257912](https://pubmed.ncbi.nlm.nih.gov/36257912/) | 2022 | ECA | Dermatol Ther | Latanoprost vs. minoxidil, betametasona y su combinación; ensayo ciego con seis grupos |
| [34400956](https://pubmed.ncbi.nlm.nih.gov/34400956/) | 2021 | ECA | Iran J Pharm Res | Pulsos orales de betametasona, metotrexato y su combinación en alopecia areata grave, con placebo |
| [32594786](https://pubmed.ncbi.nlm.nih.gov/32594786/) | 2022 | ECA intrapaciente | J Dermatol Treat | Betametasona vs. acetónido de triamcinolona intralesional en alopecia areata localizada |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Revisión | Dermatol Pract Concept | Eficacia, recaídas y efectos adversos de la terapia de pulsos de corticoides en alopecia areata |
| [38623137](https://pubmed.ncbi.nlm.nih.gov/38623137/) | 2024 | Estudio comparativo/ECA | Cureus | Dipropionato de betametasona tópico vs. minoxidil tópico |
| [36114868](https://pubmed.ncbi.nlm.nih.gov/36114868/) | 2023 | Estudio clínico comparativo | Arch Dermatol Res | Láser de CO2 fraccionado solo o combinado con valerato de betametasona |
| [40519428](https://pubmed.ncbi.nlm.nih.gov/40519428/) | 2025 | Estudio clínico | Cureus | Eficacia y seguridad de minipulsos orales de betametasona en alopecia areata moderada a grave |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20114683 | Betametasona + Clotrimazol 1% + Neomicina 0.5% | Crema tópica | Betametasona y antibióticos | Cancelado |
| 20137501 | DKG Crema® | Crema tópica | Betametasona y antibióticos | Cancelado |
| 20256128 | Derprosol Trex® Crema | Crema tópica | Betametasona y antibióticos | Cancelado |
| 20176216 | Ephitree® | Crema tópica | Betametasona y antibióticos | Cancelado |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** el grafo de conocimiento asocia la betametasona con enfermedades en las que su uso requiere precaución o está desaconsejado, entre ellas hipertensión, insuficiencia cardíaca congestiva, hiperglucemia, epilepsia, queratitis herpética por virus del herpes simple, sarampión, trastornos del ciclo de la urea (deficiencia de carbamoil fosfato sintetasa I, citrulinemia, hiperargininemia) y diversos déficits hipofisarios y de hormona del crecimiento (hipopituitarismo, síndrome de Sheehan, síndrome de Kallmann, hipogonadismo hipogonadotrópico).
- **Interacciones farmacológicas:** solo se registra la interacción farmacológica con el receptor de glucocorticoides (NR3C1), que es su diana principal. No hay interacciones con otros fármacos.

Consultar el prospecto para las advertencias y contraindicaciones oficiales.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay varios ECA y un metaanálisis en red que incluyen betametasona en alopecia areata, con un mecanismo plausible. Sin embargo, la betametasona actúa principalmente como comparador o terapia establecida, no como una novedad, y no se ha confirmado el nivel de fase de los ensayos principales. Además, los cuatro registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Confirmar la fase y los resultados de los ECA principales antes de la aprobación final del nivel L1.
- Obtener el prospecto oficial (INVIMA) con advertencias y contraindicaciones, y los datos detallados del mecanismo de acción (DrugBank).
- Definir la vía regulatoria en Colombia, dado que no hay registros vigentes y los registros existentes son de cremas combinadas con antibióticos, no de betametasona sola para esta indicación.
- Evaluar la vía de administración (tópica, intralesional o minipulsos orales) y un plan de monitoreo de seguridad, en especial por los efectos sistémicos con el uso oral (hipertensión, hiperglucemia).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

