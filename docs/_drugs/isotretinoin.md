---
layout: default
title: Isotretinoin
parent: Solo Predicción del Modelo (L5)
nav_order: 359
evidence_level: L5
indication_count: 1
monitor_inn: "Isotretinoin"
predicted_indications: ["malignant hypertensive renal disease"]
last_modified_at: 2026-11-24
description: "Isotretinoin: nueva indicación predicha, enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) (nivel de evidencia L5). Indicación original: ISOTETRINOINA"
---

# Isotretinoin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Isotretinoína: retinoide sistémico → enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)
{: .text-alpha }

## Resumen en Una Frase

Isotretinoína es un retinoide que actúa sobre los receptores del ácido retinoico y cuenta con registros sanitarios en Colombia.
El modelo TxGNN predice que podría ser efectivo para **enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)**,
pero actualmente no hay ensayos clínicos ni publicaciones que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | ISOTETRINOINA |
| Nueva Indicación Predicha | enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) |
| Puntaje de Predicción TxGNN | 0,9901 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 7 de 12) |
| Número de Registros Sanitarios | 12 (vigentes: 7) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Isotretinoin (traducción no oficial): «Se desconoce el mecanismo de acción exacto de Zenatane en el tratamiento del acné nodular grave y resistente en pacientes no embarazadas de 12 años de edad o más con múltiples nódulos inflamatorios de un diámetro de 5 mm o más que no responden al tratamiento convencional, incluidos los antibióticos sistémicos. La isotretinoína, un retinoide, inhibe la función de las glándulas sebáceas y la queratinización.» Texto original en inglés: "The exact mechanism of action of Zenatane in the treatment of severe recalcitrant nodular acne in nonpregnant patients 12 years of age and older with multiple inflammatory nodules with a diameter of 5 mm or greater who are unresponsive to conventional therapy, including systemic antibiotics is unknown. Isotretinoin, a retinoid, inhibits sebaceous gland function and keratinization." ([DailyMed: Zenatane (isotretinoin) prescribing information, Dr. Reddy's Laboratories Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=27b3cf26-f22e-5b70-1c24-009933b7c6ee), versión del 2026-09-20; consultado el 2026-11-19). Según la información conocida, la isotretinoína es un retinoide que actúa a través de los receptores del ácido retinoico, los cuales regulan la diferenciación celular.

Hay descripciones preclínicas de que la señalización del ácido retinoico podría influir en la biología renal y vascular (por ejemplo, en el sistema renina-angiotensina y en la lesión glomerular o de los podocitos). Esto es solo una hipótesis: ningún dato aportado en este informe la respalda, y el puntaje del modelo (0,9901) es únicamente una predicción computacional.

Además, la isotretinoína se asocia con posibles efectos sobre la presión arterial y los lípidos, y es fuertemente teratogénica, lo que plantea preocupaciones de seguridad en esta población.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Los datos compilados registran 3 registros sanitarios de isotretinoína en monoterapia (la lista puede ser parcial):

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19962874 | ROVACOR ® | CAPSULA BLANDA | ISOTETRINOINA | Vigente |
| 19970684 | ISOTRETINOINA 20 MG | CAPSULA BLANDA | ISOTETRINOINA | Vigente |
| 19970685 | ISOTRETINOINA 10 MG | CAPSULA BLANDA | ISOTETRINOINA | Vigente |
| 19980098 | REYTRIN 20 MG CAPSULA | CAPSULA BLANDA | ISOTETRINOINA | Vigente |
| 20020357 | ISOFACE 20 MG | CAPSULA BLANDA | ISOTETRINOINA | Vigente |

Se muestran 5 de 12 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 98 interacciones en total. Las de nivel mayor son con:
  - doxiciclina
  - minociclina
  - tetraciclina
  - vitamina A

  Entre las de nivel moderado figuran:
  - corticoesteroides (betametasona, budesonida, dexametasona, hidrocortisona, prednisolona, prednisona, triamcinolona)
  - warfarina
  - dicumarol
  - etanol
  - naltrexona
  - nitisinona
  - fostamatinib
  - ivacaftor
  - lumacaftor
  - abametapir tópico

- **Teratogenicidad**: la isotretinoína es fuertemente teratogénica. Esta información proviene de conocimiento general del fármaco y debe confirmarse en el prospecto.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5): no hay ensayos clínicos ni literatura que estudien directamente la enfermedad renal hipertensiva maligna con isotretinoína. Además, existen preocupaciones de seguridad relevantes (teratogenicidad, posibles efectos sobre la presión arterial y los lípidos).

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde fuentes como DrugBank
- Prospecto de INVIMA con advertencias y contraindicaciones, para el tamizaje de seguridad
- Estudios preclínicos o clínicos que evalúen directamente la isotretinoína en esta enfermedad renal
- Evaluación de la compatibilidad de la vía de administración y de la similitud con la indicación original

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Zenatane (isotretinoin) prescribing information, Dr. Reddy's Laboratories Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=27b3cf26-f22e-5b70-1c24-009933b7c6ee) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

