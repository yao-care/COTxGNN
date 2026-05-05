---
layout: default
title: Gilteritinib
parent: 僅模型預測 (L5)
nav_order: 85
evidence_level: L5
indication_count: 1
---

# Gilteritinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

El skill `txgnn-pipeline` confirma el contexto del proyecto. Ahora procedo a generar el informe con base en el Evidence Pack proporcionado.

---

# GILTERITINIB: De Leucemia Mieloide Aguda a Polio Bulbar

## Resumen en Una Frase

Gilteritinib es un inhibidor dual de las quinasas FLT3/AXL, aprobado internacionalmente para el tratamiento de la leucemia mieloide aguda (LMA) con mutación en FLT3, aunque actualmente no cuenta con registro sanitario en Colombia.
El modelo TxGNN predice que podría ser efectivo para **Polio Bulbar**,
sin embargo, actualmente **no existen ensayos clínicos ni publicaciones científicas** que respalden esta dirección — la predicción se apoya exclusivamente en la proximidad topológica del grafo de conocimiento, sin validación mecanística.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin registro en Colombia (aprobado internacionalmente para LMA con mutación FLT3) |
| Nueva Indicación Predicha | Polio Bulbar |
| Puntaje de Predicción TxGNN | 99.10% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Con base en la información conocida, gilteritinib es un inhibidor dual de las tirosina quinasas FLT3 y AXL, utilizado en oncohematología para el tratamiento de LMA con mutaciones en FLT3. Su acción sobre AXL ha despertado interés en el contexto de infecciones virales, dado que esta quinasa participa en la entrada celular de patógenos como Zika, SARS-CoV-2 y Ébola mediante el mecanismo de captación de cuerpos apoptóticos.

No obstante, el enlace mecanístico hacia la polio bulbar es sumamente débil. El poliovirus utiliza el receptor CD155/PVR para ingresar a las células del sistema nervioso central, un proceso en el que ni FLT3 ni AXL tienen un rol documentado. La polio bulbar representa la forma más grave de poliomielitis, con compromiso de los centros respiratorios y vasomotores del tronco encefálico, y no hay evidencia preclínica ni clínica que sugiera que la inhibición de estas quinasas ofrezca neuroprotección en este contexto.

El alto puntaje TxGNN (0.9910) se explica, con mayor probabilidad, por la proximidad topológica entre los nodos de enfermedades neurológicas en el grafo de conocimiento, y no por una relación farmacológica subyacente validada. Esta predicción debe interpretarse como una señal exploratoria de muy bajo grado de prioridad, no como evidencia de eficacia potencial.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para gilteritinib en polio bulbar.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para gilteritinib en polio bulbar.

---

## Citotoxicidad

> Gilteritinib es un agente antineoplásico (inhibidor de quinasas FLT3/AXL) indicado internacionalmente para leucemia mieloide aguda, por lo que aplica esta sección.

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor selectivo de tirosina quinasas FLT3/AXL) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma completo con diferencial, función hepática (ALT/AST), función renal (creatinina), electrocardiograma (intervalo QT) |
| Protección en Manejo | Debe seguir las regulaciones vigentes de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN para gilteritinib en polio bulbar carece por completo de soporte mecanístico, preclínico o clínico: no existen ensayos registrados, ni publicaciones, ni un enlace biológico plausible entre la inhibición de FLT3/AXL y la infección por poliovirus o la protección de neuronas bulbares. El nivel de evidencia L5 (solo predicción del modelo) y la ausencia de registro sanitario en Colombia hacen inviable cualquier avance en este momento.

**Para avanzar se necesita:**
- Verificación del mecanismo de acción (MOA) completo desde DrugBank o fuente primaria
- Evidencia preclínica que demuestre algún efecto de FLT3/AXL sobre replicación o patogénesis del poliovirus
- Revisión de la arquitectura del grafo TxGNN para identificar si la predicción proviene de un artefacto topológico (nodos de enfermedades neurológicas densamente conectados)
- Registro sanitario en Colombia como requisito previo a cualquier evaluación clínica local
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

