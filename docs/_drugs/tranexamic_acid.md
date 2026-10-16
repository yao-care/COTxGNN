---
layout: default
title: Tranexamic Acid
parent: Solo Predicción del Modelo (L5)
nav_order: 636
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Tranexamic Acid: nueva indicación predicha, Amenorrea (nivel de evidencia L5). Indicación original: No especificada en los registros (solo figura \"Ácido tranexámico\")"
monitor_inn: "tranexamic acid"
predicted_indications: ["amenorrhea (disease)"]
---

# Tranexamic Acid
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Ácido tranexámico: De Ácido tranexámico (indicación no detallada en el registro) a Amenorrea

## Resumen en Una Frase

El ácido tranexámico es un antifibrinolítico cuyos registros sanitarios en Colombia no detallan la indicación aprobada (solo figura el nombre del principio activo); en la práctica se conoce su uso para reducir el sangrado menstrual abundante.
El modelo TxGNN predice que podría ser efectivo para **Amenorrea**, pero hay **0 ensayos clínicos** y solo **2 publicaciones** de tipo revisión, que además tratan sobre sangrado uterino y supresión de la menstruación, no sobre amenorrea.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en los registros (solo figura "Ácido tranexámico") |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 99.19% |
| Nivel de Evidencia | L4 (sin ensayos clínicos; solo revisiones narrativas indirectas y razonamiento de mecanismo) |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 4 (0 vigentes, 4 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento farmacológico general, el ácido tranexámico es un antifibrinolítico, análogo de la lisina, que bloquea la unión del plasminógeno a la fibrina y así reduce la degradación de los coágulos. Está establecido para disminuir el sangrado menstrual abundante.

La amenorrea es el estado clínico opuesto: ausencia de menstruación. Por ello, el puntaje alto de TxGNN (0.99) probablemente refleja la cercanía en la red de conocimiento con trastornos menstruales (por ejemplo, sangrado uterino anormal) y no un efecto terapéutico real sobre la amenorrea.

El único vínculo plausible es indirecto: la literatura asociada trata sobre la supresión o profilaxis de la menstruación, donde el ácido tranexámico reduce el sangrado como medida sintomática. No trata ni revierte la amenorrea en sí. Por tanto, esta predicción debe considerarse con mucha cautela.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21701432](https://pubmed.ncbi.nlm.nih.gov/21701432/) | 2011 | Revisión | Menopause | Revisa las terapias farmacológicas para el sangrado uterino anormal; son eficaces y en general bien toleradas, y la elección depende de la causa, la cantidad de sangrado, la necesidad de anticoncepción y el estado perimenopáusico |
| [39043214](https://pubmed.ncbi.nlm.nih.gov/39043214/) | 2024 | Revisión | J Oncol Pharm Pract | Enfoque sistemático para la profilaxis y supresión de la menstruación en mujeres premenopáusicas con cáncer hematológico; señala escasez de datos comparativos entre terapias |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20093424 (cancelado) | TAREXA® | Solución inyectable | Ácido tranexámico |
| 20232276 (cancelado) | Ácido tranexámico inyectable 100 mg/ml | Solución inyectable | Ácido tranexámico |
| 20145093 (cancelado) | GOTRONAL® 500 mg tableta | Tableta | Ácido tranexámico |
| 20187927 (cancelado) | Ácido tranexámico solución inyectable | Solución inyectable | Ácido tranexámico |

---

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento (no provienen del prospecto):** hipertensión, trastornos de ansiedad y neuróticos, distimia, porfiria, enfermedad hepática y de la vesícula biliar, hiperglucemia, diabetes mellitus y cetoacidosis diabética, edema cerebral, hipertrigliceridemia e hiperlipidemia, carcinoma de mama femenino, cáncer de endometrio, tromboflebitis, migraña, enfermedad arterial coronaria, obesidad, accidente cerebrovascular y trastornos cerebrovasculares.
- **Interacciones farmacológicas:** se identificaron 35 interacciones, de las cuales se listan las principales:
  - **Mayores:** estrógenos y anticonceptivos hormonales (etinilestradiol, estradiol, estrógenos conjugados, estrógenos esterificados, estrona, dietilestilbestrol, estramustina, noretisterona, drospirenona, etonogestrel), complejo coagulante anti-inhibidor, complejo de factor IX humano y carfilzomib.
  - **Moderadas:** alteplasa y anistreplasa.

  Las combinaciones con estrógenos y anticonceptivos son especialmente relevantes en una población de mujeres con trastornos menstruales, por el posible aumento del riesgo trombótico.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto aprobado.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos y la literatura disponible (dos revisiones narrativas) aborda el sangrado uterino, no la amenorrea. Además, el efecto antifibrinolítico del fármaco es opuesto al estado clínico que se pretende tratar, por lo que el puntaje alto del modelo parece un artefacto de proximidad en la red. A esto se suma que los cuatro registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA con advertencias y contraindicaciones oficiales (brecha bloqueante para el tamizaje de seguridad).
- Complementar los datos del mecanismo de acción desde DrugBank.
- Confirmar si existe una hipótesis clínica real para amenorrea o si la señal corresponde a otra indicación (p. ej., sangrado menstrual abundante).
- Revisar la indicación aprobada en los registros y la razón de su cancelación.
- Evaluar el riesgo trombótico y las interacciones con estrógenos y anticonceptivos antes de cualquier consideración clínica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

