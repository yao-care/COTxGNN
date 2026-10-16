---
layout: default
title: Trandolapril
parent: Solo Predicción del Modelo (L5)
nav_order: 635
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Trandolapril: nueva indicación predicha, Hipertensión renovascular maligna (nivel de evidencia L5). Indicación original: Trandolapril y bloqueadores de canales del calcio"
monitor_inn: "TRANDOLAPRIL"
predicted_indications: ["malignant renovascular hypertension", "malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease"]
---

# Trandolapril
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

# Trandolapril: De Combinación con Bloqueadores de Canales de Calcio a Hipertensión Renovascular Maligna

## Resumen en Una Frase

Trandolapril es un inhibidor de la enzima convertidora de angiotensina (ECA), registrado en Colombia en combinación con bloqueadores de los canales del calcio (producto TARKA® SR).
El modelo TxGNN predice que podría ser efectivo para **hipertensión renovascular maligna**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden directamente esta indicación (solo predicción del modelo).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trandolapril y bloqueadores de canales del calcio |
| Nueva Indicación Predicha | Hipertensión renovascular maligna |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registro vigente) |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, trandolapril es un inhibidor de la ECA: bloquea la conversión de angiotensina I en angiotensina II, con lo que reduce la vasoconstricción y la presión arterial. Su uso en hipertensión está ampliamente establecido, y fue comercializado en Colombia en combinación con un bloqueador de canales de calcio.

En la hipertensión renovascular, la activación del sistema renina-angiotensina es una vía central, por lo que bloquear este sistema es biológicamente plausible. Sin embargo, los inhibidores de la ECA conllevan un riesgo conocido de deterioro agudo de la función renal en la estenosis bilateral de la arteria renal, lo que exige cautela.

El puntaje alto de TxGNN (99.92%) es solo una predicción computacional. No se aportaron ensayos ni literatura que la sustenten, por lo que la plausibilidad mecanística es un argumento de clase farmacológica y no una evidencia específica de trandolapril.

### Otras indicaciones predichas (para contexto)

| Indicación predicha | Puntaje TxGNN | Nivel de evidencia | Comentario |
|------|------|------|------|
| Enfermedad renal hipertensiva maligna | 99.92% | L5 | Racional de clase (menor presión intraglomerular); sin evidencia específica |
| Hipertensión pulmonar de mecanismo multifactorial poco claro | 99.92% | L5 | Racional débil (remodelado vascular pulmonar); sin evidencia |
| Hipertensión pulmonar por enfermedad pulmonar y/o hipoxia | 99.92% | L4 | Solo estudios preclínicos indirectos |
| Síndrome de Braddock | 99.88% | L5 | Sin vínculo mecanístico claro |
| Cardiopatía pulmonar crónica | 99.19% | L4 | Un estudio preclínico en ratas |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para hipertensión renovascular maligna ni para ninguna de las otras indicaciones predichas.

---

## Evidencia de Literatura

Para la indicación principal (hipertensión renovascular maligna) no hay literatura disponible. La única literatura asociada corresponde a indicaciones de menor rango, y es indirecta:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [8166049](https://pubmed.ncbi.nlm.nih.gov/8166049/) | 1994 | Revisión | Am J Cardiol | Bases moleculares de la regresión de la hipertrofia cardíaca; el proceso es reversible si el tratamiento reduce la sobrecarga |
| [7511729](https://pubmed.ncbi.nlm.nih.gov/7511729/) | 1994 | Preclínico (animal) | J Cardiovasc Pharmacol | Trandolapril en ratas hipertensas espontáneas: regresión de hipertrofia ventricular y efectos sobre resistencia coronaria y rigidez diastólica |
| [9218195](https://pubmed.ncbi.nlm.nih.gov/9218195/) | 1997 | Preclínico (animal) | J Hypertens Suppl | Consideraciones preclínicas de la combinación verapamilo + trandolapril en hipertensión y enfermedades cardiovasculares/metabólicas asociadas |
| [8909991](https://pubmed.ncbi.nlm.nih.gov/8909991/) | 1996 | Preclínico (animal) | Gen Pharmacol | Trandolapril + verapamilo inhibe el vasoespasmo coronario inducido por hipoxia tras isquemia-reperfusión en perros |
| [8989645](https://pubmed.ncbi.nlm.nih.gov/8989645/) | 1996 | Preclínico (animal) | J Card Fail | Tratamiento prolongado con trandolapril sobre la vasoconstricción aumentada en ratas con insuficiencia cardíaca crónica |
| [17393952](https://pubmed.ncbi.nlm.nih.gov/17393952/) | 2007 | Reporte de caso | J Natl Med Assoc | Resolución del dolor crónico en una paciente con anemia falciforme tratada con trandolapril (relevancia indirecta) |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 230359 (cancelado) | TARKA® SR TABLETAS | Tableta de liberación prolongada | Trandolapril y bloqueadores de canales del calcio |

---

## Consideraciones de Seguridad

- **Posibles contraindicaciones o condiciones de riesgo (según grafo de conocimiento, no según prospecto):** angioedema (incluido el hereditario y el inducido por bloqueadores del sistema renina-angiotensina), enfermedad renal, enfermedad hepática, neutropenia y agranulocitosis, estenosis aórtica, hipotensión, obstrucción de la arteria renal, miocardiopatía hipertrófica, miastenia gravis, taquicardia ventricular, bloqueo auriculoventricular e insuficiencia cardíaca.
- **Interacciones farmacológicas:** se identificaron 100 interacciones en total; entre las principales destacan las de nivel **mayor** con **citrato de potasio** y **bicarbonato de potasio** (riesgo de hiperpotasemia). Hay interacciones de nivel **moderado** con corticoides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona), antidiabéticos (metformina, alogliptina, canagliflozina, dapagliflozina, empagliflozina, glimepirida, clorpropamida), ácido acetilsalicílico, morfina, bupropión, dronabinol, ácido picosulfúrico y polietilenglicol con electrolitos.

Nota: para las advertencias y contraindicaciones del prospecto, consultar el prospecto del producto, ya que no se dispone de ese texto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5) y en un racional de clase farmacológica, sin ensayos clínicos ni literatura directa. Además, el único registro sanitario en Colombia está cancelado y existe un riesgo conocido de deterioro renal con inhibidores de la ECA en estenosis de arteria renal bilateral.

**Para avanzar se necesita:**
- Revisión de literatura clínica sobre inhibidores de la ECA (y específicamente trandolapril) en hipertensión renovascular maligna
- Obtener las advertencias y contraindicaciones del prospecto de INVIMA
- Completar los datos del mecanismo de acción desde DrugBank
- Evaluar la situación regulatoria (registro cancelado) y la disponibilidad de otros productos con trandolapril en Colombia
- Análisis de seguridad renal para pacientes con estenosis de arteria renal, y de riesgo de hiperpotasemia
- Definir la compatibilidad de vía de administración y la similitud con la indicación original
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

