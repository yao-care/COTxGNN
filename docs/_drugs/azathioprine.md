---
layout: default
title: Azathioprine
parent: Solo Predicción del Modelo (L5)
nav_order: 70
evidence_level: L5
indication_count: 10
---

# Azathioprine
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

# Azatioprina: De Indicación Original No Especificada a Síndrome de Microftalmia Colobomatosa-Displasia Rizomélica

## Resumen en Una Frase

La azatioprina es un inmunosupresor antimetabolito de purinas, comercializado en Colombia. Los registros sanitarios no detallan su indicación original.
El modelo TxGNN predice que podría ser efectiva para el **síndrome de microftalmia colobomatosa-displasia rizomélica**, con **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es una predicción puramente del grafo de conocimiento.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro sanitario solo dice «AZATIOPRINA», sin texto de indicación) |
| Nueva Indicación Predicha | Síndrome de microftalmia colobomatosa-displasia rizomélica |
| Puntaje de Predicción TxGNN | 99.9994% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, la azatioprina actúa como inmunosupresor antimetabolito de purinas, y su eficacia se ha documentado en enfermedades inmunomediadas.

**Esta predicción no tiene un vínculo mecanístico plausible.** El síndrome de microftalmia colobomatosa-displasia rizomélica es una malformación congénita del desarrollo. No hay un blanco inmunológico que la azatioprina pueda modular. El puntaje alto refleja una asociación del grafo, no una razón biológica ni clínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

---

## Información de Mercado en Colombia

Se recibieron 5 filas de registros, que corresponden a 2 registros sanitarios distintos (de un total de 20).

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20141515 | AZATIOPRINA 50 MG TABLETA RECUBIERTA | Tableta recubierta | No detallada (solo figura «AZATIOPRINA») |
| 46266 | IMURAN® 50 MG | Tableta recubierta | No detallada (solo figura «AZATIOPRINA») |

---

## Otras Indicaciones Predichas con Evidencia

Las siguientes indicaciones del mismo modelo tienen más respaldo que la de rango 1. Se incluyen como contexto y no sustituyen la evaluación principal.

| Indicación (rango) | Puntaje TxGNN | Nivel | Decisión | Evidencia destacada |
|------|------|------|------|------|
| Enfermedad inflamatoria intestinal (5) | 99.52% | L2 | Proceed with Guardrails | [NCT07235904](https://clinicaltrials.gov/study/NCT07235904) (Fase 4, reclutando, n=300, azatioprina como comparador estándar); [NCT05040464](https://clinicaltrials.gov/study/NCT05040464) (Fase 3, reclutando, n=166, azatioprina vs metotrexato con adalimumab en Crohn); [NCT00946946](https://clinicaltrials.gov/study/NCT00946946) (Fase 3, completado, n=78, azatioprina vs mesalazina en Crohn posoperatorio) |
| Colitis ulcerosa (9) | 99.33% | L2 | Proceed with Guardrails | [NCT03101800](https://clinicaltrials.gov/study/NCT03101800) (Fase 3, estado desconocido, n=84, azatioprina en dosis baja + alopurinol vs azatioprina sola); revisiones Cochrane [PMID 40013523](https://pubmed.ncbi.nlm.nih.gov/40013523/) (2025) y [PMID 27192092](https://pubmed.ncbi.nlm.nih.gov/27192092/) (2016); ECA [PMID 39586616](https://pubmed.ncbi.nlm.nih.gov/39586616/) (Gut, 2025, infliximab + azatioprina vs azatioprina sola en colitis grave aguda) |

Estos usos son práctica estándar fuera de indicación, no una señal nueva de reposicionamiento. El Evidence Pack indica que no hay un ECA de Fase 3 con azatioprina en EII, pero NCT00946946 figura como Fase 3 completado con azatioprina en Crohn. Conviene verificar este punto antes de fijar el nivel definitivo. Aun así, un solo ECA de Fase 3 completado mantiene el nivel en L2, no en L1.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para el síndrome de microftalmia colobomatosa-displasia rizomélica no existe ningún ensayo, publicación ni vínculo mecanístico documentado. La predicción es solo una salida del grafo, con nivel L5.

**Para avanzar se necesita:**
- Descartar esta predicción como candidata, o justificarla con datos preclínicos o mecanísticos que hoy no existen.
- Priorizar la evaluación de enfermedad inflamatoria intestinal y colitis ulcerosa, con salvaguardas: genotipificación TPMT/NUDT15, monitoreo de metabolitos 6-TGN/6-MMP, hemograma y función hepática.
- Obtener del sitio de INVIMA el prospecto con advertencias y contraindicaciones, y datos del mecanismo de acción desde DrugBank.
- Aclarar la indicación aprobada en los registros sanitarios colombianos, que hoy solo muestran el nombre del fármaco.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

