---
layout: default
title: Cladribine
parent: Solo Predicción del Modelo (L5)
nav_order: 161
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Cladribine: nueva indicación predicha, Rabdomiosarcoma embrionario parameníngeo (nivel de evidencia L5). Indicación original: CLADRIBINA"
monitor_inn: "Cladribine"
predicted_indications: ["parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "embryonal extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "rhabdomyosarcoma (disease)", "liver sarcoma"]
---

# Cladribine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Cladribina: De Indicación Original (CLADRIBINA) a Rabdomiosarcoma Embrionario Parameníngeo

## Resumen en Una Frase

Cladribina es un análogo de nucleósido de purina registrado en Colombia bajo los productos MAVENCLAD® (tableta) y LITAK® (solución inyectable); los registros sanitarios solo indican "CLADRIBINA" como indicación aprobada, sin detalle de la enfermedad.
El modelo TxGNN predice que podría ser efectivo para **rabdomiosarcoma embrionario parameníngeo**, pero actualmente no hay **ningún ensayo clínico** ni **publicación** que respalde esta predicción específica.
La única publicación asociada al conjunto de predicciones (un reporte de caso de 2004) corresponde a otra enfermedad (mastocitosis sistémica) y se vincula a la predicción de sarcoma hepático.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | CLADRIBINA (el registro no detalla la enfermedad) |
| Nueva Indicación Predicha | Rabdomiosarcoma embrionario parameníngeo |
| Puntaje de Predicción TxGNN | 99.77% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (0 vigentes, 2 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la cladribina (2-clorodesoxiadenosina) es un análogo de nucleósido de purina resistente a la adenosina desaminasa. Tras ser fosforilada por la desoxicitidina cinasa, se acumula como trifosfato e interfiere con la síntesis y reparación del ADN.

Este es un mecanismo citotóxico general plausible. Sin embargo, su actividad principal se da en células linfoides, que tienen alta actividad de desoxicitidina cinasa y baja actividad de 5'-nucleotidasa. Su actividad establecida es en neoplasias linfoides (como la leucemia de células pilosas) y en esclerosis múltiple. El rabdomiosarcoma, en cambio, es un tumor sólido de origen mesenquimal.

No se identificó un vínculo específico con la biología del rabdomiosarcoma embrionario. El puntaje alto de TxGNN (0.998) es solo una predicción computacional. Además, las siete predicciones principales (varios subtipos de rabdomiosarcoma, el término general y sarcoma hepático) probablemente están correlacionadas por cercanía en la ontología de enfermedades, por lo que no constituyen confirmaciones independientes.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Para la predicción principal (rabdomiosarcoma embrionario parameníngeo) actualmente no hay literatura relacionada disponible.

Entre las demás predicciones, solo sarcoma hepático (posición 7) tiene un registro, que no corresponde a la enfermedad predicha:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [15241520](https://pubmed.ncbi.nlm.nih.gov/15241520/) | 2004 | Reporte de caso | Der Hautarzt | Terapia exitosa con cladribina en mastocitosis sistémica indolente ("smoldering"); es otra enfermedad y solo aporta evidencia indirecta de actividad en neoplasias hematológicas |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20141389 | MAVENCLAD® | Tableta | CLADRIBINA | Cancelado |
| 20036307 | LITAK® | Solución inyectable | CLADRIBINA | Cancelado |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (análogo de nucleósido de purina / antimetabolito) |
| Riesgo de Mielosupresión | Alto, de acuerdo con las asociaciones de contraindicación del grafo de conocimiento (neutropenia, trombocitopenia, agranulocitosis, anemia) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, función renal y hepática, función neurológica (neuropatía periférica) |
| Protección en Manejo | Seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Contraindicaciones o condiciones de riesgo (según el grafo de conocimiento TxGNN, no texto de prospecto):** enfermedad renal, piouréter, trombocitopenia, neutropenia, agranulocitosis, anemia (incluida la macrocítica), enfermedad del sistema nervioso periférico, neuropatía periférica e hiperuricemia.
- **Interacciones Farmacológicas:** se consultaron 100 interacciones; las principales son:
  - **Mayor:** corticosteroides (hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida, prednisolona, prednisona), deferiprona, ibritumomab tiuxetán, iobenguano (I-131), tositumomab (con y sin I-131), samario (153Sm) lexidronam y cloruro de estroncio Sr-89.
  - **Moderada:** palifermina, dipiridamol, cilostazol y eltrombopag.
  - **Desconocida:** ácido acetilsalicílico.

No se dispone de advertencias ni contraindicaciones del prospecto de INVIMA; es necesario consultarlo.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura específica, y con un mecanismo solo genérico. Además, ambos registros en Colombia están cancelados y el perfil de seguridad (mielosupresión, neurotoxicidad) exige cautela.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), una brecha bloqueante para el tamizaje de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar estudios preclínicos de cladribina en modelos de rabdomiosarcoma (líneas celulares, expresión de desoxicitidina cinasa).
- Revisar la literatura y los registros de ensayos clínicos sobre análogos de purina en sarcomas de tejidos blandos pediátricos.
- Aclarar la situación regulatoria (registros cancelados) y la compatibilidad de vía de administración si se avanza.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

