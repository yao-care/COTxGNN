---
layout: default
title: Leflunomide
parent: Solo Predicción del Modelo (L5)
nav_order: 246
evidence_level: L5
indication_count: 2
---

# Leflunomide
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

# Leflunomida: De Artritis Reumatoide a Síndrome de Braquidactilia-Sindactilia

## Resumen en Una Frase

Leflunomida es un inmunomodulador oral que se usa para tratar la artritis reumatoide activa y prevenir el rechazo de trasplantes de órganos.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de braquidactilia-sindactilia**, una malformación congénita de las extremidades, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.
Además, el mecanismo del fármaco sugiere que el efecto podría ser perjudicial y no terapéutico.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Artritis reumatoide (según la ficha farmacológica; el registro INVIMA solo lista el principio activo "leflunomida") |
| Nueva Indicación Predicha | Síndrome de braquidactilia-sindactilia |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 14 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Por conocimiento general de farmacología, la leflunomida se convierte en su metabolito activo, teriflunomida, que inhibe la enzima DHODH (dihidroorotato deshidrogenasa). Esta enzima es clave en la síntesis de pirimidinas, y su inhibición frena la proliferación de linfocitos activados. Por eso el fármaco es eficaz en enfermedades autoinmunes como la artritis reumatoide. Esta información no fue verificada contra fuentes primarias.

**No se encontró un vínculo mecanístico que respalde la predicción.** El síndrome de braquidactilia-sindactilia es una malformación congénita de las extremidades. No hay una razón para que un efecto inmunomodulador o antiproliferativo posnatal revierta defectos estructurales del desarrollo. El puntaje de 0.999 es una predicción de un grafo de conocimiento y no constituye evidencia clínica.

Además, la dirección del efecto podría ser contraria a la esperada. La leflunomida es un teratógeno conocido y su uso está contraindicado en el embarazo. La pérdida de función de DHODH causa malformaciones de las extremidades (síndrome de Miller). Por lo tanto, la inhibición de esta vía es más probable que dañe el desarrollo de las extremidades que que lo corrija.

La segunda predicción del modelo, el síndrome de microftalmia colobomatosa con displasia rizomélica (puntaje 99.93%), tiene el mismo problema. Es un síndrome congénito del desarrollo, también sin evidencia clínica ni vínculo mecanístico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Hay 14 registros sanitarios en total. Se muestran los principales, sin duplicados:

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20127508 | ZORATOMIN® 20 MG TABLETAS RECUBIERTAS (HB Human Bioscience S.A.S.) | Tableta recubierta | El registro solo indica el principio activo (leflunomida) |
| 20152814 | LEFLUNOMIDA 20 MG TABLETA RECUBIERTA (Clínicos y Hospitalarios de Colombia S.A.S.) | Tableta recubierta | El registro solo indica el principio activo (leflunomida) |
| 230658 | ARAVA® TABLETAS RECUBIERTAS 20 MG (Sanofi-Aventis de Colombia S.A.) | Tableta recubierta | El registro solo indica el principio activo (leflunomida) |

## Consideraciones de Seguridad

- **Teratogenicidad**: el análisis del paquete de evidencia señala que la leflunomida es un teratógeno conocido y está contraindicada en el embarazo. Esto es conocimiento farmacológico general, no verificado contra el prospecto de INVIMA. Es especialmente relevante para cualquier indicación de tipo congénito o del desarrollo.

Para el resto de la información de seguridad (advertencias, contraindicaciones e interacciones medicamentosas), consultar el prospecto. No se dispone del prospecto de INVIMA.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (L5), sin ensayos ni publicaciones. Los datos farmacológicos disponibles indican que la inhibición de DHODH y la teratogenicidad de la leflunomida podrían empeorar, y no mejorar, una malformación congénita de las extremidades.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), que actualmente bloquea el tamizaje de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Revisar la literatura sobre DHODH y malformaciones de las extremidades para confirmar o descartar la dirección del efecto.
- Reevaluar solo si aparece un vínculo mecanístico y evidencia que respalden un efecto terapéutico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

