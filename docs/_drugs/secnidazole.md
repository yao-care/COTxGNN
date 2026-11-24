---
layout: default
title: Secnidazole
parent: Solo Predicción del Modelo (L5)
nav_order: 581
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
monitor_inn: "Secnidazole"
predicted_indications: ["postmenopausal atrophic vaginitis", "ulceration of vulva", "vaginal discharge", "vulvar neoplasm", "leukoplakia of vagina", "vulvovaginal candidiasis"]
description: "Secnidazole: nueva indicación predicha, Vaginitis atrófica posmenopáusica (postmenopausal atrophic vaginitis) (nivel de evidencia L5). Indicación original: SECNIDAZOL"
---

# Secnidazole
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

## Secnidazole: Vaginitis atrófica posmenopáusica (postmenopausal atrophic vaginitis)
{: .text-alpha }

## Resumen en Una Frase

Secnidazol es un antimicrobiano de la familia de los 5-nitroimidazoles, registrado en Colombia como principio activo único y en combinación con otros derivados imidazólicos.
El modelo TxGNN predice que podría ser efectivo para **vaginitis atrófica posmenopáusica**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección. La predicción se apoya solo en el modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | SECNIDAZOL; COMBINACIONES DE IMIDAZOL DERIVADOS |
| Nueva Indicación Predicha | Vaginitis atrófica posmenopáusica (postmenopausal atrophic vaginitis) |
| Puntaje de Predicción TxGNN | 0.9970 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 17) |
| Número de Registros Sanitarios | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Secnidazole (traducción no oficial): «SOLOSEC es un fármaco antimicrobiano del grupo de los nitroimidazoles. […] El secnidazol, al igual que otros 5-nitroimidazoles, penetra en las células bacterianas y de Trichomonas, donde el grupo nitro es reducido por una o varias enzimas nitrorreductasas, lo que da lugar a la producción de aniones radicales y de una serie de intermediarios, a la depleción de tioles, al daño del ADN y a la muerte de los aislados sensibles de bacterias grampositivas, bacterias gramnegativas y T. vaginalis.» Texto original en inglés: "SOLOSEC is a nitroimidazole antimicrobial drug. […] Secnidazole, like other 5-nitroimidazoles, enters the bacterial and Trichomonas cells where the nitro group is reduced by nitroreductase enzyme(s) leading to the production of radical anions and a series of intermediates, depletion of thiols, DNA damage, and death of susceptible isolates of Gram positive bacteria, Gram negative bacteria and T. vaginalis." ([DailyMed: Solosec (secnidazole) prescribing information, Evofem Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=056485b6-8bba-4a21-ae00-cdb4e7ae4bfa), versión del 2026-10-30; consultado el 2026-11-19). Por su clase, secnidazol es un 5-nitroimidazol: su grupo nitro se reduce dentro de organismos anaerobios y protozoarios, y genera radicales que dañan el ADN del microorganismo. Por eso se usa contra infecciones anaerobias y protozoarias, como la vaginosis bacteriana y la tricomoniasis.

La vaginitis atrófica posmenopáusica tiene un origen distinto. Se debe a la deficiencia de estrógenos y al adelgazamiento del epitelio vaginal, no a una infección por anaerobios o protozoarios, que es el terreno de acción de secnidazol. **No se identifica un vínculo mecanístico claro** entre el fármaco y esta enfermedad.

El puntaje alto del modelo probablemente refleja la cercanía en la red de conocimiento entre secnidazol y otras afecciones vaginales, y no un fundamento farmacológico. Esta predicción debe tomarse como una señal estadística sin respaldo biológico evidente.

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
| 1980632 | SECNICHEN TABLETAS | TABLETA RECUBIERTA | SECNIDAZOL | Vigente |
| 19903653 | SECNIDAZOL 1 G TABLETAS | TABLETA | SECNIDAZOL | Vigente |
| 19938955 | GIARDAMEB 1 G TABLETAS | TABLETA RECUBIERTA | SECNIDAZOL | Vigente |
| 19942227 | ALBISEC® | CAPSULA DURA | SECNIDAZOL | Vigente |
| 19947567 | NIDAZ®TABLETA 1 G | TABLETA RECUBIERTA | SECNIDAZOL | Vigente |

Se muestran 5 de al menos 20 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes. Los datos de este informe solo incluyen parte de los registros.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 92 interacciones. Las 20 listadas en los datos compilados son todas de nivel moderado (fuente: DDInter). Entre las principales:
  - Otros nitroimidazoles: metronidazol y tinidazol.
  - Estatinas: rosuvastatina, simvastatina y atorvastatina.
  - Antineoplásicos: paclitaxel, cabazitaxel, carboplatino, bortezomib, carfilzomib, trastuzumab emtansina y brentuximab vedotina.
  - Otros: amiodarona, levodopa, adalimumab, certolizumab pegol, auranofina, ácido picosulfúrico y yoduros radiactivos (I-123 e I-131).

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto, pero carece de ensayos clínicos, de literatura y de un mecanismo plausible. La vaginitis atrófica se debe a deficiencia estrogénica, no a infección, aunque el producto está comercializado en Colombia con al menos 17 registros vigentes. No se recomienda avanzar con esta indicación.

<!-- review:begin co-lic-20261112-secnidazole-1 -->

> **Corrección de revisión (2026-11-12)**: Texto original: "Colombia con 4 registros vigentes" Corregido según los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-05): al menos 17 registros sanitarios vigentes (la lista de los datos está limitada a 20 registros). Las cifras actuales están en el Resumen rápido. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261112-secnidazole-1 -->

**Para avanzar se necesita:**
- Una hipótesis mecanística que justifique el uso de un antimicrobiano en un cuadro de origen hormonal, o descartar la predicción como artefacto del modelo.
- Estudios preclínicos o clínicos que muestren algún efecto en vaginitis atrófica.
- Datos de seguridad del prospecto (advertencias y contraindicaciones).
- Confirmar el estado regulatorio y la disponibilidad del producto en Colombia, donde está comercializado y cuenta con al menos 17 registros vigentes.

<!-- review:begin co-lic-20261112-secnidazole-2 -->

> **Corrección de revisión (2026-11-12)**: Texto original: "cuenta con 4 registros vigentes" Corregido según los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-05): al menos 17 registros sanitarios vigentes (la lista de los datos está limitada a 20 registros). Las cifras actuales están en el Resumen rápido. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261112-secnidazole-2 -->

**Nota sobre otras predicciones del modelo:**
En los datos compilados, otras indicaciones tienen más respaldo que la de este informe, aunque en gran parte son usos ya conocidos del fármaco (no reposicionamiento propiamente dicho). Merecen evaluación aparte:
- **Flujo vaginal**: nivel L1, con ensayos de Fase 3 y metaanálisis de secnidazol en dosis única de 2 g para vaginosis bacteriana. Recomendación: Proceed with Guardrails.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-12 | Número de registros vigentes: 4 → al menos 17 | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-12 | Número de registros vigentes: 4 → al menos 17 | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Solosec (secnidazole) prescribing information, Evofem Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=056485b6-8bba-4a21-ae00-cdb4e7ae4bfa) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

