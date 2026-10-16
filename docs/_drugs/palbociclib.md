---
layout: default
title: Palbociclib
parent: Evidencia Moderada (L3-L4)
nav_order: 493
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-14
description: "Palbociclib: nueva indicación predicha, Artritis reumatoide (nivel de evidencia L4). Indicación original: No especificada en el registro (el texto de indicación solo indica \"P…"
---

# Palbociclib
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **4** 
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

# Palbociclib: De Palbociclib (indicación no detallada) a Artritis Reumatoide

## Resumen en Una Frase

Palbociclib es un inhibidor de CDK4/6 registrado en Colombia, aunque el texto de indicación del registro sanitario solo repite el nombre del fármaco y no detalla la enfermedad aprobada.
El modelo TxGNN predice que podría ser efectivo para **artritis reumatoide** (segunda predicción de mayor puntaje; la primera, hipertiroidismo, carece de cualquier respaldo), con **0 ensayos clínicos** y **4 publicaciones** (un reporte de caso, un estudio de cohorte y dos estudios preclínicos) que ofrecen un respaldo solo indirecto.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto de indicación solo indica "Palbociclib") |
| Nueva Indicación Predicha | Artritis reumatoide (rank 2 de TxGNN; ver nota abajo) |
| Puntaje de Predicción TxGNN | 99.36% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 4 (todos cancelados) |
| Decisión Recomendada | Hold |

**Nota sobre la selección:** la primera predicción de TxGNN es hipertiroidismo (99.44%), pero no tiene ensayos ni literatura (nivel L5). Este informe se centra en la artritis reumatoide, que es la predicción con evidencia más relevante. Las demás predicciones se comentan al final.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, palbociclib es un inhibidor de las quinasas dependientes de ciclina 4 y 6 (CDK4/6), utilizado en cáncer de mama con receptores hormonales positivos y HER2 negativo. Su eficacia en esa indicación está bien establecida en la literatura, aunque el registro colombiano no la detalla.

La relación con la artritis reumatoide es plausible desde lo biológico: la inhibición de CDK4/6 frena la proliferación celular, y en la artritis reumatoide los fibroblastos sinoviales proliferan en exceso y contribuyen al daño articular. Un estudio preclínico (PMID 39940918) señala que la hiperplasia sinovial en ratones con artritis depende de CDK6 y no de CDK4, y otro (PMID 25165034) indica que regular el ciclo celular junto con el bloqueo de citocinas potencia el efecto antiartrítico sin aumentar la inmunosupresión.

Un reporte de caso (PMID 33587021) describe mejoría de la artritis reumatoide en una paciente con cáncer de mama tratada con palbociclib. Sin embargo, la evidencia es indirecta y no existen ensayos clínicos registrados. El mismo grupo de estudios preclínicos menciona mielosupresión como posible limitación.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [40504547](https://pubmed.ncbi.nlm.nih.gov/40504547/) | 2025 | Cohorte | The Oncologist | Analiza enfermedades autoinmunes preexistentes y emergentes en pacientes con cáncer de mama que reciben inhibidores de CDK4/6 y terapia endocrina; los resultados específicos para artritis reumatoide no pueden confirmarse con la información disponible |
| [33587021](https://pubmed.ncbi.nlm.nih.gov/33587021/) | 2021 | Reporte de caso | Modern Rheumatology Case Reports | Mujer de 56 años con artritis reumatoide y cáncer de mama que mejoró su artritis durante el tratamiento con palbociclib |
| [25165034](https://pubmed.ncbi.nlm.nih.gov/25165034/) | 2016 | Preclínico (modelo animal) | Annals of the Rheumatic Diseases | Inhibir el ciclo celular de fibroblastos sinoviales con inhibidores de CDK mejoró la enfermedad en modelos animales sin debilitar la inmunidad adquirida; el efecto aumenta al combinarse con bloqueo de citocinas |
| [39940918](https://pubmed.ncbi.nlm.nih.gov/39940918/) | 2025 | Preclínico (animal/celular) | International Journal of Molecular Sciences | La hiperplasia sinovial en ratones artríticos depende de CDK6 y no de CDK4; palbociclib se ha explorado como opción para artritis reumatoide, con mielosupresión en estudios preclínicos |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20195984 | REAMPLA® 125 MG TABLETAS RECUBIERTAS | Tableta cubierta con película | Palbociclib (estado: cancelado) |
| 20242070 | BAPOCIL® 125MG | Cápsula dura | Palbociclib (estado: cancelado) |
| 20195993 | REAMPLA® 100 MG TABLETAS RECUBIERTAS | Tableta cubierta con película | Palbociclib (estado: cancelado) |
| 20242562 | BAPOCIL® 75MG | Cápsula dura | Palbociclib (estado: cancelado) |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de CDK4/6) |
| Riesgo de Mielosupresión | Alto según la literatura general de la clase (la neutropenia es un efecto frecuente); un estudio preclínico (PMID 39940918) también refiere mielosupresión inducida por palbociclib |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** se identificaron 100 interacciones en total; entre las principales (muestra de 20 revisadas):
  - **Mayores:** claritromicina, cobicistat, deferiprona y lexidronam de samario (153Sm).
  - **Moderadas (algunas relevantes):** aprepitant, dexametasona, cimetidina, miconazol, clotrimazol, simvastatina, cisaprida, cilostazol y deferasirox.
  - **Menor:** prucaloprida.
- **Señal de tromboembolismo:** estudios de farmacovigilancia (PMIDs 36794339, 39083396, 39123221) asocian los inhibidores de CDK4/6 con eventos tromboembólicos, algo a considerar en cualquier población nueva.
- **Toxicidad pulmonar:** la literatura describe enfermedad pulmonar intersticial con esta clase (PMID 37994878).

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia para artritis reumatoide se limita a estudios preclínicos, un reporte de caso y un estudio de cohorte sin confirmación de resultados, sin ensayos clínicos registrados (nivel L4). Además, todos los registros sanitarios en Colombia están cancelados y la mielosupresión y la señal tromboembólica exigen cautela en una enfermedad crónica no oncológica.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), actualmente no disponible.
- Completar los datos del mecanismo de acción desde DrugBank.
- Confirmar la indicación aprobada original, ya que el registro solo repite el nombre del fármaco.
- Revisar el texto completo del estudio de cohorte (PMID 40504547) para valorar el efecto sobre la artritis reumatoide.
- Evaluar en estudios preclínicos y de fase temprana la seguridad (mielosupresión, tromboembolismo) y la dosis en artritis reumatoide.
- Aclarar la situación comercial en Colombia, dado que no hay registros vigentes.

**Otras predicciones del modelo (no recomendadas por ahora):**
- **Hipertiroidismo (99.44%) y resistencia a la hormona tiroidea por mutación del receptor beta (99.30%):** sin ensayos ni literatura (L5); no hay vínculo biológico evidente con la inhibición de CDK4/6 y la predicción parece basada en asociaciones de red. Decisión: Hold.
- **Enfermedad trombótica (99.32%):** la literatura describe la trombosis como un evento adverso de los inhibidores de CDK4/6, no como un beneficio terapéutico. Esta dirección carece de respaldo y podría ser perjudicial. Decisión: Hold.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

