---
layout: default
title: Cetuximab
parent: Solo Predicción del Modelo (L5)
nav_order: 121
evidence_level: L5
indication_count: 10
---

# Cetuximab
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

# Cetuximab: De Indicación Original No Registrada a Hamartoma Condroide

## Resumen en Una Frase

Cetuximab es un anticuerpo monoclonal dirigido contra el receptor del factor de crecimiento epidérmico (EGFR). El registro sanitario colombiano no consigna una indicación original explícita.
El modelo TxGNN predice que podría ser efectivo para **hamartoma condroide** (una lesión benigna), pero hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro solo consigna «CETUXIMAB» como texto de indicación) |
| Nueva Indicación Predicha | Hamartoma condroide |
| Puntaje de Predicción TxGNN | 99.95% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 10 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, cetuximab es un anticuerpo anti-EGFR, y los ensayos recuperados para otras predicciones lo muestran en cáncer colorrectal y de cabeza y cuello. Mecanísticamente, su aplicación a hamartoma condroide no tiene sustento documentado.

El hamartoma condroide es una lesión benigna sin dependencia conocida de EGFR. Por eso el puntaje alto del modelo (99.95%) no basta por sí solo para justificar una acción. Tampoco hay una indicación original clara con la cual medir la similitud entre indicaciones.

En esta predicción no se recuperó ningún ensayo ni publicación, así que no existe evidencia real que confirme ni descarte el vínculo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Todos los registros recuperados corresponden al mismo número de registro sanitario, por lo que se muestra una sola vez.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19953428 | ERBITUX® 5 MG/ML (Merck S.A.) | Solución inyectable | CETUXIMAB (el registro no detalla la indicación) |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (anticuerpo monoclonal anti-EGFR) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Baja (según la categoría del fármaco) |
| Items de Monitoreo | Hemograma, función hepática y renal, electrolitos. La literatura recuperada para otras predicciones menciona reacciones a la infusión, hipersensibilidad y toxicidad cutánea |
| Protección en Manejo | Consultar el prospecto y las regulaciones locales de manejo de fármacos antineoplásicos |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5): no hay ensayos ni literatura, y no se conoce un mecanismo mediado por EGFR en una lesión benigna como el hamartoma condroide. Además, el registro colombiano no aclara la indicación original, lo que impide evaluar la similitud entre indicaciones.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA (advertencias y contraindicaciones) y la indicación aprobada real.
- Obtener el mecanismo de acción desde DrugBank.
- Realizar una búsqueda dirigida de literatura sobre hamartoma condroide y EGFR.
- Considerar priorizar otras predicciones del mismo paquete con más respaldo: «neoplasia quística» (L3, con estudios en carcinoma adenoide quístico y de glándulas salivales) y «neoplasia premaligna» (L4, con un ensayo de Fase 2 de cetuximab en lesiones premalignas del tracto aerodigestivo superior, NCT00524017).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

