---
layout: default
title: Formoterol
parent: Solo Predicción del Modelo (L5)
nav_order: 204
evidence_level: L5
indication_count: 6
---

# Formoterol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Formoterol: De Asma y EPOC a Malformación Respiratoria

## Resumen en Una Frase

Formoterol es un agonista beta-2 adrenérgico de acción prolongada (LABA), usado originalmente como broncodilatador en el asma y la enfermedad pulmonar obstructiva crónica (EPOC).
El modelo TxGNN predice que podría ser efectivo para **malformación respiratoria**, con un puntaje muy alto (99.92%).
Sin embargo, los **25 ensayos clínicos** y las **10 publicaciones** recuperadas tratan de asma, EPOC u otros temas, y **ninguno aborda malformaciones respiratorias**. La predicción no tiene respaldo real por ahora.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | El registro sanitario solo dice «FORMOTEROL Y BUDENOSINA» (composición, sin indicación explícita). El uso clínico conocido es asma y EPOC |
| Nueva Indicación Predicha | Malformación respiratoria |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L5 (solo predicción del modelo para esta indicación; el paquete de datos la clasifica como L4, pero no hay estudios preclínicos ni de mecanismo específicos) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información farmacológica disponible, formoterol actúa sobre los receptores beta-2 adrenérgicos (ADRB2) y también sobre los beta-1 (ADRB1). Su eficacia en asma y EPOC está bien establecida, y en los registros colombianos aparece combinado con budesonida (inhalador Busterol).

La relación entre la indicación original y la nueva es débil. Asma y EPOC son enfermedades obstructivas de la vía aérea, tratables con broncodilatación. Una malformación respiratoria es una anomalía estructural, en general congénita, y no responde a un efecto broncodilatador.

El puntaje de 0.999 probablemente refleja un vínculo genérico entre los agonistas beta-2 y el fenotipo de la vía aérea dentro del grafo de conocimiento. No se identificó un mecanismo específico para anomalías congénitas de la vía aérea.

---

## Evidencia de Ensayos Clínicos

Los ensayos recuperados incluyen formoterol, pero **ninguno evalúa malformación respiratoria**. Se listan los 10 más relevantes por fase y tamaño. El grado de relevancia asignado a los tres primeros es C.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00130351](https://clinicaltrials.gov/study/NCT00130351) | Fase 3 | Completado | 155 | Uso y funcionalidad de formoterol en un nuevo inhalador de polvo seco multidosis en asma |
| [NCT03324607](https://clinicaltrials.gov/study/NCT03324607) | Fase 2/3 | Completado | 20 | Glicopirrolato/formoterol (Bevespi) y anomalías de ventilación e intercambio gaseoso en EPOC, medidas con RM de 129Xe |
| [NCT03453112](https://clinicaltrials.gov/study/NCT03453112) | Fase 3 | Completado | 494 | Foster NEXThaler frente a Foster pMDI en asma controlada (no inferioridad en flujo espiratorio máximo) |
| [NCT00861926](https://clinicaltrials.gov/study/NCT00861926) | Fase 3 | Completado | 1714 | Foster como terapia de mantenimiento y rescate frente a Foster más salbutamol en asma |
| [NCT02345161](https://clinicaltrials.gov/study/NCT02345161) | Fase 3 | Completado | 1811 | Triple combinación FF/UMEC/VI frente a budesonida/formoterol en EPOC |
| [NCT03197818](https://clinicaltrials.gov/study/NCT03197818) | Fase 3 | Completado | 708 | Triple combinación beclometasona/formoterol/glicopirronio frente a Symbicort en EPOC |
| [NCT03888131](https://clinicaltrials.gov/study/NCT03888131) | Fase 3 | Completado | 750 | Beclometasona/formoterol (CHF 1535) frente a Symbicort en EPOC (VEF1 a 24 semanas) |
| [NCT01577082](https://clinicaltrials.gov/study/NCT01577082) | Fase 3 | Completado | 542 | CHF 1535 frente a beclometasona en asma no controlada con dosis altas de corticoide inhalado |
| [NCT01803555](https://clinicaltrials.gov/study/NCT01803555) | Fase 3 | Completado | 605 | Budesonida/formoterol Spiromax frente a Symbicort Turbuhaler en asma persistente |
| [NCT01245569](https://clinicaltrials.gov/study/NCT01245569) | Fase 3 | Completado | 419 | Foster 100/6 frente a Seretide 500/50 en EPOC (función pulmonar y disnea) |

---

## Evidencia de Literatura

Ninguna publicación trata malformaciones respiratorias. Se muestran las 10 recuperadas, con ECA primero y luego revisiones.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [22541245](https://pubmed.ncbi.nlm.nih.gov/22541245/) | 2012 | ECA | J Allergy Clin Immunol | Seguridad a largo plazo de budesonida/formoterol pMDI en pacientes asmáticos afroamericanos |
| [35115339](https://pubmed.ncbi.nlm.nih.gov/35115339/) | 2022 | ECA (cruzado) | Eur Respir J | Budesonida/formoterol repetido frente a salbutamol en asma adulta: broncodilatación y efectos cardiovasculares y adversos |
| [40840693](https://pubmed.ncbi.nlm.nih.gov/40840693/) | 2026 | Revisión sistemática y metaanálisis | J Am Pharm Assoc | Seguridad y eficacia de budesonida/glicopirrolato/formoterol frente a glicopirrolato/formoterol en EPOC |
| [20528601](https://pubmed.ncbi.nlm.nih.gov/20528601/) | 2010 | Revisión | J Asthma | Eficacia y seguridad de Symbicort en inhalador presurizado para asma persistente |
| [24842803](https://pubmed.ncbi.nlm.nih.gov/24842803/) | 2014 | Revisión | Prog Neuropsychopharmacol Biol Psychiatry | Estrategias basadas en neurotransmisores para la disfunción cognitiva en el síndrome de Down (relación con formoterol solo tangencial) |
| [14738234](https://pubmed.ncbi.nlm.nih.gov/14738234/) | 2004 | Estudio experimental | Eur Respir J | Formoterol protege frente a los efectos inducidos por el factor activador de plaquetas en asma |
| [35034195](https://pubmed.ncbi.nlm.nih.gov/35034195/) | 2022 | Estudio fisiológico | Eur J Appl Physiol | Respuestas compensatorias a las alteraciones mecánicas de la EPOC durante el sueño |
| [30662579](https://pubmed.ncbi.nlm.nih.gov/30662579/) | 2018 | Estudio transversal | Can Respir J | Errores en el uso de inhaladores y resultados maternos y fetales en embarazadas asmáticas |
| [37691104](https://pubmed.ncbi.nlm.nih.gov/37691104/) | 2023 | Reporte de caso | J Med Case Rep | Enfermedad de la vía aérea pequeña en COVID prolongado, con seguimiento de tres años |
| [41686546](https://pubmed.ncbi.nlm.nih.gov/41686546/) | 2026 | Reporte de caso y revisión | Medicine | Micosis broncopulmonar alérgica por *Schizophyllum commune* en un paciente operado de cáncer de pulmón |

---

## Información de Mercado en Colombia

El paquete de datos repite cinco veces el mismo registro sanitario. Aquí se muestra una sola vez. En total hay 20 registros de formoterol.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19978720 | BUSTEROL® INHALADOR (Laboratorios Chalver de Colombia S.A.S.) | Suspensión para inhalación | Formoterol y budesonida (el texto del registro solo indica la composición) |

Las formas farmacéuticas reportadas para formoterol incluyen suspensión para inhalación, polvo para inhalación y aerosoles.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje del modelo es muy alto, pero no existe ningún ensayo ni publicación sobre malformación respiratoria, y el mecanismo broncodilatador no explica un beneficio en anomalías estructurales. Las otras predicciones con evidencia sólida (bronquitis, asma, enfermedad pulmonar obstructiva) corresponden a usos ya establecidos, no a un reposicionamiento nuevo.

**Para avanzar se necesita:**
- Definir qué tipo de malformación respiratoria se plantea (congénita, estructural o funcional) y su relevancia clínica real.
- Estudios preclínicos o de mecanismo que expliquen un beneficio del agonismo beta-2 en esa condición.
- Datos completos del mecanismo de acción (DrugBank).
- Descargar y analizar el prospecto de INVIMA para advertencias y contraindicaciones, información necesaria antes de cualquier evaluación de seguridad.

*Este informe es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

