---
layout: default
title: Mercaptopurine
parent: Solo Predicción del Modelo (L5)
nav_order: 275
evidence_level: L5
indication_count: 10
---

# Mercaptopurine
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

# Mercaptopurina: De Indicación Original No Especificada a Leucemia Mieloide

## Resumen en Una Frase

La mercaptopurina es un antimetabolito análogo de purinas, comercializado en Colombia como tableta oral (PURINETHOL 50 mg). El texto del registro sanitario no detalla su indicación original.
El modelo TxGNN predice que podría ser efectiva para **leucemia mieloide**, con **30 ensayos clínicos** y **20 publicaciones** relacionados. En casi todos los ensayos la mercaptopurina es solo un componente de regímenes de varios fármacos.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada. El registro sanitario solo indica "Mercaptopurina" en el campo de indicación |
| Nueva Indicación Predicha | Leucemia mieloide |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L1 (con reserva: la evidencia es confundida por regímenes combinados) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 3 (las tres entradas corresponden al mismo registro, 46262) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información de entrada. Según la farmacología general, la mercaptopurina es un antimetabolito de purinas. La enzima HGPRT la convierte en nucleótidos de tioguanina, que se incorporan al ADN y ARN e inhiben la síntesis de novo de purinas. Por eso actúa sobre células leucémicas de división rápida. Esta descripción es farmacología general y no proviene de un campo de mecanismo de acción verificado.

Es un pilar del tratamiento de mantenimiento de la leucemia linfoblástica aguda, junto con el metotrexato. En enfermedad mieloide, su papel documentado es sobre todo el mantenimiento oral con metotrexato, por ejemplo en la leucemia promielocítica aguda (LPA). Por eso varios ensayos incluyen mercaptopurina dentro de sus protocolos. También aparece en regímenes de inducción de leucemia mieloide aguda (LMA), según algunos estudios de literatura.

La predicción es plausible desde el punto de vista mecanístico, porque un antimetabolito actúa sobre neoplasias hematológicas proliferativas. Sin embargo, la evidencia es indirecta. La mercaptopurina casi nunca es la variable evaluada, así que su contribución individual no puede aislarse con los datos disponibles.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00492856](https://clinicaltrials.gov/study/NCT00492856) | Fase 3 | Completado | 105 | Mantenimiento frente a observación en LPA de riesgo bajo e intermedio. Los esquemas de mantenimiento suelen incluir mercaptopurina, pero su aporte no se puede aislar |
| [NCT00003934](https://clinicaltrials.gov/study/NCT00003934) | Fase 3 | Completado | 420 | LPA sin tratamiento previo. Tretinoína con quimioterapia, con o sin trióxido de arsénico. Mantenimiento con tretinoína intermitente frente a tretinoína más mercaptopurina y metotrexato |
| [NCT00700544](https://clinicaltrials.gov/study/NCT00700544) | Fase 3 | Completado | 330 | LMA en adultos mayores. Se evalúan andrógenos en el tratamiento posremisión. La mercaptopurina probablemente forma parte del esquema base |
| [NCT02688140](https://clinicaltrials.gov/study/NCT02688140) | Fase 3 | Completado | 133 | LPA de alto riesgo. Trióxido de arsénico con ATRA e idarrubicina frente al régimen AIDA. La mercaptopurina es un componente de mantenimiento de fondo |
| [NCT00408278](https://clinicaltrials.gov/study/NCT00408278) | Fase 4 | Completado | 300 | Protocolo PETHEMA LPA 2005. Mantenimiento con ATRA y quimioterapia de dosis baja (metotrexato y mercaptopurina) |
| [NCT00465933](https://clinicaltrials.gov/study/NCT00465933) | Fase 4 | Completado | No reportada | Protocolo AIDA en LPA con reducción de dosis en mayores de 70 años. Mantenimiento con ATRA, metotrexato y mercaptopurina |
| [NCT00180128](https://clinicaltrials.gov/study/NCT00180128) | Fase 4 | Desconocido | 80 | AIDA2000, terapia adaptada al riesgo en LPA. Mantenimiento de dos años con 6-mercaptopurina, metotrexato y ATRA |
| [NCT01064557](https://clinicaltrials.gov/study/NCT01064557) | No aplica | Desconocido | 1068 | Guía AIDA. Evalúa el mantenimiento con ATRA intermitente, con metotrexato y 6-mercaptopurina, o ambos, en pacientes con PCR negativa |
| [NCT05506332](https://clinicaltrials.gov/study/NCT05506332) | Fase 1 | Reclutando | 10 | Venetoclax con 6-mercaptopurina en LMA recaída o refractaria. Combinación nueva con solo 10 pacientes, que genera hipótesis |
| [NCT06199557](https://clinicaltrials.gov/study/NCT06199557) | Fase 1/2 | Reclutando | 48 | Hidroxiurea con ácido valproico, o 6-mercaptopurina con ácido valproico, en LMA o SMD de alto riesgo no aptos para terapia estándar |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10497848](https://pubmed.ncbi.nlm.nih.gov/10497848/) | 1999 | ECA | Int J Hematol | Añadir etopósido a daunorrubicina, citarabina y 6-mercaptopurina en la inducción de LMA del adulto no aportó beneficio (JALSG-AML92) |
| [8174198](https://pubmed.ncbi.nlm.nih.gov/8174198/) | 1994 | ECA | Cancer Chemother Pharmacol | Comparación nacional de daunorrubicina frente a aclarrubicina, con citarabina behenoil, 6-mercaptopurina y prednisolona. Remisión completa de 63.7% frente a 53.9% |
| [31983177](https://pubmed.ncbi.nlm.nih.gov/31983177/) | 2020 | ECA | Asian Pac J Cancer Prev | Quimioterapia metronómica frente a hidroxiurea paliativa en LMA no apta para terapia intensiva |
| [26425037](https://pubmed.ncbi.nlm.nih.gov/26425037/) | 2015 | Cohorte | J Korean Med Sci | Mantenimiento oral con 6-mercaptopurina y metotrexato en LMA no elegible para trasplante. Los resultados de supervivencia no aparecen en el resumen disponible |
| [15124700](https://pubmed.ncbi.nlm.nih.gov/15124700/) | 2004 | No clasificado | Ann Hematol | Evalúa si el mantenimiento tras inducción y consolidación muy intensivas aporta ventaja en LMA infantil |
| [9095207](https://pubmed.ncbi.nlm.nih.gov/9095207/) | 1997 | Estudio piloto | Cancer Invest | Mercaptopurina en dosis altas y citarabina en dosis intermedia durante la primera remisión de LMA infantil. Explora su viabilidad |
| [1059498](https://pubmed.ncbi.nlm.nih.gov/1059498/) | 1975 | Serie de casos | Cancer | Protocolo de cuatro fármacos en 18 niños con LMA. Remisión inicial de 78% y supervivencia mediana de 7 meses |
| [265178](https://pubmed.ncbi.nlm.nih.gov/265178/) | 1977 | Serie de casos | Blood | Tres casos de leucemia mieloide crónica juvenil con respuesta a citarabina subcutánea y mercaptopurina oral. Mejoría del bienestar, sin evidencia de mayor supervivencia |
| [24492035](https://pubmed.ncbi.nlm.nih.gov/24492035/) | 2014 | Revisión | Rinsho Ketsueki | Revisión japonesa sobre el tratamiento actual de LMA y LPA. Sin resumen disponible |
| [28152123](https://pubmed.ncbi.nlm.nih.gov/28152123/) | 2017 | Cohorte | JAMA Oncol | Asocia el tratamiento de enfermedades autoinmunes con síndromes mielodisplásicos y LMA relacionados con la terapia. Es una señal de seguridad, no de eficacia |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 46262 | PURINETHOL 50 MG (Aspen Labs S.A. de C.V., México) | Tableta | MERCAPTOPURINA |

Los tres registros de la base de datos son entradas idénticas del mismo número sanitario. Se muestra una sola vez.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antimetabolito, análogo de purinas) |
| Riesgo de Mielosupresión | Medio a alto. La neutropenia es una toxicidad frecuente durante el mantenimiento y aumenta con variantes de TPMT y NUDT15 |
| Clasificación de Emetogenicidad | Baja (clasificación general del fármaco oral; no proviene de los datos de entrada) |
| Items de Monitoreo | Hemograma con diferencial, función hepática (hepatotoxicidad asociada a metabolitos metilados), función renal, genotipo TPMT/NUDT15 |
| Protección en Manejo | Seguir las regulaciones de manejo de fármacos citotóxicos. Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Señales de la literatura recuperada, que no reemplazan al prospecto:
- Las variantes de TPMT y NUDT15 modifican la toxicidad hematológica, por lo que se requiere dosificación guiada por genotipo.
- El alopurinol altera el metabolismo de la mercaptopurina.
- Se han descrito hepatotoxicidad y, en casos aislados, hipoglucemia.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay varios ensayos de Fase 3 completados en leucemia (sobre todo LPA) cuyos regímenes incluyen mercaptopurina, lo que cumple el criterio formal de L1. Aun así, el aporte individual del fármaco no se puede aislar. Además, la mercaptopurina ya es de uso establecido en leucemias agudas, por lo que la ausencia de indicación original parece una laguna de datos y no un caso claro de reposicionamiento.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA para confirmar la indicación aprobada, advertencias y contraindicaciones. Es un vacío bloqueante para la evaluación de seguridad.
- Obtener datos verificados del mecanismo de acción (por ejemplo, desde DrugBank).
- Revisar resultados de estudios que aíslen el efecto de la mercaptopurina, como NCT00003934 (mantenimiento con y sin mercaptopurina y metotrexato en LPA).
- Definir un plan de genotipificación TPMT/NUDT15 y de monitoreo hematológico y hepático.
- Aclarar si la leucemia mieloide ya está cubierta por la indicación registrada en Colombia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

