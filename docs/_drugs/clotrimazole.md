---
layout: default
title: Clotrimazole
parent: Solo Predicción del Modelo (L5)
nav_order: 175
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Clotrimazole: nueva indicación predicha, Acné (nivel de evidencia L5). Indicación original: Clotrimazol"
monitor_inn: "Clotrimazole"
predicted_indications: ["acne (disease)"]
---

# Clotrimazole
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Clotrimazol: De Infecciones Fúngicas a Acné

## Resumen en Una Frase

Clotrimazol es un antifúngico azólico que se usa de forma local en infecciones por hongos y levaduras de la piel (tiña, pie de atleta) y en candidiasis vaginal.
El modelo TxGNN predice que podría ser efectivo para **acné**, pero hoy esta dirección solo cuenta con **1 ensayo clínico** (suspendido y con una combinación de varios fármacos) y **ninguna publicación** que la respalde.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Clotrimazol (el registro sanitario solo indica el nombre del principio activo; el uso clínico conocido es el tratamiento local de infecciones fúngicas de piel y vaginales) |
| Nueva Indicación Predicha | Acné |
| Puntaje de Predicción TxGNN | 99.86% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ninguno vigente) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base consultada. Según la información conocida, clotrimazol es un antifúngico imidazólico que inhibe la enzima CYP51 (lanosterol 14-alfa-desmetilasa). Con ello bloquea la síntesis de ergosterol y daña la membrana del hongo. También se han descrito efectos antimicrobianos y antiinflamatorios.

El vínculo con el acné es plausible, pero no está demostrado. Podría pasar por la inflamación asociada a *Malassezia* o *Cutibacterium*. La relación entre la indicación original (infecciones cutáneas) y el acné es que ambos son trastornos de la piel con componente microbiano e inflamatorio. Sin embargo, el acné no es una infección fúngica, por lo que la base mecanística es débil.

El único ensayo disponible evalúa una combinación fija (beclometasona + gentamicina + clotrimazol), de modo que cualquier efecto no se puede atribuir al clotrimazol. El puntaje tan alto de TxGNN (99.86%) es solo una predicción computacional.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Fase 2/3 | Suspendido | 80 | Compara la eficacia de la combinación clotrimazol + gentamicina + beclometasona en crema tópica en sujetos con dermatosis contaminada con lesiones bilaterales simétricas. El estado suspendido hace poco probable que haya resultados fiables. El título está truncado, por lo que no queda claro si el estudio trata acné o dermatosis infectadas en general. |

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19971011 | CUTAMYCON 500 MG (cancelado) | Cápsula blanda | Clotrimazol |
| 20018316 | DERMA Q CREMA TÓPICA (cancelado) | Crema tópica | Mometasona |

Ambos registros están cancelados, por lo que actualmente no hay productos vigentes en Colombia con este principio activo según los datos compilados.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad de la base TxGNN/PrimeKG, no texto de prospecto): insuficiencia suprarrenal, enfermedad de Addison, atrofia cutánea, telangiectasia, enfermedad capilar, telangiectasia hemorrágica hereditaria, enfermedad vascular periférica, claudicación intermitente y enfermedad arterial periférica. Varias de estas señales probablemente se relacionan con los corticoides presentes en productos combinados y deben verificarse antes de sacar conclusiones.
- **Dianas farmacológicas y posibles interacciones**: los datos muestran 8 dianas de clotrimazol, no interacciones con otros fármacos con nivel de gravedad definido. Son los canales de potasio KCa1.1 y KCa3.1, los canales TRPM2, TRPM3, TRPM4 y TRPM8, y los receptores nucleares PXR y CAR. La interacción con PXR y CAR podría ser relevante para el metabolismo de otros medicamentos, pero esto requiere revisión específica.

Para advertencias y contraindicaciones formales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para acné solo existe un ensayo suspendido con una combinación de tres fármacos, sin resultados ni literatura de apoyo, y el mecanismo es especulativo. Además, no hay registros vigentes en Colombia. El alto puntaje de TxGNN no basta por sí solo para avanzar.

**Para avanzar se necesita:**
- Datos formales del mecanismo de acción y de la relación entre el efecto antimicrobiano/antiinflamatorio de clotrimazol y la fisiopatología del acné.
- Estudios preclínicos o clínicos que aíslen el efecto de clotrimazol (sin corticoide ni antibiótico asociados).
- Aclarar la indicación real y el diseño del ensayo NCT01244256.
- Obtener y revisar el prospecto aprobado por INVIMA (advertencias y contraindicaciones) y definir la situación regulatoria, dado que los registros están cancelados.

**Nota:** en los datos compilados, la segunda predicción del modelo, **vulvovaginitis**, tiene mucha más evidencia (nivel L1, varios ensayos de Fase 3 completados y literatura con ECA). Se trata de un uso ya establecido y no de un reposicionamiento propiamente dicho. Su decisión asociada es *Proceed with Guardrails*, con atención a la exposición en el primer trimestre del embarazo, a especies resistentes y a la candidiasis recurrente. Si el objetivo es priorizar el candidato más sólido, conviene evaluar esa indicación por separado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

