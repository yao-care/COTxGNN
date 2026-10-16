---
layout: default
title: Phenytoin
parent: Solo Predicción del Modelo (L5)
nav_order: 514
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Phenytoin: nueva indicación predicha, Neoplasia del nervio trigémino (nivel de evidencia L5). Indicación original: Fenitoína"
---

# Phenytoin
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

# Fenitoína: De Fenitoína (registro INVIMA) a Neoplasia del Nervio Trigémino

## Resumen en Una Frase

La fenitoína es un fármaco anticonvulsivante, registrado en Colombia bajo el nombre EPAMIN® PARENTERICO (solución inyectable), cuyo registro sanitario figura actualmente como cancelado.
El modelo TxGNN predice que podría ser efectivo para **neoplasia del nervio trigémino**, pero **no hay ensayos clínicos** y solo **2 publicaciones** relacionadas, ninguna sobre tratamiento de tumores.
La predicción debe considerarse con mucha cautela: probablemente refleja la cercanía en el grafo de conocimiento con la neuralgia del trigémino y no un efecto antitumoral.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Fenitoína (el texto del registro INVIMA no detalla la indicación) |
| Nueva Indicación Predicha | Neoplasia del nervio trigémino |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo cancelado (sin registros vigentes) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, la fenitoína es un anticonvulsivante que bloquea los canales de sodio dependientes de voltaje, lo que reduce la descarga neuronal repetitiva y la propagación de las crisis.

La relación con la nueva indicación es débil. La fenitoína se usa en dolor del nervio trigémino (neuralgia), pero no hay evidencia de que actúe sobre tejido tumoral. El puntaje alto del modelo probablemente refleja la proximidad en el grafo entre "nervio trigémino" y la neuralgia del trigémino, no un efecto antineoplásico. Las dos publicaciones recuperadas tratan sobre neuralgia del trigémino y síndrome de Sturge-Weber, no sobre el tratamiento de neoplasias.

Por ello, desde el punto de vista mecanístico, esta predicción no está respaldada. Dentro de las predicciones del modelo, la **neuralgia del trigémino** (puntaje 99.97%, nivel L3) es la candidata con evidencia más sólida y coherente con el mecanismo del fármaco.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Revisión | Expert Review of Neurotherapeutics | Revisión de los múltiples tratamientos médicos y quirúrgicos de la neuralgia del trigémino; no aborda neoplasias |
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Serie de casos | Anales Españoles de Pediatría | Experiencia con 14 casos de síndrome de Sturge-Weber; no trata neoplasias del trigémino |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 24335 (cancelado) | EPAMIN® PARENTERICO 50 MG/ML X 5 ML | Solución inyectable | Fenitoína |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): síndrome de QT largo (incluido el familiar), torsades de pointes, insuficiencia y enfermedad hepática, encefalopatía y coma hepático, enfermedad renal, porfiria (incluida la hereditaria), enfermedad de la vesícula biliar, trombocitopenia, neutropenia, agranulocitosis, hiperglucemia, diabetes mellitus y cetoacidosis diabética, lupus eritematoso sistémico, trastornos hipotensivos, trastornos de ansiedad y neuróticos, trastorno distímico, abuso o dependencia de sustancias, apnea del sueño y síndromes de hipoventilación.
- **Interacciones farmacológicas**: se identificaron 390 interacciones. Entre las listadas, la mayoría son de nivel moderado: acarbosa, famotidina, ranitidina, doxiciclina, hidrocortisona, albiglutida, colecalciferol, alogliptina, metformina, pioglitazona, bupropión, aprepitant, triamcinolona, morfina, omeprazol, dexametasona, betametasona, metronidazol y calcifediol. La interacción con ácido acetilsalicílico es de nivel menor.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos y la literatura recuperada no aborda el tratamiento de neoplasias del nervio trigémino. No hay vínculo mecanístico plausible con un efecto antitumoral, por lo que el puntaje del modelo parece un artefacto del grafo. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Priorizar la evaluación de **neuralgia del trigémino** (nivel L3), que es la indicación mejor respaldada, en lugar de la neoplasia.
- Datos del mecanismo de acción confirmados desde DrugBank.
- Prospecto de INVIMA con advertencias y contraindicaciones oficiales, necesario para cualquier evaluación de seguridad.
- Aclarar la situación regulatoria: no hay registro vigente de fenitoína inyectable en los datos compilados.
- Evidencia directa (preclínica o clínica) de actividad de la fenitoína en tumores del nervio trigémino, si se desea mantener esta hipótesis.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

