---
layout: default
title: Diazoxide
parent: Solo Predicción del Modelo (L5)
nav_order: 218
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Diazoxide: nueva indicación predicha, Alopecia (nivel de evidencia L5). Indicación original: No especificada en el registro (el texto solo indica \"DIAZOXIDO\")"
monitor_inn: "diazoxide"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "hypertrichosis (disease)", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "autosomal dominant hyperinsulinism due to Kir6.2 deficiency"]
---

# Diazoxide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Diazóxido: De Diazóxido (indicación no detallada en el registro) a Alopecia

## Resumen en Una Frase

El diazóxido es un abridor de canales de potasio sensibles a ATP (KATP), registrado en Colombia en suspensión oral. El texto del registro sanitario solo menciona el nombre del principio activo y no detalla la indicación aprobada. El modelo TxGNN predice que podría ser efectivo para **alopecia** (la predicción con mayor evidencia entre las 10 candidatas), pero **no hay ensayos clínicos** y solo existe **evidencia preclínica y de revisiones** (6 publicaciones), por lo que el respaldo es débil.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto solo indica "DIAZOXIDO") |
| Nueva Indicación Predicha | Alopecia |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L4 (solo estudios preclínicos y revisiones) |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold (la alternativa sería un programa de investigación tópico exploratorio) |

**Nota sobre la selección:** TxGNN ordenó primero "hipotricosis simple del cuero cabelludo" (99.96%, L5, sin evidencia). Este informe se centra en **alopecia** (rango 4) por ser la candidata con evidencia preclínica directa. Las demás predicciones se resumen en la conclusión.

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados no incluyen el mecanismo de acción del registro. Según el conocimiento farmacológico general, el diazóxido abre canales KATP, lo que hiperpolariza las células y relaja el músculo liso vascular. Esto explica su efecto antihipertensivo y su inhibición de la liberación de insulina en el páncreas, por lo que se usa en hiperinsulinismo.

La relación con la alopecia proviene de un efecto secundario conocido: el diazóxido causa hipertricosis. El minoxidil, otro abridor de canales KATP, se usa para tratar la alopecia androgenética. Un estudio de 1990 en macacos con calvicie frontal (PMID 2085505) aplicó diazóxido tópico para estudiar el rebrote del cabello, y una revisión de 1993 (PMID 8326148) indica que el diazóxido y el minoxidil inducen rebrote significativo en el cuero cabelludo calvo de macacos.

Esta lógica es plausible, pero no está demostrada en humanos. El uso sistémico implica riesgos importantes (hiperglucemia, retención de líquidos), por lo que cualquier exploración tendría que ser tópica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [8326148](https://pubmed.ncbi.nlm.nih.gov/8326148/) | 1993 | Revisión | J Invest Dermatol | Minoxidil y diazóxido tópicos indujeron rebrote significativo en cuero cabelludo calvo de macacos; ambos tienen hipertricosis como efecto secundario |
| [2085505](https://pubmed.ncbi.nlm.nih.gov/2085505/) | 1990 | Preclínico (primate no humano) | J Dermatol Sci | Diazóxido tópico aplicado al cuero cabelludo frontal calvo de macacos de cola corta, con seguimiento de efectos sistémicos |
| [8018303](https://pubmed.ncbi.nlm.nih.gov/8018303/) | 1994 | Revisión | Drug Safety | Incidencia, manejo y prevención de la caída y el crecimiento del cabello inducidos por fármacos |
| [37042338](https://pubmed.ncbi.nlm.nih.gov/37042338/) | 2023 | Reporte de caso | Pediatr Dermatol | Hipertricosis generalizada en un niño por exposición secundaria a minoxidil tópico; menciona el diazóxido como causa posible de hipertricosis |
| [4340017](https://pubmed.ncbi.nlm.nih.gov/4340017/) | 1972 | Serie de casos | Arch Dis Child | Exposición fetal a diazóxido en cuatro lactantes; no aborda la alopecia |
| [20682429](https://pubmed.ncbi.nlm.nih.gov/20682429/) | 2010 | Revisión | Vet Clin North Am Exot Anim Pract | Manejo de insulinomas y enfermedad adrenocortical en hurones; el diazóxido es una opción médica; no relacionado con alopecia |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20126583 (cancelado) | DIAZOXIUS® 50 MG/ML SUSPENSION ORAL | Suspensión oral | DIAZOXIDO |
| 20177313 (cancelado) | AZOXID® 50 MG/ML SUSPENSION ORAL | Suspensión oral | DIAZOXIDO |

Ambos registros están cancelados, por lo que actualmente no hay producto vigente en Colombia. Además, no existe forma tópica registrada.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (TxGNN/PrimeKG, no del prospecto):** hipotensión ortostática, síndrome de taquicardia postural ortostática, atrofia multisistémica, enfermedad renal, insuficiencia renal, uremia, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, hiperglucemia, diabetes mellitus, cetoacidosis diabética, insuficiencia cardíaca congestiva, deficiencia de potasio, hiperuricemia, gota, trastorno cerebrovascular y enfermedad coronaria.
- **Interacciones farmacológicas:** se identificaron 209 interacciones. Las 20 listadas son de nivel moderado e incluyen:
  - Antidiabéticos (acarbosa, metformina, pioglitazona, clorpropamida, acetohexamida, canagliflozina, dapagliflozina, empagliflozina, ertugliflozina, alogliptina, albiglutida, dulaglutida).
  - Corticoides (hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida).
  - Otros: bupropión, morfina, dronabinol.
- **Eventos adversos descritos en la literatura recopilada:** hipertricosis, retención de líquidos, insuficiencia cardíaca, insuficiencia renal aguda y enterocolitis necrosante en neonatos.

No se dispone de las advertencias del prospecto del INVIMA; consultar el prospecto cuando esté disponible.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia para alopecia se limita a un estudio preclínico en primates y revisiones, sin ensayos clínicos en humanos. El perfil de seguridad sistémico es desfavorable, y el producto no tiene registro vigente en Colombia ni formulación tópica.

**Otras predicciones del modelo (todas en Hold):**
- Hipotricosis simple del cuero cabelludo, hipotricosis congénita con milia, alopecia areata difusa: sin evidencia (L5). En alopecia areata el mecanismo es autoinmune, por lo que el beneficio sería a lo sumo complementario.
- Hipertricosis, hipertricosis universal congénita tipo Ambras: probablemente falsos positivos, porque el diazóxido *causa* hipertricosis y no tendría sentido usarlo para tratarla.
- Síndrome malformativo con componente dental, síndrome con malformación de Dandy-Walker, anomalía genética aislada del tallo piloso: sin fundamento mecanístico identificable.
- Hiperinsulinismo autosómico dominante por deficiencia de Kir6.2: tiene base mecanística, pero es más una cuestión de confirmación de indicación que de reposicionamiento, y la respuesta depende de la variante.

**Para avanzar se necesita:**
- Obtener el prospecto del INVIMA (advertencias y contraindicaciones) y los datos de mecanismo de acción desde DrugBank.
- Estudios de formulación tópica y de absorción sistémica, dado el riesgo de hiperglucemia y retención de líquidos.
- Estudios en humanos (fase 1/2 tópicos) que comparen con minoxidil en alopecia androgenética.
- Verificar la situación regulatoria en Colombia (los dos registros están cancelados).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

