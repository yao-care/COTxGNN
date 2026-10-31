---
layout: default
title: Tacrolimus
parent: Evidencia Alta (L1-L2)
nav_order: 600
evidence_level: L1
indication_count: 2
last_modified_at: 2026-10-31
description: "Tacrolimus: nueva indicación predicha, Dermatitis seborreica (nivel de evidencia L1). Indicación original: No especificada en los registros (el texto de indicación solo indica…"
monitor_inn: "TACROLIMUS"
predicted_indications: ["seborrheic dermatitis", "parapsoriasis"]
---

# Tacrolimus
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **2** 
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

## Tacrolimus: De Indicación No Especificada (Inmunosupresor) a Dermatitis Seborreica
{: .text-alpha }

## Resumen en Una Frase

Tacrolimus es un inhibidor de la calcineurina cuyo registro sanitario en Colombia no detalla la indicación aprobada (solo figura el nombre del principio activo).
El modelo TxGNN predice que podría ser efectivo para **dermatitis seborreica**,
con **2 ensayos clínicos** (uno de Fase 3 completado) y **20 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en los registros (el texto de indicación solo indica "Tacrolimus") |
| Nueva Indicación Predicha | Dermatitis seborreica |
| Puntaje de Predicción TxGNN | 0.9926 |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 3) |
| Número de Registros Sanitarios | al menos 3 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento farmacológico general, tacrolimus inhibe la calcineurina, lo que bloquea la activación de los linfocitos T dependiente de NFAT y reduce la liberación de citocinas proinflamatorias como la IL-2.

La dermatitis seborreica es una enfermedad inflamatoria crónica de la piel, con recaídas frecuentes, en la que interviene una respuesta inmunitaria frente a la levadura *Malassezia*. Al calmar el componente inflamatorio, un inhibidor de la calcineurina tópico es una alternativa plausible a los corticoides, cuyo uso prolongado tiene efectos adversos. El mismo mecanismo sustenta su uso establecido en la dermatitis atópica.

Cabe señalar que este vínculo mecanístico se basa en conocimiento farmacológico general y no en el registro suministrado. Además, la evidencia corresponde a la formulación **tópica** (ungüento), mientras que los registros colombianos identificados son de formas orales (cápsulas).

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02004860](https://clinicaltrials.gov/study/NCT02004860) | Fase 3 | Completado | 120 | Ungüento de tacrolimus (Protopic) como tratamiento de mantenimiento de la dermatitis seborreica grave en la cara de adultos, para reducir recaídas y uso de corticoides tópicos |
| [NCT01591070](https://clinicaltrials.gov/study/NCT01591070) | Fase 4 | Completado | 104 | Uso proactivo de tacrolimus 0.1% una o dos veces por semana para mantener la remisión de la dermatitis seborreica facial del adulto |

Los diseños detallados y los resultados de estos ensayos no están en los datos compilados y deben verificarse.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Revisión sistemática | Am J Clin Dermatol | Revisa los tratamientos tópicos de la dermatitis seborreica facial (antifúngicos, queratolíticos, corticoides) |
| [26512166](https://pubmed.ncbi.nlm.nih.gov/26512166/) | 2015 | Estudio clínico | Ann Dermatol | Terapia de mantenimiento con tacrolimus 0.1% en dermatitis seborreica facial |
| [19222250](https://pubmed.ncbi.nlm.nih.gov/19222250/) | 2009 | Revisión | Am J Clin Dermatol | Los inhibidores tópicos de la calcineurina como alternativa segura a los corticoides en dermatitis seborreica |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Revisión | J Drugs Dermatol | Estado actual y perspectivas terapéuticas de la dermatitis seborreica facial |
| [15461548](https://pubmed.ncbi.nlm.nih.gov/15461548/) | 2004 | Revisión | Expert Opin Pharmacother | Ungüento de tacrolimus en dermatitis atópica y otras enfermedades cutáneas inflamatorias |
| [24171300](https://pubmed.ncbi.nlm.nih.gov/24171300/) | 2013 | Estudio clínico | Ann Parasitol | Comparación de sertaconazol 2% y tacrolimus 0.03% en crema en 60 pacientes con dermatitis seborreica |
| [31476936](https://pubmed.ncbi.nlm.nih.gov/31476936/) | 2019 | Revisión | J Cutan Med Surg | Uso fuera de indicación de inhibidores tópicos de la calcineurina en trastornos dermatológicos |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 19983582 | PROGRAF® XL cápsulas de liberación prolongada de 0.5 mg | Cápsula de liberación prolongada | Tacrolimus | Vigente |
| 20192450 | Tacrolimus 3 mg cápsulas duras de liberación prolongada | Cápsula de liberación prolongada | Tacrolimus | Vigente |
| 20230266 | TALIMUZ® 1 mg | Cápsula dura | Tacrolimus | Vigente |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** hipertensión, síndrome de QT largo (incluido el familiar) y torsades de pointes, insuficiencia hepática, enfermedad renal, epilepsia, hiperglucemia, diabetes mellitus y cetoacidosis diabética, infecciones (herpes simple, herpes zóster, mononucleosis infecciosa, infección crónica por virus de Epstein-Barr, leucoencefalopatía multifocal progresiva), cáncer y linfomas (incluido el linfoma primario del sistema nervioso central), delirio, síndrome de leucoencefalopatía posterior y anemia aplásica hereditaria. Estas asociaciones se refieren sobre todo al uso sistémico.
- **Interacciones farmacológicas:** se identificaron 100 interacciones. Entre las de nivel **mayor** figuran anfotericina B (incluida la formulación de complejo lipídico), loperamida, mesalazina, omeprazol y balsalazida. Entre las de nivel **moderado** figuran acarbosa, famotidina, rabeprazol, hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida, metformina, pioglitazona, alogliptina, albiglutida, aprepitant y metronidazol.
- **Señal de seguridad en la literatura:** existe un metaanálisis sobre el riesgo de cáncer con inhibidores tópicos de la calcineurina en dermatitis atópica (PMID 36370744), que justifica el monitoreo a largo plazo. Otro estudio describe niveles sistémicos elevados con aplicación oclusiva (PMID 16549924).

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ensayo de Fase 3 completado y un estudio de Fase 4 completado específicamente en dermatitis seborreica con tacrolimus tópico, además de revisiones que respaldan el mecanismo. Sin embargo, solo hay un ensayo de Fase 3 (el nivel L1 asignado exige confirmar la solidez de los resultados) y en Colombia no hay registros vigentes de tacrolimus tópico.

**Para avanzar se necesita:**
- Verificar los diseños y resultados de los ensayos NCT02004860 y NCT01591070 (aleatorización, enmascaramiento, desenlaces).
- Obtener el prospecto en INVIMA (advertencias y contraindicaciones) y confirmar la situación regulatoria de una formulación tópica, ya que los registros colombianos identificados son orales y están cancelados.
- Completar los datos del mecanismo de acción desde DrugBank.
- Definir un plan de monitoreo de seguridad a largo plazo (riesgo de neoplasias, absorción sistémica, infecciones cutáneas).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

