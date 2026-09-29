---
layout: default
title: Pralatrexate
parent: Solo Predicción del Modelo (L5)
nav_order: 329
evidence_level: L5
indication_count: 10
---

# Pralatrexate
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

# Pralatrexato: De Linfoma de Células T Periférico a Tumor Adenomatoide Pleural

## Resumen en Una Frase

Pralatrexato es un antifolato inhibidor de la enzima DHFR. Se usa en el tratamiento del linfoma de células T periférico recaído o refractario.
El modelo TxGNN predice que podría ser efectivo para el **tumor adenomatoide pleural**, pero para esa indicación hay **0 ensayos clínicos** y **0 publicaciones**.
La predicción se basa solo en el modelo (L5). El mesotelioma pleural, otra indicación predicha, sí cuenta con literatura de respaldo (ver más abajo).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | El registro sanitario solo dice "PRALATREXATO". Según la farmacología, linfoma de células T periférico recaído o refractario |
| Nueva Indicación Predicha | Tumor adenomatoide pleural |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 2 (ambos con el mismo número, 20055048) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Pralatrexato inhibe la dihidrofolato reductasa (DHFR), enzima necesaria para sintetizar ADN. Es un análogo de los folatos, con alta afinidad por el transportador RFC-1 y buena poliglutamilación. Los datos entregados no incluyen una descripción detallada del mecanismo de acción, pero la DHFR aparece claramente como su blanco farmacológico.

La relación entre la indicación original y la nueva es débil. El tumor adenomatoide pleural es habitualmente benigno, así que el balance riesgo-beneficio de un antifolato citotóxico es desfavorable. El puntaje alto probablemente refleja cercanía en el grafo de conocimiento con los tumores mesoteliales y no una señal terapéutica real.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Para el tumor adenomatoide pleural, actualmente no hay literatura relacionada disponible.

**Evidencia relacionada (indicación predicha de mayor respaldo: mesotelioma pleural, TxGNN 99.85%, nivel L3):**

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [17409804](https://pubmed.ncbi.nlm.nih.gov/17409804/) | 2007 | Ensayo Fase II de un solo brazo | J Thorac Oncol | Pralatrexato en mesotelioma pleural maligno irresecable. Perfil de toxicidad favorable, limitado sobre todo a estomatitis. No se incluyeron resultados de eficacia. |
| [11595715](https://pubmed.ncbi.nlm.nih.gov/11595715/) | 2001 | Preclínico | Clin Cancer Res | El análogo PDX fue 25-30 veces más citotóxico que el metotrexato en líneas celulares de mesotelioma. Se evaluó también combinado con platino. |
| [21301589](https://pubmed.ncbi.nlm.nih.gov/21301589/) | 2010 | Revisión | Cancer Manag Res | Revisión de los antifolatos que actúan sobre la síntesis de ácido fólico en quimioterapia del cáncer. |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20055048 | DIFOLTA 20 MG/ML SOLUCION PARA INFUSION (BIOSIDUS COLOMBIA S.A.S.) | Solución inyectable | PRALATREXATO (el registro no detalla la indicación) |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antifolato, inhibidor de DHFR) |
| Riesgo de Mielosupresión | Se menciona mielosupresión como parte del perfil de toxicidad. Los datos entregados no permiten graduar su magnitud. |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal, y vigilancia de mucositis o estomatitis |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se dispone de advertencias ni contraindicaciones del prospecto de INVIMA.

- **Perfil de toxicidad conocido:** mucositis o estomatitis y mielosupresión. Son una barrera importante para su uso en condiciones crónicas o benignas.
- **Interacciones farmacológicas:** la consulta no devolvió interacciones medicamentosas clínicas. El único registro corresponde al blanco farmacológico (DHFR).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para el tumor adenomatoide pleural solo hay una predicción del modelo (L5), sin ensayos ni literatura. Además, se trata de un tumor generalmente benigno, para el cual un antifolato citotóxico tiene un balance riesgo-beneficio desfavorable.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), que hoy bloquea el tamizaje de seguridad.
- Confirmar el mecanismo de acción en DrugBank.
- Definir si se justifica reorientar el análisis hacia el **mesotelioma pleural**, la indicación predicha con mayor respaldo (L3, "Research Question"). Habría que obtener los resultados de eficacia del ensayo Fase II (PMID 17409804) y compararlos con pemetrexed, que ya ocupa ese nicho.
- Aclarar la indicación aprobada en el registro colombiano, que solo dice "PRALATREXATO".

*Los resultados son solo de referencia para investigación y no constituyen consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

