---
layout: default
title: Alfuzosin
parent: Solo Predicción del Modelo (L5)
nav_order: 36
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Alfuzosin: nueva indicación predicha, Hipertricosis universal congénita tipo Ambras (nivel de evidencia L5). Indicación original: ALFUZOSINA"
monitor_inn: "alfuzosin"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly", "allergic urticaria", "persistent fetal circulation syndrome", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia"]
---

# Alfuzosin
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

# Alfuzosina: De Alfuzosina (indicación no detallada en el registro) a Hipertricosis Universal Congénita tipo Ambras

## Resumen en Una Frase

Alfuzosina es un antagonista de los receptores adrenérgicos alfa-1, registrado en Colombia bajo la marca XATRAL OD. (el texto del registro solo menciona "ALFUZOSINA", sin detallar la indicación).
El modelo TxGNN predice que podría ser efectivo para **hipertricosis universal congénita tipo Ambras**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; es únicamente una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | ALFUZOSINA (el registro no especifica la indicación) |
| Nueva Indicación Predicha | Hipertricosis universal congénita tipo Ambras |
| Puntaje de Predicción TxGNN | 99.999% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo cancelado (sin registros vigentes) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Por farmacología general, la alfuzosina bloquea los receptores adrenérgicos alfa-1, con selectividad por el tracto urogenital, y se usa en síntomas urinarios por hiperplasia prostática benigna.

No se ha identificado un vínculo mecanístico plausible con la hipertricosis de Ambras, una enfermedad congénita asociada a reordenamientos cromosómicos que afectan la regulación de TRPS1. El puntaje alto (~0.99999) refleja probablemente la proximidad en la red del grafo de conocimiento con fenotipos relacionados con el cabello, no evidencia biológica ni clínica.

Cabe señalar que algunos agentes vasodilatadores (por ejemplo, minoxidil) se asocian con hipertricosis como efecto adverso. Si existiera una señal capilar para la alfuzosina, sería más bien una dirección de efecto adverso que terapéutica. En conjunto, la predicción debe considerarse especulativa.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19908750 (cancelado) | XATRAL OD. | Tableta de liberación prolongada | ALFUZOSINA |

Fabricante: Sanofi-Aventis de Colombia S.A. No hay registros vigentes.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad del grafo de conocimiento, no texto de prospecto): atrofia multisistémica, síndrome de taquicardia ortostática postural, hipotensión ortostática, síndrome de QT largo (incluido el familiar), torsades de pointes, insuficiencia hepática, enfermedad hepática, enfermedad de la vesícula biliar, trastornos hipotensivos y síndrome de iris flácido intraoperatorio.
- **Interacciones farmacológicas**: se identificaron 198 interacciones. Entre las de nivel **mayor** figuran **cisaprida, claritromicina y dolasetrón** (riesgo relacionado con prolongación del QT y/o inhibición metabólica). Hay además numerosas interacciones moderadas (por ejemplo, famotidina, aprepitant, bupropión, inhibidores de SGLT2 como canagliflozina, dapagliflozina y empagliflozina, levofloxacino, granisetrón y laxantes osmóticos). La cimetidina es de nivel menor.
- La hipotensión sistémica es un riesgo relevante, sobre todo en poblaciones vulnerables como los neonatos.

Para advertencias y contraindicaciones del prospecto, consultar el prospecto oficial.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos ni publicaciones, y no existe plausibilidad mecanística para una enfermedad genética congénita. Además, el producto solo tiene un registro cancelado en Colombia y el perfil de seguridad incluye riesgos cardiovasculares relevantes.

**Para avanzar se necesita:**
- Datos del mecanismo de acción confirmados (DrugBank)
- Revisión del prospecto de INVIMA (advertencias y contraindicaciones)
- Evidencia preclínica o de mecanismo que vincule el bloqueo alfa-1 con la biología de la hipertricosis
- Evaluación de las demás predicciones del listado (todas con nivel L5) para identificar candidatos con mayor plausibilidad biológica
- Aclarar la situación regulatoria, ya que no hay registros vigentes en Colombia
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

