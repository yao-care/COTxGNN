---
layout: default
title: Cladribine
parent: Solo Predicción del Modelo (L5)
nav_order: 128
evidence_level: L5
indication_count: 7
---

# Cladribine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Cladribina: De Indicación No Especificada en el Registro a Rabdomiosarcoma Embrionario Parameníngeo

## Resumen en Una Frase

Cladribina es un análogo de nucleósido de purina con registro vigente en Colombia (tabletas MAVENCLAD®). El texto del registro no detalla la indicación original.
El modelo TxGNN predice que podría ser efectivo para el **rabdomiosarcoma embrionario parameníngeo**,
pero hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro solo indica «CLADRIBINA») |
| Nueva Indicación Predicha | Rabdomiosarcoma embrionario parameníngeo |
| Puntaje de Predicción TxGNN | 99.77% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 18 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados sobre el mecanismo de acción en la fuente del registro. Según la farmacología general, la cladribina es un análogo de la desoxiadenosina, resistente a la adenosina desaminasa y fosforilado por la desoxicitidina quinasa (dCK). Provoca rupturas de las cadenas de ADN y apoptosis, sobre todo en células linfoides.

La actividad en un tumor sólido mesenquimatoso como el rabdomiosarcoma es biológicamente plausible, pero no está respaldada por ninguna evidencia. La citotoxicidad de este tipo de fármacos depende de una alta actividad de dCK y una baja actividad de 5'-nucleotidasa, perfil típico de las células linfoides. No se sabe si las células de rabdomiosarcoma lo comparten.

Además, las siete predicciones del modelo no son señales independientes. Seis de ellas son variantes anatómicas o histológicas del rabdomiosarcoma, incluido el nodo de la enfermedad general, y probablemente heredan el puntaje del mismo grupo en el grafo de conocimiento. La séptima (sarcoma hepático) tampoco tiene evidencia directa. Si se quisiera avanzar, el primer paso sería preclínico: medir la expresión de dCK y la sensibilidad de líneas celulares de rabdomiosarcoma.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

Nota: la única publicación del paquete (PMID [15241520](https://pubmed.ncbi.nlm.nih.gov/15241520/), 2004, reporte de caso, *Der Hautarzt*) corresponde a la predicción de sarcoma hepático. Describe el uso de cladribina en mastocitosis sistémica indolente, un trastorno hematológico. No es un estudio de sarcoma hepático ni de rabdomiosarcoma, por lo que no se cuenta como evidencia.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20141389 | MAVENCLAD® (MERCK S.A.) | Tableta | CLADRIBINA (el registro no detalla la indicación) |

Los datos recibidos repiten cinco veces el mismo registro, por lo que aquí se muestra una sola vez. El fármaco tiene 18 registros en total y también existe una forma de solución inyectable.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (análogo de nucleósido de purina) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal; confirmar parámetros específicos en el prospecto |
| Protección en Manejo | Seguir las regulaciones de manejo de fármacos citotóxicos |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el puntaje del modelo (nivel L5), sin ensayos ni literatura, y las predicciones de rabdomiosarcoma no son independientes entre sí. La plausibilidad mecanística depende de que las células tumorales tengan un perfil enzimático que no se ha verificado.

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de INVIMA para advertencias y contraindicaciones (bloqueante para el cribado de seguridad)
- Obtener los datos de mecanismo de acción desde DrugBank
- Definir la indicación original aprobada, porque el registro solo muestra el nombre del principio activo
- Estudios preclínicos: expresión de dCK y 5'-nucleotidasa, y sensibilidad de líneas celulares de rabdomiosarcoma a cladribina
- Confirmar la compatibilidad de vías de administración (pendiente en el paquete de evidencia)

*Este informe es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

