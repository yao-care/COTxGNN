---
layout: default
title: Lidocaine
parent: Solo Predicción del Modelo (L5)
nav_order: 403
evidence_level: L5
indication_count: 10
monitor_inn: "Lidocaine"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "papillary conjunctivitis", "rosacea conjunctivitis", "exposure keratitis", "atopic conjunctivitis", "conjunctival disorder", "nephrotic syndrome", "non-human animal disease", "tinea corporis", "sporadic idiopathic steroid-resistant nephrotic syndrome"]
last_modified_at: 2026-11-25
description: "Lidocaine: nueva indicación predicha, Queratoconjuntivitis epitelial punteada (nivel de evidencia L5). Indicación original: Anestesia local y alivio del dolor (uso descrito en la base farmacoló…"
---

# Lidocaine
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

## Lidocaína: De Anestésico Local a Queratoconjuntivitis Epitelial Punteada
{: .text-alpha }

## Resumen en Una Frase

La lidocaína es un anestésico local que se usa por inyección y en formulaciones tópicas para aliviar el dolor. El modelo TxGNN predice que podría ser efectiva para la **queratoconjuntivitis epitelial punteada**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, por lo que se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Anestesia local y alivio del dolor (uso descrito en la base farmacológica). El texto del registro INVIMA solo dice "Lidocaína combinaciones" / "Lidocaína" |
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punteada |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 18) |
| Número de Registros Sanitarios | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción. Según la información farmacológica disponible, la lidocaína bloquea los canales de sodio dependientes de voltaje (se registran interacciones con Nav1.2, Nav1.4, Nav1.5, Nav1.7 y Nav1.8). Esto explica su efecto anestésico local.

La relación con la nueva indicación es débil. La queratoconjuntivitis epitelial punteada es una alteración inflamatoria o infecciosa de la superficie ocular. Un anestésico local podría aliviar el dolor o la molestia de la superficie ocular, pero no actúa sobre la causa viral o inflamatoria. No se ha establecido ningún vínculo que modifique la enfermedad.

El alto puntaje del modelo TxGNN (deep learning) puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni clínica. Cualquier beneficio plausible sería solo sintomático. Además, los anestésicos tópicos oculares suelen usarse con cautela por su posible efecto sobre la cicatrización de la córnea.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19927232 | NEWCAINA® 2% E80 | SOLUCION INYECTABLE | LIDOCAINA COMBINACIONES | Vigente |
| 19929371 | LIDOCAINA 2% E-100 | SOLUCION INYECTABLE | LIDOCAINA COMBINACIONES | Vigente |
| 19935632 | B-VIT HT | SOLUCION INYECTABLE | TIAMINA (VIT B1) | Vigente |
| 19980849 | LIDOCAINA HCL 2% JALEA ESTERIL | JALEA | LIDOCAINA | Vigente |
| 19982562 | VERSATIS® 5% PARCHES | TRANSDERMICOS | LIDOCAINA | Vigente |

Se muestran 5 de al menos 20 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes. Los datos de este informe solo incluyen parte de los registros.

<!-- licenses:end -->

<!-- review:begin co-lic-20261124b-lidocaine-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Se listan los 3 registros disponibles; puede haber más registros no incluidos." Eliminado: describía la tabla de registros anterior (número de filas, un solo titular o fabricante, o registros que no se mostraban), reemplazada por la tabla generada a partir de los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-23). Los registros, titulares y estados actuales están en la tabla de Información de Mercado en Colombia y en el Resumen rápido. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261124b-lidocaine-1 -->

El texto del registro es una denominación del principio activo, no una indicación clínica detallada. Ninguno de estos registros incluye la queratoconjuntivitis epitelial punteada ni otra indicación ocular, y ninguno corresponde a una presentación oftálmica.

## Consideraciones de Seguridad

- **Relaciones de contraindicación en el grafo de conocimiento** (no provienen del texto del prospecto): el grafo registra relaciones entre la lidocaína y varias enfermedades, entre ellas hipertensión, insuficiencia hepática, enfermedad renal, cirrosis, epilepsia, glaucoma de ángulo abierto, insuficiencia suprarrenal (enfermedad de Addison), hipotiroidismo, osteoporosis, trastornos psicóticos y esquizoafectivos, queratitis por herpes simple, varicela zóster, dermatitis atópica, dermatofitosis, deficiencia de potasio y gastritis. Estas relaciones requieren verificación frente al prospecto oficial.
- **Señales de seguridad en la literatura revisada para otras predicciones**: se describen efectos neuropsiquiátricos y cardiológicos con lidocaína intravenosa (PMID 19250287) y un caso de metahemoglobinemia en un niño con síndrome nefrótico que recibió lidocaína tópica junto con otros fármacos (PMID 41995267).

Para las advertencias y contraindicaciones oficiales, consultar el prospecto aprobado por INVIMA.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo TxGNN (nivel L5), sin ensayos ni publicaciones sobre esta enfermedad. Además, la lidocaína solo ofrecería alivio sintomático, sin acción sobre la causa, y existen cautelas sobre el uso de anestésicos en la superficie ocular.

**Para avanzar se necesita:**
- Estudios preclínicos o clínicos que evalúen directamente la lidocaína en la queratoconjuntivitis epitelial punteada.
- Datos detallados del mecanismo de acción y de la relación con la indicación original.
- Revisión del prospecto de INVIMA para advertencias y contraindicaciones oficiales.
- Evaluación de la compatibilidad de vía y formulación (las presentaciones registradas en Colombia incluyen formas inyectables, tópicas, bucales, óticas y rectales, ninguna oftálmica).
- Evaluación de seguridad ocular, en particular el efecto de la lidocaína sobre la cicatrización corneal.

<!-- review:begin co-lic-20261125-lidocaine-1 -->

> **Corrección de revisión (2026-11-25)**: Texto original: "(las presentaciones registradas en Colombia son supositorio, ungüento y crema, ninguna oftálmica)" Corregido según los datos del INVIMA: las presentaciones registradas no se limitan a supositorio, ungüento y crema; ninguna es oftálmica. Las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261125-lidocaine-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-24 | Eliminado: "Se listan los 3 registros disponibles; puede haber más registros no incluidos." | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-25 | «son supositorio, ungüento y crema» → «incluyen formas inyectables, tópicas, bucales, óticas y rectales» | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

