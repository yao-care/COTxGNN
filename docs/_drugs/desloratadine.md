---
layout: default
title: Desloratadine
parent: Evidencia Alta (L1-L2)
nav_order: 203
evidence_level: L1
indication_count: 6
last_modified_at: 2026-10-14
description: "Desloratadine: nueva indicación predicha, Urticaria por frío (nivel de evidencia L1). Indicación original: DESLORATADINA"
monitor_inn: "Desloratadine"
predicted_indications: ["cold urticaria", "nasal cavity disease", "recalcitrant atopic dermatitis", "IgE responsiveness, atopic", "rosacea conjunctivitis"]
---

# Desloratadine
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **6** 
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

# Desloratadina: De Desloratadina (indicación no detallada en el registro) a Urticaria por Frío

## Resumen en Una Frase

Desloratadina es un antihistamínico de segunda generación que bloquea el receptor H1, utilizado en condiciones alérgicas como la rinitis y la urticaria.
El modelo TxGNN predice que podría ser efectivo para **urticaria por frío**,
con **2 ensayos clínicos** (ambos de Fase 4, completados) y **6 publicaciones** (3 ECA, 2 revisiones y 1 reporte de caso) que actualmente respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | DESLORATADINA (el registro sanitario no detalla el texto de la indicación; se usa en rinitis alérgica y urticaria) |
| Nueva Indicación Predicha | Urticaria por frío |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 7 (todos cancelados) |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción detallado. Según la información conocida, la desloratadina es un antagonista selectivo (agonista inverso) del receptor H1 periférico. Su eficacia en condiciones alérgicas como la rinitis y la urticaria está bien establecida, y mecanísticamente es aplicable a la urticaria por frío.

La urticaria por frío está mediada por la degranulación de mastocitos y la liberación de histamina tras la exposición al frío. El bloqueo H1 actúa directamente sobre la vía efectora principal. Además, aumentar la dosis de antihistamínicos de segunda generación (hasta 4 veces la dosis estándar) es una estrategia respaldada por las guías clínicas, y los ensayos de escalada de dosis disponibles son coherentes con ella.

Conviene hacer una salvedad: la evidencia proviene de ensayos de Fase 4, no de Fase 3, y el fármaco ya está aprobado para urticaria crónica. Por ello, esta predicción se parece más a una extensión de una indicación de clase existente que a un reposicionamiento en sentido estricto.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01444196](https://clinicaltrials.gov/study/NCT01444196) | Fase 4 | Completado | 30 | Estudio multicéntrico, doble ciego, de escalada de dosis (5, 10 y 20 mg) en urticaria por frío adquirida; busca la dosis suficiente para inhibir los síntomas |
| [NCT00600847](https://clinicaltrials.gov/study/NCT00600847) | Fase 4 | Completado | 33 | Estudio cruzado, aleatorizado, doble ciego y controlado con placebo; compara 5 mg vs. 20 mg en lesiones inducidas experimentalmente (termografía, volumetría y fotografía) |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [19201016](https://pubmed.ncbi.nlm.nih.gov/19201016/) | 2009 | ECA | J Allergy Clin Immunol | Con dosis alta de desloratadina disminuyó el volumen de la roncha y mejoraron los umbrales de provocación por frío frente a la dosis estándar (estudio cruzado controlado con placebo) |
| [22242678](https://pubmed.ncbi.nlm.nih.gov/22242678/) | 2012 | ECA | Br J Dermatol | Medición del umbral crítico de temperatura en urticaria por frío con escalada de dosis de antihistamínicos H1 |
| [14754651](https://pubmed.ncbi.nlm.nih.gov/14754651/) | 2004 | ECA | J Dermatolog Treat | 5 mg de desloratadina durante 4 días, probada con cubos de hielo en 12 pacientes con urticaria por frío |
| [15516152](https://pubmed.ncbi.nlm.nih.gov/15516152/) | 2004 | Revisión | Drugs | Etiología, manejo y opciones de tratamiento de la urticaria crónica |
| [19032340](https://pubmed.ncbi.nlm.nih.gov/19032340/) | 2008 | Revisión | Allergy | Ebastina en rinitis alérgica y urticaria crónica idiopática (otro antihistamínico; evidencia indirecta) |
| [38025339](https://pubmed.ncbi.nlm.nih.gov/38025339/) | 2023 | Reporte de caso | Qatar Med J | Urticaria por frío tras anafilaxia por mordedura de hormiga negra (relevancia indirecta) |

## Información de Mercado en Colombia

Los 7 registros sanitarios están cancelados; actualmente no hay ningún registro vigente.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20196512 | SINNALLER® | Tableta recubierta | DESLORATADINA |
| 20106242 | HISTALINE | Tableta recubierta | DESLORATADINA |
| 20075867 | RINILORAN® JARABE | Jarabe | DESLORATADINA |
| 20137626 | NEWTARPAN® tableta cubierta 5 mg | Tableta recubierta | DESLORATADINA |
| 20262256 | DESLORIX 50MG/100ML JARABE | Jarabe | DESLORATADINA |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: el grafo de conocimiento TxGNN (PrimeKG) asocia el fármaco con las siguientes enfermedades, que conviene evaluar con cautela:
  - Cardiovasculares: hipertensión, enfermedad coronaria, aterosclerosis y arteriosclerosis.
  - Renales y hepáticas: enfermedad renal, piouréter, enfermedad hepática y enfermedad de la vesícula biliar.
  - Metabólicas y endocrinas: diabetes mellitus, cetoacidosis diabética, hipertiroidismo, enfermedad de Graves y tirotoxicosis.
  - Otras: hiperplasia prostática benigna y glaucoma de ángulo cerrado.
- **Interacciones farmacológicas**: la consulta se completó y solo se encontró la interacción farmacológica con el receptor H1 (su diana terapéutica). No se identificaron interacciones con otros fármacos. Se ha descrito actividad antiviral in vitro contra SARS-CoV-2, probablemente por fosfolipidosis, sin relevancia clínica establecida.

Para advertencias y contraindicaciones basadas en el prospecto, consultar el prospecto del producto.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay ensayos de Fase 4 completados, controlados y doble ciego, además de varios ECA que respaldan el uso de desloratadina (incluso a dosis elevadas) en urticaria por frío, y el mecanismo H1 es coherente. Sin embargo, las muestras son pequeñas, no hay ensayos de Fase 3 y actualmente no hay registros vigentes en Colombia.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), que sigue pendiente.
- Confirmar los datos del mecanismo de acción en DrugBank.
- Definir el camino regulatorio, ya que todos los registros están cancelados (nuevo registro o reactivación).
- Evaluar la seguridad de las dosis superiores a la estándar (hasta 4 veces) y en poblaciones con las comorbilidades señaladas.
- Confirmar la compatibilidad de la vía de administración y la forma farmacéutica.

## Otras Predicciones de Menor Respaldo

| Indicación Predicha | Puntaje TxGNN | Nivel de Evidencia | Recomendación |
|------|------|------|------|
| Enfermedad de la cavidad nasal | 99.87% | L4 | Pregunta de investigación (solo estudios en animales) |
| Laringofaringitis aguda | 99.85% | L5 | Hold |
| Dermatitis atópica recalcitrante | 99.75% | L5 | Hold |
| Respuesta IgE atópica | 99.64% | L5 | Hold |
| Conjuntivitis por rosácea | 99.40% | L5 | Hold |
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

