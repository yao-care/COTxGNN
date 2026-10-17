---
layout: default
title: Pemetrexed
parent: Evidencia Alta (L1-L2)
nav_order: 506
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-14
description: "Pemetrexed: nueva indicación predicha, Mesotelioma peritoneal maligno (nivel de evidencia L2). Indicación original: Pemetrexed"
monitor_inn: "PEMETREXED"
predicted_indications: ["pleural adenomatoid tumor", "pericardium cancer", "iminoglycinuria"]
---

# Pemetrexed
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

# Pemetrexed: De Indicación Original (no especificada en el registro) a Mesotelioma Peritoneal Maligno

## Resumen en Una Frase

Pemetrexed es un antifolato multidiana. En los registros sanitarios de INVIMA su indicación aparece solo con el nombre del principio activo, sin un texto de indicación detallado. El modelo TxGNN predice que podría ser efectivo para **mesotelioma peritoneal maligno**, con **7 ensayos clínicos** y **20 publicaciones** que respaldan esta dirección. La evidencia es de Fase 2 o extrapolada desde el mesotelioma pleural.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Pemetrexed (el registro sanitario no detalla la indicación; en la práctica se usa en mesotelioma pleural y cáncer de pulmón no microcítico) |
| Nueva Indicación Predicha | Mesotelioma peritoneal maligno |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción detallado. Según la información conocida, pemetrexed es un antifolato multidiana que inhibe la timidilato sintasa (TS), la dihidrofolato reductasa (DHFR) y la GARFT. Así bloquea la síntesis de purinas y pirimidinas en células de rápida división.

El mesotelioma peritoneal y el pleural comparten histología y biología. La combinación pemetrexed + platino es el tratamiento de referencia en el mesotelioma pleural, por lo que su eficacia es plausible en el peritoneo. Los estudios de mesotelioma peritoneal son escasos por la baja incidencia, y las recomendaciones de tratamiento sistémico se extrapolan en gran parte de los ensayos en mesotelioma pleural.

Una limitación importante: no existe un ensayo de Fase 3 específico para mesotelioma peritoneal. El ensayo NCT00061477 incluyó pacientes pleurales y peritoneales de forma conjunta, por lo que no se puede aislar el efecto en el peritoneo.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00061477](https://clinicaltrials.gov/study/NCT00061477) | Fase 2 | Completado | 48 | Pemetrexed + gemcitabina como primera línea en mesotelioma pleural o peritoneal; subgrupos mezclados |
| [NCT05001880](https://clinicaltrials.gov/study/NCT05001880) | Fase 2 | Reclutando | 66 | Quimioterapia (carboplatino, pemetrexed, bevacizumab) con o sin atezolizumab en mesotelioma peritoneal; sin resultados aún |
| [NCT06543069](https://clinicaltrials.gov/study/NCT06543069) | Fase 2 | Reclutando | 28 | Sintilimab + bevacizumab con pemetrexed y cisplatino en mesotelioma peritoneal irresecable; brazo único |
| [NCT00402766](https://clinicaltrials.gov/study/NCT00402766) | Fase 1 | Completado | 19 | Dosis máxima tolerada de cisplatino, pemetrexed e imatinib en mesotelioma metastásico o irresecable |
| [NCT02535312](https://clinicaltrials.gov/study/NCT02535312) | Fase 1/2 | Activo, sin reclutar | 30 | TRC102 con cisplatino y pemetrexed en tumores sólidos avanzados; el mesotelioma es un subgrupo |
| [NCT03875144](https://clinicaltrials.gov/study/NCT03875144) | Fase 2 | Suspendido | 66 | PIPAC más quimioterapia sistémica (cisplatino + pemetrexed) frente a quimioterapia sola |
| [NCT06057935](https://clinicaltrials.gov/study/NCT06057935) | Fase 2 | Reclutando | 64 | Quimioterapia intraperitoneal frente a intravenosa tras cirugía citorreductora y HIPEC; el papel de pemetrexed no es claro |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31287877](https://pubmed.ncbi.nlm.nih.gov/31287877/) | 2019 | Estudio de eficacia y seguridad | Jpn J Clin Oncol | Pemetrexed + cisplatino en primera línea en mesotelioma peritoneal avanzado |
| [41133016](https://pubmed.ncbi.nlm.nih.gov/41133016/) | 2025 | Comparativo retrospectivo | Clin Med Insights Oncol | Compara regímenes de pemetrexed-platino y gemcitabina-platino en primera línea |
| [28594258](https://pubmed.ncbi.nlm.nih.gov/28594258/) | 2017 | Retrospectivo | Expert Rev Anticancer Ther | Eficacia de pemetrexed + cisplatino en primera línea |
| [21528659](https://pubmed.ncbi.nlm.nih.gov/21528659/) | 2011 | Serie de una institución | Tumori | Eficacia y seguridad de pemetrexed-cisplatino en pacientes sin quimioterapia previa |
| [39413826](https://pubmed.ncbi.nlm.nih.gov/39413826/) | 2024 | Revisión | J Natl Compr Canc Netw | Opciones sistémicas: inmunoterapia (nivolumab + ipilimumab) o quimioterapia con pemetrexed, extrapoladas del mesotelioma pleural |
| [38806763](https://pubmed.ncbi.nlm.nih.gov/38806763/) | 2024 | Estudio multicéntrico | Ann Surg Oncol | Estrategias de tratamiento y resultados en mesotelioma peritoneal |
| [36765620](https://pubmed.ncbi.nlm.nih.gov/36765620/) | 2023 | Revisión | Cancers | Ruta diagnóstica y terapéutica; supervivencia mediana de 34 a 92 meses con cirugía citorreductora + HIPEC en pacientes seleccionados |
| [30450291](https://pubmed.ncbi.nlm.nih.gov/30450291/) | 2018 | Revisión | Transl Lung Cancer Res | Revisión del mesotelioma peritoneal maligno |
| [26941986](https://pubmed.ncbi.nlm.nih.gov/26941986/) | 2016 | Revisión | J Gastrointest Oncol | Diagnóstico y manejo del mesotelioma peritoneal maligno |
| [35407498](https://pubmed.ncbi.nlm.nih.gov/35407498/) | 2022 | Revisión | J Clin Med | Cirugía citorreductora e HIPEC como tratamiento inicial preferido en pacientes seleccionados |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20108592 (cancelado) | REVOTRAIN 100 MG | Polvo liofilizado para reconstituir a solución inyectable | PEMETREXED |
| 20192961 (cancelado) | AUROPEXAFAR® 500 MG | Polvo liofilizado para reconstituir a solución inyectable | PEMETREXED |

Actualmente no hay registros vigentes en Colombia; los dos registros existentes están cancelados.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antimetabolito, clase antifolato) |
| Riesgo de Mielosupresión | Alto. Los datos de seguridad asocian el fármaco con neutropenia, trombocitopenia, agranulocitosis y anemia |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, función renal y hepática |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no son texto de prospecto):** enfermedad renal, función renal deteriorada, piouréter, trombocitopenia, neutropenia, agranulocitosis y anemia (incluida la macrocítica).
- **Interacciones farmacológicas:** se identificaron 100 interacciones. Las 20 primeras son de nivel moderado e incluyen:
  - Antiácidos H2: famotidina, ranitidina, cimetidina.
  - Metformina.
  - Anfotericina B, en sus distintas formulaciones.
  - Aminoglucósidos y glucopéptidos: kanamicina, neomicina, vancomicina.
  - Polimixina B.
  - Salicilatos y derivados: ácido acetilsalicílico, mesalazina, balsalazida, olsalazina.
  - Amoxicilina, levofloxacino y sapropterina.

  Muchas de estas interacciones se relacionan con la eliminación renal de pemetrexed. Se recomienda revisar especialmente los AINE.

No se dispone del texto de advertencias del prospecto de INVIMA. Consultar el prospecto para la información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Pemetrexed + platino es el estándar en mesotelioma pleural, con respaldo de un ensayo de Fase 3. Su extrapolación al mesotelioma peritoneal cuenta con estudios de Fase 2, series retrospectivas y varios ensayos en curso. Sin embargo, no hay un ensayo de Fase 3 específico para el peritoneo, y las dos licencias colombianas están canceladas.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones).
- Confirmar la disponibilidad actual de pemetrexed en Colombia, dado que no hay registros vigentes.
- Esperar resultados de los ensayos peritoneales en curso (NCT05001880, NCT06543069) o datos específicos de peritoneo.
- Aplicar medidas de protección: suplementación con ácido fólico y vitamina B12, control de la función renal, revisión de interacciones (en particular con AINE) y seguimiento hematológico.
- Datos detallados del mecanismo de acción desde DrugBank.

**Nota sobre otras indicaciones predichas:**
- **Mesotelioma pleural** (nivel L1) y **mesotelioma pleural epitelioide** (L1) tienen evidencia más sólida, incluidos ECA de Fase 3 (por ejemplo, Vogelzang 2003 y MAPS). Esto corresponde a una indicación ya establecida, no a un reposicionamiento novedoso.
- Los subtipos sarcomatoide y bifásico (L2) tienen evidencia a nivel de subgrupo.
- **Cáncer de pericardio** (L4) se apoya solo en reportes de casos.
- Para el **tumor adenomatoide pleural**, el **mesotelioma papilar bien diferenciado**, el **mesotelioma linfohistiocitoide** y la **iminoglicinuria**, el respaldo es débil o inexistente. La recomendación es Hold, y en la iminoglicinuria no hay fundamento mecanístico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

