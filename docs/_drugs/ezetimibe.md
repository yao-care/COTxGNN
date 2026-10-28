---
layout: default
title: Ezetimibe
parent: Solo Predicción del Modelo (L5)
nav_order: 276
evidence_level: L5
indication_count: 1
monitor_inn: "EZETIMIBE"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-10-23
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
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | Al menos 1 (la lista puede ser parcial) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento general, ezetimiba inhibe la absorción intestinal de colesterol al bloquear la proteína NPC1L1, lo que reduce el colesterol LDL (LDL-C).

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

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20138715 | EZIT-ST 10/10 | Tableta | Simvastatina combinaciones paquetes |

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
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

