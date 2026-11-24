---
layout: default
title: Baricitinib
parent: Solo Predicción del Modelo (L5)
nav_order: 91
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Baricitinib: nueva indicación predicha, Síndrome de microftalmía colobomatosa con displasia rizomélica (nivel de evidencia L5). Indicación original: BARICITINIB"
monitor_inn: "BARICITINIB"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome"]
---

# Baricitinib
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

## Baricitinib: De Indicación Original (BARICITINIB) a Síndrome de Microftalmía Colobomatosa con Displasia Rizomélica
{: .text-alpha }

## Resumen en Una Frase

Baricitinib es un fármaco de administración oral registrado en Colombia (INVIMA) bajo el nombre comercial OLUMIANT, cuyo texto de indicación aprobada solo menciona el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de microftalmía colobomatosa con displasia rizomélica**, con una puntuación muy alta (0,9994).
Sin embargo, actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción, por lo que se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | BARICITINIB (el registro no detalla una indicación clínica específica) |
| Nueva Indicación Predicha | Síndrome de microftalmía colobomatosa con displasia rizomélica |
| Puntaje de Predicción TxGNN | 0,9994 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Baricitinib (traducción no oficial): «El baricitinib es un inhibidor de las cinasas Janus (JAK). Las JAK son enzimas intracelulares que transmiten señales derivadas de las interacciones de citocinas o factores de crecimiento con sus receptores en la membrana celular para influir en los procesos celulares de la hematopoyesis y la función de las células inmunitarias.» Texto original en inglés: "Baricitinib is a Janus kinase (JAK) inhibitor. JAKs are intracellular enzymes which transmit signals arising from cytokine or growth factor-receptor interactions on the cellular membrane to influence cellular processes of hematopoiesis and immune cell function." ([DailyMed: Olumiant (baricitinib) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=866e9f35-9035-4581-a4b1-75a621ab55cf), versión del 2026-10-09; consultado el 2026-11-19). Según la información conocida, baricitinib es un inhibidor de las quinasas JAK1 y JAK2, que modulan la señalización inflamatoria JAK-STAT.

No se identificó un vínculo biológico plausible entre esa inhibición y este síndrome raro del desarrollo. Este tipo de síndromes suele originarse en defectos genéticos del desarrollo o estructurales, y no en inflamación mediada por JAK-STAT. Por ello, la puntuación proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

La única base de apoyo es la puntuación elevada del modelo. Sin ensayos, literatura ni datos de mecanismo, la razonabilidad de la predicción no puede confirmarse.

*Nota: otra predicción del modelo (rango 2) es el síndrome de braquidactilia-sindactilia (puntuación 0,9994). Tampoco tiene ensayos ni literatura, y no se identificó un vínculo mecanístico entre la inhibición de JAK1/JAK2 y esta malformación congénita de las extremidades. También se clasifica como L5 y Hold.*

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 20157001 | OLUMIANT 2 MG | TABLETA RECUBIERTA | BARICITINIB | Vigente |

Se muestra el único registro sanitario de este principio activo en los datos del INVIMA, Código Único de Medicamentos.

<!-- licenses:end -->

## Consideraciones de Seguridad

**Interacciones Farmacológicas** (100 interacciones registradas; se listan las principales):

- **Gravedad mayor:** hidrocortisona, triamcinolona (incluida la oftálmica), betametasona, budesonida, dexametasona, prednisolona, prednisona, deferiprona, ibritumomab tiuxetán, iobenguano (I-131) y tositumomab (I-131).
- **Gravedad moderada:** morfina (incluida la liposomal), ácido acetilsalicílico, nitisinona y opio.
- **Gravedad menor:** acetato, gluconato y sulfato de zinc.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en la puntuación del modelo (nivel L5), sin ensayos clínicos, literatura ni vínculo mecanístico plausible.

<!-- review:begin co-lic-20261105-baricitinib-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción se apoya solo en la puntuación del modelo (nivel L5), sin ensayos clínicos, literatura ni vínculo mecanístico plausible. Además, el único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-baricitinib-2 -->

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA) y análisis de su relación con la fisiopatología del síndrome.
- Estudios preclínicos o literatura que sustenten un vínculo entre la vía JAK-STAT y este síndrome.
- Advertencias y contraindicaciones del prospecto de INVIMA, para completar la evaluación de seguridad.

<!-- review:begin co-lic-20261031-baricitinib-1 -->

> **Corrección de revisión (2026-10-31)**: Texto original: "Advertencias y contraindicaciones del prospecto de INVIMA, para completar la evaluación de seguridad. / Aclarar la situación regulatoria (registro cancelado) y la indicación aprobada original." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-10-31. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261031-baricitinib-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-10-31 | Eliminado: "Aclarar la situación regulatoria (registro cancelado) y la indicación aprobada original" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Además, el único registro sanitario en Colombia está cancelado" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Olumiant (baricitinib) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=866e9f35-9035-4581-a4b1-75a621ab55cf) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

