---
layout: default
title: Dasatinib
parent: Solo Predicción del Modelo (L5)
nav_order: 197
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Dasatinib: nueva indicación predicha, Sarcoma de Ewing (nivel de evidencia L5). Indicación original: DASATINIB"
---

# Dasatinib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Dasatinib: De Indicación Original (sin texto descriptivo en el registro) a Sarcoma de Ewing

## Resumen en Una Frase

Dasatinib es un inhibidor oral de tirosina cinasas (BCR-ABL y familia SRC) con registros sanitarios en Colombia, aunque el texto de indicación registrado solo repite el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para **Sarcoma de Ewing**, con **2 ensayos clínicos** y **10 publicaciones** que actualmente respaldan esta dirección, de los cuales ninguno demuestra eficacia específica en esta enfermedad.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | DASATINIB (el registro no detalla una indicación específica) |
| Nueva Indicación Predicha | Sarcoma de Ewing |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L2 según la clasificación de los datos compilados; sin embargo, los ensayos son un ensayo de Fase 2 en sarcomas mixtos y un ensayo de Fase 1/2 terminado con 7 pacientes, por lo que la evidencia específica para Ewing es débil y se interpreta con cautela |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 3 (todos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según la información conocida, dasatinib es un inhibidor multicinasa que bloquea BCR-ABL y las cinasas de la familia SRC, además de c-KIT y PDGFR. Su eficacia está comprobada en leucemia mieloide crónica y en leucemia linfoblástica aguda Ph+.

En el sarcoma de Ewing, estudios preclínicos indican que la señalización Src/FAK impulsa la invasión, la migración y la formación de invadopodios. Dasatinib mostró actividad antiproliferativa y antimigratoria en líneas celulares de sarcoma de Ewing in vitro. Esto aporta un vínculo mecanístico plausible entre su acción sobre SRC y esta neoplasia.

Sin embargo, la plausibilidad biológica no ha sido confirmada en clínica. Una revisión de 2022 señala que dasatinib fracasó como agente único en el ensayo de Fase 2 en sarcomas avanzados, en los subtipos Ewing y rabdomiosarcoma. Las líneas de investigación actuales exploran combinaciones (por ejemplo, el esquema RIST: rapamicina, irinotecán, dasatinib y temozolomida).

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00464620](https://clinicaltrials.gov/study/NCT00464620) | Fase 2 | Completado | 366 | Respuesta y supervivencia libre de progresión a 6 meses con dasatinib en sarcomas avanzados; población mixta, sin eficacia específica en Ewing establecida |
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Fase 1/2 | Terminado | 7 | Dasatinib con ifosfamida, carboplatino y etopósido en población pediátrica; terminado con solo 7 pacientes, aporta información mínima |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35655525](https://pubmed.ncbi.nlm.nih.gov/35655525/) | 2022 | Revisión | Sarcoma | Dasatinib como agente único falló en Ewing y rabdomiosarcoma en el ensayo de Fase 2; se discute el blanco del complejo FAK-Src |
| [26170970](https://pubmed.ncbi.nlm.nih.gov/26170970/) | 2015 | Revisión | Oncology Letters | Importancia de la señalización Src en sarcomas y su viabilidad como blanco terapéutico |
| [42804591](https://pubmed.ncbi.nlm.nih.gov/42804591/) | 2026 | Serie de casos | J Pediatr Hematol Oncol | Experiencia descriptiva de un centro con el régimen RIST (incluye dasatinib) en sarcoma de Ewing recaído |
| [18202781](https://pubmed.ncbi.nlm.nih.gov/18202781/) | 2008 | In vitro | Oncology Reports | Actividad antiproliferativa y antimigratoria de dasatinib en líneas de neuroblastoma y sarcoma de Ewing |
| [17363602](https://pubmed.ncbi.nlm.nih.gov/17363602/) | 2007 | In vitro | Cancer Research | Dasatinib inhibe migración e invasión en líneas de sarcoma e induce apoptosis en sarcomas óseos dependientes de SRC |
| [27566104](https://pubmed.ncbi.nlm.nih.gov/27566104/) | 2016 | In vitro | Neoplasia | El estrés microambiental activa invadopodios y migración dependientes de Src en sarcoma de Ewing |
| [31521948](https://pubmed.ncbi.nlm.nih.gov/31521948/) | 2019 | In vitro | Neoplasia | Cooperación entre tenascina C y Src en la formación de invadopodios en sarcoma de Ewing |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20002502 | SPRYCEL 100 MG tableta recubierta (Bristol Myers Squibb) | Tableta recubierta | DASATINIB (cancelado) |
| 20187895 | DAKMIRED tabletas recubiertas 100 mg (Dr. Reddy's) | Tableta recubierta | DASATINIB (cancelado) |
| 20188738 | DAKMIRED tabletas recubiertas 70 mg (Dr. Reddy's) | Tableta recubierta | DASATINIB (cancelado) |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina cinasas multiobjetivo) |
| Riesgo de Mielosupresión | Alto: los datos de seguridad del grafo de conocimiento asocian el fármaco con trombocitopenia, neutropenia, agranulocitosis y anemia |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, función hepática, electrocardiograma (intervalo QT), electrolitos y vigilancia de derrame pleural/pericárdico |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

No se dispone de texto de prospecto en los datos compilados. A continuación se presentan las señales de seguridad disponibles.

- **Enfermedades asociadas a contraindicación (según el grafo de conocimiento TxGNN/PrimeKG, no texto de etiqueta):**
  - Cardiovasculares: síndrome de QT largo (incluido el familiar), torsades de pointes, insuficiencia cardíaca congestiva, infarto de miocardio, trombosis coronaria, derrame pericárdico y hemopericardio.
  - Hematológicas: trombocitopenia, neutropenia, agranulocitosis, anemia (incluida la macrocítica) y hemoglobinopatía.
  - Digestivas y hepáticas: enfermedad hepática, enfermedad de la vesícula biliar y úlcera péptica activa.
  - Neurológicas: hemorragia intracerebral.
- **Interacciones farmacológicas (100 registradas; se muestran las principales):**
  - Gravedad mayor: famotidina, ranitidina, cimetidina, rabeprazol, omeprazol (los antiácidos y supresores de ácido pueden reducir la absorción de dasatinib), dexametasona, ácido acetilsalicílico y claritromicina.
  - Gravedad moderada: hidrocortisona, budesonida, loperamida, aprepitant, bisacodilo, óxido de magnesio, hidróxido de aluminio, carbonato de calcio, saxagliptina, aceite de ricino y polietilenglicol.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Existe un vínculo mecanístico plausible (inhibición de SRC) y apoyo preclínico en sarcoma de Ewing, pero la evidencia clínica es débil: un ensayo de Fase 2 en sarcomas mixtos que no demostró eficacia como agente único en Ewing, y un ensayo pediátrico terminado con 7 pacientes. Además, los tres registros sanitarios en Colombia están cancelados y no hay datos de prospecto.

**Para avanzar se necesita:**
- Datos de eficacia específicos de sarcoma de Ewing, preferiblemente de combinaciones (por ejemplo, el régimen RIST) en estudios prospectivos.
- Datos del mecanismo de acción confirmados desde DrugBank.
- Prospecto de INVIMA con advertencias y contraindicaciones para completar el análisis de seguridad.
- Aclarar la situación regulatoria en Colombia (todos los registros cancelados) y la disponibilidad real del producto.
- Plan de monitoreo de seguridad hematológica y cardiovascular.

---

### Nota sobre otras indicaciones predichas

La segunda predicción, **leucemia mieloide** (puntaje 99.68%, nivel de evidencia L1, recomendación "Proceed with Guardrails"), cuenta con ensayos de Fase 3 completados (por ejemplo, DASISION) y un ensayo de Fase 3 en leucemia mieloide aguda con factor de unión al núcleo. Sin embargo, el uso en leucemia mieloide crónica es en esencia una indicación original y no un reposicionamiento genuino; el valor de reposicionamiento reside en subtipos de leucemia mieloide aguda. Las demás predicciones (liposarcoma, dermatofibrosarcoma protuberans y otras) tienen evidencia nula o solo preclínica (L4-L5) y se mantienen en Hold.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

