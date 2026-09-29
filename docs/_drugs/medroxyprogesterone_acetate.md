---
layout: default
title: Medroxyprogesterone Acetate
parent: Solo Predicción del Modelo (L5)
nav_order: 271
evidence_level: L5
indication_count: 10
---

# Medroxyprogesterone Acetate
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

# Acetato de Medroxiprogesterona: De Progestágeno Sintético (Indicación No Especificada en el Registro) a Amenorrea

## Resumen en Una Frase

El acetato de medroxiprogesterona (MPA) es un progestágeno sintético comercializado en Colombia, pero el registro sanitario no detalla su indicación original.
El modelo TxGNN predice que podría ser efectivo para **amenorrea**, con **10 ensayos clínicos** y **20 publicaciones** asociados. Solo 2 de esos ensayos tienen relación directa o cercana con el tema, y la mayoría de las publicaciones son revisiones sobre anticoncepción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro solo indica «Medroxiprogesterona», sin texto de indicación) |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L2 (según el Evidence Pack; la evidencia es indirecta, ver nota abajo) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Proceed with Guardrails |

> **Nota sobre el nivel de evidencia:** ningún ensayo de Fase 2/3 completado evalúa directamente al MPA como tratamiento de la amenorrea. El ensayo más cercano (NCT03309176, Fase 4) usa sangrado por privación inducido por progestágeno como paso previo a la inducción de ovulación. Por eso el L2 debe leerse con cautela.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos. Según la farmacología general, el MPA es un progestágeno sintético. Provoca la transformación secretora del endometrio previamente estimulado por estrógenos y, al suspenderse, induce sangrado por privación.

Esto encaja con la amenorrea anovulatoria o secundaria en mujeres con estrógeno endógeno suficiente. En ese contexto, el progestágeno se usa para provocar un sangrado y comprobar la respuesta del endometrio, o para regular el ciclo. Este vínculo proviene de la farmacología general y no de los datos del Evidence Pack, cuyos campos de indicación original y mecanismo están vacíos.

La relación con la indicación original no puede evaluarse con los datos disponibles, porque el registro colombiano no especifica el texto de indicación. Aun así, la predicción es coherente con el perfil hormonal del fármaco.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03309176](https://clinicaltrials.gov/study/NCT03309176) | Fase 4 | Completado | 42 | ECA de viabilidad: ¿es necesario el sangrado por privación inducido por progesterona antes de inducir la ovulación con clomifeno en mujeres con oligo o amenorrea? Los brazos exactos no están confirmados. |
| [NCT02449161](https://clinicaltrials.gov/study/NCT02449161) | Fase 3 | Terminado | 60 | ECA de MPA después de la ablación endometrial, con la tasa de amenorrea endometrial como desenlace. Ajuste indirecto (población posablación). |
| [NCT00808132](https://clinicaltrials.gov/study/NCT00808132) | Fase 3 | Completado | 1886 | Bazedoxifeno/estrógenos conjugados frente a placebo y comparador activo en mujeres posmenopáusicas. El MPA probablemente es comparador; no evalúa amenorrea. |
| [NCT01463202](https://clinicaltrials.gov/study/NCT01463202) | Fase 4 | Completado | 184 | Momento de la administración posparto de DMPA y su efecto en la lactancia. Anticoncepción, no tratamiento de amenorrea. |
| [NCT00392093](https://clinicaltrials.gov/study/NCT00392093) | Fase 4 | Completado | 108 | Terapia hormonal en mujeres peri y posmenopáusicas con lupus: actividad de la enfermedad y densidad ósea. Sin relación con amenorrea. |
| [NCT01300676](https://clinicaltrials.gov/study/NCT01300676) | Fase 2/3 | Completado | 79 | Miel de Tualang frente a terapia hormonal en mujeres posmenopáusicas (perfil de seguridad). Periférico. |
| [NCT06671548](https://clinicaltrials.gov/study/NCT06671548) | Fase 3 | Reclutando | 120 | Relugolix frente a placebo en sangrado menstrual abundante por miomas. No está claro el papel del MPA. |
| [NCT03018366](https://clinicaltrials.gov/study/NCT03018366) | Fase 2 | Completado | 29 | Aterosclerosis e inflamación en mujeres jóvenes con amenorrea hipotalámica funcional. Solo contexto hormonal. |
| [NCT07020429](https://clinicaltrials.gov/study/NCT07020429) | No aplica | Aún no recluta | 276 | Fórmula herbal china en insuficiencia ovárica prematura. El MPA sería, a lo sumo, terapia de fondo. |
| [NCT02792153](https://clinicaltrials.gov/study/NCT02792153) | Fase 1 | Retirado | 0 | Estradiol y extinción del miedo a alimentos en anorexia nerviosa. Sin participantes, sin evidencia. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38530848](https://pubmed.ncbi.nlm.nih.gov/38530848/) | 2024 | ECA | PloS one | Ensayo WHICH: compara DMPA-IM y NET-EN en niveles de estradiol y efectos menstruales, psicológicos y conductuales relevantes al riesgo de VIH. |
| [23641480](https://pubmed.ncbi.nlm.nih.gov/23641480/) | 2013 | Revisión sistemática | Cochrane Database Syst Rev | Anticonceptivos inyectables combinados: alta eficacia y aceptabilidad limitada por los cambios en el patrón de sangrado. |
| [18843662](https://pubmed.ncbi.nlm.nih.gov/18843662/) | 2008 | Revisión sistemática | Cochrane Database Syst Rev | Versión anterior de la misma revisión Cochrane sobre inyectables combinados. |
| [8725701](https://pubmed.ncbi.nlm.nih.gov/8725701/) | 1996 | Revisión | J Reprod Med | Asesoría y manejo de efectos secundarios en usuarias de DMPA para anticoncepción. |
| [6119259](https://pubmed.ncbi.nlm.nih.gov/6119259/) | 1981 | Revisión | Int J Gynaecol Obstet | Anticoncepción posparto: el retorno de la ovulación es impredecible aun durante la amenorrea posparto. |
| [6232474](https://pubmed.ncbi.nlm.nih.gov/6232474/) | 1984 | Revisión | Obstet Gynecol Annu | Enfermedad ovárica poliquística, un contexto frecuente de oligo o amenorrea. |
| [8829701](https://pubmed.ncbi.nlm.nih.gov/8829701/) | 1996 | Revisión | Int J Fertil Menopausal Stud | Opciones anticonceptivas de acción prolongada, con eficacia inferior a 1 embarazo por 100 mujeres-año. |
| [6141923](https://pubmed.ncbi.nlm.nih.gov/6141923/) | 1984 | Revisión | Drug Intell Clin Pharm | Infertilidad inducida por fármacos y su efecto sobre el eje hipotálamo-hipófisis-gónada. |
| [7139435](https://pubmed.ncbi.nlm.nih.gov/7139435/) | 1982 | Sin clasificar | CMAJ | Debate sobre usos adicionales del DMPA. Sin resumen disponible. |
| [120837](https://pubmed.ncbi.nlm.nih.gov/120837/) | 1979 | Revisión | IARC Monogr | Monografía sobre el riesgo carcinogénico del acetato de medroxiprogesterona. |

> Ninguna de las publicaciones evalúa directamente al MPA como tratamiento de la amenorrea. La mayoría trata de anticoncepción.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 21776 | PROVERA 5MG TABLETAS (Pfizer S.A.S.) | Tableta | Solo figura «Medroxiprogesterona», sin texto de indicación |

Los cinco registros listados en el Evidence Pack son entradas repetidas del mismo producto. En total hay 20 registros. Además de la vía oral (tableta), existe la forma de suspensión inyectable.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El mecanismo progestagénico es plausible para la amenorrea con estrógeno endógeno adecuado y el puntaje TxGNN es muy alto. Sin embargo, la evidencia clínica directa es escasa: un ECA de Fase 4 de viabilidad y un ECA de Fase 3 terminado en población posablación. Además, faltan por completo los datos de seguridad del prospecto, por lo que se avanza solo con salvaguardas.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto del INVIMA (advertencias y contraindicaciones), un vacío bloqueante para el tamizaje de seguridad.
- Obtener el mecanismo de acción desde DrugBank y confirmar la indicación aprobada en Colombia.
- Definir qué tipo de amenorrea (secundaria, anovulatoria, con estrógeno adecuado) sería la población objetivo y descartar embarazo y otras causas antes de su uso.
- Buscar ensayos que evalúen directamente al MPA en amenorrea; los actuales son indirectos.
- Tomar las otras predicciones con cautela. Las de mama fibroquística y displasia mamaria benigna tienen evidencia débil y antigua, con dirección de efecto incierta. Las de endometriosis solo tienen respaldo mecanístico. Las de hipoplasia renal parecen artefactos del grafo de conocimiento.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

