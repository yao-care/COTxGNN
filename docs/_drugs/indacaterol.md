---
layout: default
title: Indacaterol
parent: Solo Predicción del Modelo (L5)
nav_order: 221
evidence_level: L5
indication_count: 10
---

# Indacaterol
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

# Indacaterol: De Indicación Original No Especificada a Síndrome Nefrogénico de Antidiuresis Inapropiada

## Resumen en Una Frase

Indacaterol es un agonista beta2 de acción ultra-prolongada, utilizado en enfermedades obstructivas de las vías respiratorias. En Colombia se comercializa dentro de una combinación inhalada con mometasona. El modelo TxGNN predice que podría ser efectivo para el **síndrome nefrogénico de antidiuresis inapropiada**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | FORMOTEROL Y MOMETASONA (texto tal como figura en el registro INVIMA; no describe con claridad una indicación) |
| Nueva Indicación Predicha | Síndrome nefrogénico de antidiuresis inapropiada |
| Puntaje de Predicción TxGNN | 99.54% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, indacaterol es un agonista beta2-adrenérgico de acción ultra-prolongada que relaja el músculo liso de las vías respiratorias y produce broncodilatación sostenida. Su uso está establecido en la enfermedad pulmonar obstructiva crónica (EPOC) y en combinaciones fijas para asma.

**Con la evidencia disponible, la predicción no parece razonable desde el punto de vista mecanístico.** El síndrome nefrogénico de antidiuresis inapropiada surge de variantes con ganancia de función del receptor V2 de la vasopresina (AVPR2), una vía distinta de la señalización beta2-adrenérgica. No se identificó ningún vínculo entre ambas.

El puntaje alto de TxGNN refleja una asociación en el grafo de conocimiento, sin respaldo clínico ni bibliográfico. Debe leerse como una hipótesis computacional, no como una señal de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20209060 | ATECTURA® BREEZHALER® 150/80 MCG polvo para inhalación cápsula dura (Novartis Pharma AG) | Cápsula dura | FORMOTEROL Y MOMETASONA |

Nota: los 5 registros listados en el paquete de evidencia son idénticos (mismo número, producto e indicación), por lo que se muestran una sola vez. El total reportado es de 20 registros.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5), sin ensayos ni publicaciones, y no existe un vínculo mecanístico plausible entre la agonía beta2 y la ganancia de función de AVPR2. No hay base para avanzar.

**Para avanzar se necesita:**
- Un vínculo mecanístico creíble, apoyado en estudios preclínicos o de mecanismo, entre la vía beta2-adrenérgica y la vía de AVPR2
- Confirmar la indicación original en el prospecto de INVIMA, ya que el texto del registro solo menciona "formoterol y mometasona"
- Datos de mecanismo de acción, advertencias y contraindicaciones desde DrugBank e INVIMA

**Observación complementaria:** dentro de las predicciones del mismo paquete, "enfermedad bronquial" (posición 7) tiene evidencia L1 y recomendación "Proceed with Guardrails". Sin embargo, corresponde a un uso en asma y EPOC que es esencialmente el uso habitual del fármaco, no un reposicionamiento nuevo. Si se desea una evaluación completa de esa indicación, conviene generar un informe separado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

