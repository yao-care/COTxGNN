---
layout: default
title: Letrozol
parent: Solo Predicción del Modelo (L5)
nav_order: 391
evidence_level: L5
indication_count: 4
drugbank_id: DB01006
monitor_inn: "Letrozole"
predicted_indications: ["nipple carcinoma", "Ehrlich tumor carcinoma", "breast fibrocystic disease", "benign mammary dysplasia"]
last_modified_at: 2026-11-24
description: "Letrozol: nueva indicación predicha, Carcinoma del pezón (nipple carcinoma) (nivel de evidencia L5). Indicación original: LETROZOL"
---

# Letrozol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Letrozol: Carcinoma del pezón (nipple carcinoma)
{: .text-alpha }

## Resumen en Una Frase

Letrozol es un inhibidor de la aromatasa que reduce la síntesis de estrógenos y que en Colombia cuenta con múltiples registros sanitarios vigentes.
El modelo TxGNN predice que podría ser efectivo para **carcinoma del pezón (nipple carcinoma)**,
pero actualmente no hay ensayos clínicos registrados y la literatura disponible se limita a **reportes de caso y revisiones** sobre cáncer de mama y de pezón, sin estudios que evalúen letrozol directamente en esta enfermedad.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | LETROZOL |
| Nueva Indicación Predicha | Carcinoma del pezón (nipple carcinoma) |
| Puntaje de Predicción TxGNN | 0.9976 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 8 de 8) |
| Número de Registros Sanitarios | 8 (vigentes: 8) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Letrozol (traducción no oficial): «El crecimiento de algunos cánceres de mama es estimulado o mantenido por los estrógenos. El tratamiento del cáncer de mama que se considera hormonosensible (es decir, positivo para receptores de estrógeno y/o de progesterona o con estado de receptores desconocido) ha incluido diversos intentos de disminuir los niveles de estrógeno (ovariectomía, adrenalectomía, hipofisectomía) o de inhibir los efectos estrogénicos (antiestrógenos y agentes progestacionales). […] El letrozol es un inhibidor competitivo no esteroideo del sistema enzimático de la aromatasa; inhibe la conversión de andrógenos en estrógenos.» Texto original en inglés: "The growth of some cancers of the breast is stimulated or maintained by estrogens. Treatment of breast cancer thought to be hormonally responsive (i.e., estrogen and/or progesterone receptor positive or receptor unknown) has included a variety of efforts to decrease estrogen levels (ovariectomy, adrenalectomy, hypophysectomy) or inhibit estrogen effects (antiestrogens and progestational agents). […] Letrozole is a nonsteroidal competitive inhibitor of the aromatase enzyme system; it inhibits the conversion of androgens to estrogens." ([DailyMed: Femara (letrozole) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=82b77d74-085f-45ac-a7dd-1f5c038bf406), versión del 2026-06-11; consultado el 2026-11-19). Según la información conocida, letrozol es un inhibidor de la aromatasa: bloquea la conversión de andrógenos en estrógenos y, con ello, reduce los estrógenos circulantes. Es una terapia endocrina establecida en el cáncer de mama con receptores hormonales positivos.

Los carcinomas de la región del pezón (por ejemplo, el carcinoma papilar originado en el pezón o las lesiones tipo Paget) surgen del epitelio mamario y podrían expresar receptores de estrógeno o progesterona. Por ello, un mecanismo de privación estrogénica es biológicamente plausible.

Sin embargo, esta relación es indirecta: se apoya en la cercanía con el cáncer de mama en general y no en datos específicos del pezón. El puntaje alto del modelo es una predicción computacional y no constituye evidencia clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [41607681](https://pubmed.ncbi.nlm.nih.gov/41607681/) | 2026 | Reporte de caso y revisión | Clinical Case Reports | Carcinoma papilar sólido in situ originado en el pezón en una mujer de 73 años; hay poca evidencia sobre criterios diagnósticos y tratamiento óptimo |
| [33120755](https://pubmed.ncbi.nlm.nih.gov/33120755/) | 2020 | Cohorte/Retrospectivo (reporte de caso) | Medicine | Eficacia de la terapia endocrina neoadyuvante en carcinoma neuroendocrino de mama poco diferenciado; no es específico del pezón |
| [42040393](https://pubmed.ncbi.nlm.nih.gov/42040393/) | 2026 | Reporte de caso | Clinical Case Reports | Carcinoma de células altas de mama con polaridad invertida y mutación IDH1 R132, con secreción purulenta por el pezón |
| [40395253](https://pubmed.ncbi.nlm.nih.gov/40395253/) | 2025 | Reporte de caso | Cureus | Recurrencia axilar inusual en cáncer de mama que se presentó con secreción sanguinolenta por el pezón |
| [34495428](https://pubmed.ncbi.nlm.nih.gov/34495428/) | 2021 | Reporte de caso y revisión | Surgical Case Reports | Cáncer de mama accesorio en la región inframamaria |
| [39682607](https://pubmed.ncbi.nlm.nih.gov/39682607/) | 2024 | Reporte de caso | Diagnostics (Basel) | Cáncer de mama accesorio metastásico sincrónico con cáncer de mama ipsilateral |
| [42416948](https://pubmed.ncbi.nlm.nih.gov/42416948/) | 2026 | Reporte de caso | Cureus | Carcinoma lobulillar in situ florido: hallazgos ecográficos |
| [42305961](https://pubmed.ncbi.nlm.nih.gov/42305961/) | 2026 | Reporte de caso | Frontiers in Medicine | Tríada de neoplasias sincrónicas: cáncer de mama accesorio, carcinoma papilar de tiroides y papiloma nasal inflamatorio |

Ninguna de estas publicaciones estudia letrozol directamente en el carcinoma del pezón, por lo que el nivel de evidencia se mantiene en L5.

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 20024551 | LETROZOL2.5 MG | TABLETA RECUBIERTA | LETROZOL | Vigente |
| 20060915 | HB ONCOBREAST® 2.5 MG TABLETAS RECUBIERTAS | TABLETA RECUBIERTA | LETROZOL | Vigente |
| 20065665 | LETROLE® | TABLETA RECUBIERTA | LETROZOL | Vigente |
| 20126083 | LETARA® 2.5 MG TABLETAS | TABLETA | LETROZOL | Vigente |
| 20136242 | LATOREN® 2.5 MG TABLETAS RECUBIERTAS | TABLETA RECUBIERTA | LETROZOL | Vigente |

Se muestran 5 de 8 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia hormonal (inhibidor de la aromatasa); no es un citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo y en un razonamiento mecanístico indirecto. No hay ensayos clínicos y la literatura son reportes de caso que no evalúan letrozol en el carcinoma del pezón.

**Para avanzar se necesita:**
- Estudios que evalúen letrozol directamente en carcinoma del pezón o enfermedad de Paget (por ejemplo, series de casos con estado de receptores hormonales)
- Datos de mecanismo de acción confirmados (por ejemplo, desde DrugBank)
- Advertencias y contraindicaciones del prospecto de INVIMA para el análisis de seguridad
- Evaluación del beneficio y riesgo de la privación estrogénica (pérdida ósea, síntomas menopáusicos) en esta población

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Femara (letrozole) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=82b77d74-085f-45ac-a7dd-1f5c038bf406) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

