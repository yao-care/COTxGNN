---
layout: default
title: Ranitidine
parent: Solo Predicción del Modelo (L5)
nav_order: 549
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ranitidine: nueva indicación predicha, Enfermedad ulcerosa péptica activa (nivel de evidencia L5). Indicación original: RANITIDINA"
monitor_inn: "ranitidine"
predicted_indications: ["peptic ulcer perforation", "duodenal obstruction", "gastroduodenitis", "Smouldering systemic mastocytosis", "abnormality of glucagon secretion", "lymphoadenopathic mastocytosis with eosinophilia"]
---

# Ranitidine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Ranitidina: De Indicación Registrada (Ranitidina) a Enfermedad Ulcerosa Péptica Activa

## Resumen en Una Frase

Ranitidina es un antagonista de los receptores H2 de histamina, registrado en Colombia en tabletas recubiertas de 150 mg y solución inyectable de 50 mg/2 mL. El texto de indicación de ambos registros solo repite el nombre del fármaco.
El modelo TxGNN predice que podría ser efectiva para la **enfermedad ulcerosa péptica activa**, aunque sin ensayos clínicos vinculados a esa predicción y con **20 publicaciones** de apoyo, en su mayoría revisiones narrativas.
Se trata de un uso de clase ya establecido más que de un reposicionamiento genuino, y el fármaco tiene los registros sanitarios cancelados en Colombia.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | RANITIDINA (el registro no detalla indicaciones; solo repite el nombre del producto) |
| Nueva Indicación Predicha | Enfermedad ulcerosa péptica activa |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L4 (sin ensayos clínicos vinculados; literatura compuesta sobre todo por revisiones) |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, ranitidina es un antagonista selectivo de los receptores H2 de histamina que reduce la secreción de ácido gástrico. Mecanísticamente, esto es aplicable a la enfermedad ulcerosa péptica.

La cicatrización de las úlceras depende en gran medida de la supresión del ácido, y la literatura recuperada describe el uso de ranitidina en úlcera duodenal y gástrica desde la década de 1980. Por ello, la predicción es coherente con un uso ya establecido de la clase, más que con una indicación nueva.

Hay límites importantes. La ranitidina fue retirada del mercado por preocupaciones de contaminación con NDMA, y los inhibidores de la bomba de protones han mostrado mayor eficacia en la cicatrización de úlceras. Por eso no se respalda un nuevo desarrollo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para la indicación principal (enfermedad ulcerosa péptica activa).

Para la entidad cercana "enfermedad ulcerosa péptica" (rango 7) sí hay ensayos, pero evalúan sobre todo otros fármacos (esomeprazol, omeprazol, YF476), con ranitidina como comparador, por lo que son evidencia indirecta:

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00633672](https://clinicaltrials.gov/study/NCT00633672) | Fase 3 | Completado | 400 | Esomeprazol 40 mg y 20 mg vs. ranitidina 150 mg c/12 h en úlceras gástricas asociadas a AINE |
| [NCT00633412](https://clinicaltrials.gov/study/NCT00633412) | Fase 3 | Completado | 400 | Diseño paralelo al anterior, solo en EE. UU. |
| [NCT00401752](https://clinicaltrials.gov/study/NCT00401752) | Fase 3 | Completado | 397 | Esomeprazol 20 mg vs. ranitidina 150 mg c/12 h durante 8 semanas, úlcera gástrica asociada a AINE |
| [NCT00247130](https://clinicaltrials.gov/study/NCT00247130) | Fase 4 | Retirado | 0 | Omeprazol vs. ranitidina intravenosos tras hemostasia endoscópica; sin participantes, sin datos |
| [NCT01538797](https://clinicaltrials.gov/study/NCT01538797) | Fase 1 | Completado | 22 | YF476 vs. placebo y ranitidina sobre el pH gástrico en voluntarios sanos |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [6317325](https://pubmed.ncbi.nlm.nih.gov/6317325/) | 1983 | Revisión | Drug Intell Clin Pharm | Ranitidina es 4 a 10 veces más potente que cimetidina para inhibir la secreción ácida y es igual de eficaz en úlcera duodenal |
| [2905237](https://pubmed.ncbi.nlm.nih.gov/2905237/) | 1988 | Revisión | Drugs | Prostaglandinas, antagonistas H2 y enfermedad ulcerosa péptica |
| [9506245](https://pubmed.ncbi.nlm.nih.gov/9506245/) | 1998 | Revisión | Drugs | Rabeprazol, inhibidor de la bomba de protones; más eficaz que placebo y famotidina en ensayos comparativos |
| [2905640](https://pubmed.ncbi.nlm.nih.gov/2905640/) | 1988 | Revisión | Drugs | Nizatidina en enfermedad ulcerosa péptica |
| [1717223](https://pubmed.ncbi.nlm.nih.gov/1717223/) | 1991 | Revisión | Drugs | Roxatidina, antagonista H2, en úlcera péptica |
| [3527658](https://pubmed.ncbi.nlm.nih.gov/3527658/) | 1986 | Revisión | Drugs | Omeprazol en úlcera péptica y síndrome de Zollinger-Ellison |
| [3909374](https://pubmed.ncbi.nlm.nih.gov/3909374/) | 1985 | Estudio clínico | Scand J Gastroenterol | Ranitidina 300 mg/día: cicatrización a 4 semanas de 91% en úlcera duodenal, 68% prepilórica y 81% gástrica; se evaluó la prevención de recaídas |
| [6317740](https://pubmed.ncbi.nlm.nih.gov/6317740/) | 1983 | Estudio farmacológico | J Clin Gastroenterol | Comparación farmacodinámica y farmacocinética de cimetidina y ranitidina |
| [2878343](https://pubmed.ncbi.nlm.nih.gov/2878343/) | 1986 | Revisión | Med Toxicol | Reacciones adversas e interacciones de los antagonistas H2, con baja toxicidad general |
| [11166000](https://pubmed.ncbi.nlm.nih.gov/11166000/) | 2001 | Comentario | Am J Med | H. pylori y AINE; omeprazol superó a una dosis ineficaz de ranitidina en prevención de úlceras |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 207409 | RANITIDINA TABLETAS RECUBIERTAS 150 MG | Tableta recubierta | RANITIDINA | Cancelado |
| 19924286 | RANITIDINA SOLUCIÓN INYECTABLE 50 MG/2ML | Solución inyectable | RANITIDINA | Cancelado |

---

## Consideraciones de Seguridad

- **Contraindicaciones en el grafo de conocimiento (no provienen del prospecto):** porfiria (hereditaria y trastornos del metabolismo de porfirinas), enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar y cáncer gástrico (incluyendo neoplasia gástrica, adenocarcinoma gástrico difuso, linitis plástica y carcinoma gástrico).
- **Interacciones farmacológicas:** se identificaron 585 interacciones. Entre las listadas:
  - **Mayor:** atazanavir.
  - **Moderada:** acalabrutinib, acetohexamida, aminofilina, bacampicilina, bosutinib, brigatinib, cefditoren, cefpodoxima, cefuroxima, ceritinib y clorpropamida.
  - **Menor:** paracetamol, ácido alendrónico, hidróxido de aluminio, atracurio, axitinib, carbonato de calcio, cisaprida y cisatracurio.
- Las advertencias y contraindicaciones del prospecto de INVIMA no están disponibles; consultar el prospecto.
- Además, la literatura y la justificación mencionan la retirada del mercado por preocupaciones de contaminación con NDMA.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación predicha corresponde a un uso de clase ya establecido, sin ensayos que evalúen a ranitidina como brazo de investigación, y con evidencia de nivel L4 compuesta sobre todo por revisiones antiguas. Además, los registros en Colombia están cancelados, los inhibidores de la bomba de protones son superiores y existe preocupación por NDMA, por lo que no se justifica un nuevo desarrollo.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción.
- Advertencias y contraindicaciones del prospecto de INVIMA (descarga y análisis del PDF).
- Evaluación del riesgo de NDMA y de la situación regulatoria.
- Comparación con alternativas vigentes (inhibidores de la bomba de protones, otros antagonistas H2 como famotidina).
- Otras predicciones del modelo, como mastocitosis (rangos 8 y 10), son solo teóricas, sin ensayos ni literatura, y no cambian la decisión.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

