---
layout: default
title: Atezolizumab
parent: Solo Predicción del Modelo (L5)
nav_order: 72
evidence_level: L5
indication_count: 6
monitor_inn: "ATEZOLIZUMAB"
predicted_indications: ["uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
last_modified_at: 2026-11-24
description: "Atezolizumab: nueva indicación predicha, Adenocarcinoma del ligamento uterino (nivel de evidencia L5). Indicación original: No especificada: el texto del registro solo indica \"ATEZOLIZUMAB\""
---

# Atezolizumab
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

## Atezolizumab: De la indicación registrada (sin detalle) a adenocarcinoma del ligamento uterino
{: .text-alpha }

## Resumen en Una Frase

Atezolizumab es un anticuerpo monoclonal dirigido contra PD-L1 (ligando de muerte programada 1), comercializado en Colombia como TECENTRIQ®. El texto de su registro sanitario solo repite el nombre del principio activo, sin detallar la indicación.
El modelo TxGNN predice que podría ser efectivo para el **adenocarcinoma del ligamento uterino**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada: el texto del registro solo indica "ATEZOLIZUMAB" |
| Nueva Indicación Predicha | Adenocarcinoma del ligamento uterino |
| Puntaje de Predicción TxGNN | 0.9993 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Atezolizumab (traducción no oficial): «PD L1 puede expresarse en las células tumorales o en las células inmunitarias que infiltran el tumor, o en ambas, y puede contribuir a la inhibición de la respuesta inmunitaria antitumoral en el microentorno tumoral. La unión de PD L1 a los receptores PD 1 y B7.1 presentes en los linfocitos T y en las células presentadoras de antígenos suprime la actividad citotóxica de los linfocitos T, la proliferación de los linfocitos T y la producción de citocinas. […] Atezolizumab es un anticuerpo monoclonal que se une a PD L1 y bloquea sus interacciones con los receptores PD 1 y B7.1.» Texto original en inglés: "PD L1 may be expressed on tumor cells and/or tumor infiltrating immune cells and can contribute to the inhibition of the anti-tumor immune response in the tumor microenvironment. Binding of PD L1 to the PD 1 and B7.1 receptors found on T cells and antigen presenting cells suppresses cytotoxic T-cell activity, T-cell proliferation and cytokine production. […] Atezolizumab is a monoclonal antibody that binds to PD L1 and blocks its interactions with both PD 1 and B7.1 receptors." ([DailyMed: Tecentriq (atezolizumab) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6fa682c9-a312-4932-9831-f286908660ee), versión del 2026-10-13; consultado el 2026-11-19). Según lo conocido, atezolizumab bloquea la proteína PD-L1 y con ello puede restablecer la actividad antitumoral de los linfocitos T. Se trata de un enfoque de inmunoterapia contra el cáncer.

La relación con la nueva indicación es solo especulativa. Un posible vínculo sería el bloqueo de PD-L1 en adenocarcinomas ginecológicos, pero no hay ningún dato directo que lo sustente: no se recuperaron ensayos clínicos ni literatura sobre esta enfermedad. El puntaje alto del modelo (0.9993) es solo una predicción computacional y no sustituye la evidencia clínica.

Como referencia, otras predicciones del mismo análisis, como el carcinoma endocervical, sí cuentan con ensayos clínicos: un ensayo de Fase 2 con bevacizumab (n=11) y uno de Fase 1 con quimiorradioterapia (n=40). Ninguno de ellos estudia el adenocarcinoma del ligamento uterino, por lo que no elevan el nivel de evidencia de esta indicación.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 20145962 | TECENTRIQ® | SOLUCION INYECTABLE | ATEZOLIZUMAB | Vigente |

Se muestra el único registro sanitario de este principio activo en los datos del INVIMA, Código Único de Medicamentos.

<!-- licenses:end -->

Titular: F. Hoffmann-La Roche Ltd. Estado: vigente, producto de un solo principio activo.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (anticuerpo anti-PD-L1) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 75 interacciones en la base consultada. Estas son algunas de las principales:
  - **Mayores**: adalimumab, baricitinib y vacuna BCG de cepa Tice con antígeno vivo.
  - **Moderadas**: corticosteroides (hidrocortisona, triamcinolona, betametasona, budesonida, dexametasona, prednisolona, prednisona, metilprednisolona y deflazacort), roflumilast, azatioprina, alefacept, alemtuzumab, anakinra, la vacuna antitetánica con toxoide inactivado y la vacuna contra el ántrax, entre otros.

Para advertencias y contraindicaciones, consultar el prospecto, ya que el texto del registro no estaba disponible para este análisis.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para el adenocarcinoma del ligamento uterino se basa únicamente en el modelo, sin ensayos clínicos ni publicaciones que estudien directamente esta enfermedad (nivel L5). Además, falta la información de seguridad del prospecto, por lo que no es posible avanzar en la evaluación de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones).
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una búsqueda dirigida de literatura y ensayos sobre el adenocarcinoma del ligamento uterino y tumores ginecológicos afines.
- Evaluar la expresión de PD-L1 en este tipo tumoral.
- Considerar priorizar la indicación de carcinoma endocervical, que ya cuenta con ensayos clínicos directos, aunque pequeños y sin resultados disponibles.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Tecentriq (atezolizumab) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6fa682c9-a312-4932-9831-f286908660ee) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

