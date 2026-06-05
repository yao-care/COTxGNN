---
layout: default
title: Perindopril
parent: 僅模型預測 (L5)
nav_order: 196
evidence_level: L5
indication_count: 5
---

# Perindopril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Perindopril: De Hipertensión Arterial a Enfermedad Renal por Hipertensión Maligna

## Resumen en Una Frase

Perindopril es un inhibidor de la enzima convertidora de angiotensina (IECA), utilizado principalmente para el tratamiento de la hipertensión arterial, la insuficiencia cardíaca y la reducción del riesgo cardiovascular. El modelo TxGNN predice que podría ser efectivo para la **Enfermedad Renal por Hipertensión Maligna**, con **0 ensayos clínicos** y **1 publicación** que respaldan directamente esta dirección. La conexión mecanística es biológicamente plausible, pero la evidencia clínica directa es insuficiente y existen advertencias de seguridad importantes que deben evaluarse antes de avanzar.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial, insuficiencia cardíaca (clase IECA) |
| Nueva Indicación Predicha | Enfermedad Renal por Hipertensión Maligna |
| Puntaje de Predicción TxGNN | 99.77% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, Perindopril pertenece a la clase de los Inhibidores de la Enzima Convertidora de Angiotensina (IECA). Su eficacia en hipertensión arterial e insuficiencia cardíaca ha sido ampliamente comprobada, y mecanísticamente podría ser aplicable a la enfermedad renal por hipertensión maligna.

El vínculo mecanístico propuesto es el siguiente: Perindopril inhibe la generación de Angiotensina II → reduce la resistencia de la arteriola eferente → disminuye la presión intraglomerular y la proteinuria → genera efecto nefroprotector. La hipertensión maligna con afectación renal podría teóricamente beneficiarse de este mecanismo, dado que la hipertensión arterial sistémica severa es el sustrato patológico compartido tanto con la indicación original como con la indicación predicha.

Sin embargo, existe una advertencia mecanística crítica: durante la fase aguda de deterioro renal severo en hipertensión maligna, la perfusión glomerular puede depender de la Angiotensina II para mantener la presión de filtración. El bloqueo de este mecanismo compensador mediante un IECA puede precipitar lesión renal aguda (AKI). Esta consideración hace obligatoria una evaluación de seguridad formal antes de cualquier uso en esta indicación.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [36382821](https://pubmed.ncbi.nlm.nih.gov/36382821/) | 2022 | Observacional/Reporte Clínico | *Urologiia* (Moscow, Russia) | Evaluación del estado funcional del riñón solitario tras nefrectomía por cáncer renal; analiza pérdida progresiva de función renal post-quirúrgica y factores pronósticos |

> **Nota de relevancia:** Esta publicación aborda la función renal post-nefrectomía oncológica, no el uso de Perindopril en hipertensión maligna renal. Su relevancia directa para la indicación predicha es marginal; se incluye como único resultado disponible en la búsqueda.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia clínica directa de Perindopril en enfermedad renal por hipertensión maligna es insuficiente (nivel L4: solo sustento mecanístico), sin ensayos clínicos ni literatura específica que respalde la indicación. Adicionalmente, el perfil mecanístico del fármaco identifica un riesgo potencial de lesión renal aguda en la fase activa de hipertensión maligna, lo que requiere evaluación de seguridad formal antes de avanzar.

**Para avanzar se necesita:**
- Completar el mecanismo de acción detallado (MOA) mediante consulta a DrugBank API
- Obtener información de seguridad completa (advertencias, contraindicaciones, interacciones) del prospecto oficial INVIMA o TFDA
- Evaluar función renal basal y descartar estenosis de arteria renal en pacientes candidatos antes de cualquier uso
- Realizar búsqueda bibliográfica ampliada con términos específicos (perindopril + malignant hypertension + renal)
- Definir diseño de estudio observacional o ensayo piloto en unidades de nefrología especializadas
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

