---
layout: default
title: Labetalol
parent: Evidencia Moderada (L3-L4)
nav_order: 369
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-14
description: "Labetalol: nueva indicación predicha, Hipertensión renovascular maligna (nivel de evidencia L4). Indicación original: Labetalol"
monitor_inn: "labetalol"
predicted_indications: ["malignant renovascular hypertension", "malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism"]
---

# Labetalol
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **4** 
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

# Labetalol: De Hipertensión Severa a Hipertensión Renovascular Maligna

## Resumen en Una Frase

Labetalol es un bloqueador combinado alfa-1 y beta-adrenérgico no selectivo, utilizado originalmente como antihipertensivo en solución inyectable (según los registros sanitarios en Colombia, que solo indican "labetalol" como indicación).
El modelo TxGNN predice que podría ser efectivo para **hipertensión renovascular maligna**, pero actualmente no hay ensayos clínicos y solo **1 publicación** (un reporte de caso no específico de labetalol) se relaciona con esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Labetalol (el registro sanitario no detalla la indicación; corresponde a hipertensión severa según el uso conocido del fármaco) |
| Nueva Indicación Predicha | Hipertensión renovascular maligna |
| Puntaje de Predicción TxGNN | 99.08% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 5 (todos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, labetalol bloquea los receptores alfa-1 (reduce la resistencia vascular) y los receptores beta (reduce la liberación de renina y la frecuencia cardíaca), y se emplea en hipertensión severa y emergencias hipertensivas.

La hipertensión renovascular maligna es una emergencia hipertensiva impulsada por la activación del sistema renina-angiotensina. El bloqueo beta reduce la liberación de renina y el bloqueo alfa-1 disminuye la resistencia vascular, por lo que existe un fundamento mecanístico plausible.

Es importante notar que esta predicción es en gran parte una extensión de la indicación antihipertensiva existente y no un reposicionamiento genuino. La única publicación recuperada (vasculitis inducida por alucinógenos) no trata sobre labetalol en esta condición.

Otras predicciones del modelo (puntajes similares, cercanos a 99%):
- **Enfermedad renal hipertensiva maligna** (L5): plausible por la reducción de la presión arterial, pero sin ensayos ni literatura.
- **Hipertensión pulmonar por enfermedad pulmonar o hipoxia** (L4) e **hipertensión pulmonar de mecanismo multifactorial poco claro** (L5): sin fundamento mecanístico evidente. El bloqueo beta no selectivo podría empeorar el broncoespasmo y la hipoxia. El puntaje parece reflejar el término compartido "hipertensión" y no biología vascular pulmonar.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Para la indicación principal (hipertensión renovascular maligna):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [7242419](https://pubmed.ncbi.nlm.nih.gov/7242419/) | 1981 | Reporte de caso | Med J Aust | Hombre de 20 años con hipertensión maligna y vasculitis renal por alucinógenos; respondió a prednisona. Minoxidil y labetalol se usaron para el control inicial de la presión, pero el estudio no es específico de labetalol |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20104881 | DIBLOREC (cancelado) | Solución inyectable | Labetalol |
| 20090031 | DUOBLOQ 100 MG / 20 ML (cancelado) | Solución inyectable | Labetalol |
| 20087030 | Labetalol clorhidrato 100 mg / 20 ml (cancelado) | Solución inyectable | Labetalol |
| 20004699 | TRANDATE® Labetalol clorhidrato 100 mg (cancelado) | Solución inyectable | Labetalol |
| 20068280 | PRESEQUIL (cancelado) | Solución inyectable | Labetalol |

Los cinco registros están cancelados; actualmente no hay registros vigentes.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no según el prospecto)**: el modelo asocia labetalol con contraindicación en enfermedades como insuficiencia hepática, enfermedad hepática, encefalopatía hepática, enfermedad renal, anuria, bloqueo auriculoventricular, enfisema pulmonar, enfermedad bronquial, diabetes mellitus, cetoacidosis diabética, hipotensión, lupus eritematoso sistémico, gota, pancreatitis, enfermedad de la vesícula biliar, trastornos de ansiedad y trastorno distímico, entre otras. Esta lista debe verificarse con el prospecto oficial.
- **Interacciones farmacológicas**: se identificaron 241 interacciones. Entre las principales:
  - **Mayor**: epinefrina, dolasetrón.
  - **Moderada**: hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida, morfina, atropina, cimetidina, canagliflozina, dapagliflozina, clorpropamida, dicicloverina, entre otras.
  - **Menor**: ácido acetilsalicílico, óxido de magnesio.
- **Preocupación específica**: el bloqueo beta no selectivo podría agravar el broncoespasmo y la hipoxia, lo que es relevante para las predicciones de hipertensión pulmonar.

No se dispone de advertencias ni contraindicaciones del prospecto; consultar el prospecto para información de seguridad adicional.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto, pero no hay ensayos clínicos ni literatura específica que la respalde (nivel L4), y se trata en esencia de una extensión de la indicación antihipertensiva ya conocida. Además, los cinco registros sanitarios en Colombia están cancelados y faltan datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto oficial del INVIMA (advertencias y contraindicaciones), una brecha de datos crítica.
- Complementar los datos del mecanismo de acción desde DrugBank.
- Buscar evidencia clínica específica de labetalol en hipertensión renovascular maligna y en enfermedad renal hipertensiva maligna.
- Aclarar la situación regulatoria: los registros cancelados y la disponibilidad actual del producto en Colombia.
- Descartar o deprioritizar las predicciones de hipertensión pulmonar por falta de fundamento mecanístico y riesgo de seguridad.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

