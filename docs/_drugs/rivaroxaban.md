---
layout: default
title: Rivaroxaban
parent: Solo Predicción del Modelo (L5)
nav_order: 568
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-12
description: "Rivaroxaban: nueva indicación predicha, Artritis reumatoide (nivel de evidencia L5). Indicación original: Rivaroxabán"
monitor_inn: "RIVAROXABAN"
predicted_indications: ["rheumatoid arthritis", "gout", "HIV infectious disease", "brachydactyly-syndactyly syndrome"]
---

# Rivaroxaban
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Rivaroxabán: De Indicación Original (Anticoagulación) a Artritis Reumatoide
{: .text-alpha }

## Resumen en Una Frase

Rivaroxabán es un anticoagulante oral que inhibe el factor Xa y se usa para prevenir y tratar eventos tromboembólicos. El modelo TxGNN predice que podría ser efectivo para **artritis reumatoide**, pero **no hay ensayos clínicos** y la literatura recuperada **no evalúa** rivaroxabán como tratamiento de esta enfermedad. La predicción se apoya únicamente en el modelo computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Rivaroxabán (el registro sanitario no detalla el texto de la indicación; el uso conocido es anticoagulación) |
| Nueva Indicación Predicha | Artritis reumatoide |
| Puntaje de Predicción TxGNN | 0.9957 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 19) |
| Número de Registros Sanitarios | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, rivaroxabán es un inhibidor directo del factor Xa, y su eficacia en la prevención y el tratamiento del tromboembolismo venoso y de eventos embólicos asociados a fibrilación auricular está bien establecida.

La conexión con la artritis reumatoide es solo una hipótesis indirecta: la **trombo-inflamación**. Las enfermedades autoinmunes se asocian con un estado de hipercoagulabilidad (la generación de trombina está alterada), y la señalización del factor Xa y la trombina puede favorecer la inflamación.

Esta relación es de nivel hipotético. La anticoagulación podría, como máximo, reducir el riesgo trombótico, pero no hay evidencia de que modifique la actividad de la enfermedad articular. El puntaje alto del modelo no equivale a respaldo clínico.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para artritis reumatoide.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Revisión | JAMA | Diagnóstico y tratamiento del tromboembolismo venoso de miembros inferiores; incidencia de TVP de 88 a 112 por 100 000 personas-año. No trata artritis reumatoide. |
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Revisión | La Revue de médecine interne | El ensayo de generación de trombina es útil para evaluar hipercoagulabilidad en enfermedades autoinmunes. Respalda indirectamente el vínculo trombo-inflamatorio. |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Cohorte | PLoS One | Adherencia a rivaroxabán frente a apixabán en fibrilación auricular no valvular. No trata artritis reumatoide. |
| [41918541](https://pubmed.ncbi.nlm.nih.gov/41918541/) | 2026 | Reporte de caso | Cureus | Paciente de 88 años con enfermedad renal crónica y artritis reumatoide tratada con esteroides orales que sufrió eventos embólicos pese a anticoagulación. Es un contexto de comorbilidad, no de eficacia. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20233281 | Rivaroxabán 20 mg tabletas recubiertas | Tableta recubierta | Rivaroxabán |
| 20233324 | Decoag® 20 mg tabletas | Tableta recubierta | Rivaroxabán |
| 20204324 | Svatrom 20 mg tabletas recubiertas | Tableta recubierta | Rivaroxabán |
| 20192388 | Rivaroxabán 20 mg tabletas recubiertas | Tableta recubierta | Rivaroxabán |
| 20177233 | Xaroban® 20 | Tableta recubierta | Rivaroxabán |

---

## Consideraciones de Seguridad

- **Enfermedades con riesgo de contraindicación según el grafo de conocimiento** (no provienen del prospecto): insuficiencia hepática, enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar y trastornos de la coagulación sanguínea.
- **Interacciones farmacológicas** (100 interacciones identificadas; se destacan las de nivel mayor):
  - Ácido acetilsalicílico (mayor)
  - Cobicistat (mayor)
  - Deferasirox (mayor)
  - Ibritumomab tiuxetán (mayor)
  - Tositumomab (I-131) (mayor)
  - Entre las de nivel moderado figuran aprepitant, dexametasona, cimetidina, claritromicina, miconazol y clotrimazol.
- **Contexto de VIH:** los antirretrovirales potenciados con ritonavir o cobicistat inhiben CYP3A4 y la glicoproteína P, lo que aumenta la exposición a rivaroxabán y el riesgo de sangrado.

<!-- review:begin co-lic-20261105-rivaroxaban-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Los cinco registros sanitarios están **cancelados**; no hay registros vigentes." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-rivaroxaban-1 -->

No se dispone de las advertencias y contraindicaciones del prospecto; consultar el prospecto para completar la información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Pese al puntaje alto de TxGNN, no existen ensayos clínicos ni estudios que evalúen rivaroxabán en artritis reumatoide, y no hay un mecanismo creíble de modificación de la enfermedad. Además, falta la información de seguridad del prospecto.

<!-- review:begin co-lic-20261105-rivaroxaban-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, no hay registros sanitarios vigentes en Colombia y falta la información de seguridad del prospecto." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-rivaroxaban-2 -->

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones).
- Completar los datos del mecanismo de acción desde DrugBank.
- Estudios preclínicos que respalden el vínculo trombo-inflamatorio en artritis reumatoide.
- Evaluar la relevancia clínica de los otros candidatos predichos, aunque ninguno cuenta con respaldo: gota (L5, sin mecanismo creíble), infección por VIH (L4, la literatura se refiere a interacciones de seguridad, no a eficacia) y síndrome de braquidactilia-sindactilia (L5, sin datos).
- Confirmar el estatus regulatorio local, dado que el medicamento está comercializado y cuenta con al menos 19 licencias vigentes.

<!-- review:begin co-lic-20261112-rivaroxaban-1 -->

> **Corrección de revisión (2026-11-12)**: Texto original: "5 licencias vigentes" Corregido según los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-05): al menos 19 registros sanitarios vigentes (la lista de los datos está limitada a 20 registros). Las cifras actuales están en el Resumen rápido. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261112-rivaroxaban-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Los cinco registros sanitarios están **cancelados**; no hay registros vigentes" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "no hay registros sanitarios vigentes en Colombia y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-12 | Número de registros vigentes: 5 → al menos 19 | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

