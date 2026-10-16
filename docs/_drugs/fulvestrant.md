---
layout: default
title: Fulvestrant
parent: Evidencia Moderada (L3-L4)
nav_order: 304
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Fulvestrant: nueva indicación predicha, Infección por VIH (HIV infectious disease) (nivel de evidencia L4). Indicación original: FLUVESTRANT"
monitor_inn: "FULVESTRANT"
predicted_indications: ["HIV infectious disease", "multiple endocrine neoplasia", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "rheumatoid arthritis", "acne (disease)", "brachydactyly-syndactyly syndrome", "hemoglobinopathy", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
---

# Fulvestrant
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Fulvestrant: De Indicación Registrada (texto "FLUVESTRANT") a Infección por VIH

## Resumen en Una Frase

Fulvestrant es un antagonista y degradador del receptor de estrógenos, utilizado en cáncer de mama con receptores hormonales positivos. En Colombia, el texto de indicación de sus registros sanitarios figura únicamente como "FLUVESTRANT" (un error de transcripción del nombre del fármaco).
El modelo TxGNN predice que podría ser efectivo para **infección por VIH** (enfermedad infecciosa), pero actualmente **no hay ensayos clínicos** y solo **2 publicaciones** relacionadas, una de ellas preclínica in vitro y la otra sobre otro retrovirus (HTLV-1), por lo que la evidencia es muy limitada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | FLUVESTRANT (texto del registro INVIMA, sin una indicación clínica descrita) |
| Nueva Indicación Predicha | Infección por VIH (HIV infectious disease) |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (0 vigentes, 2 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, fulvestrant es un antagonista del receptor de estrógenos alfa (ERα) que además favorece su degradación, y su eficacia en cáncer de mama con receptores hormonales positivos está bien establecida. Esta descripción proviene del conocimiento general del fármaco y no de los datos compilados.

El vínculo con el VIH es indirecto. El ERα se expresa en los linfocitos T CD4+ y se ha planteado que podría influir en la transcripción y la latencia del VIH. Un estudio de 2026 evaluó cómo interactúan los ligandos del ERα (incluido fulvestrant) y los agentes reversores de latencia en estas células. Esto sugiere que fulvestrant podría modular la reversión de la latencia viral, pero se trata de evidencia preclínica in vitro, sin datos en humanos.

La otra publicación identificada trata sobre la mielopatía asociada a HTLV-1, un retrovirus distinto del VIH, por lo que no constituye evidencia directa. La relación entre la indicación original (oncología hormonal) y la nueva (infección viral) es por tanto débil y se apoya sobre todo en similitudes del grafo de conocimiento.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [42430506](https://pubmed.ncbi.nlm.nih.gov/42430506/) | 2026 | Estudio preclínico in vitro | JCI Insight | Evalúa el efecto del estrógeno, de fulvestrant y de los agentes reversores de latencia del VIH sobre el ERα en linfocitos T CD4+; apunta a un posible papel del ER en la latencia del VIH |
| [40343334](https://pubmed.ncbi.nlm.nih.gov/40343334/) | 2025 | Análisis ómico multicohorte | Research Square | Estudio de mecanismos y dianas terapéuticas en la mielopatía asociada a HTLV-1; es un retrovirus distinto y no aporta evidencia directa sobre el VIH |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20190314 (cancelado) | FULVESANT® 250 MG/5 ML | Solución inyectable | FLUVESTRANT |
| 19955642 (cancelado) | FASLODEX® 250 MG / 5 ML | Solución inyectable | FLUVESTRANT |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia hormonal (antagonista y degradador del receptor de estrógenos); no es un citotóxico convencional |
| Riesgo de Mielosupresión | Bajo en general; sin embargo, el grafo de conocimiento lista la trombocitopenia entre las enfermedades contraindicadas, por lo que se recomienda precaución |
| Clasificación de Emetogenicidad | Baja |
| Ítems de Monitoreo | Hemograma con recuento de plaquetas, función hepática, parámetros de coagulación |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas por el grafo de conocimiento** (aristas fármaco-enfermedad de PrimeKG, no texto del prospecto): enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia y trastornos de la coagulación sanguínea.
- **Interacciones farmacológicas**: se identificaron 92 posibles interacciones, todas con nivel de gravedad desconocido. Entre las principales figuran warfarina (relevante por el riesgo hemorrágico, dado que se administra por vía intramuscular), metformina, simvastatina, ácido acetilsalicílico, dexametasona, prednisona, omeprazol, pantoprazol, ondansetrón y morfina.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para VIH tiene un puntaje alto en el modelo, pero solo cuenta con un estudio preclínico in vitro y sin ensayos clínicos, lo que corresponde a un nivel de evidencia L4. Además, los registros sanitarios en Colombia están cancelados y la indicación registrada está mal transcrita.

**Para avanzar se necesita:**
- Datos de mecanismo de acción confirmados, por ejemplo mediante consulta a DrugBank.
- Estudios preclínicos adicionales (in vitro e in vivo) sobre fulvestrant y la latencia del VIH, con replicación independiente.
- Obtener y revisar el prospecto de INVIMA para completar las advertencias y contraindicaciones, ya que esta brecha impide avanzar al tamizaje de seguridad.
- Aclarar la situación regulatoria en Colombia, dado que ambos registros están cancelados.
- Evaluar si el posible efecto de reversión de latencia tiene sentido clínico, pues el bloqueo estrogénico podría tener efectos inmunológicos no deseados.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

