---
layout: default
title: Vincristine
parent: Evidencia Moderada (L3-L4)
nav_order: 661
evidence_level: L3
indication_count: 3
last_modified_at: 2026-10-14
description: "Vincristine: nueva indicación predicha, Ganglioneuroblastoma (nivel de evidencia L3). Indicación original: Vincristina"
monitor_inn: "Vincristine"
predicted_indications: ["ganglioneuroblastoma (disease)", "vertebral anomalies and variable endocrine and T-cell dysfunction", "retroperitoneal neoplasm"]
---

# Vincristine
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **3** 
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

# Vincristina: De Indicación Registrada (Vincristina) a Ganglioneuroblastoma

## Resumen en Una Frase

Vincristina es un alcaloide de la vinca utilizado como antineoplásico; en Colombia sus registros sanitarios solo indican "vincristina" como indicación, sin mayor detalle.
El modelo TxGNN predice que podría ser efectiva para **ganglioneuroblastoma**, con **0 ensayos clínicos** y **6 publicaciones** (en su mayoría reportes de caso) que respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Vincristina (el registro sanitario no detalla una enfermedad específica) |
| Nueva Indicación Predicha | Ganglioneuroblastoma |
| Puntaje de Predicción TxGNN | 99.31% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción del fármaco. Según el conocimiento general de la clase, la vincristina es un alcaloide de la vinca que se une a la tubulina (el registro farmacológico señala como diana TUBB, tubulina beta clase I) e inhibe la polimerización de los microtúbulos, lo que provoca detención mitótica en células de división rápida.

La vincristina es un componente histórico de los esquemas de quimioterapia combinada para tumores neuroblásticos (neuroblastoma y ganglioneuroblastoma), que comparten origen en la cresta neural. Su uso clínico conocido incluye leucemia, enfermedad de Hodgkin, linfomas no Hodgkin, rabdomiosarcoma, neuroblastoma y tumor de Wilms. Esto vuelve biológicamente plausible la predicción del modelo.

Conviene tener presente que la relación con la indicación original no puede evaluarse con precisión, porque el registro colombiano solo menciona "vincristina". El puntaje alto de TxGNN es una predicción basada en grafos y no reemplaza la evidencia clínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31342649](https://pubmed.ncbi.nlm.nih.gov/31342649/) | 2019 | Ensayo clínico prospectivo (JN-L-10) | Pediatric Blood & Cancer | Uso de factores de riesgo definidos por imagen para decidir el momento de la cirugía en neuroblastoma de bajo riesgo; la quimioterapia no es la variable principal |
| [8255850](https://pubmed.ncbi.nlm.nih.gov/8255850/) | 1993 | Reporte de caso | Postgraduate Medical Journal | Ganglioneuroblastoma espinal irresecable con remisión completa histológica tras quimioterapia combinada (doxorrubicina, vincristina, ciclofosfamida, etopósido, ifosfamida y cisplatino) |
| [15701990](https://pubmed.ncbi.nlm.nih.gov/15701990/) | 2005 | Reporte de caso | J Pediatr Hematol Oncol | Ganglioneuroblastoma con ictericia obstructiva; tratado con quimioterapia que incluyó vincristina |
| [7421294](https://pubmed.ncbi.nlm.nih.gov/7421294/) | 1980 | Reporte de caso (serie de 31 pacientes) | J Thorac Cardiovasc Surg | Ganglioneuroblastoma intratorácico; tratamiento con resección, radioterapia o quimioterapia; supervivencia de 27/31 pacientes |
| [8888754](https://pubmed.ncbi.nlm.nih.gov/8888754/) | 1996 | Reporte de caso | J Pediatr Hematol Oncol | Lactante con ganglioneuroblastoma multifocal en estadio 4 con compromiso gástrico |
| [3071124](https://pubmed.ncbi.nlm.nih.gov/3071124/) | 1988 | Reporte de caso | Hinyokika Kiyo | Ganglioneuroblastoma suprarrenal en adulto con tratamiento multimodal |

La evidencia es principalmente de reportes de caso; solo uno de los trabajos es un ensayo prospectivo, y no evalúa la quimioterapia como variable principal.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20006838 (cancelado) | Vincristina sulfato 1 mg/1 ml solución inyectable (Venus Remedies Limited) | Solución inyectable | Vincristina |
| 20097927 (cancelado) | Sulfato de vincristina 1 mg polvo liofilizado para reconstituir a solución inyectable (Blau Farmacéutica Colombia S.A.S) | Polvo liofilizado para reconstituir a solución inyectable | Vincristina |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (alcaloide de la vinca, inhibidor de microtúbulos) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto. La base de conocimiento señala leucopenia como contraindicación asociada |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, función hepática (bilirrubina), función neurológica periférica |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

No se dispone del texto del prospecto de INVIMA con advertencias y contraindicaciones. Consultar el prospecto para esa información.

- **Contraindicaciones según el grafo de conocimiento (TxGNN/PrimeKG, no provienen del prospecto)**: insuficiencia hepática, colestasis (incluida la colestasis intrahepática familiar y recurrente benigna), hiperbilirrubinemia (incluido el síndrome de Gilbert), leucopenia, neuropatía periférica y enfermedades neuromusculares (incluida la enfermedad de Charcot-Marie-Tooth, neuritis y neuropatía motora), nefropatía aguda por uratos, infecciones (incluidas las fúngicas y la dermatofitosis).
- **Interacciones farmacológicas**: solo se registra la interacción farmacológica con su diana, la tubulina beta clase I (TUBB), sin interacciones medicamentosas clínicas documentadas.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje de TxGNN es muy alto (99.31%) y el mecanismo es plausible, pero la evidencia se limita a reportes de caso y no hay ensayos clínicos registrados. Además, ambos registros sanitarios en Colombia están cancelados y no se cuenta con el prospecto para el análisis de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), ya que su ausencia bloquea el análisis de seguridad
- Confirmar el mecanismo de acción mediante DrugBank
- Revisar la literatura de esquemas actuales para neuroblastoma/ganglioneuroblastoma y el papel específico de la vincristina
- Aclarar la situación regulatoria (registros cancelados) y la disponibilidad de producto en Colombia
- Valorar un plan de monitoreo para hepatotoxicidad, neurotoxicidad y mielosupresión
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

