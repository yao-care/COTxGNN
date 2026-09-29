---
layout: default
title: Diclofenac
parent: Solo Predicción del Modelo (L5)
nav_order: 162
evidence_level: L5
indication_count: 10
---

# Diclofenac
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Diclofenaco: De Analgésico Antiinflamatorio (AINE) a Hipotricosis Simple del Cuero Cabelludo

## Resumen en Una Frase

Diclofenaco es un antiinflamatorio no esteroideo (AINE), utilizado para tratar el dolor y la inflamación de la osteoartritis y la artritis reumatoide.
El modelo TxGNN predice que podría ser efectivo para **hipotricosis simple del cuero cabelludo**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción. Es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tramadol y diclofenaco (texto registrado en INVIMA; uso clínico general: dolor e inflamación) |
| Nueva Indicación Predicha | Hipotricosis simple del cuero cabelludo |
| Puntaje de Predicción TxGNN | 99.69% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Diclofenaco inhibe las enzimas COX-1 y COX-2 (ciclooxigenasas), lo que reduce la producción de prostaglandinas. Así alivia el dolor, la inflamación y la fiebre. Las bases de datos farmacológicas también lo asocian con otros blancos (TRPM3, PPARG, ASIC3 y el transportador SLC36A1). No hay una descripción detallada del mecanismo de acción en el registro.

**En este caso la predicción no parece razonable.** La hipotricosis simple es un trastorno hereditario del folículo piloso y no se conoce que la inhibición de COX influya en su vía. El puntaje alto de TxGNN (0.997) es solo una predicción y probablemente sea un artefacto del grafo de conocimiento.

La relación con la indicación original (dolor e inflamación) es débil. No hay similitud mecanística ni clínica que sustente el reposicionamiento.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Hay 20 registros sanitarios. Los 5 principales devueltos son idénticos, por lo que se muestran una sola vez:

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20220497 | DICASEN® 50/50 | Tableta (vía oral) | Tramadol y diclofenaco |

## Consideraciones de Seguridad

- **Blancos farmacológicos registrados** (no son interacciones con otros medicamentos): COX-1 (PTGS1), COX-2 (PTGS2), TRPM3, PPARG, ASIC3 y SLC36A1.

Consultar el prospecto para información sobre advertencias y contraindicaciones.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (L5), sin ensayos ni literatura, y no se identifica un vínculo mecanístico plausible con la hipotricosis simple.

**Nota sobre otras predicciones del mismo fármaco:** la única con evidencia real es la **artritis idiopática juvenil** (posición 9, puntaje 99.25%, nivel L3). Tiene 2 ensayos clínicos (un registro observacional de seguridad de AINE, terminado, y un ensayo de fase 2/3 con coenzima Q10 que no evalúa diclofenaco) y 18 publicaciones. Entre estas hay estudios pequeños de diclofenaco en artritis juvenil, como un ensayo cruzado de 1988 con naproxeno y tolmetina y un estudio abierto de 1983. Se trata más de un uso de clase de los AINE que de un reposicionamiento nuevo. Merece evaluarse como pregunta de investigación, no como candidato principal.

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de INVIMA (advertencias y contraindicaciones).
- Obtener datos detallados del mecanismo de acción desde DrugBank.
- Si se desea avanzar con artritis idiopática juvenil, revisar la seguridad pediátrica (gastrointestinal, renal, hepática y cardiovascular) y la preferencia actual por otros AINE.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

