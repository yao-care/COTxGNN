---
layout: default
title: Flutamide
parent: Solo Predicción del Modelo (L5)
nav_order: 202
evidence_level: L5
indication_count: 10
---

# Flutamide
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

# Flutamida: De Indicación No Especificada en el Registro a Susceptibilidad a Cáncer de Próstata/Cerebro

## Resumen en Una Frase

Flutamida es un antiandrógeno oral que actúa sobre el receptor de andrógenos y se usa en cáncer de próstata localmente confinado o metastásico. El registro sanitario colombiano solo menciona el nombre del principio activo, sin describir la indicación.
El modelo TxGNN predice que podría ser efectiva para **susceptibilidad a cáncer de próstata/cerebro**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción específica.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el texto del registro solo dice «FLUTAMIDA») |
| Nueva Indicación Predicha | Susceptibilidad a cáncer de próstata/cerebro |
| Puntaje de Predicción TxGNN | 99,98 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 6 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha del fármaco. Según los datos farmacológicos disponibles, flutamida es un antagonista del receptor de andrógenos (gen *AR*). Su uso clínico documentado es el cáncer de próstata localmente confinado o metastásico. Mecanísticamente, el bloqueo de andrógenos es plausible para el cáncer de próstata.

El problema está en la etiqueta predicha. «Susceptibilidad» es un concepto de riesgo genético, no una enfermedad tratable. La parte «cáncer cerebral» no tiene un vínculo mecanístico identificado con el bloqueo androgénico. El puntaje alto de TxGNN es solo una predicción del modelo, sin ensayos ni literatura que la sostengan.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 35440 | ETACONIL DE 250 MG COMPRIMIDOS (ASOFARMA DE MEXICO S.A. DE C.V.) | Tableta | Solo figura «FLUTAMIDA», sin texto de indicación |

El pack contiene entradas repetidas del mismo registro 35440, por lo que aquí se muestra una sola vez.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia hormonal (antiandrógeno no esteroideo), no citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Función hepática (prioritaria); además hemograma y función renal según el prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Advertencias Principales**: hepatotoxicidad con advertencia en recuadro, según la nota de racionalidad del pack. Falta confirmarla con el prospecto de INVIMA.
- **Interacciones Farmacológicas**: la consulta se completó, pero solo devolvió el receptor de andrógenos como blanco farmacológico. No hay interacciones con otros fármacos listadas.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación predicha es un concepto de riesgo genético, no una enfermedad tratable. No tiene ensayos ni literatura propios (nivel L5, etapa S0), y el puntaje alto del modelo no basta por sí solo.

Otras predicciones del mismo fármaco merecen revisión aparte:
- **Cáncer de órganos reproductivos masculinos** (rank 6): nivel L2, con un ensayo Fase 2 aleatorizado que incluye flutamida (NCT00450463). Probablemente corresponde a una indicación ya vigente, es decir, confirmación de uso existente y no reposicionamiento.
- **Neoplasia benigna del sistema reproductivo** (rank 4): nivel L3, solo estudios pequeños y antiguos.

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de INVIMA (advertencias, contraindicaciones, indicación aprobada real del registro 35440)
- Completar el mecanismo de acción desde DrugBank
- Aclarar la definición de «susceptibilidad a cáncer de próstata/cerebro» o priorizar las predicciones con evidencia real
- Definir un plan de monitoreo hepático si se avanza con cualquier indicación
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

