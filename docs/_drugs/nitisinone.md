---
layout: default
title: Nitisinone
parent: Solo Predicción del Modelo (L5)
nav_order: 470
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
description: "Nitisinone: nueva indicación predicha, Acidosis tubular renal (nivel de evidencia L5). Indicación original: NITISINONA"
monitor_inn: "nitisinone"
predicted_indications: ["renal tubular acidosis", "galactosemia", "serpinopathy with toxic serpin polymerization", "C1 inhibitor deficiency", "glycogen storage disease", "adult polyglucosan body disease", "glycogen storage disease due to glucose-6-phosphatase deficiency", "Griscelli syndrome", "granulomatous disease, chronic, X-linked", "ermine phenotype"]
---

# Nitisinone
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

## Nitisinona: De Tirosinemia Tipo 1 a Acidosis Tubular Renal
{: .text-alpha }

## Resumen en Una Frase

Nitisinona es un inhibidor de la enzima HPPD, utilizado originalmente para el tratamiento de la tirosinemia hereditaria tipo 1 (el registro sanitario en Colombia solo indica "NITISINONA" como indicación).
El modelo TxGNN predice que podría ser efectivo para **acidosis tubular renal**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, por lo que se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | NITISINONA (el registro no detalla la indicación; por mecanismo y uso conocido corresponde a tirosinemia hereditaria tipo 1) |
| Nueva Indicación Predicha | Acidosis tubular renal |
| Puntaje de Predicción TxGNN | 0.9996 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 6 de 6) |
| Número de Registros Sanitarios | 6 (vigentes: 6) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Nitisinona inhibe la enzima 4-hidroxifenilpiruvato dioxigenasa (HPPD), una enzima de la vía de degradación de la tirosina. En la tirosinemia tipo 1 evita la acumulación de metabolitos tóxicos como la succinilacetona. Los datos compilados para este informe no incluyen una descripción formal del mecanismo de acción, por lo que esta explicación se basa en el rationale de reposicionamiento disponible.

En la tirosinemia tipo 1, una complicación frecuente es la tubulopatía renal proximal (acidosis tubular renal de tipo Fanconi), causada por esos metabolitos tóxicos. Por ello, el vínculo entre ambas indicaciones es indirecto: nitisinona podría beneficiar al riñón solo al prevenir el daño tubular derivado de la tirosinemia.

Es importante ser claro: **no hay evidencia de un efecto directo sobre la acidosis tubular renal primaria**. El puntaje tan alto de TxGNN es una predicción computacional y no debe interpretarse como prueba de eficacia.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para acidosis tubular renal.

---

## Información de Mercado en Colombia

Todos los registros son de VEXXOR MEDICAL INC.

<!-- review:begin co-lic-20261105-nitisinone-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Todos los registros son de VEXXOR MEDICAL INC. y están **cancelados**; no hay productos vigentes." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 6 registros sanitarios (vigentes: 6); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-nitisinone-1 -->

<!-- review:begin co-lic-20261105-nitisinone-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "(Se muestran 5 de los 6 registros; el sexto, 20110232, NITISOR® 5 MG cápsulas, también está cancelado.)" Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 6 registros sanitarios (vigentes: 6); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-nitisinone-2 -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20141253 | NITISINONA 10 MG | Cápsula dura | NITISINONA |
| 20141952 | NITISINONA 5 MG | Cápsula dura | NITISINONA |
| 20141256 | NITISINONA 2 MG | Cápsula dura | NITISINONA |
| 20144070 | NITISOR® 10 MG CAPSULAS | Cápsula dura | NITISINONA |
| 20140690 | NITISOR® 2 MG | Cápsula dura | NITISINONA |

---

## Consideraciones de Seguridad

- **Enfermedades con asociación de contraindicación en el grafo de conocimiento** (no provienen del texto del prospecto): enfermedad renal, piouréter, trombocitopenia, leucopenia, hipofosfatemia y tirosinemia. Deben verificarse con el prospecto oficial.
- **Interacciones farmacológicas**: se identificaron 201 interacciones, en su mayoría de nivel moderado. Algunos ejemplos: abametapir (tópico), abiraterona, isotretinoína, nifedipino, ibuprofeno, aldesleucina, pioglitazona, amiodarona, amlodipino, amobarbital, apalutamida, aprepitant, atazanavir, avatrombopag, baricitinib, dexametasona, bexaroteno, bicalutamida y jengibre. La interacción con armodafinilo es de nivel menor.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos ni publicaciones, y el vínculo con la acidosis tubular renal es solo indirecto, a través de la tirosinemia tipo 1. Además, faltan datos de seguridad del prospecto.

<!-- review:begin co-lic-20261105-nitisinone-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, no hay registros vigentes en Colombia y faltan datos de seguridad del prospecto." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 6 registros sanitarios (vigentes: 6); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-nitisinone-3 -->

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), un vacío de información que bloquea la evaluación de seguridad.
- Confirmar el mecanismo de acción con fuentes como DrugBank.
- Revisar la literatura sobre tubulopatía en tirosinemia tipo 1 tratada con nitisinona, para evaluar el efecto indirecto.
- Confirmar la situación regulatoria: el medicamento está comercializado y los 6 registros de 6 están vigentes.
- Si se continúa, plantear estudios preclínicos o de mecanismo antes de cualquier ensayo clínico.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "y están **cancelados**; no hay productos vigentes" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "(Se muestran 5 de los 6 registros; el sexto, 20110232, NITISOR® 5 MG cápsulas, también está cancelado.)" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "no hay registros vigentes en Colombia y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

