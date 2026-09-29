---
layout: default
title: Terbutaline
parent: Evidencia Alta (L1-L2)
nav_order: 379
evidence_level: L1
indication_count: 3
---

# Terbutaline
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **3** 
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

# Terbutalina: De Indicación No Especificada en el Registro a Enfermedad Pulmonar Obstructiva

## Resumen en Una Frase

La terbutalina es un agonista beta-2 adrenérgico. Se usa como broncodilatador en broncoespasmo, asma, bronquitis y enfisema, aunque el registro sanitario colombiano solo consigna el nombre del principio activo.
El modelo TxGNN predice que podría ser efectiva para **enfermedad pulmonar obstructiva**, con **48 ensayos clínicos** y **20 publicaciones** asociados.
Esto probablemente refleja un uso ya establecido y no un reposicionamiento genuino.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | TERBUTALINA (el registro no detalla la indicación; según la farmacología, broncoespasmo en enfermedad obstructiva de la vía aérea) |
| Nueva Indicación Predicha | Enfermedad pulmonar obstructiva |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Proceed with Guardrails |

## Por qué es Razonable esta Predicción?

La terbutalina es un agonista selectivo de los receptores beta-2 adrenérgicos (ADRB2), con actividad secundaria sobre ADRB1. Al activarlos aumenta el AMPc y relaja el músculo liso de las vías aéreas, lo que produce broncodilatación. No se dispone de un campo de mecanismo de acción detallado en el registro; esta descripción proviene de la fundamentación farmacológica del paquete de evidencia.

Ese mecanismo coincide con la fisiopatología de la obstrucción reversible del flujo aéreo en asma y EPOC, lo que explica el puntaje tan alto del modelo. Sin embargo, la indicación original está vacía en los datos de entrada. Lo más probable es que esta predicción corresponda a un uso ya etiquetado o consolidado y no a una señal de reposicionamiento. Conviene verificar el registro fuente antes de presentarla como candidato novedoso.

## Evidencia de Ensayos Clínicos

Se listan 10 de los 48 ensayos registrados, priorizando los que incluyen terbutalina como intervención o comparador.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06626620](https://clinicaltrials.gov/study/NCT06626620) | Fase 3 | Completado | 120 | ECA de sulfato de magnesio IV frente a terbutalina en niños con exacerbación aguda de asma. Evidencia comparativa directa (relevancia A). |
| [NCT02224157](https://clinicaltrials.gov/study/NCT02224157) | Fase 3 | Completado | 4215 | Symbicort "a demanda" frente a Pulmicort dos veces al día más terbutalina "a demanda" en asma. La terbutalina es el rescate del brazo comparador (relevancia B). |
| [NCT00839800](https://clinicaltrials.gov/study/NCT00839800) | Fase 3 | Completado | 2091 | Symbicort SMART frente a Symbicort más terbutalina a demanda durante 12 meses en asma (relevancia B). |
| [NCT00252863](https://clinicaltrials.gov/study/NCT00252863) | Fase 3 | Completado | 1600 | Symbicort como terapia única frente a la práctica habitual en asma persistente; la terbutalina es el rescate del comparador (relevancia B). |
| [NCT02149199](https://clinicaltrials.gov/study/NCT02149199) | Fase 3 | Completado | 3850 | Symbicort a demanda frente a terbutalina a demanda y frente a Pulmicort más terbutalina en asma leve. |
| [NCT01096017](https://clinicaltrials.gov/study/NCT01096017) | Fase 3 | Completado | 24 | Eficacia relativa de terbutalina Turbuhaler 0.4 mg frente a salbutamol pMDI en adultos japoneses con asma (cruzado, dosis única). |
| [NCT00849095](https://clinicaltrials.gov/study/NCT00849095) | Fase 3 | Completado | 860 | Budesonida/formoterol a demanda frente a la combinación regular más terbutalina a demanda en asma persistente leve a moderada. |
| [NCT00326053](https://clinicaltrials.gov/study/NCT00326053) | Fase 3 | Completado | 600 | Symbicort frente a Pulmicort y Bricanyl (terbutalina) para prevenir recaídas de asma tras el alta de urgencias. |
| [NCT02322788](https://clinicaltrials.gov/study/NCT02322788) | Fase 3 | Completado | 95 | Farmacodinamia de Bricanyl Turbuhaler M3 frente a M2: protección frente a broncoconstricción inducida por metacolina en asma. |
| [NCT00750568](https://clinicaltrials.gov/study/NCT00750568) | N/A | Desconocido | 36 | Farmacocinética y eficacia de terbutalina en infusión IV continua en niños con estado asmático grave. |

## Evidencia de Literatura

Se listan 10 de las 20 publicaciones, priorizando ECA y revisiones.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30156361](https://pubmed.ncbi.nlm.nih.gov/30156361/) | 2019 | ECA | Acad Emerg Med | Terbutalina nebulizada más ipratropio frente a terbutalina sola en exacerbación aguda de EPOC que requiere ventilación no invasiva. |
| [3073804](https://pubmed.ncbi.nlm.nih.gov/3073804/) | 1988 | ECA | Br J Dis Chest | Terbutalina oral frente a placebo en EPOC: aumentó la fuerza de contracción diafragmática (presión inspiratoria máxima +5.8 cmH2O). |
| [6988343](https://pubmed.ncbi.nlm.nih.gov/6988343/) | 1980 | ECA | Int J Clin Pharmacol Ther Toxicol | Clenbuterol frente a terbutalina oral durante dos semanas en enfermedad pulmonar obstructiva crónica con obstrucción parcialmente reversible. |
| [10384064](https://pubmed.ncbi.nlm.nih.gov/10384064/) | 1999 | ECA | Lung | Dosis única de terbutalina Turbuhaler frente a placebo: efecto sobre función pulmonar y capacidad de ejercicio en 26 pacientes con EPOC. |
| [1615190](https://pubmed.ncbi.nlm.nih.gov/1615190/) | 1992 | ECA (cruzado) | Respir Med | Terbutalina inhalada frente a placebo: efecto sobre FEV1, FVC, disnea y distancia de marcha en enfermedad pulmonar obstructiva crónica. |
| [6624778](https://pubmed.ncbi.nlm.nih.gov/6624778/) | 1983 | ECA (cruzado) | Am J Med | Aminofilina y terbutalina orales frente a albuterol en aerosol en EPOC estable. |
| [2031046](https://pubmed.ncbi.nlm.nih.gov/2031046/) | 1991 | Estudio clínico (cruzado) | Pneumologie | Terbutalina nebulizada con presión espiratoria positiva (PEP) en 10 pacientes con EPOC. |
| [33065789](https://pubmed.ncbi.nlm.nih.gov/33065789/) | 2020 | Estudio clínico | Ann Palliat Med | N-acetilcisteína combinada con sulfato de terbutalina en ancianos con EPOC y su efecto sobre la apoptosis. |
| [36227333](https://pubmed.ncbi.nlm.nih.gov/36227333/) | 2023 | Revisión sistemática | Naunyn Schmiedebergs Arch Pharmacol | Farmacocinética clínica de la terbutalina en humanos según vía, estereoisomería, enfermedad, tabaquismo y edad. |
| [18761816](https://pubmed.ncbi.nlm.nih.gov/18761816/) | 2008 | Estudio clínico | Cell Mol Immunol | Terbutalina y budesonida nebulizadas mejoraron la inmunidad y la función pulmonar en pacientes con EPOC exacerbada. |

## Información de Mercado en Colombia

Los datos recibidos repiten cinco veces el mismo registro (38998). Se muestra una sola vez, aunque el total informado es de 20 registros sanitarios. Además de la solución para nebulización, el paquete menciona la forma jarabe.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 38998 | TERBUROP® SOLUCIÓN PARA NEBULIZACIÓN (Ropsohn Therapeutics SAS) | Solución para nebulización | TERBUTALINA (sin texto de indicación detallado) |

## Consideraciones de Seguridad

- **Farmacología de receptores**: la terbutalina actúa sobre los receptores beta-2 adrenérgicos (ADRB2) y, en menor medida, beta-1 (ADRB1). No se cuenta con datos de interacciones entre medicamentos con nivel de gravedad.

Consultar el prospecto para informacion de seguridad (advertencias y contraindicaciones).

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay varios ensayos de Fase 3 completados en asma y un ECA de Fase 3 con terbutalina como brazo de tratamiento. También hay múltiples ECA en EPOC, y el mecanismo beta-2 es coherente con la indicación. Sin embargo, la mayoría de los ensayos usan terbutalina solo como rescate del comparador, y la señal parece corresponder a un uso ya establecido, no a un reposicionamiento novedoso.

Las otras dos predicciones del modelo son débiles y quedan en **Hold**: malformación respiratoria (L4, evidencia indirecta y sin mecanismo plausible) y síndrome de Rienhoff (L5, solo predicción del modelo).

**Para avanzar se necesita:**
- Verificar en el registro fuente si esta indicación ya está aprobada, para no reportarla como novedosa.
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones), hoy sin datos.
- Completar el mecanismo de acción desde DrugBank (DB00871).
- Confirmar la indicación aprobada en los registros colombianos, que solo consignan "TERBUTALINA", y aclarar la discrepancia entre los 20 registros informados y el único registro distinto que aparece en los datos.
- Definir un plan de monitoreo de seguridad para poblaciones específicas (por ejemplo, niños y pacientes con enfermedad cardiovascular).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

