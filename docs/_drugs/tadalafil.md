---
layout: default
title: Tadalafil
parent: Solo Predicción del Modelo (L5)
nav_order: 371
evidence_level: L5
indication_count: 8
---

# Tadalafil
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

# Tadalafilo: De Indicación No Especificada en el Registro a Hipertricosis Universal Congénita Tipo Ambras

## Resumen en Una Frase

Tadalafilo es un inhibidor de la fosfodiesterasa 5 (PDE5) comercializado en Colombia, pero el registro sanitario disponible no detalla su indicación original.
El modelo TxGNN predice que podría ser efectivo para la **hipertricosis universal congénita tipo Ambras**,
con **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que es solo una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el texto del registro solo dice «TADALAFIL») |
| Nueva Indicación Predicha | Hipertricosis universal congénita tipo Ambras |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, el tadalafilo es un inhibidor de PDE5 que actúa sobre la vía del GMP cíclico (cGMP).

**No se identificó un mecanismo plausible.** El síndrome de Ambras es una condición congénita ligada a reordenamientos cromosómicos cerca de la región del gen *TRPS1* (efecto de posición). El tadalafilo no tiene acción conocida sobre los genes que regulan el desarrollo del folículo piloso.

El puntaje alto de TxGNN (0.9998) proviene solo de asociaciones en el grafo de conocimiento y no está respaldado por evidencia clínica ni bibliográfica. Debe interpretarse con cautela.

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
| 20007296 | CIALIS® 5 MG (ELI LILLY AND COMPANY) | Tableta recubierta | Solo figura el principio activo: TADALAFIL |

Nota: el paquete de evidencia informa 20 registros en total, pero las entradas entregadas corresponden todas al mismo registro sanitario (20007296), por lo que se muestra una sola vez. La única vía de administración registrada es la oral.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos ni publicaciones para esta indicación, y no existe un mecanismo plausible que conecte la inhibición de PDE5 con un defecto genético del desarrollo del folículo piloso. La predicción parece un artefacto del grafo de conocimiento y no justifica avanzar.

Las otras siete predicciones del modelo tampoco tienen respaldo clínico y quedan en Hold. En migraña con aura del tronco encefálico hay un solo reporte de caso (PMID 17059442, 2006), y sugiere que el tadalafilo podría desencadenar aura, no tratarla. Esto amerita una revisión de señales de seguridad.

**Para avanzar se necesita:**
- Obtener del prospecto de INVIMA las advertencias y contraindicaciones, que hoy son un vacío bloqueante para el tamizaje de seguridad.
- Confirmar la indicación original aprobada en Colombia, porque el registro solo lista el principio activo.
- Completar los datos del mecanismo de acción (por ejemplo, desde DrugBank).
- Buscar evidencia preclínica o clínica que vincule la vía PDE5/cGMP con la biología del folículo piloso o con *TRPS1*. Sin ella, no se justifica continuar con esta indicación.
- Priorizar la revisión de la señal de seguridad de migraña con aura antes de considerar cualquier otra indicación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

