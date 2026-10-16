---
layout: default
title: Nitisinone
parent: Solo Predicción del Modelo (L5)
nav_order: 470
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Nitisinone: nueva indicación predicha, Acidosis tubular renal (nivel de evidencia L5). Indicación original: NITISINONA"
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

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Nitisinona: De Tirosinemia Tipo 1 a Acidosis Tubular Renal

## Resumen en Una Frase

Nitisinona es un inhibidor de la enzima HPPD, utilizado originalmente para el tratamiento de la tirosinemia hereditaria tipo 1 (el registro sanitario en Colombia solo indica "NITISINONA" como indicación).
El modelo TxGNN predice que podría ser efectivo para **acidosis tubular renal**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, por lo que se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | NITISINONA (el registro no detalla la indicación; por mecanismo y uso conocido corresponde a tirosinemia hereditaria tipo 1) |
| Nueva Indicación Predicha | Acidosis tubular renal |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 6 (0 vigentes, 6 cancelados) |
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

Todos los registros son de VEXXOR MEDICAL INC. y están **cancelados**; no hay productos vigentes.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20141253 | NITISINONA 10 MG | Cápsula dura | NITISINONA |
| 20141952 | NITISINONA 5 MG | Cápsula dura | NITISINONA |
| 20141256 | NITISINONA 2 MG | Cápsula dura | NITISINONA |
| 20144070 | NITISOR® 10 MG CAPSULAS | Cápsula dura | NITISINONA |
| 20140690 | NITISOR® 2 MG | Cápsula dura | NITISINONA |

(Se muestran 5 de los 6 registros; el sexto, 20110232, NITISOR® 5 MG cápsulas, también está cancelado.)

---

## Consideraciones de Seguridad

- **Enfermedades con asociación de contraindicación en el grafo de conocimiento** (no provienen del texto del prospecto): enfermedad renal, piouréter, trombocitopenia, leucopenia, hipofosfatemia y tirosinemia. Deben verificarse con el prospecto oficial.
- **Interacciones farmacológicas**: se identificaron 201 interacciones, en su mayoría de nivel moderado. Algunos ejemplos: abametapir (tópico), abiraterona, isotretinoína, nifedipino, ibuprofeno, aldesleucina, pioglitazona, amiodarona, amlodipino, amobarbital, apalutamida, aprepitant, atazanavir, avatrombopag, baricitinib, dexametasona, bexaroteno, bicalutamida y jengibre. La interacción con armodafinilo es de nivel menor.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos ni publicaciones, y el vínculo con la acidosis tubular renal es solo indirecto, a través de la tirosinemia tipo 1. Además, no hay registros vigentes en Colombia y faltan datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), un vacío de información que bloquea la evaluación de seguridad.
- Confirmar el mecanismo de acción con fuentes como DrugBank.
- Revisar la literatura sobre tubulopatía en tirosinemia tipo 1 tratada con nitisinona, para evaluar el efecto indirecto.
- Aclarar la situación regulatoria, ya que todos los registros están cancelados.
- Si se continúa, plantear estudios preclínicos o de mecanismo antes de cualquier ensayo clínico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

