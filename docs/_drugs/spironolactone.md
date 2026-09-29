---
layout: default
title: Spironolactone
parent: Solo Predicción del Modelo (L5)
nav_order: 362
evidence_level: L5
indication_count: 2
---

# Spironolactone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Espironolactona: De Hipertensión y Trastornos por Exceso de Aldosterona a Hipotricosis Simple del Cuero Cabelludo

## Resumen en Una Frase

La espironolactona es un antagonista del receptor de mineralocorticoides, usado clásicamente para la hipertensión de renina baja, la hipopotasemia, el síndrome de Conn y la insuficiencia cardiaca.
El modelo TxGNN predice que podría ser efectiva para la **hipotricosis simple del cuero cabelludo**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es solo una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro sanitario (el texto solo dice "Espironolactona"). Uso clínico conocido: hipertensión de renina baja, hipopotasemia, síndrome de Conn e insuficiencia cardiaca |
| Nueva Indicación Predicha | Hipotricosis simple del cuero cabelludo |
| Puntaje de Predicción TxGNN | 99.26% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados del mecanismo de acción en el paquete de evidencia. Sí se sabe que la espironolactona actúa sobre el receptor de mineralocorticoides (gen NR3C2). En general se le reconoce además una actividad antiandrogénica, por la que se usa fuera de indicación en la pérdida de cabello de origen androgénico.

Esa lógica no se traslada con claridad a la hipotricosis simple, que es un trastorno hereditario del crecimiento del cabello. Los datos disponibles no muestran que sea de origen androgénico. El vínculo es especulativo y se apoya solo en el puntaje del grafo de conocimiento de TxGNN (0.993). Es un puntaje alto, pero sigue siendo una predicción computacional y no evidencia clínica.

TxGNN también predijo la **hipotricosis congénita con milia** (puntaje 99.04%, nivel L5). Aquí el razonamiento antiandrogénico tampoco tiene relevancia demostrada. El puntaje podría reflejar en parte la similitud con otras entidades de hipotricosis en el grafo, más que un mecanismo específico entre fármaco y enfermedad.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Se reportan 20 registros sanitarios. En los datos recibidos solo aparece un registro distinto, repetido varias veces:

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19933407 | DOXICLAT® TABLETA (PHARMADERM S.A.) | Tableta (oral) | Solo figura "Espironolactona", sin indicación detallada |

El nombre comercial del producto no coincide con el principio activo listado. Conviene verificar este dato en INVIMA.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

La consulta de interacciones devolvió únicamente el receptor de mineralocorticoides como diana farmacológica, no interacciones con otros fármacos.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni publicaciones que respalden el uso en hipotricosis simple del cuero cabelludo (nivel L5). El mecanismo propuesto no está demostrado para una condición hereditaria y solo se sostiene en el puntaje del modelo.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), que es un vacío bloqueante para el tamizaje de seguridad
- Completar el mecanismo de acción desde DrugBank
- Revisar la literatura sobre espironolactona en hipotricosis hereditarias y su base genética, para confirmar si existe un vínculo mecanístico real
- Confirmar la indicación aprobada y la identidad del producto en el registro 19933407
- Evaluar la compatibilidad de la vía de administración (oral frente a la tópica que suele usarse en el cabello)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

