---
layout: default
title: Obinutuzumab
parent: Solo Predicción del Modelo (L5)
nav_order: 298
evidence_level: L5
indication_count: 3
---

# Obinutuzumab
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

# Obinutuzumab: De Indicación No Especificada en el Registro a Leucemia Linfocítica Crónica/Linfoma Linfocítico de Células Pequeñas con Hipermutación Somática del Gen IGHV

## Resumen en Una Frase

Obinutuzumab es un anticuerpo monoclonal anti-CD20 comercializado en Colombia como Gazyva®. El registro sanitario disponible no detalla su indicación original, solo menciona el principio activo.
El modelo TxGNN predice que podría ser efectivo para **leucemia linfocítica crónica/linfoma linfocítico de células pequeñas (LLC/LLCP) con hipermutación somática del gen IGHV**.
Por ahora hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción para este subtipo específico.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el texto aprobado en el registro solo dice "OBINUTUZUMAB") |
| Nueva Indicación Predicha | LLC/LLCP con hipermutación somática del gen de la región variable de la cadena pesada de inmunoglobulina (IGHV) |
| Puntaje de Predicción TxGNN | 99.21% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 4 (las 4 filas corresponden al mismo número de registro, 20065694) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro de origen. Según la información conocida, obinutuzumab es un anticuerpo monoclonal anti-CD20 de tipo II, con glicoingeniería. Su mecanismo incluye muerte celular directa, citotoxicidad celular dependiente de anticuerpos y fagocitosis.

El CD20 se expresa en las células B de la LLC/LLCP. Por eso, mecanísticamente, un anticuerpo anti-CD20 podría ser aplicable a esta enfermedad, y la predicción es biológicamente plausible.

Sin embargo, no se recuperaron ensayos ni literatura para este subtipo molecular. Además, el puntaje es idéntico al del subtipo "LLC/LLCP pregerminal" (rank 2), lo que sugiere nodos solapados en la ontología y no señales independientes. Con los datos entregados, la predicción específica del subtipo no se puede verificar.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20065694 | GAZYVA® concentrado para solución para infusión, 1000 mg/vial 40 mL (F. Hoffmann-La Roche Ltd.) | Solución concentrada para infusión | Solo figura el principio activo: OBINUTUZUMAB |

Los 4 registros de la fuente son filas duplicadas del mismo número de registro, por lo que aquí se muestran una sola vez.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (anticuerpo monoclonal anti-CD20 con glicoingeniería) |
| Riesgo de Mielosupresión, Emetogenicidad, Monitoreo y Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

La consulta de interacciones farmacológicas no devolvió resultados. Esto no demuestra que no existan interacciones.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para este subtipo (puntaje 99.21%) es solo del modelo (nivel L5), sin ensayos ni publicaciones específicos. Además, faltan la indicación original, el mecanismo de acción y los datos de seguridad locales.

Otra predicción del mismo fármaco, el **linfoma folicular** (rank 3, puntaje 99.18%), sí tiene respaldo sólido. Incluye el ensayo de Fase 3 completado GALLIUM (NCT01332968, n=1401) y varios estudios de Fase 1/2 con combinaciones. Esa indicación podría ser un uso ya establecido y no un reposicionamiento real. Conviene evaluarla por separado y verificar su estado regulatorio en Colombia.

**Para avanzar se necesita:**
- Verificar si la LLC ya es una indicación aprobada en el prospecto de INVIMA, y así determinar si es reposicionamiento real.
- Descargar y revisar el prospecto de INVIMA (advertencias y contraindicaciones).
- Obtener el mecanismo de acción y la indicación original desde DrugBank.
- Buscar evidencia específica por subtipo IGHV (mutado o no mutado) en LLC/LLCP.
- Corregir la duplicación de registros sanitarios en la fuente de datos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

