---
layout: default
title: Mebendazole
parent: Solo Predicción del Modelo (L5)
nav_order: 419
evidence_level: L5
indication_count: 1
---

# Mebendazole
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Mebendazol: De Antihelmíntico (Mebendazol) a Acné

## Resumen en Una Frase

Mebendazol es un antihelmíntico del grupo de los benzimidazoles, registrado en Colombia como mebendazol en suspensión oral.
El modelo TxGNN predice que podría ser efectivo para **acné**, pero actualmente no hay **ningún ensayo clínico** y solo existe **1 publicación** (un reporte de caso sobre esparganosis, sin relación directa con el acné) que respalde esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Mebendazol (el registro no detalla la indicación; se trata de un antiparasitario) |
| Nueva Indicación Predicha | Acné |
| Puntaje de Predicción TxGNN | 99.20% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, mebendazol es un antihelmíntico benzimidazólico que se une a la beta-tubulina del parásito e inhibe la polimerización de los microtúbulos. Su eficacia en infecciones parasitarias intestinales es conocida.

El acné vulgar depende de la producción excesiva de sebo, la hiperqueratinización folicular, la colonización por *Cutibacterium acnes* y la inflamación. No se identificó un vínculo mecanístico creíble con la alteración de los microtúbulos. Un posible efecto antiproliferativo o antiinflamatorio sobre sebocitos o queratinocitos es puramente especulativo.

El puntaje alto de TxGNN (99.20%) proviene solo de una predicción basada en grafos de conocimiento y no está respaldado por datos clínicos ni mecanísticos. Debe interpretarse con mucha cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [7072899](https://pubmed.ncbi.nlm.nih.gov/7072899/) | 1982 | Reporte de caso | The American Journal of Tropical Medicine and Hygiene | Primer caso de esparganosis proliferativa humana en el hemisferio sur (Venezuela). El paciente presentaba lesiones nodulares y papulares similares al acné, junto con anemia, eosinofilia y abscesos. No evalúa mebendazol como tratamiento del acné. |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19948951 | ASCAZOL® 100 MG/5ML SUSPENSION (cancelado) | Suspensión oral | Mebendazol |
| 19946472 | CHALVER ZAKOR® SUSPENSION (cancelado) | Suspensión oral | Mebendazol |

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no provienen del prospecto): enfermedad hepática y enfermedad de la vesícula biliar.
- **Interacciones Farmacológicas**: se identificaron 10 interacciones, la mayoría de nivel moderado:
  - Moderadas: metronidazol, yoduro I-131, yoduro I-123, fenobarbital, carbamazepina, ritonavir, fosfenitoína, fenitoína y primidona.
  - Leve: cimetidina.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos y sin vínculo mecanístico plausible con el acné. Además, los dos registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA para completar la revisión de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar estudios preclínicos (por ejemplo, en sebocitos o queratinocitos) que respalden alguna hipótesis mecanística.
- Evaluar la compatibilidad de la vía de administración (la presentación existente es oral, y el acné suele tratarse de forma tópica o sistémica con otros fármacos).
- Reconsiderar la candidatura solo si aparece evidencia clínica o mecanística sólida.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

