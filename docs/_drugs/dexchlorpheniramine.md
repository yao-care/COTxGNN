---
layout: default
title: Dexchlorpheniramine
parent: Evidencia Moderada (L3-L4)
nav_order: 209
evidence_level: L3
indication_count: 2
last_modified_at: 2026-10-14
description: "Dexchlorpheniramine: nueva indicación predicha, Urticaria alérgica (nivel de evidencia L3). Indicación original: Paracetamol combinaciones excluyendo sicolépticos"
---

# Dexchlorpheniramine
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **2** 
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

## Dexclorfeniramina: De Combinaciones de Paracetamol (excluyendo psicolépticos) a Urticaria Alérgica
{: .text-alpha }

## Resumen en Una Frase

Dexclorfeniramina es un antihistamínico H1 de primera generación; en Colombia su único registro sanitario conocido (una solución oral pediátrica combinada con acetaminofén) figura como "combinaciones de paracetamol excluyendo psicolépticos".
El modelo TxGNN predice que podría ser efectivo para **urticaria alérgica**,
con **0 ensayos clínicos** y **3 publicaciones** (solo una de ellas, un estudio farmacodinámico, usa directamente dexclorfeniramina como comparador) que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Paracetamol combinaciones excluyendo sicolépticos |
| Nueva Indicación Predicha | Urticaria alérgica |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los registros compilados. Según el conocimiento farmacológico general, la dexclorfeniramina es un antagonista (agonista inverso) del receptor de histamina H1 de primera generación. Su indicación registrada en Colombia se refiere a la combinación con paracetamol y no refleja su actividad antihistamínica.

En la urticaria alérgica, la histamina liberada por los mastocitos es el principal mediador de ronchas, eritema y prurito. Por ello, el bloqueo H1 es un mecanismo directo y coherente con el alto puntaje de TxGNN (99.89%).

Conviene matizar que esto se parece más a un uso propio de la clase antihistamínica que a un reposicionamiento verdadero. La pregunta abierta es si los agentes de primera generación ofrecen alguna ventaja frente a los de segunda generación, dada su carga sedante y anticolinérgica.

Como segunda predicción, la **urticaria por frío** (puntaje 99.61%) es biológicamente plausible por el mismo mecanismo, pero no cuenta con ensayos ni literatura en los datos compilados, por lo que es solo una predicción computacional (nivel L5, Hold).

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39265704](https://pubmed.ncbi.nlm.nih.gov/39265704/) | 2024 | Ensayo aleatorizado de fase I (farmacodinámico) | Eur J Pharm Sci | Compara la inhibición de la roncha y el eritema inducidos por histamina entre bilastina oral, dexclorfeniramina parenteral (comparador) y una nueva formulación parenteral de bilastina |
| [29723372](https://pubmed.ncbi.nlm.nih.gov/29723372/) | 2018 | Estudio farmacodinámico | An Bras Dermatol | Evalúa la supresión de roncha y eritema en la prueba de histamina por los principales antihistamínicos H1 comercializados en Brasil |
| [39803](https://pubmed.ncbi.nlm.nih.gov/39803/) | 1979 | Estudio clínico-inmunológico / serie de casos | Dermatologica | Describe un caso de urticaria por contacto con calor adquirida; su relación con la dexclorfeniramina no puede confirmarse solo con el título |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 50400 (cancelado) | CORICIDIN® GOTAS PEDIATRICAS CON ACETAMINOFEN (BAYER S.A.) | Solución oral | PARACETAMOL COMBINACIONES EXCLUYENDO SICOLEPTICOS |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento (no provienen del prospecto):** el grafo de conocimiento TxGNN asocia el fármaco con contraindicación en las siguientes condiciones:
  - Cardiovasculares: hipertensión, hipotensión, enfermedad coronaria, infarto de miocardio, trombosis coronaria, aterosclerosis coronaria y arteriosclerosis.
  - Hepáticas, renales y digestivas: insuficiencia y enfermedad hepática, enfermedad renal, pancreatitis, enfermedad de la vesícula biliar, úlcera gástrica y péptica, enfermedad inflamatoria intestinal, colitis por *Clostridium difficile* y enterocolitis necrotizante perinatal.
  - Endocrinas y metabólicas: hipotiroidismo (incluidos mixedema y congénito), diabetes mellitus y cetoacidosis diabética.
  - Otras: epilepsia, hiperplasia prostática benigna, hipertensión ocular, hemoglobinopatías, piourete y abuso/dependencia de sustancias.
- **Interacciones farmacológicas:** no se encontraron interacciones registradas en la consulta realizada.

Consultar el prospecto para las advertencias y contraindicaciones oficiales, que no están disponibles en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia para urticaria alérgica es de nivel L3 y se limita a estudios farmacodinámicos en los que la dexclorfeniramina es sobre todo un comparador, sin ensayos clínicos registrados. Además, el único registro sanitario en Colombia está cancelado y no hay datos oficiales de seguridad.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones oficiales), un vacío de información que bloquea el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Buscar ensayos clínicos o revisiones sistemáticas que comparen específicamente la dexclorfeniramina con antihistamínicos de segunda generación en urticaria.
- Evaluar la compatibilidad de vías y formas farmacéuticas disponibles, dado que no hay productos vigentes en el país.
- Para urticaria por frío, verificar la literatura de forma independiente antes de cualquier consideración.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

