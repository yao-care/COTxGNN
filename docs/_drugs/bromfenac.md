---
layout: default
title: Bromfenac
parent: Evidencia Alta (L1-L2)
nav_order: 118
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Bromfenac: nueva indicación predicha, Enfermedad ocular (eye disease) (nivel de evidencia L1). Indicación original: Bromfenaco"
monitor_inn: "bromfenac"
predicted_indications: ["eye disease", "optic papillitis", "von Hippel anomaly", "mcpherson robertson cammarano syndrome", "vulvar inverted follicular keratosis", "lagophthalmos", "microblepharon-ablephara syndrome", "seborrheic keratosis", "conjunctival degeneration", "luxation of globe"]
---

# Bromfenac
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **10** 
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

# Bromfenaco: De Bromfenaco (Solución Oftálmica) a Enfermedad Ocular

## Resumen en Una Frase

Bromfenaco es un antiinflamatorio no esteroideo (AINE) de uso oftálmico tópico, registrado en Colombia como solución oftálmica (producto ZEBESTEN®).
El modelo TxGNN predice que podría ser efectivo para **enfermedad ocular** (categoría amplia), con **34 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección, de los cuales la evidencia más sólida corresponde a la inflamación posoperatoria y al edema macular quistoide.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Bromfenaco (el registro sanitario solo indica el nombre del principio activo, sin texto de indicación detallado) |
| Nueva Indicación Predicha | Enfermedad ocular (eye disease) |
| Puntaje de Predicción TxGNN | 99.80% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos consultada. Según la información conocida, bromfenaco es un AINE tópico que inhibe las ciclooxigenasas (COX-1 y COX-2) y reduce la síntesis de prostaglandina E2 (PGE2), mediador clave de la inflamación ocular, el dolor y el edema macular.

Su uso original en solución oftálmica se relaciona con la inflamación y el dolor tras cirugía de catarata. Como la inflamación mediada por prostaglandinas participa en muchas patologías oculares, es coherente que el modelo prediga utilidad en "enfermedad ocular". Los ensayos que miden directamente la inhibición de PGE2 en humanos (por ejemplo, NCT01021761) apoyan este mecanismo.

Conviene precisar que "enfermedad ocular" es una categoría muy amplia: la evidencia es más fuerte para subindicaciones específicas (inflamación posoperatoria, edema macular quistoide pseudofáquico) y más débil para otras (ojo seco, enfermedades retinianas, neuroprotección en glaucoma).

---

## Evidencia de Ensayos Clínicos

Se identificaron 34 ensayos relacionados; se listan los 10 más relevantes (priorizando fase 3 completados y los de mayor relevancia directa).

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01212471](https://clinicaltrials.gov/study/NCT01212471) | Fase 3 | Completado | 840 | Estudio de rango de dosis de bromfenaco oftálmico en ojo seco; seguridad y eficacia |
| [NCT00198445](https://clinicaltrials.gov/study/NCT00198445) | Fase 3 | Completado | 527 | Bromfenaco vs. placebo en inflamación ocular tras cirugía de catarata |
| [NCT01367249](https://clinicaltrials.gov/study/NCT01367249) | Fase 3 | Completado | 440 | Bromfenaco vs. placebo en inflamación y dolor asociados a cirugía de catarata |
| [NCT01774474](https://clinicaltrials.gov/study/NCT01774474) | Fase 3 | Completado | 1127 | Prevención del edema macular tras cirugía de catarata, en pacientes con y sin diabetes |
| [NCT00704418](https://clinicaltrials.gov/study/NCT00704418) | Fase 3 | Completado | 156 | Eficacia y seguridad de bromfenaco en cirugía de catarata |
| [NCT00423007](https://clinicaltrials.gov/study/NCT00423007) | Fase 3 | Completado | 90 | Bromfenaco vs. placebo en pacientes con antecedente de conjuntivitis alérgica |
| [NCT03597867](https://clinicaltrials.gov/study/NCT03597867) | Fase 3 | Completado | 104 | Niveles vítreos de PGE2 tras diclofenaco, nepafenaco, indometacina y bromfenaco en vitrectomía |
| [NCT03521791](https://clinicaltrials.gov/study/NCT03521791) | Fase 4 | Completado | 166 | PRO-155 (Zebesten Ofteno®) vs. placebo en inflamación conjuntival por pterigión grado I-III |
| [NCT01021761](https://clinicaltrials.gov/study/NCT01021761) | Fase 4 | Completado | 126 | Comparación de la inhibición de PGE2 entre Acuvail, Xibrom y Nevanac en facoemulsificación |
| [NCT00805233](https://clinicaltrials.gov/study/NCT00805233) | Fase 2 | Completado | 30 | Ranibizumab más bromfenaco en degeneración macular neovascular; estudio pequeño y de combinación |

Nota: el ensayo NCT05158699 (Fase 3, 628 participantes) fue terminado anticipadamente y el NCT00438243 (Fase 2) fue retirado, por lo que no se consideran evidencia sólida.

---

## Evidencia de Literatura

Se listan las publicaciones más relevantes, priorizando metaanálisis, revisiones sistemáticas y ensayos aleatorizados.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39180057](https://pubmed.ncbi.nlm.nih.gov/39180057/) | 2024 | Metaanálisis | BMC Ophthalmology | Bromfenaco tópico como adyuvante de la terapia anti-VEGF en maculopatías (DMAE neovascular, edema macular diabético, oclusiones venosas) |
| [25686158](https://pubmed.ncbi.nlm.nih.gov/25686158/) | 2015 | Revisión sistemática | Cochrane Database Syst Rev | AINE tópicos para edema macular quístico diabético |
| [31343372](https://pubmed.ncbi.nlm.nih.gov/31343372/) | 2019 | ECA/Revisión | Expert Opin Pharmacother | Bromfenaco 0.075% en DuraSite: eficacia y seguridad en dolor e inflamación tras catarata |
| [39095467](https://pubmed.ncbi.nlm.nih.gov/39095467/) | 2024 | Revisión sistemática con metaanálisis en red | Eye (Lond) | Comparación de AINE tópicos en edema macular y desenlace visual tras facoemulsificación |
| [19735215](https://pubmed.ncbi.nlm.nih.gov/19735215/) | 2009 | Revisión | Expert Opin Pharmacother | Utilidad oftálmica de bromfenaco dos veces al día; superior a placebo en inflamación posoperatoria |
| [26502088](https://pubmed.ncbi.nlm.nih.gov/26502088/) | 2016 | Revisión | Dev Ophthalmol | Uso de AINE en enfermedades retinianas |
| [26068607](https://pubmed.ncbi.nlm.nih.gov/26068607/) | 2015 | Estudio clínico | Asia Pac J Ophthalmol | Eficacia de bromfenaco en ojo seco no controlado con lágrimas artificiales |
| [37083870](https://pubmed.ncbi.nlm.nih.gov/37083870/) | 2023 | Estudio clínico | Int Ophthalmol | Bromfenaco tópico como adyuvante de ranibizumab intravítreo en edema macular diabético |
| [17445902](https://pubmed.ncbi.nlm.nih.gov/17445902/) | 2007 | Estudio clínico | Ophthalmology | Bromfenaco 0.09% (Xibrom) en dolor e inflamación posoperatorios |
| [38920673](https://pubmed.ncbi.nlm.nih.gov/38920673/) | 2024 | Preclínico (modelo animal) | Cells | Reducción de la neuroinflamación en un modelo de glaucoma por isquemia-reperfusión |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20108768 | ZEBESTEN® | Solución oftálmica | Bromfenaco | Cancelado |

El único registro sanitario existente figura como cancelado, por lo que actualmente no hay producto vigente en el mercado colombiano.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: artritis reumatoide, diabetes mellitus y cetoacidosis diabética.
- **Interacciones farmacológicas**: se identificaron 132 interacciones en total. Entre las listadas, la mayoría son de nivel moderado:
  - Corticosteroides: hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida.
  - Ácido acetilsalicílico y salicilatos relacionados: mesalazina, balsalazida.
  - Antidiabéticos: metformina, clorpropamida, glimepirida.
  - Otros: vancomicina, kanamicina, citrato y bicarbonato de potasio, y laxantes (ácido picosulfúrico, polietilenglicol, sulfato de sodio).
  - De nivel leve: cimetidina y linaclotida.
- **Alertas desde la literatura**:
  - Fusión y perforación corneal con uso tópico, descritas en pacientes con superficie ocular comprometida (síndrome de Stevens-Johnson, PMID 17720085; síndrome de Sjögren no diagnosticado, PMID 30042108).
  - Un caso de necrólisis epidérmica tóxica con gotas de bromfenaco sódico (PMID 38734855).
  - La hepatotoxicidad grave llevó al retiro de bromfenaco sistémico (formulación oral, no oftálmica).

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen múltiples ensayos de Fase 3 completados (inflamación posoperatoria, edema macular, ojo seco, conjuntivitis alérgica) y metaanálisis que respaldan el uso de bromfenaco en enfermedades oculares inflamatorias. Sin embargo, la indicación predicha es muy amplia, el único registro colombiano está cancelado y existen alertas de seguridad corneal y cutánea, por lo que se recomienda avanzar solo con restricciones.

**Para avanzar se necesita:**
- Delimitar subindicaciones concretas (inflamación posoperatoria de catarata y edema macular quistoide pseudofáquico) en lugar de "enfermedad ocular".
- Obtener y analizar el prospecto del INVIMA para completar advertencias y contraindicaciones.
- Confirmar los datos del mecanismo de acción en DrugBank.
- Definir un plan de monitoreo del estado corneal y limitar la duración del tratamiento, evitando su uso en superficies oculares comprometidas.
- Aclarar la situación regulatoria: tramitar un nuevo registro o verificar la disponibilidad de otros productos con bromfenaco en Colombia.

---

### Nota sobre otras predicciones

Las demás indicaciones predichas (papilitis óptica, anomalía de von Hippel, síndrome de McPherson-Robertson-Cammarano, queratosis folicular invertida vulvar, lagoftalmos, síndrome de microblefaron-ablefaria, queratosis seborreica, degeneración conjuntival y luxación del globo ocular) tienen evidencia de nivel L4–L5 y decisión **Hold**. No cuentan con ensayos ni literatura que evalúen directamente bromfenaco en esas condiciones, o su relación mecanística es implausible.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

