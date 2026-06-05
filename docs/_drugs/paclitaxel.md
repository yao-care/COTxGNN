---
layout: default
title: Paclitaxel
parent: 僅模型預測 (L5)
nav_order: 187
evidence_level: L5
indication_count: 10
---

# Paclitaxel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Paclitaxel: De Agente Antineoplásico (Taxano) a Carcinoma de Mama Femenino

## Resumen en Una Frase

Paclitaxel es un agente quimioterapéutico citotóxico de la clase taxano, ampliamente utilizado en el tratamiento de neoplasias malignas mediante la estabilización de microtúbulos e inducción de apoptosis.
El modelo TxGNN predice que podría ser efectivo para **Carcinoma de Mama Femenino**,
con **50 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin datos en registro consultado (base de datos INVIMA no reporta registros activos) |
| Nueva Indicación Predicha | Carcinoma de Mama Femenino |
| Puntaje de Predicción TxGNN | 99.995% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | Sin registro activo en base de datos consultada |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Paclitaxel es el representante más conocido de la clase taxano, cuyo mecanismo de acción se basa en la **estabilización de microtúbulos**: se une a la subunidad β de la tubulina e inhibe su despolimerización, lo que provoca la formación de haces anormales de microtúbulos, el arresto del ciclo celular en la transición G2/M y la activación de la vía apoptótica intrínseca. A diferencia de los agentes dirigidos, este mecanismo es independiente del estado de receptores hormonales (ER/PR) o HER2, lo que confiere amplitud de acción en todos los subtipos moleculares del carcinoma de mama.

Las células del carcinoma de mama presentan un índice proliferativo elevado —especialmente en subtipos de alto grado como triple negativo (TNBC) y luminal B—, lo que las convierte en blancos particularmente sensibles a los agentes mitóticos como paclitaxel. La relación entre su uso antineoplásico general y el carcinoma de mama femenino es directa: la dependencia de la maquinaria de división celular en tumores de alta proliferación es la base mecanística que sustenta tanto las predicciones del modelo TxGNN como la evidencia clínica acumulada.

Actualmente, paclitaxel es un componente estándar de los esquemas neoadyuvantes y adyuvantes para cáncer de mama a nivel mundial, confirmado en múltiples ensayos de Fase 3 completados que abarcan contextos HER2+, HER2−, ER+ y triple negativo. El puntaje de 99.995% del modelo TxGNN refleja con precisión la solidez de esta evidencia clínica robusta.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00281658](https://clinicaltrials.gov/study/NCT00281658) | Fase 3 | Completado | 444 | Lapatinib + paclitaxel vs. placebo + paclitaxel en cáncer de mama HER2+ metastásico; evaluación directa de eficacia de paclitaxel como backbone en primera línea metastásica |
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Fase 3 | Completado | 3270 | Terapia adyuvante con/sin trastuzumab tras quimioterapia incluyendo paclitaxel semanal en cáncer de mama HER2-low; mayor ensayo en términos de reclutamiento |
| [NCT00003088](https://clinicaltrials.gov/study/NCT00003088) | Fase 3 | Completado | 2005 | Quimioterapia secuencial (doxorrubicina → paclitaxel → ciclofosfamida) vs. concurrente en cáncer de mama con ganglios positivos estadio II/IIIA; estableció la secuencia óptima de administración |
| [NCT01901146](https://clinicaltrials.gov/study/NCT01901146) | Fase 3 | Completado | 725 | ABP 980 vs. trastuzumab en cáncer de mama temprano HER2+ con paclitaxel como backbone quimioterapéutico; eficacia y seguridad del biosimilar |
| [NCT00431080](https://clinicaltrials.gov/study/NCT00431080) | Fase 3 | Completado | 478 | Docetaxel vs. paclitaxel en quimioterapia adyuvante de alta densidad de dosis para cáncer de mama con ganglios axilares positivos |
| [NCT00513292](https://clinicaltrials.gov/study/NCT00513292) | Fase 3 | Completado | 280 | FEC → paclitaxel + trastuzumab vs. paclitaxel + trastuzumab → FEC + trastuzumab en cáncer de mama HER2+ operable; optimización del esquema neoadyuvante |
| [NCT00455533](https://clinicaltrials.gov/study/NCT00455533) | Fase 2 | Completado | 384 | Ixabepilona vs. paclitaxel como continuación de AC en neoadyuvancia; estudio aleatorizado de biomarcadores con paclitaxel como brazo control activo |
| [NCT00003992](https://clinicaltrials.gov/study/NCT00003992) | Fase 2 | Completado | 200 | Paclitaxel + trastuzumab adyuvante en cáncer de mama estadio II/IIIA HER2+; uno de los primeros ensayos en establecer la sinergia paclitaxel-trastuzumab |
| [NCT02280252](https://clinicaltrials.gov/study/NCT02280252) | Fase 2 | Completado | 69 | Paclitaxel concurrente con radioterapia en cáncer de mama localmente avanzado (LABC) en cohorte multiétnica multinacional; respuesta patológica y supervivencia |
| [NCT00272987](https://clinicaltrials.gov/study/NCT00272987) | Fase 3 | Terminado | 63 | Paclitaxel + trastuzumab + lapatinib vs. paclitaxel + trastuzumab en cáncer de mama HER2+ metastásico; terminado en fase de seguridad inicial (63/765 planeados) |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31783552](https://pubmed.ncbi.nlm.nih.gov/31783552/) | 2019 | Revisión | Biomolecules | Resumen integral del mecanismo de acción de paclitaxel (estabilización de microtúbulos, G2/M, apoptosis) y aplicaciones clínicas en cáncer de mama; análisis sistemático de mecanismos de resistencia |
| [39317691](https://pubmed.ncbi.nlm.nih.gov/39317691/) | 2024 | Revisión | Chem Biol Drug Des | Combinaciones terapéuticas con paclitaxel en carcinoma mamario; identificación computacional de pares sinérgicos e biomarcadores in vivo |
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | ECA | Cancer | Ensayo multicéntrico de Fase II: eficacia y toxicidad de doxorrubicina + paclitaxel en carcinoma mamario metastásico; tasa de respuesta objetiva documentada |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Revisión | Drug Ther Bull | Evaluación comparativa de paclitaxel y docetaxel en cáncer de mama y ovario; análisis del momento en que la licencia se extendió al carcinoma mamario metastásico |
| [32461977](https://pubmed.ncbi.nlm.nih.gov/32461977/) | 2020 | Cohorte | BioMed Res Int | Eficacia de EC + paclitaxel semanal + trastuzumab neoadyuvante en carcinoma mamario HER2+; tasa de respuesta patológica completa en práctica clínica real |
| [39009452](https://pubmed.ncbi.nlm.nih.gov/39009452/) | 2024 | Traslacional | J Immunother Cancer | Paclitaxel reprograma los macrófagos asociados al tumor potenciando el bloqueo de PD-1 en cáncer de mama triple negativo; mecanismo inmunomodulador adicional |
| [20665703](https://pubmed.ncbi.nlm.nih.gov/20665703/) | 2011 | In vitro + Clínico | J Cell Physiol | ZD6474 (inhibidor dual EGFR/VEGFR) potencia los efectos antiproliferativos y apoptóticos de paclitaxel en carcinoma mamario con sobreexpresión de EGFR |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | Genómica | Nat Commun | Variantes germinales TEKT4 enriquecidas en tumores post-tratamiento como mecanismo principal de resistencia a paclitaxel en cáncer de mama; implicaciones para selección de pacientes |
| [17272681](https://pubmed.ncbi.nlm.nih.gov/17272681/) | 2007 | Traslacional | Mol Pharmacol | Estatmina media resistencia a paclitaxel y vinblastina mediante despolimerización microtubular alterada; reversión de resistencia en líneas celulares de carcinoma mamario |
| [14508823](https://pubmed.ncbi.nlm.nih.gov/14508823/) | 2003 | Traslacional | Cancer | Trastuzumab + paclitaxel inhibe la angiogénesis mediada por ErbB-2 mediante supresión de Akt; efecto antiangiogénico superior al de cada agente por separado |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional — clase Taxano (inhibidor de la despolimerización de microtúbulos, agente antimicrotubular estabilizador) |
| Riesgo de Mielosupresión | **Alto** — neutropenia es la toxicidad limitante de dosis; leucopenia, trombocitopenia y anemia son frecuentes; riesgo de neutropenia febril requiere profilaxis con G-CSF en esquemas de alta densidad de dosis |
| Clasificación de Emetogenicidad | **Baja a moderada** — esquema semanal: bajo potencial emetogénico; esquema cada 3 semanas (175 mg/m²): potencial moderado; profilaxis antiemética de corto plazo recomendada |
| Ítems de Monitoreo | Hemograma completo con diferencial (antes de cada ciclo), función hepática (AST, ALT, fosfatasa alcalina, bilirrubina), función renal, evaluación de neuropatía periférica sensitiva/motora en cada visita |
| Protección en Manejo | Cumplimiento obligatorio de normativas de manejo de fármacos citotóxicos: preparación en cabina de bioseguridad clase II tipo B, equipo de protección personal (doble guante de nitrilo, bata impermeable de manga larga, protección ocular y respiratoria), protocolo de derrames disponible |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Múltiples ensayos de Fase 3 completados —con hasta 3.270 participantes— respaldan la eficacia y seguridad de paclitaxel en carcinoma de mama femenino en los contextos neoadyuvante, adyuvante y metastásico, abarcando todos los subtipos moleculares; el puntaje TxGNN de 99.995% refleja con precisión esta evidencia clínica consolidada a nivel global.

**Para avanzar se necesita:**
- Verificar directamente en INVIMA el estado actualizado de registros sanitarios para paclitaxel y sus formulaciones (convencional, nab-paclitaxel/Abraxane) en Colombia
- Completar el perfil de seguridad obteniendo el prospecto oficial: advertencias de caja negra (reacciones de hipersensibilidad severas, mielosupresión), contraindicaciones absolutas e interacciones farmacológicas relevantes
- Obtener datos del mecanismo de acción completo desde DrugBank para el análisis formal de relación mecanística
- Definir el subgrupo de pacientes objetivo (TNBC, HER2+, ER+/luminal B) que maximizará el impacto del plan de reposicionamiento en el contexto colombiano
- Evaluar la cadena de suministro y costos comparativos entre formulación convencional y nab-paclitaxel para acceso en el sistema de salud colombiano
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

