---
layout: default
title: Salmeterol
parent: Evidencia Alta (L1-L2)
nav_order: 355
evidence_level: L1
indication_count: 7
---

# Salmeterol
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **7** 
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

# Salmeterol: De Salmeterol y Fluticasona (texto del registro) a Bronquitis

## Resumen en Una Frase

Salmeterol es un agonista beta2 de acción prolongada (LABA). En Colombia está registrado en una combinación con fluticasona para inhalación, y el registro no detalla la indicación original.
El modelo TxGNN predice que podría ser efectivo para **bronquitis**, con **16 ensayos clínicos** y **20 publicaciones** que respaldan esta dirección.
Casi toda esa evidencia proviene de estudios en EPOC (bronquitis crónica/enfisema), por lo que esta predicción se acerca más a un uso ya establecido que a un reposicionamiento novedoso.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Salmeterol y fluticasona (texto literal del registro; no especifica la enfermedad) |
| Nueva Indicación Predicha | Bronquitis |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 16 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, salmeterol es un agonista beta2-adrenérgico de acción prolongada. Relaja el músculo liso bronquial y aumenta el aclaramiento mucociliar. Un estudio en bronquíticos crónicos (PMID 15970448) evaluó precisamente este efecto sobre el aclaramiento mucociliar y de la tos.

La bronquitis crónica es uno de los fenotipos de la EPOC. La broncodilatación sostenida y el efecto antiinflamatorio de la combinación con fluticasona (por ejemplo, PMID 16424444 en EPOC) son mecanísticamente aplicables a esta condición.

La combinación fluticasona/salmeterol ya tiene indicación en EPOC asociada a bronquitis crónica en Estados Unidos, según los ensayos y la revisión citados. Por eso el puntaje alto del modelo es coherente con el uso clínico existente. No se trata de un hallazgo completamente nuevo.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02173691](https://clinicaltrials.gov/study/NCT02173691) | Fase 3 | Completado | 584 | Tiotropio vs aerosol de salmeterol vs placebo durante 6 meses en EPOC; compara la eficacia broncodilatadora y la seguridad a largo plazo |
| [NCT00268177](https://clinicaltrials.gov/study/NCT00268177) | Fase 3 | Completado | 130 | Salmeterol/fluticasona 50/500 mcg vs placebo durante 13 semanas; evalúa la actividad antiinflamatoria bronquial en EPOC |
| [NCT00064402](https://clinicaltrials.gov/study/NCT00064402) | Fase 3 | Completado | 741 | Arformoterol en EPOC con control activo y placebo, doble ciego; el resumen no detalla el comparador activo |
| [NCT00269126](https://clinicaltrials.gov/study/NCT00269126) | Fase 3 | Completado | 150 | Compara el efecto de dos medicamentos en EPOC durante 18 semanas; el título no permite verificar el brazo de salmeterol |
| [NCT00269087](https://clinicaltrials.gov/study/NCT00269087) | Fase 3 | Completado | 122 | GW815SF 50/500 µg (salmeterol/fluticasona) en tratamiento a largo plazo (56 semanas) en EPOC (bronquitis crónica, enfisema); evalúa seguridad |
| [NCT01110200](https://clinicaltrials.gov/study/NCT01110200) | Fase 4 | Completado | 639 | Fluticasona/salmeterol 250/50 vs salmeterol 50 mcg en la tasa de exacerbaciones de EPOC tras hospitalización |
| [NCT00857766](https://clinicaltrials.gov/study/NCT00857766) | Fase 4 | Completado | 249 | Fluticasona/salmeterol 250/50 vs placebo durante 16 semanas; evalúa la rigidez arterial en EPOC |
| [NCT00633217](https://clinicaltrials.gov/study/NCT00633217) | Fase 4 | Completado | 247 | Fluticasona/salmeterol en inhalador presurizado (HFA) vs DISKUS durante 12 semanas en EPOC; eficacia y seguridad |
| [NCT01332409](https://clinicaltrials.gov/study/NCT01332409) | N/A | Completado | 2000 | Investigación poscomercialización en Japón de salmeterol/fluticasona en EPOC (bronquitis crónica/enfisema); prioriza la aparición de neumonía |
| [NCT01361984](https://clinicaltrials.gov/study/NCT01361984) | Fase 4 | Desconocido | 20 | Arformoterol nebulizado vs salmeterol en polvo seco en EPOC; capacidad inspiratoria y tomografía de alta resolución (estudio pequeño) |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [12970006](https://pubmed.ncbi.nlm.nih.gov/12970006/) | 2003 | ECA | Chest | Eficacia y seguridad de fluticasona 250 µg/salmeterol 50 µg en un solo inhalador Diskus vs placebo y cada componente por separado en EPOC |
| [19124357](https://pubmed.ncbi.nlm.nih.gov/19124357/) | 2008 | ECA | Ther Adv Respir Dis | Seguridad y tolerancia de arformoterol y salmeterol durante 12 meses en EPOC, incluida la aparición de tolerancia |
| [9916607](https://pubmed.ncbi.nlm.nih.gov/9916607/) | 1998 | ECA (abierto) | Clin Ther | Salmeterol inhalado vs teofilina oral en EPOC leve a moderada: eficacia, tolerabilidad y calidad de vida |
| [15970448](https://pubmed.ncbi.nlm.nih.gov/15970448/) | 2006 | Estudio clínico | Pulm Pharmacol Ther | Efecto agudo de salmeterol vs placebo sobre el aclaramiento mucociliar y de la tos en 14 pacientes con bronquitis crónica |
| [17196106](https://pubmed.ncbi.nlm.nih.gov/17196106/) | 2006 | Metaanálisis | Respir Res | Salmeterol 50 mcg dos veces al día frente a placebo/tratamiento habitual en EPOC: estimaciones agrupadas de desenlaces clínicos |
| [15329047](https://pubmed.ncbi.nlm.nih.gov/15329047/) | 2004 | Revisión | Drugs | Revisión del uso de salmeterol/fluticasona inhalado en EPOC; aprobada en EE. UU. para EPOC asociada a bronquitis crónica |
| [19210134](https://pubmed.ncbi.nlm.nih.gov/19210134/) | 2009 | Cohorte | Curr Med Res Opin | Hospitalizaciones, visitas a urgencias y costos en pacientes con bronquitis crónica que inician fluticasona/salmeterol frente a otras terapias de mantenimiento |
| [16915216](https://pubmed.ncbi.nlm.nih.gov/16915216/) | 2006 | Ensayo de experiencia del paciente | MedGenMed | Manejo de la EPOC asociada a bronquitis crónica con fluticasona/salmeterol 250/50 (Advair Diskus) |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Guía | Basic Clin Pharmacol Toxicol | Guía finlandesa de diagnóstico y farmacoterapia de la EPOC estable |

## Información de Mercado en Colombia

Los cinco registros del paquete de datos corresponden al mismo registro sanitario (repetido). En total existen 16 registros.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20128097 | SEROHALE 125 SYNCHROBREATHE SB (CIPLA LTD) | Suspensión para inhalación | Salmeterol y fluticasona |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay varios ensayos de Fase 3 y Fase 4 completados y ECA publicados que respaldan la combinación con salmeterol en EPOC/bronquitis crónica (nivel L1). Sin embargo, la mayoría de los estudios se hizo en EPOC y no en "bronquitis" como entidad separada, y varios títulos están truncados o no identifican claramente el brazo de salmeterol.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA para completar advertencias y contraindicaciones (actualmente sin datos).
- Obtener el mecanismo de acción detallado desde DrugBank.
- Confirmar que las poblaciones de los ensayos corresponden a bronquitis crónica/EPOC y verificar el rol de salmeterol en los ensayos con títulos truncados.
- Definir el monitoreo de seguridad de los LABA, en particular el riesgo cardiovascular.
- Usar salmeterol junto con un corticoide inhalado o un LAMA cuando las guías lo indiquen.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

