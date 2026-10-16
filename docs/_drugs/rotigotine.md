---
layout: default
title: Rotigotine
parent: Evidencia Moderada (L3-L4)
nav_order: 572
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Rotigotine: nueva indicación predicha, Trastorno por déficit de atención e hiperactividad (TDAH) (nivel de evidencia L4). Indicación original: Rotigotina"
---

# Rotigotine
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

# Rotigotina: De Rotigotina (indicación registrada) a Trastorno por Déficit de Atención e Hiperactividad

## Resumen en Una Frase

Rotigotina es un agonista dopaminérgico no ergolínico, registrado en Colombia en forma de sistema de liberación (parche transdérmico) bajo la denominación "ROTIGOTINA"; a nivel internacional se usa en la enfermedad de Parkinson y el síndrome de piernas inquietas.
El modelo TxGNN predice que podría ser efectivo para **trastorno por déficit de atención e hiperactividad (TDAH)**,
pero **no hay ensayos clínicos** y solo hay **3 publicaciones** indirectas (revisiones sobre síndrome de piernas inquietas y un estudio mecanístico de receptores), por lo que la evidencia es muy limitada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Rotigotina (el registro sanitario no detalla la indicación; en la literatura se asocia a enfermedad de Parkinson y síndrome de piernas inquietas) |
| Nueva Indicación Predicha | Trastorno por déficit de atención e hiperactividad (TDAH) |
| Puntaje de Predicción TxGNN | 99.997% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información farmacológica disponible, rotigotina es un agonista dopaminérgico no ergolínico que actúa sobre los receptores D1 a D5 (con mayor afinidad por D3) y tiene además actividad sobre receptores 5-HT1A y alfa2B.

La desregulación dopaminérgica y noradrenérgica es un componente central del TDAH, por lo que existe una justificación mecanística plausible. Además, variantes polimórficas del receptor D4 (DRD4) se han asociado con el TDAH, y rotigotina interactúa con este receptor. Un estudio preclínico (2021) sobre heterómeros entre receptores α2A y D4 respalda esta conexión biológica.

Sin embargo, la literatura recuperada trata sobre el síndrome de piernas inquietas (una condición relacionada y a menudo comórbida con el TDAH) y sobre trabajo a nivel de receptores. Ningún estudio evalúa rotigotina en pacientes con TDAH. El puntaje TxGNN, aunque muy alto, es una predicción computacional y no constituye evidencia clínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [18656214](https://pubmed.ncbi.nlm.nih.gov/18656214/) | 2008 | Revisión | Revue Neurologique | Revisión del síndrome de piernas inquietas: características clínicas, prevalencia (2-3% en países occidentales) y criterios diagnósticos |
| [21476956](https://pubmed.ncbi.nlm.nih.gov/21476956/) | 2011 | Revisión | Current Pharmaceutical Design | Revisión de opciones farmacológicas para el síndrome de piernas inquietas en niños |
| [34182128](https://pubmed.ncbi.nlm.nih.gov/34182128/) | 2021 | Preclínico/Mecanístico | Pharmacological Research | Heteromerización entre receptores α2A y variantes del receptor D4; implicaciones para trastornos del control de impulsos y TDAH |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20019919 (cancelado) | NEUPRO® 6 MG/24 H | Sistemas de liberación | ROTIGOTINA |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** hipertensión y trastorno hipertensivo, atrofia multisistémica, síndrome de taquicardia postural ortostática, hipotensión ortostática y discinesia inducida por fármacos.
- **Perfil farmacológico (interacciones con dianas):** rotigotina actúa como agonista sobre los receptores de dopamina D1, D2, D3, D4 y D5. No se dispone de datos de interacciones fármaco-fármaco clasificadas por nivel de gravedad.
- **Consideración para esta predicción:** los agonistas dopaminérgicos pueden provocar hipotensión ortostática, lo que se solapa con las condiciones señaladas arriba. Para TDAH, que suele tratarse en población pediátrica, esto exige especial cautela.

Para información completa de advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción solo cuenta con soporte mecanístico indirecto (nivel L4): no existen ensayos clínicos ni estudios de rotigotina en TDAH. Además, el único registro sanitario en Colombia está cancelado, y no se dispone de datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto del INVIMA para obtener advertencias y contraindicaciones (brecha bloqueante para el tamizaje de seguridad)
- Completar los datos del mecanismo de acción desde DrugBank
- Buscar estudios clínicos o evidencia preclínica específica de rotigotina en TDAH
- Evaluar la viabilidad regulatoria, dado que no hay producto vigente en el mercado colombiano
- Evaluar la seguridad en población pediátrica y los riesgos cardiovasculares (hipotensión ortostática)

**Otras predicciones del modelo (todas en Hold):**
- **Esquizofrenia** (L4, puntaje 99.996%): existe una revisión sistemática y metaanálisis sobre fármacos prodopaminérgicos para síntomas negativos, pero no es específica de rotigotina. Un agonista pleno de D1/D2/D3 podría empeorar los síntomas psicóticos positivos, lo que representa una preocupación de seguridad importante.
- **Miopía ligada al X** y **miopía 26 ligada al X, limitada a mujeres** (L5): la dopamina retiniana participa en el crecimiento ocular en modelos preclínicos, lo que da una justificación débil e indirecta, sin datos específicos de rotigotina.
- **Polimicrogiria perisilviana con hipoplasia cerebelosa y artrogriposis, síndrome faciodigitogenital, trastorno congénito de la glicosilación con fucosilación defectuosa, distrofia retiniana, encefalopatía atípica por glicina y enfermedad de Charcot-Marie-Tooth desmielinizante tipo 1G** (L5): no se identificó un vínculo mecanístico plausible, y no hay ensayos ni literatura.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

