---
layout: default
title: Lisinopril
parent: Solo Predicción del Modelo (L5)
nav_order: 405
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Lisinopril: nueva indicación predicha, Infarto de miocardio posterolateral (nivel de evidencia L5). Indicación original: LISINOPRIL"
monitor_inn: "lisinopril"
predicted_indications: ["pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "chronic pulmonary heart disease", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome"]
---

# Lisinopril
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Lisinopril: De Indicación No Especificada a Infarto de Miocardio Posterolateral

## Resumen en Una Frase

Lisinopril es un inhibidor de la enzima convertidora de angiotensina (IECA) registrado en Colombia, aunque el texto de indicación del registro solo repite el nombre del principio activo y no detalla el uso aprobado.
El modelo TxGNN predice que podría ser efectivo para **infarto de miocardio posterolateral**, pero actualmente **no hay ensayos clínicos ni publicaciones** específicas que respalden esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | LISINOPRIL (el registro no detalla una indicación clínica) |
| Nueva Indicación Predicha | Infarto de miocardio posterolateral |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, lisinopril es un inhibidor de la ECA, una clase que bloquea el sistema renina-angiotensina-aldosterona (RAAS). Esta clase tiene un papel establecido en la atención posterior a un infarto de miocardio, al reducir el remodelado ventricular adverso.

La relación con la indicación original es solo de clase: el registro colombiano no especifica una indicación clínica, por lo que la similitud con la nueva indicación no pudo evaluarse formalmente. Existe un racional general para el infarto de miocardio, pero no hay ensayos ni literatura específicos del subtipo posterolateral. La evidencia general de la clase (por ejemplo, estudios como GISSI-3) no forma parte de los datos suministrados y no se acredita aquí.

**Otras predicciones del modelo (para contexto):**

| Indicación Predicha | Puntaje TxGNN | Nivel | Recomendación |
|------|------|------|------|
| Infarto de miocardio posteroinferior | 99.90% | L5 | Hold |
| Hipertensión pulmonar por enfermedad pulmonar y/o hipoxia | 99.89% | L4 | Pregunta de investigación |
| Hipertensión pulmonar de mecanismo multifactorial poco claro | 99.89% | L5 | Hold |
| Enfermedad renal hipertensiva maligna | 99.89% | L5 | Hold |
| Hipertensión renovascular maligna | 99.89% | L5 | Hold |
| Infarto de miocardio septal | 99.88% | L4 | Pregunta de investigación |
| Síndrome de Braddock | 99.86% | L5 | Hold |
| Enfermedad cardíaca pulmonar crónica (cor pulmonale) | 99.68% | L3 | Pregunta de investigación |
| Síndrome autosómico dominante de hematuria familiar con tortuosidad arteriolar retiniana y contracturas | 99.33% | L5 | Hold |

La candidata con mayor respaldo es el **cor pulmonale crónico**, con dos reportes clínicos específicos de lisinopril (PMID 17047621 y 14524095), aunque probablemente pequeños y sin control.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para infarto de miocardio posterolateral.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para infarto de miocardio posterolateral.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 37168 | LISIPRIL® TABLETAS | Tableta | LISINOPRIL | Cancelado |
| 19951978 | LISIPRIL® 5 | Tableta | LISINOPRIL | Cancelado |

Ambos registros corresponden a monofármacos del Laboratorio Franco Colombiano - Lafrancol S.A.S. No hay registros vigentes.

---

## Consideraciones de Seguridad

- **Contraindicaciones y enfermedades de riesgo (grafo de conocimiento TxGNN, no texto del prospecto)**: el grafo señala relaciones de contraindicación con, entre otras, angioedema (incluido el hereditario, el adquirido y el inducido por bloqueadores del RAAS), enfermedad renal, enfermedad hepática y encefalopatía hepática, pancreatitis, enfermedad de la vesícula biliar, diabetes mellitus y cetoacidosis diabética, lupus eritematoso sistémico, neutropenia y agranulocitosis, estenosis aórtica, trastornos hipotensivos, deficiencia de potasio, hiperparatiroidismo y enfermedades del tejido conectivo y óseas.
- **Interacciones farmacológicas**: se identificaron 308 interacciones; las más relevantes de las listadas:
  - **Mayores**: citrato de potasio y bicarbonato de potasio (riesgo de hiperpotasemia).
  - **Moderadas**: corticosteroides (hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida), antidiabéticos (metformina, inhibidores de SGLT2 como dapagliflozina, empagliflozina y canagliflozina, inhibidores de DPP-4 como alogliptina y saxagliptina, clorpropamida), ácido acetilsalicílico, morfina, bupropión, dronabinol, ácido picosulfúrico y polietilenglicol con electrolitos.
- **Señal adicional de la literatura**: un reporte de caso describe hipotensión y bradicardia graves con el uso concomitante de tizanidina y lisinopril. Además, en hipertensión renovascular, los IECA pueden precipitar insuficiencia renal aguda en estenosis bilateral de la arteria renal.

No se dispone de advertencias ni contraindicaciones del prospecto de INVIMA; consultar el prospecto para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para infarto de miocardio posterolateral es solo del modelo (nivel L5), sin ensayos ni literatura específica. Además, el producto no tiene registros vigentes en Colombia y faltan datos del prospecto y del mecanismo de acción.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), lo cual es un vacío bloqueante para el tamizaje de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Aclarar la indicación aprobada real del producto, ya que el registro solo indica el nombre del principio activo.
- Revisar la evidencia clínica general de los IECA en infarto de miocardio y evaluar si la subclasificación (posterolateral) aporta algo distinto.
- Considerar priorizar el cor pulmonale crónico, que tiene la mayor evidencia entre las candidatas (L3), verificando el diseño de los estudios disponibles.
- Verificar la situación de comercialización: sin registros vigentes, un reposicionamiento exigiría un nuevo registro o reactivación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

