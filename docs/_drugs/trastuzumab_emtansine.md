---
layout: default
title: Trastuzumab Emtansine
parent: Solo Predicción del Modelo (L5)
nav_order: 639
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Trastuzumab Emtansine: nueva indicación predicha, Subtipo \"normal breast-like\" del carcinoma de mama (nivel de evidencia L5). Indicación original: No especificada en el registro"
---

# Trastuzumab Emtansine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Trastuzumab emtansina: De Indicación no especificada en el registro a Carcinoma de mama normal-like (subtipo "normal breast-like")

> **Nota sobre la predicción principal:** la predicción de mayor puntaje (rank 1) es el subtipo "normal breast-like" del carcinoma de mama, sin ensayos clínicos ni literatura específica. Los datos compilados muestran evidencia más sólida en otras indicaciones del mismo grupo (cáncer de mama RP-negativo, nivel L2), que se detallan en este informe.

---

## Resumen en Una Frase

Trastuzumab emtansina (T-DM1) es un conjugado anticuerpo-fármaco dirigido a HER2, registrado en Colombia bajo la marca Kadcyla®; el registro sanitario no detalla el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para el **subtipo "normal breast-like" del carcinoma de mama**, pero **sin ensayos clínicos ni publicaciones específicas** que lo respalden.
Para otras indicaciones cercanas dentro del cáncer de mama hay más soporte (1 ensayo clínico de Fase 2 en cáncer de mama RP-negativo y abundante literatura), aunque en su mayoría corresponde a la población HER2-positiva ya cubierta por el uso establecido del fármaco.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto registrado solo repite el nombre del principio activo, "trastuzumab emtansina") |
| Nueva Indicación Predicha | Subtipo "normal breast-like" del carcinoma de mama |
| Puntaje de Predicción TxGNN | 99.82% |
| Nivel de Evidencia | L5 (solo predicción del modelo) |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

**Otras predicciones evaluadas (para contexto):**

| Posición | Indicación predicha | Puntaje TxGNN | Nivel de evidencia | Recomendación |
|------|------|------|------|------|
| 1 | Carcinoma de mama subtipo normal breast-like | 99.82% | L5 | Hold |
| 2 | Cáncer de mama RP-positivo | 99.82% | L4 | Pregunta de investigación |
| 3 | Cáncer de mama RP-negativo | 99.82% | L2 | Pregunta de investigación |
| 4 | Tumor de mama luminal A o B | 99.81% | L3 | Pregunta de investigación |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, T-DM1 es un conjugado anticuerpo-fármaco: un anticuerpo (trastuzumab) dirigido contra el receptor HER2 unido a DM1, un inhibidor de microtúbulos. El anticuerpo se une a HER2, el conjugado es internalizado por la célula y libera DM1 en su interior, lo que provoca la muerte celular.

El subtipo "normal breast-like" suele ser HER2-bajo o HER2-negativo, por lo que el fundamento mecanístico es **débil**. El puntaje tan alto del modelo (99.82%) probablemente refleja la actividad bien establecida del fármaco en nodos cercanos del cáncer de mama y no un hallazgo específico de este subtipo. No hay ensayos ni literatura propios de esta indicación.

En cambio, para los subgrupos RP-positivo, RP-negativo y luminal, el mecanismo es plausible **solo si el tumor es HER2-positivo**: T-DM1 actúa a través de HER2 independientemente del estado de receptores hormonales. Por ello, estas predicciones son más bien una extensión de la indicación ya conocida (cáncer de mama HER2-positivo) que un reposicionamiento genuino.

---

## Evidencia de Ensayos Clínicos

Para la indicación principal (subtipo normal breast-like): actualmente no hay ensayos clínicos relacionados registrados.

Para la predicción de cáncer de mama RP-negativo (única con ensayo registrado):

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04675827](https://clinicaltrials.gov/study/NCT04675827) | Fase 2 | Terminado | 139 | Estudio DECRESCENDO de de-escalada de quimioterapia adyuvante en cáncer de mama temprano HER2-positivo, RE-negativo y ganglios negativos, con respuesta patológica completa tras tratamiento neoadyuvante y bloqueo dual de HER2 (paclitaxel o docetaxel con pertuzumab/trastuzumab subcutáneo). Relevancia moderada (B): la terminación temprana limita las conclusiones y T-DM1 no figura como agente experimental único. |

---

## Evidencia de Literatura

Para la indicación principal (subtipo normal breast-like): actualmente no hay literatura relacionada disponible.

Selección de las publicaciones más relevantes para las indicaciones cercanas (cáncer de mama RP-positivo y luminal):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38825627](https://pubmed.ncbi.nlm.nih.gov/38825627/) | 2024 | Seguimiento de ECA | Nature Medicine | DESTINY-Breast03: trastuzumab deruxtecán mostró mayor eficacia que T-DM1 en cáncer de mama metastásico HER2-positivo previamente tratado, con seguimiento a 41 meses |
| [38092229](https://pubmed.ncbi.nlm.nih.gov/38092229/) | 2024 | Seguimiento de ECA (Fase 2) | Annals of Oncology | DESTINY-Breast01: resultados de supervivencia actualizados de trastuzumab deruxtecán en pacientes previamente tratadas con T-DM1 |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guía | Journal of Clinical Oncology | Actualización de la guía ASCO sobre terapia sistémica en cáncer de mama avanzado HER2-positivo |
| [28259011](https://pubmed.ncbi.nlm.nih.gov/28259011/) | 2017 | Guía | European Journal of Cancer | Guías EGTM: la determinación de HER2 es obligatoria para seleccionar terapias anti-HER2, incluido T-DM1 |
| [34215766](https://pubmed.ncbi.nlm.nih.gov/34215766/) | 2021 | Cohorte | Scientific Reports | Relevancia pronóstica de la ganancia de positividad HER2 en cáncer de mama metastásico tratado con pertuzumab y/o T-DM1 |
| [38300710](https://pubmed.ncbi.nlm.nih.gov/38300710/) | 2024 | Cohorte | J Clin Invest | Heterogeneidad de HER2 y respuesta al tratamiento en un ensayo neoadyuvante de T-DM1 más pertuzumab: ningún paciente con tumores heterogéneos logró respuesta patológica completa |
| [33726508](https://pubmed.ncbi.nlm.nih.gov/33726508/) | 2021 | Revisión | Future Oncology | Tendencias actuales en el tratamiento del cáncer de mama HR+/HER2+, incluyendo neratinib y T-DM1 |
| [39631485](https://pubmed.ncbi.nlm.nih.gov/39631485/) | 2024 | Revisión | Pharmacological Research | Revisión de inhibidores dirigidos y citotóxicos usados en cáncer de mama |
| [33493147](https://pubmed.ncbi.nlm.nih.gov/33493147/) | 2021 | Revisión | Clin Adv Hematol Oncol | Revisión integral del cáncer de mama metastásico HER2-positivo |
| [25873876](https://pubmed.ncbi.nlm.nih.gov/25873876/) | 2015 | Reporte de caso | Case Reports in Oncology | T-DM1 a dosis reducidas fue activo y seguro en una paciente con disfunción hepática aguda |

La literatura consiste principalmente en guías, revisiones y reportes de caso; no se muestra evidencia primaria de ECA directa para los subtipos predichos. Varias publicaciones recuperadas no guardan relación con el tema (linfoma, cáncer gástrico, un artículo de química de marcaje de proteínas).

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20058197 | KADCYLA® 100 mg/vial | Polvo liofilizado para reconstituir a solución inyectable | Trastuzumab emtansina (sin detalle de indicación) — **Cancelado** |
| 20064940 | KADCYLA® 160 mg/vial | Polvo liofilizado para reconstituir a solución inyectable | Trastuzumab emtansina (sin detalle de indicación) — **Cancelado** |

Fabricante de ambos registros: F. Hoffmann-La Roche Ltd. No hay registros vigentes en Colombia.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Conjugado anticuerpo-fármaco (terapia dirigida) con carga citotóxica inhibidora de microtúbulos (DM1) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma, función hepática y renal (monitoreo general para citotóxicos; confirmar en el prospecto) |
| Protección en Manejo | Seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

**Interacciones farmacológicas:** la consulta de interacciones se completó con 100 interacciones registradas. Entre las primeras 20 listadas:

- **Mayores:** ácido acetilsalicílico, deferasirox, abciximab, apixabán, argatrobán, betrixabán, bivalirudina, cangrelor, caplacizumab y cilostazol. Predominan antitrombóticos, anticoagulantes y antiagregantes plaquetarios, lo que sugiere un mayor riesgo de sangrado en combinación.
- **Moderadas:** claritromicina, dexfenfluramina, fenfluramina, metronidazol, naltrexona, rosuvastatina, sibutramina, simvastatina, tinidazol y cobicistat.

No se dispone de advertencias ni contraindicaciones del prospecto en los datos compilados. Consultar el prospecto para el resto de la información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal (subtipo normal breast-like) es solo una predicción del modelo (L5), sin ensayos ni literatura, con un fundamento mecanístico débil por su perfil HER2-bajo/negativo. Las indicaciones vecinas tienen más soporte, pero corresponden esencialmente al uso ya establecido en cáncer de mama HER2-positivo, y todos los registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones), pendiente y necesario para la evaluación de seguridad
- Completar los datos del mecanismo de acción (por ejemplo, consultando DrugBank)
- Verificar el motivo de la cancelación de los registros y la situación actual de comercialización o importación en Colombia
- Definir si el interés recae en el subtipo normal breast-like (evidencia nula) o en subgrupos HER2-positivos (que son una extensión de la indicación conocida)
- Para el subgrupo RP-negativo, revisar si NCT04675827 incluye T-DM1 y qué resultados publicó tras su terminación
- Evaluar de forma explícita el riesgo de sangrado frente a la lista de interacciones con anticoagulantes y antiagregantes
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

