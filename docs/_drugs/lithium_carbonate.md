---
layout: default
title: Lithium Carbonate
parent: Solo Predicción del Modelo (L5)
nav_order: 261
evidence_level: L5
indication_count: 10
---

# Lithium Carbonate
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

# Carbonato de litio: De Indicación Original No Especificada a Pseudoacondroplasia

## Resumen en Una Frase

El carbonato de litio está registrado en Colombia como tabletas orales, pero el texto de indicación del registro solo dice "LITIO" y no detalla el uso aprobado.
El modelo TxGNN predice que podría ser efectivo para **pseudoacondroplasia**,
pero hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción, por lo que es solo una hipótesis del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado dice solo "LITIO") |
| Nueva Indicación Predicha | Pseudoacondroplasia |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 14 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, el litio inhibe la enzima GSK-3 y modula la vía Wnt y la autofagia. Como la indicación original no está detallada en el registro, no se puede comparar con la nueva indicación.

La pseudoacondroplasia es una displasia esquelética causada por mutaciones en el gen COMP, que provocan estrés del retículo endoplásmico en los condrocitos. Especulativamente, los efectos del litio sobre Wnt y la autofagia podrían influir en la biología de la placa de crecimiento. Esta relación es solo una hipótesis mecanística: no hay evidencia clínica ni preclínica que la respalde.

El puntaje TxGNN es muy alto (99.98%, posición 322). Sin embargo, en enfermedades ultra raras los puntajes altos pueden reflejar cercanía en el grafo de conocimiento y no una relación terapéutica real. Por eso el puntaje no debe interpretarse como evidencia de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20018308 | ACTILITIO® TABLETAS 300 MG (ACTIFARMA S.A.) | Tableta | LITIO |

El Evidence Pack lista cinco entradas, pero todas corresponden al mismo registro 20018308, por lo que se muestra una sola vez. El total reportado es de 14 registros. La única vía de administración registrada es la oral.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Otras Predicciones del Modelo (Contexto)

El modelo también predijo otras nueve enfermedades raras, todas con nivel de evidencia L5 y recomendación Hold. Las de mayor relevancia son:

- **Síndrome WHIM (puntaje 99.56%):** es la más plausible biológicamente del conjunto. El litio eleva el recuento de neutrófilos y esta enfermedad cursa con neutropenia. Aun así, no trata el defecto de fondo (ganancia de función de CXCR4) y no hay evidencia aportada.
- **Síndrome braquiolmia-amelogénesis imperfecta:** la única publicación recuperada es una revisión general sobre terapias de trastornos esqueléticos genéticos (PMID [31888683](https://pubmed.ncbi.nlm.nih.gov/31888683/), 2019, *Orphanet J Rare Dis*). No se verificó que trate sobre litio.
- **Resto de predicciones** (displasias esqueléticas, miosclerosis, síndrome de Behr, inmunodeficiencia por deficiencia de moesina): no hay vínculo mecanístico identificable o es muy indirecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (nivel L5), sin ensayos clínicos ni literatura que la respalden. Además, faltan datos de seguridad y el mecanismo de acción del fármaco no está documentado en el Evidence Pack.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), un requisito bloqueante para la evaluación de seguridad.
- Completar los datos de mecanismo de acción desde DrugBank.
- Aclarar la indicación aprobada real de los registros, que hoy dice solo "LITIO".
- Buscar evidencia preclínica (modelos de condrocitos o de placa de crecimiento con COMP) que sustente el vínculo con pseudoacondroplasia.
- Evaluar si el síndrome WHIM merece una revisión de literatura dirigida como alternativa más plausible.

*Este informe es solo una referencia de investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

