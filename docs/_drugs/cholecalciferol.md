---
layout: default
title: Cholecalciferol
parent: Solo Predicción del Modelo (L5)
nav_order: 124
evidence_level: L5
indication_count: 7
---

# Cholecalciferol
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

# Colecalciferol: De Multivitamínicos y Minerales a Hipoparatiroidismo Aislado Familiar por Secreción Deficiente de PTH

## Resumen en Una Frase

El colecalciferol (vitamina D3) está registrado en Colombia como componente de productos multivitamínicos con minerales.
El modelo TxGNN predice que podría ser efectivo para **hipoparatiroidismo aislado familiar por secreción deficiente de PTH**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que es solo una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Multivitaminas y otros minerales, incluidas combinaciones |
| Nueva Indicación Predicha | Hipoparatiroidismo aislado familiar por secreción deficiente de PTH |
| Puntaje de Predicción TxGNN | 99.79% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, el colecalciferol es un precursor de la vitamina D que el organismo convierte en su forma activa (1,25-dihidroxivitamina D) mediante hidroxilaciones en hígado y riñón. Su papel en el equilibrio de calcio y fósforo está bien establecido, y por eso el modelo lo relaciona con un trastorno del calcio como el hipoparatiroidismo.

La relación entre la indicación original y la nueva es indirecta. Una es suplementación nutricional y la otra es una enfermedad genética rara con secreción insuficiente de hormona paratiroidea (PTH). Sin PTH, la activación renal de la vitamina D (1-alfa-hidroxilación) es muy limitada. Por eso el colecalciferol nativo es un sustituto pobre de los análogos activos de la vitamina D.

Por esta razón la aplicabilidad mecanística es dudosa. No se aportaron ensayos ni literatura que sustenten el vínculo, así que la predicción debe tratarse como una hipótesis por verificar.

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
| 19908281 | SUPRAVITAL (PROCAPS S.A.) | Cápsula blanda | Multivitaminas y otros minerales, incluidas combinaciones |

El resultado repetía el mismo registro cinco veces, por lo que se muestra una sola vez. Los 20 registros totales incluyen formas de cápsula blanda y tableta oral.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: solo hay una entrada, de tipo farmacológico y no de interacción clínica con otro medicamento. Indica que la vitamina D3 actúa como metabolito sobre el receptor X farnesoide-β (especie: ratón). No tiene nivel de gravedad asignado ni implicación clínica establecida.

Consultar el prospecto para el resto de la información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto (99.79%), pero no hay ensayos ni publicaciones que la respalden (L5). Además, el mecanismo va en contra de la hipótesis: sin PTH, el colecalciferol nativo no se activa bien y los análogos activos son la opción esperable.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (DrugBank).
- Advertencias y contraindicaciones del prospecto aprobado por INVIMA.
- Evidencia clínica o preclínica específica de colecalciferol en esta enfermedad, comparada con análogos activos de vitamina D.

**Nota sobre otras predicciones del mismo fármaco:** la enfermedad renal ósea (osteodistrofia renal) tiene mejor respaldo (L3, *Proceed with Guardrails*), con el ensayo NCT00285467 que compara colecalciferol con doxercalciferol. Raquitismo hipofosfatémico y acidosis tubular renal quedan en L4 (pregunta de investigación). Si se busca una dirección con mayor probabilidad de avanzar, conviene priorizar la osteodistrofia renal antes que esta.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

