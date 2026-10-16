---
layout: default
title: Salmeterol
parent: Solo Predicción del Modelo (L5)
nav_order: 580
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Salmeterol: nueva indicación predicha, Bronquitis (nivel de evidencia L5). Indicación original: Salmeterol y fluticasona"
monitor_inn: "SALMETEROL"
predicted_indications: ["bronchitis", "respiratory malformation", "obstructive lung disease", "Rienhoff syndrome", "asthma", "asthma-related traits, susceptibility to", "atopic eczema"]
---

# Salmeterol
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

# Salmeterol: De Salmeterol y Fluticasona (Asma/EPOC) a Bronquitis

## Resumen en Una Frase

Salmeterol es un agonista beta2 de acción prolongada, registrado en Colombia en combinación con fluticasona (inhalador) para enfermedades obstructivas de las vías respiratorias.
El modelo TxGNN predice que podría ser efectivo para **bronquitis**, con **9 ensayos clínicos** y **20 publicaciones** que respaldan esta dirección. Se trata de un uso ya establecido de la clase (EPOC con bronquitis crónica), no de un reposicionamiento novedoso.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Salmeterol y fluticasona |
| Nueva Indicación Predicha | Bronquitis |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L1 (varios ECA de Fase 3 completados) |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados; 0 vigentes) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, salmeterol es un agonista beta2-adrenérgico de acción prolongada que relaja el músculo liso de las vías respiratorias y puede mejorar el aclaramiento mucociliar. Se combina con fluticasona, un corticosteroide inhalado que reduce la inflamación de las vías respiratorias.

La indicación original (salmeterol/fluticasona para enfermedad obstructiva de las vías respiratorias) y la bronquitis comparten el mismo sustrato fisiopatológico: obstrucción e inflamación bronquial. La bronquitis crónica forma parte del espectro de la EPOC, en la que esta combinación ya se usa. Por ello, la evidencia confirma principalmente el uso existente y no un hallazgo nuevo.

Un estudio aleatorizado pequeño (PMID 15970448) respalda además el efecto de salmeterol sobre el aclaramiento mucociliar y de la tos en bronquitis crónica.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00268177](https://clinicaltrials.gov/study/NCT00268177) | Fase 3 | Completado | 130 | Salmeterol/fluticasona 50/500 mcg vs. placebo: efecto antiinflamatorio bronquial en EPOC |
| [NCT00269087](https://clinicaltrials.gov/study/NCT00269087) | Fase 3 | Completado | 122 | Seguridad a largo plazo (56 semanas) de salmeterol/fluticasona en EPOC (bronquitis crónica y enfisema) |
| [NCT02173691](https://clinicaltrials.gov/study/NCT02173691) | Fase 3 | Completado | 584 | Tiotropio vs. salmeterol vs. placebo durante 6 meses en EPOC |
| [NCT00269126](https://clinicaltrials.gov/study/NCT00269126) | Fase 3 | Completado | 150 | Comparación de dos medicamentos en EPOC durante 18 semanas (relevancia probable, no verificada) |
| [NCT00064415](https://clinicaltrials.gov/study/NCT00064415) | Fase 3 | Completado | 799 | Seguridad crónica de arformoterol frente a control activo (probablemente salmeterol) en EPOC |
| [NCT00064402](https://clinicaltrials.gov/study/NCT00064402) | Fase 3 | Completado | 741 | Arformoterol vs. placebo y control activo en EPOC; evidencia indirecta |
| [NCT00403286](https://clinicaltrials.gov/study/NCT00403286) | Fase 2 | Completado | 457 | Búsqueda de dosis de fluticasona/formoterol frente a fluticasona/salmeterol en EPOC |
| [NCT01361984](https://clinicaltrials.gov/study/NCT01361984) | Fase 4 | Desconocido | 20 | Arformoterol nebulizado vs. salmeterol en polvo seco en EPOC; estudio pequeño |
| [NCT00233051](https://clinicaltrials.gov/study/NCT00233051) | NA | Terminado | 20 | Biomarcadores inflamatorios en esputo inducido en EPOC; valor limitado de eficacia |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [15970448](https://pubmed.ncbi.nlm.nih.gov/15970448/) | 2006 | ECA | Pulm Pharmacol Ther | Salmeterol vs. placebo sobre el aclaramiento mucociliar y de la tos en bronquitis crónica leve a moderada (n=14) |
| [17557771](https://pubmed.ncbi.nlm.nih.gov/17557771/) | 2007 | ECA | Thorax | Efecto de salmeterol/fluticasona sobre la inflamación de las vías respiratorias en EPOC |
| [12970006](https://pubmed.ncbi.nlm.nih.gov/12970006/) | 2003 | Estudio clínico | Chest | Eficacia y seguridad de fluticasona 250/salmeterol 50 en Diskus frente a placebo y componentes individuales en EPOC |
| [17196106](https://pubmed.ncbi.nlm.nih.gov/17196106/) | 2006 | Metaanálisis | Respir Res | Salmeterol 50 mcg dos veces al día mejora desenlaces clínicos en EPOC frente a placebo/tratamiento habitual |
| [15329047](https://pubmed.ncbi.nlm.nih.gov/15329047/) | 2004 | Revisión | Drugs | Salmeterol/fluticasona aprobado en EE. UU. para EPOC asociada a bronquitis crónica |
| [19210134](https://pubmed.ncbi.nlm.nih.gov/19210134/) | 2009 | Cohorte | Curr Med Res Opin | Uso de servicios y costos en bronquitis crónica con fluticasona/salmeterol frente a otras terapias inhaladas |
| [19124357](https://pubmed.ncbi.nlm.nih.gov/19124357/) | 2008 | Estudio clínico | Ther Adv Respir Dis | Seguridad y tolerancia a un año de arformoterol y salmeterol en EPOC |
| [12236842](https://pubmed.ncbi.nlm.nih.gov/12236842/) | 2002 | Revisión | Br J Clin Pharmacol | Efectos aditivos de salmeterol y formoterol sobre exacerbaciones y ahorro de corticosteroide inhalado |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20128097 (cancelado) | SEROHALE 125 SYNCHROBREATHE SB | Suspensión para inhalación | Salmeterol y fluticasona |
| 20128029 (cancelado) | SEROHALE 250 SYNCHROBREATHE SB | Suspensión para inhalación | Salmeterol y fluticasona |

Ambos registros pertenecen a CIPLA LTD y están cancelados; actualmente no hay registros vigentes.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no proviene del prospecto):** el modelo asocia salmeterol con hipertensión, síndrome de QT largo (incluida la forma familiar), epilepsia, hiperglucemia, queratitis por herpes simple, déficits de hormonas hipofisarias (hipopituitarismo, deficiencia de hormona de crecimiento, hipogonadismo hipogonadotrópico, síndrome de Kallmann, síndrome de Sheehan), enfermedad del timo y osteoporosis. Estas relaciones deben verificarse contra la información oficial del producto.
- **Interacciones farmacológicas:** se identificaron 100 interacciones. Entre las principales:
  - **Mayor:** claritromicina.
  - **Moderada:** acarbosa, isometepteno, famotidina, epinefrina, albiglutida, alogliptina, canagliflozina, clorpropamida, dapagliflozina, dietilpropión, dolasetrón, dulaglutida, empagliflozina.
  - **Menor:** hidrocortisona, triamcinolona, dexametasona, beclometasona, betametasona, budesonida.
- **Precaución de clase:** la monoterapia con agonistas beta2 de acción prolongada se asocia con mayor riesgo de eventos adversos graves en asma; debe usarse siempre junto con un corticosteroide inhalado.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Varios ECA de Fase 3 completados en EPOC (incluida bronquitis crónica) respaldan la combinación salmeterol/fluticasona, por lo que el nivel de evidencia es L1. Sin embargo, se trata de un uso de clase ya establecido y no de un reposicionamiento nuevo, y en Colombia no hay registros vigentes.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto oficial del INVIMA (advertencias y contraindicaciones), actualmente sin datos.
- Completar los datos de mecanismo de acción desde DrugBank.
- Definir la situación regulatoria: ambos registros están cancelados, por lo que se requeriría un nuevo registro o un producto alternativo vigente.
- Establecer salvaguardas de uso: siempre en combinación con corticosteroide inhalado, y monitoreo de riesgo cardiovascular (QT, hipertensión) y metabólico (glucemia).
- Distinguir la bronquitis crónica (dentro de EPOC) de otros cuadros bronquíticos, para los que la evidencia es menos directa.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

