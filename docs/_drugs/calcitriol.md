---
layout: default
title: Calcitriol
parent: Solo Predicción del Modelo (L5)
nav_order: 107
evidence_level: L5
indication_count: 7
---

# Calcitriol
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

# Calcitriol: De Indicación No Especificada a Deficiencia de Vitamina D (término obsoleto)

## Resumen en Una Frase

Calcitriol es la forma activa de la vitamina D (1,25-dihidroxivitamina D3). En Colombia está registrado como cápsula blanda de 0,25 mcg, pero el registro sanitario no detalla su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **deficiencia de vitamina D**, un término que la ontología marca como **obsoleto**.
Actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción específica; se trata solo de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro solo dice «CALCITRIOL») |
| Nueva Indicación Predicha | Deficiencia de vitamina D (término obsoleto) |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 7 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Calcitriol es la forma hormonal activa de la vitamina D, así que una relación con la deficiencia de vitamina D es biológicamente plausible.

Sin embargo, el puntaje alto (99.96%) es solo una predicción basada en el grafo de conocimiento. Además, el término de la enfermedad está marcado como obsoleto, lo que sugiere un artefacto de mapeo de vocabulario y no una hipótesis clínica nueva. No se aportaron ensayos ni literatura, y el texto de indicación registrado en Colombia no permite comparar con la indicación original. Por estas razones la predicción debe tomarse con cautela.

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
| 19934690 | CALCITRIOL 0.25 MCG CAPSULA BLANDA (COLMED LTDA) | Cápsula blanda | Solo figura «CALCITRIOL», sin indicación detallada |

Nota: el sistema reporta 7 registros en total, pero las entradas recibidas corresponden todas al mismo registro 19934690 (repetido), por lo que se muestra una sola fila.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para esta indicación no hay ensayos ni literatura (nivel L5), y el término de la enfermedad es obsoleto, por lo que el puntaje alto del modelo no basta para avanzar.

**Para avanzar se necesita:**
- Reemplazar el término obsoleto por la entidad vigente (por ejemplo, deficiencia de vitamina D actual) y volver a evaluar la predicción.
- Obtener el prospecto de INVIMA para conocer indicación aprobada, advertencias y contraindicaciones.
- Completar los datos del mecanismo de acción desde DrugBank.
- Considerar otras predicciones del mismo paquete que tienen más respaldo. La más avanzada es **raquitismo hipofosfatémico hereditario**: 6 ensayos relacionados, nivel L2 y recomendación *Proceed with Guardrails*. Los ensayos más relevantes son NCT03748966 (calcitriol en monoterapia en XLH) y NCT03820518 (Fase 4, comparación de dosis), sin resultados publicados en el paquete. Con esa indicación se recomienda vigilar hipercalciuria, nefrocalcinosis e hiperparatiroidismo. La predicción de **acidosis tubular renal** tiene solo evidencia indirecta (L4): reportes de casos y estudios fisiológicos, uno de los cuales indica que no altera el calcitriol circulante.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

