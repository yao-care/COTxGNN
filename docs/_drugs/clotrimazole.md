---
layout: default
title: Clotrimazole
parent: Solo Predicción del Modelo (L5)
nav_order: 175
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
monitor_inn: "Clotrimazole"
predicted_indications: ["acne (disease)", "postmenopausal atrophic vaginitis"]
description: "Clotrimazole: nueva indicación predicha, Acné (acne (disease)) (nivel de evidencia L5). Indicación original: CLOTRIMAZOL"
---

# Clotrimazole
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Clotrimazole: Acné (acne (disease))
{: .text-alpha }

## Resumen en Una Frase

Clotrimazol es un antifúngico azólico que se usa de forma local en infecciones por hongos y levaduras de la piel (tiña, pie de atleta) y en candidiasis vaginal.
El modelo TxGNN predice que podría ser efectivo para **acné**, pero hoy esta dirección solo cuenta con **1 ensayo clínico** (suspendido y con una combinación de varios fármacos) y **ninguna publicación** que la respalde.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | CLOTRIMAZOL; MOMETASONE; COMBINACIONES; MUPIROCINA |
| Nueva Indicación Predicha | Acné (acne (disease)) |
| Puntaje de Predicción TxGNN | 0.9986 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 20) |
| Número de Registros Sanitarios | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base consultada. Según la información conocida, clotrimazol es un antifúngico imidazólico que inhibe la enzima CYP51 (lanosterol 14-alfa-desmetilasa). Con ello bloquea la síntesis de ergosterol y daña la membrana del hongo. También se han descrito efectos antimicrobianos y antiinflamatorios.

El vínculo con el acné es plausible, pero no está demostrado. Podría pasar por la inflamación asociada a *Malassezia* o *Cutibacterium*. La relación entre la indicación original (infecciones cutáneas) y el acné es que ambos son trastornos de la piel con componente microbiano e inflamatorio. Sin embargo, el acné no es una infección fúngica, por lo que la base mecanística es débil.

El único ensayo disponible evalúa una combinación fija (beclometasona + gentamicina + clotrimazol), de modo que cualquier efecto no se puede atribuir al clotrimazol. El puntaje tan alto de TxGNN (0.9986) es solo una predicción computacional.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Fase 2/3 | Suspendido | 80 | Compara la eficacia de la combinación clotrimazol + gentamicina + beclometasona en crema tópica en sujetos con dermatosis contaminada con lesiones bilaterales simétricas. El estado suspendido hace poco probable que haya resultados fiables. El título está truncado, por lo que no queda claro si el estudio trata acné o dermatosis infectadas en general. |

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

<!-- review:begin co-lic-20261105-clotrimazole-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Ambos registros están cancelados, por lo que actualmente no hay productos vigentes en Colombia con este principio activo según los datos compilados." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-clotrimazole-1 -->

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19971011 | CUTAMYCON 500 MG (vigente) | Cápsula blanda | Clotrimazol |
| 20018316 | DERMA Q CREMA TÓPICA (vigente) | Crema tópica | Mometasona |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad de la base TxGNN/PrimeKG, no texto de prospecto): insuficiencia suprarrenal, enfermedad de Addison, atrofia cutánea, telangiectasia, enfermedad capilar, telangiectasia hemorrágica hereditaria, enfermedad vascular periférica, claudicación intermitente y enfermedad arterial periférica. Varias de estas señales probablemente se relacionan con los corticoides presentes en productos combinados y deben verificarse antes de sacar conclusiones.
- **Dianas farmacológicas y posibles interacciones**: los datos muestran 8 dianas de clotrimazol, no interacciones con otros fármacos con nivel de gravedad definido. Son los canales de potasio KCa1.1 y KCa3.1, los canales TRPM2, TRPM3, TRPM4 y TRPM8, y los receptores nucleares PXR y CAR. La interacción con PXR y CAR podría ser relevante para el metabolismo de otros medicamentos, pero esto requiere revisión específica.

Para advertencias y contraindicaciones formales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para acné solo existe un ensayo suspendido con una combinación de tres fármacos, sin resultados ni literatura de apoyo, y el mecanismo es especulativo. El alto puntaje de TxGNN no basta por sí solo para avanzar.

<!-- review:begin co-lic-20261105-clotrimazole-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, no hay registros vigentes en Colombia. El alto puntaje de TxGNN no basta por sí solo para avanzar." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-clotrimazole-2 -->

**Para avanzar se necesita:**
- Datos formales del mecanismo de acción y de la relación entre el efecto antimicrobiano/antiinflamatorio de clotrimazol y la fisiopatología del acné.
- Estudios preclínicos o clínicos que aíslen el efecto de clotrimazol (sin corticoide ni antibiótico asociados).
- Aclarar la indicación real y el diseño del ensayo NCT01244256.
- Obtener y revisar el prospecto aprobado por INVIMA (advertencias y contraindicaciones) y definir la situación regulatoria.

<!-- review:begin co-lic-20261105-clotrimazole-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Obtener y revisar el prospecto aprobado por INVIMA (advertencias y contraindicaciones) y definir la situación regulatoria, dado que los registros están cancelados." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-clotrimazole-3 -->

Se trata de un uso ya establecido y no de un reposicionamiento propiamente dicho. Su decisión asociada es *Proceed with Guardrails*, con atención a la exposición en el primer trimestre del embarazo, a especies resistentes y a la candidiasis recurrente. Si el objetivo es priorizar el candidato más sólido, conviene evaluar esa indicación por separado.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Ambos registros están cancelados, por lo que actualmente no hay productos vigentes en Colombia con este principio activo según los datos com" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Además, no hay registros vigentes en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "dado que los registros están cancelados" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

