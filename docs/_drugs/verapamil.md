---
layout: default
title: Verapamil
parent: Solo Predicción del Modelo (L5)
nav_order: 657
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-31
description: "Verapamil: nueva indicación predicha, Bloqueo de rama (término obsoleto) (nivel de evidencia L5). Indicación original: Trandolapril y bloqueadores de canales de calcio"
monitor_inn: "verapamil"
predicted_indications: ["obsolete bundle branch block", "malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "periodic paralysis with transient compartment-like syndrome"]
---

# Verapamil
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Verapamilo: De Bloqueador de Canales de Calcio (asociado a Trandolapril) a Bloqueo de Rama Haz de His (obsoleto)
{: .text-alpha }

## Resumen en Una Frase

Verapamilo es un bloqueador de canales de calcio, registrado en Colombia como parte de la combinación con trandolapril (TARKA® SR), usado originalmente en el tratamiento cardiovascular.
El modelo TxGNN predice que podría ser efectivo para **bloqueo de rama (término obsoleto)**, con **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.
La predicción se basa únicamente en el puntaje del modelo y, según el análisis mecanístico, no cuenta con respaldo biológico sólido.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trandolapril y bloqueadores de canales de calcio |
| Nueva Indicación Predicha | Bloqueo de rama (término obsoleto) |
| Puntaje de Predicción TxGNN | 0.9962 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | al menos 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, el verapamilo es un antiarrítmico de clase IV que bloquea los canales de calcio tipo L y enlentece la conducción del nodo auriculoventricular. En Colombia se registró en combinación con trandolapril (un inhibidor de la ECA) como tratamiento antihipertensivo.

La relación con la nueva indicación es débil. El bloqueo de rama es un defecto de conducción del sistema His-Purkinje que depende en gran medida de los canales de sodio, y enlentecer la conducción podría empeorarlo. Además, la etiqueta de la enfermedad está marcada como "obsoleta", lo que sugiere un artefacto de la ontología más que una indicación clínica real.

Por lo tanto, el alto puntaje de TxGNN no tiene sustento mecanístico claro. Debe leerse como una señal computacional sin validar y no como una hipótesis terapéutica creíble.

### Otras indicaciones predichas (contexto)

| Rango | Indicación Predicha | Puntaje | Nivel | Comentario |
|---|---|---|---|---|
| 2 | Enfermedad renal hipertensiva maligna | 0.9927 | L5 | Plausible como antihipertensivo, pero es una emergencia manejada normalmente con fármacos intravenosos; sin evidencia |
| 3 | Hipertensión renovascular maligna | 0.9927 | L5 | Dos artículos recuperados sin evidencia de eficacia del verapamilo |
| 4 | Hipertensión pulmonar por enfermedad pulmonar o hipoxia | 0.9926 | L4 | Solo estudios preclínicos indirectos; la clase puede empeorar el equilibrio V/Q |
| 5 | Hipertensión pulmonar de mecanismo multifactorial incierto | 0.9926 | L5 | No es un agente recomendado; sin evidencia |
| 6 | Síndrome de Braddock | 0.9915 | L5 | Sin vínculo mecanístico identificado |
| 7 | Parálisis periódica con síndrome compartimental transitorio | 0.9908 | L5 | Vínculo conceptual con canales de calcio, pero efecto no demostrado |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal (bloqueo de rama).

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 230359 (cancelado) | TARKA® SR TABLETAS | Tableta de liberación prolongada | Trandolapril y bloqueadores de canales de calcio |

El único registro sanitario está cancelado, por lo que actualmente no hay producto vigente con verapamilo en este registro.

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento** (no provienen del prospecto): bloqueo auriculoventricular, insuficiencia cardíaca, estenosis aórtica, cardiomiopatía hipertrófica, taquicardia ventricular, trastornos hipotensivos, miastenia gravis, enfermedad renal, enfermedad hepática, neutropenia/agranulocitosis y angioedema (incluido el inducido por bloqueadores del sistema renina-angiotensina-aldosterona; parte de ellas se relaciona con el componente trandolapril de la combinación).
- **Interacciones farmacológicas**: se identificaron 328 interacciones. Entre las principales:
  - **Mayor**: loperamida.
  - **Moderadas**: cimetidina, claritromicina, aprepitant, bupropión, metformina, canagliflozina, ácido acetilsalicílico, corticoides (hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida) y sales de calcio (carbonato, cloruro, citrato, acetato, fosfato).
  - **Menor**: morfina.

Consultar el prospecto para la información completa de advertencias, ya que no se obtuvo el texto del prospecto de INVIMA.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal carece de ensayos clínicos y literatura, tiene nivel de evidencia L5 y es mecanísticamente contradictoria (el bloqueo de calcio puede empeorar los defectos de conducción). Además, la enfermedad aparece como término obsoleto y el producto registrado en Colombia está cancelado.

**Para avanzar se necesita:**
- Aclarar si el término "bloqueo de rama (obsoleto)" corresponde a un artefacto de la ontología y reemplazarlo por un término vigente.
- Obtener el prospecto de INVIMA (advertencias y contraindicaciones) y el mecanismo de acción detallado desde DrugBank.
- Considerar priorizar indicaciones con mayor plausibilidad farmacológica (p. ej., hipertensión renovascular o enfermedad renal hipertensiva) y realizar una revisión sistemática específica de verapamilo.
- Confirmar la situación regulatoria actual del verapamilo en Colombia, dado que el único registro identificado está cancelado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

