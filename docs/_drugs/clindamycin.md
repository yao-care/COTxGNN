---
layout: default
title: Clindamycin
parent: Solo Predicción del Modelo (L5)
nav_order: 165
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-12
description: "Clindamycin: nueva indicación predicha, Queratoconjuntivitis epitelial punteada (nivel de evidencia L5). Indicación original: Clindamicina combinaciones"
monitor_inn: "Clindamycin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "exposure keratitis", "non-human animal disease", "neurotrophic keratopathy", "epidemic keratoconjunctivitis", "postmenopausal atrophic vaginitis"]
---

# Clindamycin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Clindamicina: De Clindamicina (Combinaciones) a Queratoconjuntivitis Epitelial Punteada
{: .text-alpha }

## Resumen en Una Frase

Clindamicina es un antibiótico lincosamida, registrado en Colombia en presentaciones vaginales (óvulos y cremas) para el tratamiento de infecciones ginecológicas.
El modelo TxGNN predice que podría ser efectivo para **queratoconjuntivitis epitelial punteada**,
pero **no hay ensayos clínicos ni publicaciones** que respalden esta indicación; se trata únicamente de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Clindamicina combinaciones |
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punteada |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 11 de 11) |
| Número de Registros Sanitarios | 11 (vigentes: 11) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la clindamicina es un antibiótico del grupo de las lincosamidas que inhibe la síntesis de proteínas bacterianas y es activo principalmente frente a bacterias Gram positivas. Su eficacia en infecciones ginecológicas locales es la base de su uso original.

La relación con la nueva indicación es débil. La queratopatía epitelial punteada suele ser de origen no infeccioso (ojo seco, toxicidad o infección viral), por lo que un mecanismo antibacteriano no resulta claramente relevante. Además, la clindamicina sistémica difícilmente alcanzaría la superficie ocular en concentraciones útiles.

En consecuencia, el puntaje alto del modelo (0.9997) no está respaldado por evidencia clínica ni por un vínculo mecanístico claro. Debe interpretarse como una hipótesis para generar ideas, no como una recomendación terapéutica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

Como referencia, la segunda indicación predicha (queratitis por exposición, puntaje 0.9980) cuenta con literatura indirecta sobre queratitis infecciosa (por *Staphylococcus aureus* y *Bacillus cereus*). Ninguno de esos estudios evalúa la clindamicina para esa indicación, y las demás indicaciones predichas tampoco tienen respaldo clínico relevante.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20131113 | PRIVARE® 2C1019541002 | Óvulo | Clindamicina combinaciones | Vigente |
| 20129610 | CLINDASHER® Crema Vaginal | Crema vaginal | Clindamicina | Vigente |
| 20097862 | GYNO BACLIN® | Crema vaginal | Clindamicina | Vigente |
| 20014120 | VAGYLIN | Crema vaginal | Clindamicina | Vigente |

---

## Consideraciones de Seguridad

- **Enfermedades con contraindicación según el grafo de conocimiento (no proviene del prospecto)**: insuficiencia hepática, enfermedad de Crohn, enfermedad inflamatoria intestinal, colitis ulcerosa, colitis por *Clostridium difficile*, enfermedad diarreica, enterocolitis necrosante perinatal, dermatitis atópica, dermatitis exfoliativa, dermatitis, quemadura solar y candidiasis vulvovaginal.
- **Interacciones farmacológicas**: se identificaron 100 interacciones en total. Las de nivel moderado incluyen balsalazida, claritromicina, ácido picosulfúrico, atapulgita y caolín. Entre las de nivel no clasificado figuran anfotericina B, ácido acetilsalicílico, amoxicilina, bupropión, pantoprazol, glimepirida, doxiciclina, clotrimazol, morfina, metformina, omeprazol, sucralfato, rosiglitazona, lansoprazol y vancomicina.

Para advertencias y contraindicaciones del prospecto, consultar el prospecto del producto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción carece de ensayos clínicos y literatura de apoyo, y el mecanismo antibacteriano de la clindamicina no se relaciona claramente con una queratopatía mayormente no infecciosa. Además, el medicamento está comercializado en Colombia y cuenta con 11 registros sanitarios vigentes.

<!-- review:begin co-lic-20261112-clindamycin-1 -->

> **Corrección de revisión (2026-11-12)**: Texto original: "4 registros sanitarios vigentes" Corregido según los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-05): 11 registros sanitarios, de los cuales 11 vigentes. Las cifras actuales están en el Resumen rápido. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261112-clindamycin-1 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción de la clindamicina y análisis de su relevancia para la superficie ocular
- Estudios preclínicos o de farmacocinética ocular que respalden una vía tópica oftálmica
- Revisión del prospecto (advertencias y contraindicaciones) para completar la evaluación de seguridad
- Confirmar la causa (infecciosa o no) de la queratopatía epitelial punteada, para definir si hay un papel plausible de un antibacteriano
- Evaluar la situación regulatoria

<!-- review:begin co-lic-20261105-clindamycin-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Evaluar la situación regulatoria, dado que no hay registros vigentes en Colombia" Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 11 registros sanitarios (vigentes: 11); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-clindamycin-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "dado que no hay registros vigentes en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-12 | Número de registros vigentes: 4 → 11 | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

