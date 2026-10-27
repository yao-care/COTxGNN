---
layout: default
title: Buprenorphine
parent: Evidencia Moderada (L3-L4)
nav_order: 121
evidence_level: L4
indication_count: 6
last_modified_at: 2026-10-14
description: "Buprenorphine: nueva indicación predicha, Porfiria aguda intermitente (nivel de evidencia L4). Indicación original: Buprenorfina"
monitor_inn: "Buprenorphine"
predicted_indications: ["acute intermittent porphyria", "lingual-facial-buccal dyskinesia", "chronic tic disorder", "continuous spikes and waves during sleep", "benign shuddering attacks", "extrapyramidal and movement disease"]
---

# Buprenorphine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **6** 
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

## Buprenorfina: De Buprenorfina (indicación no detallada) a Porfiria Aguda Intermitente
{: .text-alpha }

## Resumen en Una Frase

Buprenorfina es un opioide agonista parcial del receptor mu (y antagonista del receptor kappa), utilizado para tratar el dolor intenso y la dependencia de opioides.
El modelo TxGNN predice que podría ser efectivo para **porfiria aguda intermitente**, pero **no hay ensayos clínicos** y solo **1 publicación** (un reporte de caso sobre manejo anestésico de 1993) relacionada, que no demuestra beneficio terapéutico.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Buprenorfina (el registro sanitario no detalla la indicación; en la práctica, dolor intenso y dependencia de opioides) |
| Nueva Indicación Predicha | Porfiria aguda intermitente |
| Puntaje de Predicción TxGNN | 99.41% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información farmacológica conocida, la buprenorfina actúa sobre el receptor opioide mu (OPRM1) y el receptor kappa (OPRK1), y se emplea en dolor intenso y dependencia de opioides.

No se identificó un vínculo mecanístico claro con la porfiria aguda intermitente. La única publicación recuperada describe el manejo anestésico de una paciente con esta enfermedad, es decir, un tema de seguridad perioperatoria de fármacos anestésicos y analgésicos, no un beneficio terapéutico. El dolor abdominal es una manifestación frecuente de los ataques, pero esto no respalda por sí solo que la buprenorfina trate la enfermedad de fondo.

El puntaje alto del modelo (99.41%) no está respaldado por datos clínicos. El uso de opioides en porfiria se considera sobre todo un tema de seguridad (riesgo porfirinogénico), no una opción de tratamiento.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [8301837](https://pubmed.ncbi.nlm.nih.gov/8301837/) | 1993 | Reporte de caso | Masui (Japanese Journal of Anesthesiology) | Manejo anestésico de una paciente de 40 años con sospecha de porfiria aguda intermitente sometida a histerectomía radical por tumor ovario maligno; no evalúa eficacia de buprenorfina |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 19967654 | TRANSTEC® 70 MCG/H | Solución para uso transdérmico (parche) | BUPRENORFINA | Cancelado |
| 19967651 | TRANSTEC® 35 MCG/H | Solución para uso transdérmico (parche) | BUPRENORFINA | Cancelado |

## Consideraciones de Seguridad

- **Enfermedades asociadas a contraindicación o precaución** (según el grafo de conocimiento de TxGNN, no según el prospecto): 
  - Respiratorias: enfermedad pulmonar obstructiva crónica (incluida la de inicio temprano grave), insuficiencia respiratoria.
  - Cardiovasculares: síndrome de QT largo (incluido el familiar), torsades de pointes, hipotensión ortostática, síndrome de taquicardia postural ortostática, atrofia multisistémica, insuficiencia de la válvula pulmonar.
  - Hepáticas y biliares: enfermedad hepática, enfermedad de la vesícula biliar, hepatitis C (aguda y crónica), hepatitis B crónica.
  - Endocrinas: insuficiencia suprarrenal, enfermedad de Addison, hipotiroidismo, mixedema, hipotiroidismo congénito.
  - Gastrointestinales y urinarias: íleo paralítico, obstrucción intestinal, miopatía visceral familiar, hiperplasia prostática benigna, estenosis uretral.
  - Neurológicas: hipertensión intracraneal, pseudotumor cerebral.
  - Dependencia: dependencia de drogas, trastornos relacionados con sustancias.
- **Interacciones farmacológicas**: los datos disponibles describen únicamente la farmacología de la unión a receptores (receptor kappa y receptor mu), sin interacciones con otros fármacos.
- **Consideración específica para la nueva indicación**: los opioides pueden tener riesgo porfirinogénico, por lo que la seguridad en porfiria aguda intermitente requiere una evaluación cuidadosa.

Para advertencias y contraindicaciones del prospecto, consultar el prospecto del producto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN para porfiria aguda intermitente carece de ensayos clínicos y de un vínculo mecanístico claro; la única publicación es un reporte de caso sobre manejo anestésico. Además, los registros sanitarios en Colombia están cancelados y existe una preocupación de seguridad (riesgo porfirinogénico de los opioides).

**Para avanzar se necesita:**
- Datos del mecanismo de acción y análisis de un posible vínculo mecanístico con la porfiria aguda intermitente.
- Revisión de la seguridad porfirinogénica de la buprenorfina en la literatura y bases de datos especializadas.
- Advertencias y contraindicaciones del prospecto del INVIMA.
- Aclarar la situación regulatoria, ya que ambos registros están cancelados.
- Estudios preclínicos o clínicos que evalúen un beneficio terapéutico real.

**Otras predicciones del modelo (todas con decisión Hold):** discinesia linguo-facial-bucal (99.32%, evidencia indirecta L4, centrada en agitación en demencia y farmacología general), trastorno de tics crónico (99.13%, L5), punta-onda continua durante el sueño (99.05%, L5; los opioides podrían reducir el umbral convulsivo), ataques de estremecimiento benignos (99.03%, L5) y enfermedad extrapiramidal y de movimiento (99.03%, L5). Ninguna cuenta con ensayos clínicos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

