---
layout: default
title: Mirtazapine
parent: Solo Predicción del Modelo (L5)
nav_order: 287
evidence_level: L5
indication_count: 3
---

# Mirtazapine
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

# Mirtazapina: De Trastorno Depresivo Mayor a Síndrome de Ohdo y Variantes

## Resumen en Una Frase

La mirtazapina es un antidepresivo que se usa para el trastorno depresivo mayor. El modelo TxGNN predice que podría ser efectiva para el **síndrome de Ohdo y variantes**, pero hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción. Es solo una señal del modelo, sin evidencia real, y no tiene un vínculo mecanístico plausible.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trastorno depresivo mayor (según la referencia farmacológica; el texto de los registros sanitarios solo dice «Mirtazapina» y no detalla la indicación) |
| Nueva Indicación Predicha | Síndrome de Ohdo y variantes |
| Puntaje de Predicción TxGNN | 99.42% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según los datos farmacológicos disponibles, la mirtazapina tiene la mayor afinidad por los adrenorreceptores α2 (α2A > α2C > α2B) y por los receptores serotoninérgicos 5-HT2A y 5-HT2C. Su eficacia en el trastorno depresivo mayor es conocida, y a veces se combina con ISRS o IRSN en depresión grave.

**No se identificó un vínculo mecanístico que respalde la predicción.** El síndrome de Ohdo (relacionado con KAT6B, regulación epigenética y de la cromatina) no tiene una conexión conocida con la vía adrenérgica/serotoninérgica. Es un síndrome congénito raro del neurodesarrollo, sin un blanco sintomático plausible para este fármaco. El puntaje de 99.42% es solo una salida del modelo.

Las otras dos predicciones tampoco tienen respaldo:
- **Síndrome de blefarofimosis con discapacidad intelectual, tipo Ohdo** (99.11%): es casi con certeza un nodo duplicado de la primera predicción, así que no cuenta como señal independiente.
- **Tortícolis paroxística benigna de la infancia** (99.11%): el vínculo es solo especulativo, porque se la considera un equivalente migrañoso y algunos agentes serotoninérgicos o antihistamínicos se usan en la profilaxis de la migraña. No hay evidencia para la mirtazapina. Además, usar un antidepresivo sedante en lactantes requeriría una justificación de seguridad muy sólida, y el trastorno se resuelve solo con el tiempo.

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
| 20165068 | AUROZAPINE OD 30 MG TABLETAS ORODISPERSABLES | Tableta orodispersable | Mirtazapina (sin detalle de indicación) |
| 19928993 | MIRTAPAX ® | Tableta recubierta | Mirtazapina (sin detalle de indicación) |

*Se muestran los registros únicos; los demás registros del listado repiten estos números. En total hay 20 registros sanitarios.*

---

## Consideraciones de Seguridad

- **Perfil de receptores (no son interacciones con otros fármacos):** la mirtazapina se une a los receptores 5-HT2A, 5-HT2C, α2A, α2B y α2C humanos. La referencia farmacológica indica que a veces se combina con un ISRS o un IRSN en depresión grave, por lo que conviene vigilar el efecto aditivo serotoninérgico y adrenérgico en cualquier combinación.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- La predicción se basa solo en el modelo (nivel L5), sin ensayos ni publicaciones, y no hay un vínculo mecanístico plausible entre la mirtazapina y el síndrome de Ohdo.
- Las tres predicciones son débiles, y dos de ellas parecen ser el mismo nodo duplicado.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones), ya que su ausencia impide la evaluación de seguridad inicial.
- Completar los datos del mecanismo de acción (por ejemplo, consultando DrugBank) para poder analizar un posible vínculo mecanístico.
- Encontrar alguna evidencia preclínica o clínica que conecte la mirtazapina con la vía de KAT6B o con los síntomas del síndrome de Ohdo.
- Aclarar la indicación aprobada en los registros, que hoy solo repiten el nombre del principio activo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

