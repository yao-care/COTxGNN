---
layout: default
title: Vildagliptin
parent: Solo Predicción del Modelo (L5)
nav_order: 406
evidence_level: L5
indication_count: 10
---

# Vildagliptin
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

# Vildagliptina: De Diabetes Tipo 2 a Síndrome de Extremidad Rígida Focal

## Resumen en Una Frase

La vildagliptina es un inhibidor de la dipeptidil peptidasa-4 (DPP-4), utilizado originalmente para el tratamiento de la diabetes mellitus tipo 2.
El modelo TxGNN predice que podría ser efectiva para el **síndrome de extremidad rígida focal**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección. Es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Diabetes mellitus tipo 2 (según los datos farmacológicos; el registro INVIMA solo lista "Metformina / Vildagliptina" como texto de indicación) |
| Nueva Indicación Predicha | Síndrome de extremidad rígida focal |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el campo correspondiente. Según la información conocida, la vildagliptina inhibe la enzima DPP-4, lo que prolonga la acción de las incretinas y mejora el control glucémico. Los datos farmacológicos también la vinculan con DPP-8, DPP-9 y TRPV4. Su eficacia en diabetes tipo 2 está comprobada.

La relación con la nueva indicación es indirecta y especulativa. Los síndromes de rigidez de extremidad y de persona rígida suelen ser autoinmunes, con anticuerpos anti-GAD65, y esa autoinmunidad también aparece en la diabetes tipo 1. Es probable que la predicción refleje esa cercanía en el grafo de conocimiento y no un efecto real de la inhibición de DPP-4.

Además, el puntaje (99.88%) es idéntico al del síndrome de persona rígida clásico, por lo que no aporta información diferenciadora por sí solo. Con los datos disponibles no hay un mecanismo plausible por el cual inhibir DPP-4 modifique este síndrome.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19998394 | GALVUS® MET COMPRIMIDOS RECUBIERTOS CON PELÍCULA 50 MG / 1000 MG (Novartis Pharma AG) | Tableta cubierta con película | Metformina / Vildagliptina |

Nota: las cinco entradas recibidas corresponden al mismo registro, por eso se muestra una sola vez. El total reportado es de 20 registros.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: los 4 registros disponibles no son interacciones con otros fármacos, sino dianas farmacológicas de la vildagliptina: DPP-4, DPP-8, DPP-9 y TRPV4.
- **Señal de seguridad en la literatura**: se recuperó un reporte de caso de pancreatitis aguda probablemente asociada a vildagliptina ([PMID 42539684](https://pubmed.ncbi.nlm.nih.gov/42539684/), 2026). Es una señal de seguridad, no evidencia de eficacia.

Para las advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún ensayo clínico ni publicación para esta indicación, y el nivel de evidencia es L5. El vínculo mecanístico no está respaldado y el puntaje del modelo no diferencia esta predicción de otras.

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de INVIMA (advertencias y contraindicaciones), que sigue pendiente.
- Completar los datos de mecanismo de acción desde DrugBank.
- Descartar este síndrome como prioridad, salvo que aparezca evidencia clínica o mecanística nueva.
- Evaluar por separado la predicción de **diabetes mellitus tipo 1** (rango 10 en el paquete). Tiene evidencia mucho mayor, con nivel L2 y varios ensayos de Fase 2, incluido un ECA de rapamicina más vildagliptina ([PMID 33124663](https://pubmed.ncbi.nlm.nih.gov/33124663/)), aunque debe verificarse contra los registros completos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

