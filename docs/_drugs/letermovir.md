---
layout: default
title: Letermovir
parent: Solo Predicción del Modelo (L5)
nav_order: 249
evidence_level: L5
indication_count: 1
---

# Letermovir
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Letermovir: De Infección por Citomegalovirus (CMV) a Candidiasis Vulvovaginal

## Resumen en Una Frase

Letermovir es un antiviral que actúa contra el citomegalovirus humano (CMV). Está comercializado en Colombia como PREVYMIS 240 mg tabletas. El modelo TxGNN predice que podría ser efectivo para **candidiasis vulvovaginal**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, y no se identificó un vínculo mecanístico creíble.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto solo repite "LETERMOVIR"); por su mecanismo, antiviral contra CMV |
| Nueva Indicación Predicha | Candidiasis vulvovaginal |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 2 (ambos con el mismo número, 20194849) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Letermovir inhibe el complejo terminasa del ADN del CMV (pUL56/pUL89/pUL51), una pieza esencial para empaquetar el genoma viral. Este complejo no tiene homólogo fúngico conocido, y letermovir no tiene actividad antifúngica establecida contra *Candida*.

Por eso la relación entre la indicación original (una infección viral) y la nueva (una infección fúngica de la mucosa vaginal) no es clara. El puntaje de 99.88% (posición 1453 en el ranking del modelo) proviene solo del grafo de conocimiento. Probablemente refleja asociaciones indirectas, como poblaciones de pacientes en común (receptores de trasplante propensos a infecciones oportunistas), y no un efecto farmacológico directo sobre *Candida*.

Además, el mecanismo de acción no está documentado en los datos de entrada, así que la predicción no se puede contrastar con un mecanismo registrado. La compatibilidad de vía de administración (oral frente a la vía requerida para esta indicación) tampoco está evaluada.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20194849 | PREVYMIS 240MG TABLETAS (MERCK SHARP & DOHME LLC) | Tableta | LETERMOVIR (el registro no detalla la indicación) |

El registro aparece duplicado en los datos, por eso se cuentan 2 registros con el mismo número.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas en la consulta realizada.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5), sin ensayos ni literatura, y no hay un mecanismo plausible que conecte la inhibición de la terminasa del CMV con la candidiasis. Con estos datos no se justifica avanzar.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA para completar advertencias y contraindicaciones (brecha bloqueante para el tamizaje de seguridad)
- Completar el mecanismo de acción desde DrugBank
- Buscar evidencia preclínica de actividad antifúngica in vitro de letermovir contra *Candida*
- Evaluar la compatibilidad de vía de administración (la presentación local es solo oral en tabletas)
- Reevaluar la decisión solo si aparece evidencia real que respalde la hipótesis
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

