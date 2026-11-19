---
layout: default
title: Etanercept
parent: Solo Predicción del Modelo (L5)
nav_order: 265
evidence_level: L5
indication_count: 3
monitor_inn: "ETANERCEPT"
predicted_indications: ["hypermobility of coccyx", "Kummell disease", "vertebral disease"]
last_modified_at: 2026-11-06
description: "Etanercept: nueva indicación predicha, Hipermovilidad del coxis (hypermobility of coccyx) (nivel de evidencia L5). Indicación original: ETANERCEPT"
---

# Etanercept
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Etanercept: inhibidor del factor de necrosis tumoral (TNF) → Hipermovilidad del coxis (hypermobility of coccyx)
{: .text-alpha }

## Resumen en Una Frase

Etanercept es un fármaco biológico que bloquea el TNF, una molécula inflamatoria, y en Colombia tiene registros sanitarios locales. El modelo TxGNN predice que podría ser efectivo para **Hipermovilidad del coxis (hypermobility of coccyx)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que estudien directamente esta condición.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | ETANERCEPT |
| Nueva Indicación Predicha | Hipermovilidad del coxis (hypermobility of coccyx) |
| Puntaje de Predicción TxGNN | 0,9963 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 5 de 5) |
| Número de Registros Sanitarios | 5 (vigentes: 5) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Etanercept (traducción no oficial): «El TNF es una citocina de origen natural que participa en las respuestas inflamatorias e inmunitarias normales. Desempeña un papel importante en los procesos inflamatorios de la AR, la AIJ poliarticular, la APs y la EA, y en la patología articular resultante. […] El etanercept es una forma soluble dimérica del receptor p75 del TNF que puede unirse a moléculas de TNF.» Texto original en inglés: "TNF is a naturally occurring cytokine that is involved in normal inflammatory and immune responses. It plays an important role in the inflammatory processes of RA, polyarticular JIA, PsA, and AS and the resulting joint pathology. […] Etanercept is a dimeric soluble form of the p75 TNF receptor that can bind TNF molecules." ([DailyMed: Enbrel (etanercept) prescribing information, Immunex Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a002b40c-097d-47a5-957f-7a7b1807af7f), versión del 2026-05-11; consultado el 2026-11-19). Etanercept se conoce como una proteína de fusión que actúa como receptor soluble de TNF y, por tanto, bloquea la inflamación mediada por esta molécula.

La hipermovilidad del coxis es principalmente una condición mecánica o traumática, no una enfermedad inflamatoria impulsada por TNF. Por eso el alto puntaje de predicción no tiene, por ahora, un fundamento mecanístico claro. Tampoco hay estudios que conecten el bloqueo del TNF con esta condición.

El puntaje del modelo es una señal computacional de partida. Por sí solo no demuestra eficacia y debe interpretarse con cautela hasta contar con datos clínicos o preclínicos específicos.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: se identificaron 100 interacciones potenciales. Entre las de nivel **Mayor** figuran:
  - corticosteroides (hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida, prednisona, prednisolona);
  - deferiprona;
  - radiofármacos y anticuerpos radiomarcados (iobenguano I-131, ibritumomab tiuxetán, tositumomab).
- Entre las de nivel **Moderado** figuran metronidazol, tinidazol, rosuvastatina y simvastatina.
- Entre las de nivel **Menor** figuran las sales de zinc (sulfato, acetato, gluconato).

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos ni publicaciones que estudien directamente la hipermovilidad del coxis con etanercept, y la naturaleza mecánica de la condición no se corresponde con el mecanismo de bloqueo del TNF. El nivel de evidencia es L5, solo predicción del modelo.

**Para avanzar se necesita:**
- Una hipótesis mecanística plausible que vincule la inflamación mediada por TNF con esta condición
- Estudios preclínicos o series de casos que exploren el uso en esta condición
- Datos del mecanismo de acción y de advertencias y contraindicaciones del prospecto local
- Revisión del perfil de interacciones, en especial con corticosteroides, si se continúa la evaluación

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Enbrel (etanercept) prescribing information, Immunex Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a002b40c-097d-47a5-957f-7a7b1807af7f) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

