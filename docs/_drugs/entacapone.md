---
layout: default
title: Entacapone
parent: Solo Predicción del Modelo (L5)
nav_order: 178
evidence_level: L5
indication_count: 10
---

# Entacapone
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

# Entacapona: De Terapia Adyuvante con Levodopa a Neurodegeneración Asociada a PLA2G6

## Resumen en Una Frase

Entacapona es un inhibidor periférico de la COMT que prolonga la acción de la levodopa. En Colombia figura en un registro de una combinación con levodopa e inhibidor de descarboxilasa (uso en enfermedad de Parkinson).
El modelo TxGNN predice que podría ser efectiva para **neurodegeneración asociada a PLA2G6**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Levodopa e inhibidor de descarboxilasa (texto del registro INVIMA) |
| Nueva Indicación Predicha | Neurodegeneración asociada a PLA2G6 |
| Puntaje de Predicción TxGNN | 99.76% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, la entacapona es un inhibidor periférico de la COMT (catecol-O-metiltransferasa). Al bloquear la degradación periférica de la levodopa, prolonga su efecto. Por eso se usa como complemento de la levodopa en la enfermedad de Parkinson.

La enfermedad asociada a PLA2G6 puede incluir distonía-parkinsonismo (PARK14). Por eso es concebible un fundamento dopaminérgico **sintomático**: la entacapona podría ayudar con los síntomas parkinsonianos si el paciente recibe levodopa. Sin embargo, no modificaría el defecto de fondo, que afecta el metabolismo de fosfolípidos y el remodelado de membranas.

La predicción se apoya solo en el modelo. No se recuperaron ensayos ni literatura para esta indicación. El puntaje alto de TxGNN debe interpretarse con cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Los 5 registros devueltos corresponden al mismo número de registro sanitario (20147960), por lo que se muestra una sola vez.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20147960 | LEVOCAPONE 50/12.5/200 TABLETA RECUBIERTA (HUMAX PHARMACEUTICAL S.A.) | Tableta recubierta (vía oral) | Levodopa e inhibidor de descarboxilasa |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5), sin ensayos ni literatura. El fundamento mecanístico se limita al alivio sintomático del parkinsonismo y no aborda la causa de la enfermedad.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (DrugBank) y del prospecto de INVIMA (advertencias y contraindicaciones).
- Revisión de casos o series clínicas de parkinsonismo/distonía en pacientes con mutaciones PLA2G6 tratados con levodopa y entacapona.
- Priorizar otras predicciones del mismo fármaco con mejor respaldo indirecto: la **demencia con cuerpos de Lewy** (L4, con estudios in vitro y de modelos celulares) y el **parkinsonismo juvenil** (racional biológico plausible, sin evidencia específica).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

