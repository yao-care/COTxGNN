---
layout: default
title: Caplacizumab
parent: Evidencia Alta (L1-L2)
nav_order: 133
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Caplacizumab: nueva indicación predicha, Púrpura trombocitopénica trombótica (nivel de evidencia L1). Indicación original: Sin texto de indicación detallado en el registro (solo figura \"CAPLAC…"
monitor_inn: "CAPLACIZUMAB"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "Scott syndrome", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "fetal and neonatal alloimmune thrombocytopenia", "hemophilia", "platelet-type bleeding disorder"]
---

# Caplacizumab
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

## Caplacizumab: De Indicación Registrada sin Texto Específico a Púrpura Trombocitopénica Trombótica
{: .text-alpha }

## Resumen en Una Frase

Caplacizumab es un nanocuerpo dirigido contra el factor de von Willebrand (vWF), registrado en Colombia bajo el nombre comercial CABLIVI®. El modelo TxGNN predice que podría ser efectivo para **púrpura trombocitopénica trombótica (PTT)**, con **7 ensayos clínicos** y **20 publicaciones** que respaldan esta dirección. Cabe aclarar que la PTT adquirida es la indicación ya aprobada del fármaco, por lo que no constituye un reposicionamiento en sentido estricto.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin texto de indicación detallado en el registro (solo figura "CAPLACIZUMAB") |
| Nueva Indicación Predicha | Púrpura trombocitopénica trombótica (rank 5 del modelo; las predicciones de mayor puntaje carecen de evidencia) |
| Puntaje de Predicción TxGNN | 99.996% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Proceed with Guardrails (solo para PTT); Hold para las demás indicaciones predichas |

**Nota sobre la selección de la indicación:** la primera predicción del modelo (trastorno de liberación plaquetaria primario) tiene un puntaje ligeramente mayor, pero no cuenta con ensayos ni literatura y es mecanísticamente poco creíble. Este informe se centra en la PTT, la única predicción con evidencia clínica sustancial. Las demás predicciones se resumen en la conclusión.

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según el conocimiento farmacológico disponible, caplacizumab se une al dominio A1 del vWF y bloquea su interacción con el receptor plaquetario GPIb, impidiendo la adhesión plaquetaria mediada por vWF.

En la PTT adquirida, la deficiencia de ADAMTS13 (generalmente por autoanticuerpos) deja multímeros ultra grandes de vWF que se unen a las plaquetas y causan microtrombosis, trombocitopenia, anemia hemolítica e isquemia de órganos. Bloquear la interacción vWF-plaqueta ataca directamente este paso de la fisiopatología, lo que da un fundamento mecanístico sólido.

La PTT es la indicación aprobada del fármaco: el ensayo de Fase 3 HERCULES, el de Fase 2 TITAN, el seguimiento a largo plazo y las guías ISTH 2020 y su actualización 2025 respaldan su uso. Las demás predicciones del modelo (trastornos hemorrágicos plaquetarios, hemofilia, etc.) son mecanísticamente contradictorias, porque un inhibidor de la adhesión plaquetaria podría agravar el sangrado.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02553317](https://clinicaltrials.gov/study/NCT02553317) | Fase 3 | Completado | 145 | HERCULES: ensayo pivotal doble ciego, aleatorizado y controlado con placebo; evalúa la recuperación más rápida del recuento plaquetario |
| [NCT02878603](https://clinicaltrials.gov/study/NCT02878603) | Fase 3 | Completado | 104 | Post-HERCULES: seguridad y eficacia a largo plazo, incluido el uso repetido |
| [NCT05468320](https://clinicaltrials.gov/study/NCT05468320) | Fase 3 | Completado | 51 | Caplacizumab con inmunosupresión sin intercambio plasmático de primera línea; estudio abierto de un solo brazo |
| [NCT04074187](https://clinicaltrials.gov/study/NCT04074187) | Fase 2/3 | Completado | 21 | Estudio abierto en pacientes japoneses; prevención de recurrencia de PTT adquirida |
| [NCT01151423](https://clinicaltrials.gov/study/NCT01151423) | Fase 2 | Completado | 75 | TITAN: aleatorizado, controlado con placebo; menor tiempo hasta la normalización plaquetaria |
| [NCT04720261](https://clinicaltrials.gov/study/NCT04720261) | Fase 2 | Terminado | 58 | Régimen personalizado según actividad de ADAMTS13; no inferioridad de un solo brazo |
| [NCT05263193](https://clinicaltrials.gov/study/NCT05263193) | N/A | Completado | 4 | Recolección retrospectiva en pacientes pediátricos con PTT inmunomediada |
| [NCT05785468](https://clinicaltrials.gov/study/NCT05785468) | N/A | Desconocido | 1 | Estudio observacional retrospectivo italiano (ROSCAPLI); valor probatorio mínimo |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30625070](https://pubmed.ncbi.nlm.nih.gov/30625070/) | 2019 | ECA | N Engl J Med | Tratamiento con caplacizumab en PTT adquirida (HERCULES) |
| [26863353](https://pubmed.ncbi.nlm.nih.gov/26863353/) | 2016 | ECA | N Engl J Med | Resultados de caplacizumab en PTT adquirida (TITAN) |
| [40533296](https://pubmed.ncbi.nlm.nih.gov/40533296/) | 2025 | Guía | J Thromb Haemost | Actualización 2025 de las guías ISTH 2020 para el manejo de la PTT |
| [32914526](https://pubmed.ncbi.nlm.nih.gov/32914526/) | 2020 | Guía | J Thromb Haemost | Guías ISTH para el tratamiento de la PTT |
| [40388146](https://pubmed.ncbi.nlm.nih.gov/40388146/) | 2025 | Revisión | JAMA | Revisión de la PTT inmune; incidencia de 2 a 6 casos por millón al año |
| [40235949](https://pubmed.ncbi.nlm.nih.gov/40235949/) | 2025 | Cohorte | EClinicalMedicine | Proyecto Capla 1000+: uso de caplacizumab, mortalidad y momento óptimo de inicio |
| [36138517](https://pubmed.ncbi.nlm.nih.gov/36138517/) | 2022 | Cohorte | J Thromb Haemost | Post-HERCULES: seguimiento a largo plazo y uso repetido |
| [33881463](https://pubmed.ncbi.nlm.nih.gov/33881463/) | 2021 | Cohorte | Blood Adv | Análisis integrado TITAN y HERCULES: menos muertes y menor refractariedad con caplacizumab |
| [38838300](https://pubmed.ncbi.nlm.nih.gov/38838300/) | 2024 | Retrospectivo | Blood | Manejo de la PTT inmune sin intercambio plasmático terapéutico (42 casos) |
| [37689812](https://pubmed.ncbi.nlm.nih.gov/37689812/) | 2023 | Guía | Int J Hematol | Guías diagnósticas y terapéuticas de PTT en Japón 2023 |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20176684 (cancelado) | CABLIVI® | Polvo liofilizado para reconstituir a solución inyectable | CAPLACIZUMAB |

El único registro sanitario (Sanofi-Aventis de Colombia S.A.) figura como cancelado, por lo que actualmente no hay presentación vigente en el mercado colombiano.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** se identificaron 100 interacciones potenciales. Las principales de nivel mayor, relacionadas sobre todo con riesgo hemorrágico, son:
  - Ácido acetilsalicílico
  - Abciximab
  - Fondaparinux
  - Alteplasa
  - Anagrelida
  - Acalabrutinib
  - Deferasirox
  - Trastuzumab emtansina
  - Ibritumomab tiuxetán
  - Tositumomab (con y sin I-131)
- **Interacciones de nivel moderado:** AINE (ibuprofeno, ketorolaco, celecoxib, diclofenaco tópico), fluvoxamina, fenfluramina, dexfenfluramina y sibutramina.
- **Consideración mecanística:** al inhibir la adhesión plaquetaria dependiente de vWF, caplacizumab aumenta el riesgo de sangrado. Esto lo hace inadecuado en trastornos hemorrágicos como los otros candidatos predichos.

Para advertencias y contraindicaciones específicas, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails** (solo para PTT adquirida/inmunomediada). **Hold** para las otras nueve predicciones.

**Justificación:**
- Para la PTT hay dos ensayos de Fase 3 completados (HERCULES y Post-HERCULES, más un tercero de Fase 3 sin intercambio plasmático), un ensayo aleatorizado de Fase 2 y guías internacionales que lo respaldan. Sin embargo, es la indicación ya aprobada, no un reposicionamiento nuevo.
- Las demás predicciones (trastorno de liberación plaquetaria, pseudo-enfermedad de von Willebrand, Glanzmann, síndrome de Scott, defecto del receptor de colágeno, trombocitopenia constitucional, trombocitopenia aloinmune fetal y neonatal, hemofilia y trastorno hemorrágico de tipo plaquetario) carecen de ensayos y de literatura específica. Además, el mecanismo del fármaco sugiere que empeoraría el sangrado, por lo que se recomienda no avanzar.

**Para avanzar se necesita:**
- Resolver la situación regulatoria en Colombia: el único registro está cancelado, por lo que hay que confirmar si se requiere un nuevo trámite ante INVIMA.
- Obtener y revisar el prospecto de INVIMA para advertencias y contraindicaciones.
- Completar los datos del mecanismo de acción desde DrugBank.
- Definir un plan de monitoreo: sangrado, actividad de ADAMTS13 para guiar la duración, e intercambio plasmático e inmunosupresión concurrentes.
- Revisar y manejar las interacciones mayores con antiplaquetarios, anticoagulantes y trombolíticos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

