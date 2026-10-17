---
layout: default
title: Vilanterol
parent: Evidencia Alta (L1-L2)
nav_order: 658
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Vilanterol: nueva indicación predicha, Enfermedad pulmonar obstructiva (nivel de evidencia L1). Indicación original: Vilanterol y bromuro de umeclidinio"
monitor_inn: "VILANTEROL"
predicted_indications: ["tracheal stenosis", "bronchial neoplasm (disease)", "respiratory malformation", "tracheal calcification", "laryngotracheitis"]
---

# Vilanterol
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

# Vilanterol: De Combinación Vilanterol/Bromuro de Umeclidinio a Enfermedad Pulmonar Obstructiva

## Resumen en Una Frase

Vilanterol es un agonista beta2 de acción prolongada (LABA), registrado en Colombia como parte de la combinación con bromuro de umeclidinio (ANORO® ELLIPTA®).
El modelo TxGNN predice que podría ser efectivo para **enfermedad pulmonar obstructiva**, con **28 ensayos clínicos** y **20 publicaciones** que respaldan esta dirección. Cabe señalar que esta predicción coincide en la práctica con el uso ya establecido del fármaco, por lo que no constituye un reposicionamiento en sentido estricto.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Vilanterol y bromuro de umeclidinio |
| Nueva Indicación Predicha | Enfermedad pulmonar obstructiva |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, vilanterol es un agonista beta2-adrenérgico de acción prolongada que relaja el músculo liso de las vías respiratorias y produce broncodilatación sostenida, con actividad de aproximadamente 24 horas que permite una sola dosis diaria.

La indicación original (combinación con umeclidinio, un antagonista muscarínico de acción prolongada) ya corresponde al tratamiento de mantenimiento de la EPOC. La enfermedad pulmonar obstructiva incluye la EPOC y el asma, por lo que la predicción del modelo es esencialmente una confirmación del uso aprobado en otros países, no una indicación nueva. Vilanterol también se ha estudiado combinado con furoato de fluticasona (FF/VI) y en terapia triple (FF/UMEC/VI).

Esto explica la solidez de la evidencia, pero también implica que el valor del análisis como reposicionamiento es limitado. El estado local de mercado (solo registro cancelado) puede afectar la disponibilidad en Colombia, aunque no la evidencia clínica.

---

## Evidencia de Ensayos Clínicos

Se muestran los ensayos más relevantes de los 28 identificados (priorizando fase 3 completados y con mayor relevancia directa).

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT05062304](https://clinicaltrials.gov/study/NCT05062304) | N/A (diseño de ECA fase 3 pivotal) | Completado | 17281 | IMPACT: terapia triple FF/UMEC/VI una vez al día frente a terapia dual en EPOC |
| [NCT03162055](https://clinicaltrials.gov/study/NCT03162055) | Fase 3 | Completado | 1119 | AERISTO: glicopirronio/formoterol vs. umeclidinio/vilanterol durante 24 semanas en EPOC moderada a muy grave |
| [NCT01777334](https://clinicaltrials.gov/study/NCT01777334) | Fase 3 | Completado | 905 | Umeclidinio/vilanterol vs. tiotropio durante 24 semanas en EPOC (FEV1 valle) |
| [NCT01342913](https://clinicaltrials.gov/study/NCT01342913) | Fase 3 | Completado | 528 | FF/VI una vez al día vs. salmeterol/fluticasona dos veces al día en EPOC (función pulmonar 24 h) |
| [NCT01323621](https://clinicaltrials.gov/study/NCT01323621) | Fase 3 | Completado | 512 | FF/VI 100/25 vs. fluticasona propionato/salmeterol en EPOC, perfil de 24 horas |
| [NCT02487446](https://clinicaltrials.gov/study/NCT02487446) | Fase 3 | Completado | 357 | Indacaterol/glicopirronio vs. umeclidinio/vilanterol en EPOC moderada a grave |
| [NCT01716520](https://clinicaltrials.gov/study/NCT01716520) | Fase 3 | Completado | 182 | Estudio cruzado de umeclidinio, vilanterol y su combinación en EPOC |
| [NCT01706198](https://clinicaltrials.gov/study/NCT01706198) | Fase 3 | Completado | 4233 | Efectividad de FF/VI frente al tratamiento habitual en asma durante 12 meses |
| [NCT02301975](https://clinicaltrials.gov/study/NCT02301975) | Fase 3 | Completado | 1526 | FF/VI vs. fluticasona/salmeterol en asma ya controlada (no inferioridad) |
| [NCT01686633](https://clinicaltrials.gov/study/NCT01686633) | Fase 3 | Completado | 1040 | FF/VI 200/25 y 100/25 vs. FF en asma persistente |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29668352](https://pubmed.ncbi.nlm.nih.gov/29668352/) | 2018 | ECA | N Engl J Med | Terapia triple en un solo inhalador frente a terapia dual en EPOC (IMPACT) |
| [28375647](https://pubmed.ncbi.nlm.nih.gov/28375647/) | 2017 | ECA | Am J Respir Crit Care Med | Estudio FULFIL: terapia triple una vez al día en EPOC |
| [32162970](https://pubmed.ncbi.nlm.nih.gov/32162970/) | 2020 | ECA (análisis post hoc) | Am J Respir Crit Care Med | Reducción de mortalidad por todas las causas con FF/UMEC/VI frente a UMEC/VI |
| [32918892](https://pubmed.ncbi.nlm.nih.gov/32918892/) | 2021 | ECA | Lancet Respir Med | CAPTAIN: FF/UMEC/VI vs. FF/VI en asma no controlada adecuadamente (fase 3A) |
| [35849317](https://pubmed.ncbi.nlm.nih.gov/35849317/) | 2022 | Metaanálisis en red | Adv Ther | Comparación de FF/UMEC/VI con otras terapias duales y triples en EPOC |
| [39696097](https://pubmed.ncbi.nlm.nih.gov/39696097/) | 2024 | Revisión sistemática y metaanálisis | BMC Pulm Med | Eficacia comparativa de umeclidinio/vilanterol frente a otros broncodilatadores en EPOC |
| [31389190](https://pubmed.ncbi.nlm.nih.gov/31389190/) | 2019 | Revisión sistemática | Clin Respir J | Combinación fija umeclidinio/vilanterol en pacientes con EPOC |
| [39797646](https://pubmed.ncbi.nlm.nih.gov/39797646/) | 2024 | Estudio de cohorte | BMJ | Efectividad y seguridad comparada de terapias triples en un solo inhalador en la práctica clínica |
| [41729543](https://pubmed.ncbi.nlm.nih.gov/41729543/) | 2026 | Efectividad comparada | JAMA Intern Med | Efectividad y seguridad de inhaladores LAMA-LABA en EPOC |
| [24909949](https://pubmed.ncbi.nlm.nih.gov/24909949/) | 2014 | Revisión | Expert Rev Clin Pharmacol | Umeclidinio y vilanterol combinados: mejora de FEV1 frente a cada fármaco por separado |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20073341 (cancelado) | ANORO® ELLIPTA® | Polvo para inhalación | Vilanterol y bromuro de umeclidinio |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones, de las cuales se muestran las primeras 20 revisadas:
  - **Moderadas**: antidiabéticos (acarbosa, albiglutida, alogliptina, canagliflozina, clorpropamida, dapagliflozina, dulaglutida, empagliflozina), simpaticomiméticos (efedrina, epinefrina, dietilpropión), y fármacos que prolongan el intervalo QT o se asocian a ello (cisaprida, claritromicina, dolasetrón).
  - **Menores**: corticosteroides (beclometasona, betametasona, budesonida, dexametasona).

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen múltiples ensayos de fase 3 completados y ECA publicados que respaldan la eficacia de vilanterol en EPOC y asma (nivel de evidencia L1). Sin embargo, se trata del uso ya establecido del fármaco, no de un reposicionamiento, y el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Aclarar la situación regulatoria local: motivo de la cancelación del registro y vías para una nueva solicitud ante INVIMA
- Obtener el prospecto para completar advertencias y contraindicaciones
- Confirmar los datos del mecanismo de acción desde una fuente primaria
- Revisar el manejo clínico de las interacciones con antidiabéticos, simpaticomiméticos y fármacos que prolongan el QT
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

