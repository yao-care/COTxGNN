---
layout: default
title: Procaine
parent: Evidencia Moderada (L3-L4)
nav_order: 536
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Procaine: nueva indicación predicha, Metahemoglobinemia (nivel de evidencia L4). Indicación original: Procaína"
monitor_inn: "procaine"
predicted_indications: ["methemoglobinemia", "methemoglobinemia, alpha type", "Tourette syndrome", "anaphylaxis", "methemoglobin reductase deficiency", "hyperthyroidism", "fibromyalgia", "tendinitis", "myositis fibrosa", "idiopathic granulomatous myositis"]
---

# Procaine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

## Procaína: De Anestesia Local a Metahemoglobinemia
{: .text-alpha }

## Resumen en Una Frase

La procaína es un anestésico local de tipo éster, registrado en Colombia con la indicación "procaína" (solución inyectable de uso odontológico).
El modelo TxGNN predice que podría ser efectiva para **metahemoglobinemia**, pero la literatura disponible (**5 publicaciones**, sin ensayos clínicos) describe a la procaína como **causa** de esta condición y no como tratamiento, por lo que la predicción no tiene respaldo terapéutico.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Procaína (el registro no detalla una indicación clínica específica; es un anestésico local) |
| Nueva Indicación Predicha | Metahemoglobinemia |
| Puntaje de Predicción TxGNN | 0.9950 |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según el conocimiento general, la procaína es un anestésico local que bloquea canales de sodio y, por ello, interrumpe la conducción nerviosa. Los datos farmacológicos compilados la vinculan además con los receptores de rianodina RyR1 y RyR2, aunque sin datos de bioactividad que confirmen un blanco principal.

**La predicción no parece razonable desde el punto de vista terapéutico.** La literatura identificada (PMID 5529388 y 14246695) describe la metahemoglobinemia como un efecto adverso de la procaína y de otros anestésicos locales como la lignocaína. El puntaje alto proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica, y no un beneficio terapéutico. Usar procaína en esta indicación podría empeorar los niveles de metahemoglobina.

Las demás predicciones de mayor rango siguen un patrón similar. La metahemoglobinemia tipo alfa y la deficiencia de metahemoglobina reductasa carecen de evidencia y también son mecanísticamente implausibles. En anafilaxia, la literatura documenta a la procaína como desencadenante. Las únicas líneas con cierta plausibilidad mecanística son el dolor miofascial/fibromialgia y la tendinitis (infiltración anestésica, bloqueo de la nocicepción), aunque con evidencia limitada.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [5529388](https://pubmed.ncbi.nlm.nih.gov/5529388/) | 1970 | Reporte de caso | Acta physiologica latino americana | Metahemoglobinemia causada por procaína intravenosa |
| [14246695](https://pubmed.ncbi.nlm.nih.gov/14246695/) | 1965 | Reporte de caso | Lancet | Metahemoglobinemia tras el uso de lignocaína |
| [3691245](https://pubmed.ncbi.nlm.nih.gov/3691245/) | 1987 | Estudio observacional | Zhonghua Wai Ke Za Zhi | Efecto de la anestesia con procaína intravenosa sobre los niveles de metahemoglobina |
| [6705717](https://pubmed.ncbi.nlm.nih.gov/6705717/) | 1984 | Revisión | Drugs | Uso racional de anestésicos locales (revisión general) |
| [5644303](https://pubmed.ncbi.nlm.nih.gov/5644303/) | 1968 | Estudio farmacocinético | Am J Obstet Gynecol | Paso de procaína y ácido para-aminobenzoico a través de la placenta humana |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20026717 (cancelado) | SATYA®AL 1% | Solución inyectable | Procaína |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas por el grafo de conocimiento (no provienen del prospecto):** síndrome de QT largo (incluida la forma familiar), torsades de pointes, bloqueo auriculoventricular, enfermedad cardiovascular y cardíaca, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, lupus eritematoso sistémico, deficiencia de potasio, trastornos hipotensivos, miastenia gravis y enfermedad de la unión neuromuscular, deficiencia de butirilcolinesterasa, agranulocitosis y neutropenias (incluidas formas congénitas), colitis por *Clostridium difficile* y enterocolitis necrosante perinatal.
- **Interacciones farmacológicas (15 registradas):**
  - *Mayor:* ácido nitroso.
  - *Moderadas:* sulfasalazina y otros anestésicos locales (lidocaína tópica y oftálmica, benzocaína, cocaína tópica y nasal, tetracaína, oxibuprocaína, cinchocaína).
  - *Menores:* laronidasa, hialuronidasa, doxorrubicina (incluida la liposomal).
- **Reacciones adversas descritas en la literatura:** metahemoglobinemia, reacciones alérgicas y pseudoalérgicas (síndrome de Hoigné, dermatitis de contacto) y anafilaxia.

No se dispone de las advertencias y contraindicaciones del prospecto; se recomienda consultarlo.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La literatura sobre metahemoglobinemia indica que la procaína es una causa de la condición y no un tratamiento, por lo que el puntaje del modelo no se traduce en beneficio terapéutico. Además, no existen ensayos clínicos, el único registro sanitario colombiano está cancelado y faltan datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Descartar formalmente esta predicción para metahemoglobinemia, anafilaxia y deficiencia de metahemoglobina reductasa, por riesgo de empeorar la condición.
- Si se desea explorar la procaína, redirigir el análisis hacia indicaciones con plausibilidad mecanística (fibromialgia/dolor miofascial y tendinopatía). Para ello se requieren ensayos controlados modernos; el estudio de 2022 sobre terapia neural en tendinopatía del supraespinoso (PMID 35480510) es un punto de partida.
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones).
- Completar los datos del mecanismo de acción desde DrugBank.
- Verificar la situación regulatoria: no hay registros vigentes en Colombia, por lo que cualquier uso requeriría un nuevo registro o una vía alternativa.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

