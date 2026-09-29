---
layout: default
title: Oxybutynin
parent: Solo Predicción del Modelo (L5)
nav_order: 310
evidence_level: L5
indication_count: 3
---

# Oxybutynin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Oxibutinina: De Vejiga Hiperactiva a Síndrome de Piernas Inquietas

## Resumen en Una Frase

La oxibutinina es un antimuscarínico que se usa para tratar la vejiga hiperactiva.
El modelo TxGNN predice que podría ser efectiva para el **síndrome de piernas inquietas**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción, y el mecanismo propuesto es dudoso.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Vejiga hiperactiva (según el uso clínico en los datos farmacológicos; el texto del registro INVIMA solo dice «OXIBUTININA») |
| Nueva Indicación Predicha | Síndrome de piernas inquietas |
| Puntaje de Predicción TxGNN | 99.74% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente principal. Según la información conocida, la oxibutinina es un antagonista muscarínico que actúa sobre los receptores M1 a M5 (genes CHRM1 a CHRM5) y tiene además un efecto antiespasmódico directo sobre el músculo liso. Su eficacia en la vejiga hiperactiva está establecida.

En este caso **no hay un vínculo mecanístico plausible** con el síndrome de piernas inquietas. Esta enfermedad se relaciona con las vías dopaminérgica y del hierro, y la oxibutinina no actúa sobre ninguna de las dos. Además, los anticolinérgicos sedantes pueden empeorar los síntomas, por lo que la dirección del efecto es incierta y posiblemente adversa. El puntaje tan alto probablemente refleja artefactos de la topología del grafo y no una relación farmacológica real.

El modelo también predijo la gastroduodenitis (99.62%) y la enfermedad ulcerosa péptica (99.31%). El efecto antisecretor y antiespasmódico podría ser plausible en teoría, pero hoy los inhibidores de la bomba de protones y la erradicación de *H. pylori* hacen poco competitiva a la oxibutinina. Además, hay un reporte de que causa esofagitis por reflujo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20099350 | SINORIN® (QUIRUPOS LTDA) | Tableta cubierta con película | OXIBUTININA (el registro no detalla la indicación) |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos ni literatura. No existe un mecanismo plausible, y el efecto anticolinérgico sedante podría empeorar el síndrome de piernas inquietas.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA para completar advertencias y contraindicaciones (brecha bloqueante).
- Completar el mecanismo de acción desde DrugBank.
- Realizar una búsqueda dirigida de literatura y ensayos sobre anticolinérgicos y síndrome de piernas inquietas, para confirmar si el efecto es adverso.
- Si se quiere explorar otra indicación, priorizar la enfermedad ulcerosa péptica solo como análisis de seguridad. Allí la evidencia es histórica (nivel L4) y hay señal de reflujo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

