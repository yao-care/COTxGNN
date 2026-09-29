---
layout: default
title: Atezolizumab
parent: Solo Predicción del Modelo (L5)
nav_order: 61
evidence_level: L5
indication_count: 10
---

# Atezolizumab
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

# Atezolizumab: De Indicación Original No Especificada en el Registro a Carcinoma Urotelial de la Uretra Prostática

## Resumen en Una Frase

Atezolizumab es un anticuerpo monoclonal que bloquea PD-L1 y se comercializa en Colombia como TECENTRIQ®. El registro sanitario solo indica el nombre del principio activo y no describe la indicación original.
El modelo TxGNN predice que podría ser efectivo para el **carcinoma urotelial de la uretra prostática**, con **2 ensayos clínicos** y **ninguna publicación** que respalden esta dirección. Los ensayos incluyen poblaciones de vejiga y urotelio en general, no este sitio específico.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el texto del registro solo dice "ATEZOLIZUMAB") |
| Nueva Indicación Predicha | Carcinoma urotelial de la uretra prostática |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L2 (un ensayo de Fase 2 completado, no aleatorizado y en población de vejiga) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 9 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Atezolizumab bloquea la unión de PD-L1 con PD-1 y con B7.1, lo que restablece la actividad de los linfocitos T contra el tumor. No se dispone de datos de mecanismo de acción provenientes de DrugBank, por lo que esta descripción se basa en el análisis mecanístico del propio paquete de evidencia.

El carcinoma urotelial suele expresar PD-L1 y es un tipo de tumor reconocido como sensible a la inmunoterapia. La uretra prostática está revestida por urotelio, así que el mecanismo debería ser trasladable desde la vejiga.

Como la indicación original no aparece en el registro, no se puede evaluar la relación con ella. Además, los ensayos disponibles incluyeron poblaciones de vejiga o urotelio en general, no la uretra prostática en particular. La plausibilidad es biológica y aún no está demostrada en este sitio.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02844816](https://clinicaltrials.gov/study/NCT02844816) | Fase 2 | Completado | 172 | Atezolizumab en cáncer de vejiga no músculo-invasivo sin respuesta a BCG. Es evidencia en el mismo linaje urotelial, pero en vejiga y no en uretra prostática. |
| [NCT03170960](https://clinicaltrials.gov/study/NCT03170960) | Fase 1 | Activo, sin reclutar | 914 | Cabozantinib solo o con atezolizumab en tumores sólidos, con cohortes de carcinoma urotelial (incluida la uretra). Es un estudio de combinación en fase temprana y sin datos específicos de esta indicación. |

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20145962 | TECENTRIQ® (F. Hoffmann-La Roche Ltd.) | Solución inyectable | Solo figura "ATEZOLIZUMAB" |

Los datos muestran 9 registros en total, pero las entradas recibidas repiten el mismo número (20145962), por lo que se presenta una sola fila.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (inhibidor de PD-L1) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Hay un ensayo de Fase 2 completado en cáncer de vejiga y un mecanismo plausible, pero ningún dato específico de uretra prostática. Tampoco hay literatura ni información de seguridad del prospecto local, lo que impide avanzar al tamizaje de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones).
- Consultar el mecanismo de acción en DrugBank.
- Buscar literatura y datos de subgrupos de uretra prostática en los estudios en urotelio, incluido NCT02844816.
- Confirmar la indicación original aprobada en Colombia y los 9 registros sanitarios.
- Evaluar si los datos de vejiga pueden extrapolarse a la uretra prostática.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

