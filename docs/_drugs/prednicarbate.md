---
layout: default
title: Prednicarbate
parent: Solo Predicción del Modelo (L5)
nav_order: 330
evidence_level: L5
indication_count: 7
---

# Prednicarbate
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Prednicarbato: De Corticosteroide Tópico a Queratosis Folicular Invertida Vulvar

## Resumen en Una Frase

Prednicarbato es un corticosteroide tópico de potencia media, comercializado en Colombia en emulsión y crema. Su registro no detalla la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **queratosis folicular invertida vulvar**, pero hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es una predicción puramente del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | PREDNICARBATO (el registro solo indica el nombre del principio activo, sin describir la indicación) |
| Nueva Indicación Predicha | Queratosis folicular invertida vulvar |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 10 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, prednicarbato es un corticosteroide tópico, y su eficacia antiinflamatoria en dermatosis inflamatorias está establecida.

Sin embargo, la queratosis folicular invertida es una lesión epitelial benigna que normalmente se maneja con escisión, por lo que no hay una justificación antiinflamatoria clara. No se encontraron ensayos ni literatura. El puntaje alto (99.88%) probablemente refleja un artefacto de proximidad en el grafo de conocimiento y no una relación biológica real.

Nota: entre las demás indicaciones predichas, las variantes de liquen plano (por ejemplo, liquen plano anular atrófico, nivel L4) tienen una base mecanística más plausible. Los corticosteroides tópicos son tratamiento de primera línea en liquen plano cutáneo. Aun así, solo hay un reporte de caso cuyo uso de prednicarbato no está confirmado.

## Informacion de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19975547 | SKINPRED® EMULSION GEL (EUROETIKA SAS) | Emulsión | PREDNICARBATO |
| 20033013 | PEITEL® 0.25 % CREMA (FERRER INTERNACIONAL S.A.) | Crema tópica | PREDNICARBATO |

Los datos de origen repiten cuatro veces el registro 19975547. Aquí se muestra una sola vez.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos ni literatura que respalden esta indicación (nivel L5). La lesión es benigna, se trata habitualmente con escisión y no hay un mecanismo antiinflamatorio claro. El puntaje alto del modelo es probablemente un artefacto del grafo.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA (advertencias y contraindicaciones), que hoy bloquea el tamizaje de seguridad.
- Obtener los datos del mecanismo de acción desde DrugBank.
- Revisión dermatológica para confirmar si esta predicción tiene algún sentido clínico.
- Priorizar la evaluación de las indicaciones de liquen plano (especialmente el liquen plano anular atrófico) como candidatas más plausibles.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

