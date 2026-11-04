---
layout: default
title: Glucagon
parent: Solo Predicción del Modelo (L5)
nav_order: 316
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-04
monitor_inn: "GLUCAGON"
predicted_indications: ["irritable bowel syndrome"]
description: "Glucagon: nueva indicación predicha, Síndrome del intestino irritable (irritable bowel syndrome) (nivel de evidencia L5). Indicación original: GLUCAGON"
---

# Glucagon
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Glucagon: Síndrome del intestino irritable (irritable bowel syndrome)
{: .text-alpha }

## Resumen en Una Frase

Glucagón es una hormona peptídica que cuenta con registro sanitario vigente en Colombia.
El modelo TxGNN predice que podría ser útil para el **síndrome del intestino irritable (irritable bowel syndrome)**, pero ningún estudio evalúa el glucagón en esta enfermedad: la evidencia disponible se refiere al péptido similar al glucagón tipo 1 (GLP-1) y a sus análogos, que son fármacos distintos. El nivel de evidencia es **L5**.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | GLUCAGON |
| Nueva Indicación Predicha | Síndrome del intestino irritable (irritable bowel syndrome) |
| Puntaje de Predicción TxGNN | 0.9924 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción del glucagón en los datos compilados para este informe. Se sabe que el glucagón y el GLP-1 derivan del mismo precursor, el proglucagón, y que el glucagón se emplea como relajante del músculo liso gastrointestinal (por ejemplo, en endoscopia y radiología).

Los estudios citados se centran en el GLP-1 y sus análogos (como ROSE-010), que inhiben la motilidad antro-duodeno-yeyunal y podrían reducir el dolor abdominal en el síndrome del intestino irritable con estreñimiento. Esto es evidencia de una clase relacionada, no del glucagón. El vínculo mecanístico con el glucagón es plausible pero indirecto.

El puntaje de 0,9924 es una predicción computacional y no constituye evidencia clínica. Ningún ensayo ni publicación evalúa directamente el glucagón en esta enfermedad.

## Evidencia de Ensayos Clínicos

Los siguientes ensayos estudian análogos o mecanismos del GLP-1, no el glucagón.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Fase 1/2 | Completado | 52 | ROSE-010 (análogo de GLP-1) sobre la función motora gastrointestinal en mujeres con síndrome del intestino irritable con estreñimiento; es el más cercano a la población objetivo, pero no prueba glucagón |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Fase 1 | Completado | 12 | GLP-1 nativo frente a ROSE-010 sobre la motilidad antro-duodeno-yeyunal en humanos; estudio mecanístico, no en pacientes con SII |

## Evidencia de Literatura

Ninguna publicación evalúa el glucagón en el síndrome del intestino irritable; las más relevantes se refieren al GLP-1.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Revisión sistemática | Front Endocrinol | Agonistas del receptor de GLP-1 y mejoría del SII; el GLP-1 y ROSE-010 inhiben la motilidad gastrointestinal |
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | Análisis exploratorio | Scand J Gastroenterol | Alivio del dolor con ROSE-010 en SII según características del paciente |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Revisión | Exp Physiol | Papel de las células L y del GLP-1 en la fisiopatología del SII |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | Revisión | Adv Exp Med Biol | GLP-1 en aerosol para diabetes y SII |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | Cohorte | Ann Gastroenterol | Patrones de prescripción y suspensión de agonistas de GLP-1 en pacientes con SII |
| [40880735](https://pubmed.ncbi.nlm.nih.gov/40880735/) | 2025 | Observacional | Front Nutr | Aumento del GLP-1 circulante tras dieta baja en FODMAP en SII |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 208565 | GLUCAGEN INYECTABLE (Novo Nordisk A/S) | Polvo liofilizado para reconstituir a solución inyectable | Glucagón |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registraron 25 interacciones, todas de nivel menor. Las principales son con warfarina y con betabloqueantes (acebutolol, atenolol, bisoprolol, carvedilol, metoprolol, propranolol, nadolol, labetalol, sotalol, timolol, esmolol, entre otros).

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Ningún estudio evalúa el glucagón en el síndrome del intestino irritable; la evidencia procede de GLP-1 y sus análogos, fármacos distintos. El alto puntaje del modelo no sustituye la evidencia clínica, por lo que el nivel es L5.

**Para avanzar se necesita:**
- Estudios preclínicos o clínicos que prueben el glucagón directamente en el síndrome del intestino irritable
- Datos del mecanismo de acción del glucagón en el tracto gastrointestinal
- Advertencias y contraindicaciones del prospecto del registro sanitario
- Evaluación de la vía de administración y la posología adecuadas para un uso crónico o episódico en esta condición

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

