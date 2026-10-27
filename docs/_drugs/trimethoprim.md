---
layout: default
title: Trimethoprim
parent: Solo Predicción del Modelo (L5)
nav_order: 646
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Trimethoprim: nueva indicación predicha, Queratoconjuntivitis epitelial punteada (nivel de evidencia L5). Indicación original: Sulfametoxazol y trimetoprim (combinación antibacteriana)"
monitor_inn: "Trimethoprim"
predicted_indications: ["punctate epithelial keratoconjunctivitis"]
---

# Trimethoprim
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

## Trimetoprima: De Sulfametoxazol y Trimetoprim a Queratoconjuntivitis Epitelial Punteada
{: .text-alpha }

## Resumen en Una Frase

Trimetoprima es un antibacteriano que en Colombia se registró como parte de la combinación sulfametoxazol y trimetoprim, en tabletas de uso oral.
El modelo TxGNN predice que podría ser efectivo para **queratoconjuntivitis epitelial punteada**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta indicación específica. Es una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sulfametoxazol y trimetoprim (combinación antibacteriana) |
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punteada |
| Puntaje de Predicción TxGNN | 99.57% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento general, la trimetoprima inhibe la enzima bacteriana dihidrofolato reductasa y bloquea la síntesis de folato, por lo que tiene actividad contra bacterias comunes de la superficie ocular. Su eficacia como antibacteriano está bien establecida, sobre todo en combinación con sulfametoxazol.

La relación con la nueva indicación es débil. La trimetoprima oftálmica, normalmente combinada con polimixina B, ya se usa en infecciones bacterianas de la superficie ocular. Sin embargo, la queratoconjuntivitis epitelial punteada suele ser de origen viral (por ejemplo, adenoviral) o inflamatorio. Un mecanismo antibacteriano no tiene un vínculo directo claro con esa causa, salvo que exista un componente bacteriano.

El puntaje del modelo es muy alto (0.996), pero se basa solo en patrones del grafo de conocimiento biomédico. No hay estudios que lo confirmen, así que debe tratarse como una hipótesis inicial.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20128365 (cancelado) | TRIMETOPRIMA SULFAMETOXAZOL 160/800 MG TABLETA (Laboratorios Ecar S.A.) | Tableta (vía oral) | Sulfametoxazol y trimetoprim |

No hay registros vigentes. Además, la única forma farmacéutica registrada es oral, y no existe una presentación oftálmica en el mercado colombiano según los datos disponibles.

---

## Consideraciones de Seguridad

- **Contraindicaciones o condiciones de riesgo asociadas al fármaco** (según relaciones fármaco-enfermedad del grafo de conocimiento, no según el prospecto):
  - Porfiria (incluida la hereditaria) y trastornos del metabolismo de las porfirinas
  - Enfermedad renal y enfermedad hepática
  - Enfermedad de la vesícula biliar
  - Trombocitopenia, neutropenia y agranulocitosis
  - Deficiencia de G6PD
  - Anemia por deficiencia de ácido fólico
  - Colitis por *Clostridium difficile* y enterocolitis necrosante perinatal
  - Enfermedad por almacenamiento de glucógeno, cistinuria, galactosemia y piuria por uréter (pioureter)
- **Interacciones farmacológicas**: se identificaron 100 interacciones. En las 20 principales disponibles:
  - **Mayores**: citrato de potasio, bicarbonato de potasio, cloruro de potasio y gluconato de potasio. Todas implican riesgo de hiperpotasemia.
  - **Moderadas**: metformina, pioglitazona, rosiglitazona, repaglinida, balsalazida, ácido picosulfúrico y sapropterina.
  - **Nivel no determinado**: pantoprazol, doxiciclina, clotrimazol, morfina, omeprazol, sucralfato, vancomicina, lactulosa y simvastatina.

Estas interacciones corresponden al uso sistémico. Para una formulación oftálmica tópica la exposición sistémica sería mucho menor, pero esto debería confirmarse.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene respaldo de ensayos clínicos ni de literatura (nivel L5), y el vínculo mecanístico con una enfermedad frecuentemente viral es débil. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Revisar la literatura sobre la etiología de la queratoconjuntivitis epitelial punteada y determinar si existe un subtipo bacteriano tratable con trimetoprima.
- Obtener datos del mecanismo de acción y las advertencias y contraindicaciones del prospecto (INVIMA), que no están disponibles actualmente.
- Evaluar la viabilidad de una formulación oftálmica y su vía de administración, ya que en Colombia solo se registró la forma oral.
- Considerar priorizar la segunda predicción del modelo, **conjuntivitis** (puntaje 99.17%, nivel L3). Cuenta con literatura clínica sobre trimetoprima/polimixina B oftálmica en conjuntivitis bacteriana, aunque se parece más a un uso tópico ya establecido que a un reposicionamiento real. Sus diseños de estudio aún deben verificarse.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

