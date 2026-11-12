---
layout: default
title: Benzydamine
parent: Solo Predicción del Modelo (L5)
nav_order: 102
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
description: "Benzydamine: nueva indicación predicha, Hiperplasia prostática benigna (nivel de evidencia L5). Indicación original: Benzidamina"
monitor_inn: "benzydamine"
predicted_indications: ["benign prostatic hyperplasia (disease)"]
---

# Benzydamine
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

## Benzidamina: De Indicación Original (Benzidamina, solución bucal) a Hiperplasia Prostática Benigna
{: .text-alpha }

## Resumen en Una Frase

Benzidamina es un agente de acción local con propiedades antiinflamatorias, analgésicas y anestésicas locales, comercializado en Colombia como solución bucal.
El modelo TxGNN predice que podría ser efectivo para **hiperplasia prostática benigna (HPB)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Benzidamina (el registro sanitario solo indica el nombre del principio activo, sin detalle de indicación) |
| Nueva Indicación Predicha | Hiperplasia prostática benigna |
| Puntaje de Predicción TxGNN | 0.9926 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la benzidamina es un agente de acción local de tipo antiinflamatorio no esteroideo, con efectos analgésicos y anestésicos locales. Se le atribuye la inhibición de citocinas proinflamatorias (como TNF-alfa e IL-1beta) y un efecto estabilizador de membrana.

Una posible relación, todavía no verificada, es que la inflamación prostática crónica contribuye a la patogénesis de la HPB y a los síntomas del tracto urinario inferior. Por ello, una actividad antiinflamatoria podría ser teóricamente relevante.

Sin embargo, no existe evidencia mecanística directa que vincule la benzidamina con el tejido prostático. Además, su uso es principalmente tópico (enjuague bucal, spray de garganta, uso vaginal), por lo que la exposición sistémica o prostática es incierta. La puntuación alta del modelo es el único sustento de esta hipótesis.

<!-- review:begin co-lic-20261105-benzydamine-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "El único registro existente, fabricado por Laboratorios Remo S.A.S., está cancelado; no hay productos vigentes en el mercado colombiano." Eliminado: el número o el estado de los registros sanitarios no coincidía con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-benzydamine-1 -->

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19966754 | BENZYCOL® VERDE SOLUCION BUCAL | Solución bucal | Benzidamina |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se cuenta con interacciones farmacológicas registradas en los datos compilados para este informe.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura. Además, el producto es de uso tópico, lo que limita la viabilidad a corto plazo.

<!-- review:begin co-lic-20261105-benzydamine-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, el producto es de uso tópico y su único registro sanitario en Colombia está cancelado, lo que limita la viabilidad a corto plazo." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-benzydamine-2 -->

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), actualmente no disponible
- Completar los datos del mecanismo de acción desde DrugBank
- Buscar evidencia preclínica o clínica sobre benzidamina en HPB o inflamación prostática
- Evaluar la compatibilidad de vías de administración (tópica/local frente a la exposición prostática requerida)
- Confirmar si existe algún producto con benzidamina vigente en Colombia que permita el desarrollo

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "El único registro existente, fabricado por Laboratorios Remo S.A.S., está cancelado; no hay productos vigentes en el mercado colombiano" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "y su único registro sanitario en Colombia está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

