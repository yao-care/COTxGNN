---
layout: default
title: Quetiapine
parent: Solo Predicción del Modelo (L5)
nav_order: 336
evidence_level: L5
indication_count: 10
---

# Quetiapine
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

# Quetiapina: De Esquizofrenia y Trastorno Bipolar a Distrofia Retiniana con o sin Anomalías Extraoculares

## Resumen en Una Frase

La quetiapina es un antipsicótico atípico, usado originalmente para la esquizofrenia, el trastorno bipolar y el trastorno depresivo mayor.
El modelo TxGNN predice que podría ser efectivo para **distrofia retiniana con o sin anomalías extraoculares**,
pero **no hay ensayos clínicos** y las **15 publicaciones** recuperadas no mencionan la quetiapina ni el tratamiento de esta enfermedad. El puntaje alto parece provenir solo de la predicción del grafo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Esquizofrenia, trastorno bipolar I y trastorno depresivo mayor (según la base farmacológica). En el registro INVIMA el texto de indicación solo dice «Quetiapina». |
| Nueva Indicación Predicha | Distrofia retiniana con o sin anomalías extraoculares |
| Puntaje de Predicción TxGNN | 99.57% (posición 3924 en el ranking del modelo) |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Se sabe que la quetiapina actúa sobre receptores de serotonina (5-HT1A, 5-HT1D, 5-HT1E, 5-HT1F y 5-HT2A), sobre el receptor de dopamina D2, sobre el receptor de histamina H1 y sobre el transportador de noradrenalina (NET). Es principalmente un antagonista D2/5-HT2A con actividad adicional sobre H1 y alfa-1.

**Con los datos disponibles, esta predicción no es razonable.** Ninguno de esos blancos se relaciona con la degeneración retiniana hereditaria. La distrofia retiniana es un grupo de enfermedades genéticas de la retina, y la eficacia de la quetiapina en trastornos psiquiátricos no se traslada a ellas.

La literatura recuperada trata sobre diplopía, infecciones orbitarias, ptosis, anomalías del cristalino y oftalmoplejía. Ningún artículo menciona la quetiapina. Es probable que la búsqueda haya coincidido solo por palabras clave oculares. El puntaje de 0.996 es una predicción basada en el grafo y no equivale a evidencia clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Se recuperaron 15 publicaciones. Se muestran las 10 más relevantes, con prioridad para las revisiones. Ninguna estudia la quetiapina ni el tratamiento de la distrofia retiniana, y todas figuran con relevancia pendiente de revisión.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Revisión | Seminars in Neurology | Enfoque sistemático para evaluar la diplopía, con historia clínica, examen físico y diagnóstico diferencial. |
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Revisión | Seminars in Ultrasound, CT, and MR | Infecciones orbitarias, con la sinusitis como causa más común, y sus signos clínicos. |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Revisión | Klinische Monatsblätter für Augenheilkunde | Ptosis congénita: formas simple y complicada, y su asociación con errores refractivos. |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Revisión | Taiwan Journal of Ophthalmology | Anomalías congénitas del cristalino en tamaño, forma y posición. |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Revisión | Pediatric Radiology | Diagnóstico diferencial y hallazgos de imagen de patologías oculares pediátricas. |
| [30747268](https://pubmed.ncbi.nlm.nih.gov/30747268/) | 2019 | Revisión | Neuroradiology | Evaluación neurorradiológica de la oftalmoplejía de inicio agudo. |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Revisión | Journal of Binocular Vision and Ocular Motility | Oftalmoplejía congénita y trastornos congénitos de disinervación craneal. |
| [10192514](https://pubmed.ncbi.nlm.nih.gov/10192514/) | 1999 | Revisión | Progress in Retinal and Eye Research | Propioceptores de los músculos extraoculares y su papel en la percepción espacial visual. |
| [31359131](https://pubmed.ncbi.nlm.nih.gov/31359131/) | 2019 | Revisión | Human Genetics | Arquitectura genética de los defectos del desarrollo ocular asociados a la señalización del ácido retinoico. |
| [37408430](https://pubmed.ncbi.nlm.nih.gov/37408430/) | 2023 | Revisión | Zhonghua Yan Ke Za Zhi | Avances sobre la estructura e inervación de los músculos extraoculares. |

## Información de Mercado en Colombia

El paquete de evidencia lista 20 registros sanitarios, pero las cinco filas recibidas son idénticas (mismo registro, producto y fabricante). Se muestra una sola vez.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20115222 | QUEPINA 100 MG TABLETAS RECUBIERTAS (HUMAX PHARMACEUTICAL S.A.) | Tableta recubierta (vía oral) | Solo figura «Quetiapina»; el texto de indicación no está detallado |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

La consulta de interacciones devolvió 8 registros, pero corresponden a receptores y transportadores donde actúa la quetiapina, no a interacciones con otros medicamentos. No hay información utilizable sobre interacciones farmacológicas.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5): no hay ensayos clínicos, la literatura recuperada no menciona la quetiapina y no se identifica ningún vínculo mecanístico con la distrofia retiniana.

**Para avanzar se necesita:**
- Un vínculo mecanístico plausible entre los blancos de la quetiapina y la biología de la degeneración retinal, o abandonar esta indicación.
- Revisar el prospecto de INVIMA (advertencias y contraindicaciones), que no está disponible en el paquete actual.
- Completar los datos de mecanismo de acción desde DrugBank.
- Considerar otras predicciones del mismo farmaco. La **tricotilomanía** (puesto 8, puntaje 99.38%) es la única con literatura directa sobre quetiapina, con reportes de casos y series pequeñas (PMID 12405081 y 19142421). Está clasificada como L4 y como pregunta de investigación. Hay incertidumbre sobre la dirección del efecto, porque también se han reportado síntomas obsesivo-compulsivos inducidos por quetiapina (PMID 11212595). Sigue sin haber ensayos controlados.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

