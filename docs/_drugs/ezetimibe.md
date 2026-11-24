---
layout: default
title: Ezetimibe
parent: Solo Predicción del Modelo (L5)
nav_order: 276
evidence_level: L5
indication_count: 1
monitor_inn: "EZETIMIBE"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-11-24
description: "Ezetimibe: nueva indicación predicha, Deficiencia de la proteína de transferencia de ésteres de colesterol (nivel de evidencia L5). Indicación original: Simvastatina combinaciones paquetes"
---

# Ezetimibe
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Ezetimiba: De Simvastatina en combinaciones a Deficiencia de la proteína de transferencia de ésteres de colesterol
{: .text-alpha }

## Resumen en Una Frase

Ezetimiba es un fármaco que, según el registro sanitario local, se comercializa en combinación con simvastatina (indicación registrada: "Simvastatina combinaciones paquetes"). El modelo TxGNN predice que podría ser efectivo para la **deficiencia de la proteína de transferencia de ésteres de colesterol (CETP)**, pero actualmente no hay ensayos clínicos y solo hay **2 publicaciones** de contexto general (una revisión y un estudio en animales), que no estudian directamente esta enfermedad.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Simvastatina combinaciones paquetes |
| Nueva Indicación Predicha | Deficiencia de la proteína de transferencia de ésteres de colesterol |
| Puntaje de Predicción TxGNN | 0.9909 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 19) |
| Número de Registros Sanitarios | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Ezetimibe (traducción no oficial): «La ezetimiba reduce el colesterol en sangre al inhibir la absorción del colesterol en el intestino delgado. Se ha demostrado que la diana molecular de la ezetimiba es el transportador de esteroles Niemann-Pick C1-Like 1 (NPC1L1), que participa en la captación intestinal del colesterol y de los fitoesteroles.» Texto original en inglés: "Ezetimibe reduces blood cholesterol by inhibiting the absorption of cholesterol by the small intestine. The molecular target of ezetimibe has been shown to be the sterol transporter, Niemann-Pick C1-Like 1 (NPC1L1), which is involved in the intestinal uptake of cholesterol and phytosterols." ([DailyMed: ezetimibe prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c37c695b-fb40-423c-9b73-d1aa58a34db9), versión del 2026-10-08; consultado el 2026-11-19). Según el conocimiento general, ezetimiba inhibe la absorción intestinal de colesterol al bloquear la proteína NPC1L1, lo que reduce el colesterol LDL (LDL-C).

La deficiencia de CETP es una condición genética caracterizada por HDL-C marcadamente elevado y un metabolismo lipoproteico alterado. Existe un vínculo conceptual por las vías compartidas del metabolismo de lípidos, y el puntaje alto de TxGNN (0.9909) proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

Sin embargo, ningún dato muestra que ezetimiba trate la deficiencia de CETP o modifique los desenlaces de los pacientes afectados. Además, esta condición no suele considerarse una que requiera terapia reductora de LDL, por lo que la justificación clínica del tratamiento no es clara. Este vínculo se basa en conocimiento general y no en los datos aportados.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [40911366](https://pubmed.ncbi.nlm.nih.gov/40911366/) | 2025 | Revisión | European Heart Journal | Panorama de dianas para reducir lípidos: además del LDL-C, destaca triglicéridos, apoB y Lp(a) como fuentes de riesgo cardiovascular residual. No estudia directamente la deficiencia de CETP. |
| [31779098](https://pubmed.ncbi.nlm.nih.gov/31779098/) | 2019 | Estudio en animales | International Journal of Molecular Sciences | Modelo de hámster heterocigoto Ldlr para evaluar un anticuerpo anti-PCSK9 en hiperlipidemia y aterosclerosis. No evalúa ezetimiba ni la deficiencia de CETP. |

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19936459 | ZETIA® TABLETAS. | TABLETA | EZETIMIBE | Vigente |
| 19951296 | VYTORIN ® 10/10MG | TABLETA | SIMVASTATIN Y EZETIMIBE | Vigente |
| 19951298 | VYTORIN ® 10/20 MG | TABLETA | SIMVASTATIN Y EZETIMIBE | Vigente |
| 19951299 | VYTORIN ® 10/40 MG | TABLETA | SIMVASTATIN Y EZETIMIBE | Vigente |
| 19974991 | TIAZOMET S® | TABLETA RECUBIERTA | SIMVASTATINA COMBINACIONES PAQUETES | Vigente |

Se muestran 5 de al menos 20 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes. Los datos de este informe solo incluyen parte de los registros.

<!-- licenses:end -->

La lista puede ser parcial.

## Consideraciones de Seguridad

- **Relaciones de contraindicación registradas en el grafo de conocimiento** (no provienen del texto del prospecto): pancreatitis, enfermedad hepática, enfermedad de la vesícula biliar, miopatía, enfermedad muscular, enfermedad del músculo esquelético, parálisis periódica familiar, abuso/dependencia de sustancias, rabdomiólisis y fascitis nodular.
- **Interacciones farmacológicas**: se identificaron 100 interacciones en total. Las de nivel moderado incluyen ácido quenodesoxicólico, eluxadolina, rosuvastatina y simvastatina. Otras (calcitriol, pantoprazol, glimepirida, mesalazina, doxiciclina, metformina, omeprazol, morfina, entre otras) tienen nivel de gravedad no determinado.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (L5): no hay ensayos clínicos ni estudios que evalúen ezetimiba en la deficiencia de CETP, y la necesidad clínica de reducir el LDL en esta condición es dudosa.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de ezetimiba en los datos compilados.
- Evidencia directa (preclínica o clínica) sobre ezetimiba en la deficiencia de CETP.
- Justificación clínica de que esta población se beneficiaría de una terapia reductora de LDL.
- Advertencias y contraindicaciones del prospecto del INVIMA para la evaluación de seguridad.
- Revisión de las relaciones de contraindicación del grafo de conocimiento (hígado, músculo, páncreas) frente a la población objetivo.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: ezetimibe prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c37c695b-fb40-423c-9b73-d1aa58a34db9) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

