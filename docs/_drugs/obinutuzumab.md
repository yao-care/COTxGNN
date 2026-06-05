---
layout: default
title: Obinutuzumab
parent: 僅模型預測 (L5)
nav_order: 179
evidence_level: L5
indication_count: 3
---

# Obinutuzumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# OBINUTUZUMAB: De Leucemia Linfocítica Crónica a LLC/SLL con Hipermutación Somática de IGHV

## Resumen en Una Frase

Obinutuzumab es un anticuerpo monoclonal anti-CD20 glicoingenierizado de tipo II, utilizado globalmente para el tratamiento de la leucemia linfocítica crónica (LLC) y el linfoma folicular, aunque **no cuenta con registro sanitario INVIMA en Colombia**.
El modelo TxGNN predice que podría ser efectivo para **LLC/SLL con hipermutación somática de IGHV** (subgrupo molecular de mejor pronóstico dentro de la LLC), con un puntaje de predicción de 99.21%.
No existe ningún ensayo clínico ni publicación científica específica que respalde esta subindicación molecular, situándola en evidencia nivel L5 (predicción pura del modelo).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Leucemia linfocítica crónica y linfoma folicular (uso global aprobado; sin registro INVIMA en Colombia) |
| Nueva Indicación Predicha | LLC/SLL con hipermutación somática de IGHV |
| Puntaje de Predicción TxGNN | 99.21% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios INVIMA | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos detallados de mecanismo de acción no están disponibles en el Evidence Pack, sin embargo la farmacología de obinutuzumab está bien documentada en la literatura científica global. Se trata de un anticuerpo monoclonal anti-CD20 tipo II, totalmente humanizado y glicoingenierizado mediante defucosilación de la región Fc: la modificación de la región bisagra-codo (elbow-hinge) mejora la muerte celular directa por apoptosis en comparación con rituximab, mientras que la defucosilación amplifica la afinidad por el receptor FcγRIIIa, potenciando la citotoxicidad celular dependiente de anticuerpos (ADCC) mediada por células NK y la fagocitosis celular dependiente de anticuerpos (ADCP). A diferencia de rituximab, presenta menor actividad de citotoxicidad dependiente de complemento (CDC reducida), lo que puede traducirse en menor riesgo de reacciones de infusión severas.

Las células de LLC/SLL expresan consistentemente el antígeno CD20 en su superficie, independientemente del estado mutacional de IGHV. La subpoblación con IGHV mutado (≥2% de desviación de la línea germinal) corresponde al subtipo de LLC de pronóstico más favorable, con evolución clínica más indolente y mayor sobrevida libre de progresión. Dado que la expresión de CD20 es estructuralmente independiente del estado mutacional de IGHV, el mecanismo de obinutuzumab es teóricamente aplicable a este subgrupo molecular específico.

No obstante, existe una limitación metodológica relevante: el puntaje TxGNN para LLC/SLL IGHV-mutado (0.9921) es idéntico al del subtipo IGHV no mutado (Rango 2), lo que indica que el modelo no distingue entre ambas subclasificaciones moleculares. Esta observación sugiere que la predicción refleja la relación general obinutuzumab-LLC/SLL, más que una especificidad clínica diferencial hacia el subtipo IGHV mutado como entidad independiente.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para LLC/SLL con hipermutación somática de IGHV como indicación específica.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para LLC/SLL con hipermutación somática de IGHV como indicación específica.

---

## Información de Mercado en Colombia

Obinutuzumab no cuenta con registros sanitarios INVIMA vigentes en Colombia. El fármaco no está disponible comercialmente en el mercado colombiano.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia oncológica dirigida (anticuerpo monoclonal anti-CD20 tipo II, glicoingenierizado; no es quimioterapia citotóxica convencional) |
| Riesgo de Mielosupresión | Moderado-alto — neutropenia es el efecto adverso hematológico más frecuente, documentada en los ensayos GALLIUM y GADOLIN; trombocitopenia reportada con menor frecuencia |
| Clasificación de Emetogenicidad | Baja (anticuerpo monoclonal de administración intravenosa) |
| Ítems de Monitoreo | Hemograma completo con diferencial (antes de cada ciclo), función hepática y renal, monitoreo de reacciones a la infusión (IRR) durante y post-administración, síndrome de lisis tumoral (riesgo elevado en primeras dosis con alta carga tumoral), serología HBV previa al inicio (riesgo de reactivación) |
| Protección en Manejo | Preparación y administración por personal oncológico capacitado en entorno hospitalario; premedicación antihistamínica, antipirética y corticoide requerida antes de cada infusión para reducir riesgo de IRR; precauciones estándar para biológicos oncológicos IV |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción TxGNN para LLC/SLL con hipermutación somática de IGHV carece de cualquier evidencia clínica directa (L5), obinutuzumab no está registrado en Colombia (barrera regulatoria primaria), y la identidad de puntajes entre los subtipos IGHV mutado y no mutado indica que el modelo no agrega especificidad clínica diferencial para este subgrupo molecular en particular.

**Para avanzar se necesita:**
- Gestión de acceso al mercado colombiano: registro INVIMA, importación para uso investigacional o acceso por vía compasiva
- Búsqueda de análisis de subgrupos IGHV-mutado dentro de ensayos clínicos existentes de obinutuzumab en LLC (p. ej., ensayo CLL11), como datos secundarios que podrían elevar el nivel de evidencia
- Datos completos de MOA y perfil de seguridad desde DrugBank y prospecto oficial FDA/EMA (resolución de Data Gaps DG001 y DG002)
- Evaluación de si esta subindicación aporta valor clínico diferencial frente a la indicación general de LLC
- **Prioridad alternativa recomendada:** Generar evaluación separada para **linfoma folicular** (Rango 3 en esta evaluación, TxGNN 99.18%, Nivel L1, Decisión: *Proceed with Guardrails*), que cuenta con evidencia Phase 3 robusta — ensayo pivotal GALLIUM (n=1,401) y más de 50 ensayos clínicos registrados —, y representa el candidato con mayor respaldo clínico para gestión de acceso de obinutuzumab en Colombia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

