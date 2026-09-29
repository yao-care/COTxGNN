---
layout: default
title: Norethisterone
parent: Solo Predicción del Modelo (L5)
nav_order: 295
evidence_level: L5
indication_count: 1
---

# Norethisterone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Noretisterona: De Noretisterona y Estrógeno (anticoncepción y trastornos menstruales) a Amenorrea

## Resumen en Una Frase

La noretisterona es un progestágeno sintético que se usa como anticonceptivo y para tratar trastornos menstruales como la endometriosis o el sangrado vaginal anormal. En Colombia está registrada en una combinación con estrógeno.
El modelo TxGNN predice que podría ser efectiva para **amenorrea**, con **8 ensayos clínicos** y **20 publicaciones** relacionados. Ninguno evalúa directamente la noretisterona como tratamiento de la amenorrea, por lo que la evidencia es indirecta y débil.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Noretisterona y estrógeno (texto del registro INVIMA) |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 99.60% |
| Nivel de Evidencia | L4 (los ensayos de Fase 3 encontrados son indirectos; ver explicación abajo) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 8 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, la noretisterona es un progestágeno sintético que actúa sobre el receptor de progesterona (gen *PGR*). Se emplea como anticonceptivo y en trastornos menstruales, y mecanísticamente podría ser aplicable a la amenorrea.

Hay dos vínculos plausibles:
- Los progestágenos provocan decidualización y atrofia del endometrio, lo que suprime el sangrado. En ese caso la amenorrea sería un efecto del fármaco.
- La noretisterona puede usarse como progestágeno en una prueba de sangrado por privación en la amenorrea secundaria.

Esta predicción tiene una ambigüedad importante. En la evidencia recuperada, la amenorrea aparece sobre todo como resultado o efecto secundario del tratamiento, y no como la enfermedad que se trata. El puntaje alto (0.996) probablemente refleja la cercanía en el grafo de conocimiento con nodos de progestágenos, anticoncepción y trastornos menstruales. No es una prueba de eficacia clínica.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03103087](https://clinicaltrials.gov/study/NCT03103087) | Fase 3 | Completado | 382 | LIBERTY 2: relugolix + estradiol + noretisterona acetato vs placebo en sangrado menstrual abundante por miomas. La noretisterona es un componente de terapia de reposición, no el tratamiento principal. |
| [NCT03049735](https://clinicaltrials.gov/study/NCT03049735) | Fase 3 | Completado | 388 | LIBERTY 1: mismo diseño y combinación que LIBERTY 2. El efecto no puede atribuirse solo a la noretisterona. |
| [NCT03412890](https://clinicaltrials.gov/study/NCT03412890) | Fase 3 | Completado | 477 | Extensión abierta de un solo brazo de la misma combinación; puede incluir tasas de amenorrea, pero sin grupo control. |
| [NCT03751124](https://clinicaltrials.gov/study/NCT03751124) | Fase 3 | Completado | 229 | Estudio de retiro aleatorizado de la combinación con relugolix en miomas; mide supresión del sangrado sin aislar el aporte de la noretisterona. |
| [NCT05620355](https://clinicaltrials.gov/study/NCT05620355) | Fase 3 | Desconocido | 312 | BG2109 solo o con terapia de reposición vs placebo en sangrado menstrual abundante por miomas; no hay evidencia de que evalúe noretisterona. |
| [NCT06953076](https://clinicaltrials.gov/study/NCT06953076) | N/A | Reclutando | 111 | Estudio ecográfico del aspecto de los miomas durante el tratamiento con relugolix/estradiol/noretisterona; no mide eficacia en amenorrea. |
| [NCT01817530](https://clinicaltrials.gov/study/NCT01817530) | Fase 2 | Completado | 571 | Elagolix (con y sin terapia de reposición) en sangrado abundante por miomas; no incluye noretisterona. |
| [NCT01441635](https://clinicaltrials.gov/study/NCT01441635) | Fase 2 | Completado | 271 | Prueba de concepto de elagolix en sangrado uterino y miomas; sin exposición a noretisterona. |

Cuatro ensayos de Fase 3 están completados, pero todos estudian sangrado menstrual abundante por miomas con una combinación que incluye noretisterona acetato como complemento. Por eso la evidencia es indirecta y no cumple los criterios de L1 para esta indicación.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38530848](https://pubmed.ncbi.nlm.nih.gov/38530848/) | 2024 | ECA | PloS one | Ensayo WHICH: DMPA-IM vs enantato de noretisterona (NET-EN) inyectable; compara niveles de estradiol y efectos menstruales. |
| [41489365](https://pubmed.ncbi.nlm.nih.gov/41489365/) | 2026 | Análisis secundario de ECA | Biology of reproduction | En el ensayo WHICH, los anticonceptivos inyectables afectan de forma distinta el eje hipotálamo-hipófisis-gónadas. Ambos bajan el estradiol, pero hay más amenorrea con DMPA-IM que con NET-EN. |
| [37863160](https://pubmed.ncbi.nlm.nih.gov/37863160/) | 2024 | Estudio de extensión a largo plazo | Am J Obstet Gynecol | La terapia combinada con relugolix mejoró el sangrado menstrual abundante por miomas durante 52 semanas en mujeres afrodescendientes. |
| [37103532](https://pubmed.ncbi.nlm.nih.gov/37103532/) | 2023 | Revisión | Obstetrics and gynecology | Eficacia y seguridad de los antagonistas orales de GnRH con esteroides de reposición en miomas uterinos. |
| [23641480](https://pubmed.ncbi.nlm.nih.gov/23641480/) | 2013 | Revisión (Cochrane) | Cochrane Database Syst Rev | Anticonceptivos inyectables combinados: alta eficacia; los cambios en el patrón de sangrado pueden limitar su aceptación. |
| [18843662](https://pubmed.ncbi.nlm.nih.gov/18843662/) | 2008 | Revisión (Cochrane) | Cochrane Database Syst Rev | Versión anterior de la revisión sobre anticonceptivos inyectables combinados. |
| [1908716](https://pubmed.ncbi.nlm.nih.gov/1908716/) | 1991 | Revisión | Curr Opin Obstet Gynecol | Implantes subdérmicos de progestágeno: niveles bajos y estables del fármaco, sin estrógeno. |
| [2660092](https://pubmed.ncbi.nlm.nih.gov/2660092/) | 1989 | Revisión | Pediatr Clin North Am | Principios de la anticoncepción hormonal en adolescentes. |
| [6508652](https://pubmed.ncbi.nlm.nih.gov/6508652/) | 1984 | Revisión | Aust Fam Physician | Revisión general de anticonceptivos orales. |
| [12317413](https://pubmed.ncbi.nlm.nih.gov/12317413/) | 1987 | Revisión | Current therapeutics | Revisión general de anticonceptivos orales (sin resumen disponible). |

La mayoría de las publicaciones son revisiones antiguas sobre anticoncepción. Solo el ensayo WHICH y su análisis secundario tocan la amenorrea, y en ellos es un resultado de la anticoncepción, no una indicación terapéutica.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 38690 | PRIMOSISTON® (UNIAO QUIMICA FARMACEUTICA NACIONAL S.A) | Tableta | Noretisterona y estrógeno |

El paquete de evidencia informa 8 registros sanitarios en total, pero en el detalle solo aparece el registro 38690 (repetido cinco veces con datos idénticos), por lo que se muestra una sola vez.

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas:** el paquete de evidencia registra una sola entrada, de farmacología y no de interacción entre medicamentos. Es la unión de la noretisterona a su blanco, el receptor de progesterona (*PGR*, humano). No hay interacciones con otros medicamentos con nivel de gravedad definido.

Para advertencias y contraindicaciones, consultar el prospecto aprobado por INVIMA.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje del modelo es muy alto (99.60%), pero ningún ensayo ni publicación evalúa la noretisterona como tratamiento de la amenorrea. Los ensayos de Fase 3 estudian miomas uterinos con una combinación en la que la noretisterona es un complemento, y en la literatura la amenorrea aparece como efecto de la anticoncepción. En esta etapa es una pregunta de investigación, no una recomendación clínica.

**Para avanzar se necesita:**
- Aclarar la dirección de la relación: si la noretisterona **trata** la amenorrea (por ejemplo, prueba de sangrado por privación en amenorrea secundaria) o la **produce** como efecto.
- Datos del mecanismo de acción desde DrugBank.
- Advertencias y contraindicaciones del prospecto de INVIMA (revisión de seguridad todavía pendiente).
- Revisión de literatura específica sobre progestágenos en amenorrea primaria y secundaria.
- Confirmar los 8 registros sanitarios y sus indicaciones aprobadas en INVIMA.

*Este informe es solo de investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

