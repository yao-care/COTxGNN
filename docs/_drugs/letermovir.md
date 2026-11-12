---
layout: default
title: Letermovir
parent: Solo Predicción del Modelo (L5)
nav_order: 390
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
description: "Letermovir: nueva indicación predicha, Candidiasis vulvovaginal (nivel de evidencia L5). Indicación original: LETERMOVIR"
monitor_inn: "LETERMOVIR"
predicted_indications: ["vulvovaginal candidiasis"]
---

# Letermovir
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

## Letermovir: De Letermovir (CMV) a Candidiasis Vulvovaginal
{: .text-alpha }

## Resumen en Una Frase

Letermovir es un antiviral específico contra el citomegalovirus (CMV), registrado en Colombia bajo el nombre PREVYMIS en tabletas.
El modelo TxGNN predice que podría ser efectivo para **candidiasis vulvovaginal**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es solo una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | LETERMOVIR (el registro sanitario no detalla el texto de la indicación) |
| Nueva Indicación Predicha | Candidiasis vulvovaginal |
| Puntaje de Predicción TxGNN | 0.9988 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según el conocimiento farmacológico general, letermovir es un antiviral específico contra el CMV que inhibe el complejo terminasa viral (subunidades pUL56/pUL51/pUL89), bloqueando el corte y empaquetamiento del ADN viral.

La candidiasis vulvovaginal es una infección fúngica. Los hongos del género *Candida* no tienen un blanco equivalente al complejo terminasa del CMV, por lo que no se esperaría actividad antifúngica. **No se identifica un vínculo mecanístico creíble** entre la indicación original y la nueva.

El puntaje alto de TxGNN (0.9988) es una predicción del modelo TxGNN (aprendizaje profundo). Puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, y no es evidencia biológica. Cualquier hipótesis requeriría validación experimental independiente, por ejemplo pruebas de susceptibilidad in vitro frente a *Candida* spp.

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
| 20194849 | PREVYMIS 240MG TABLETAS | Tableta | LETERMOVIR |

El fabricante es Merck Sharp & Dohme LLC. La única vía de administración registrada es la oral.

<!-- review:begin co-lic-20261105-letermovir-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La única vía de administración registrada es la oral. Dado que el único registro está cancelado, actualmente no hay presentación vigente en el mercado colombiano." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-letermovir-1 -->

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. En la muestra analizada predominan las de nivel moderado y destacan tres de nivel **mayor**:
  - Eliglustat
  - Naloxegol
  - Cisaprida

  Otras interacciones de nivel moderado incluyen corticoides (hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida), antidiabéticos (pioglitazona, saxagliptina, glimepirida, clorpropamida, acetohexamida), inhibidores de bomba de protones (omeprazol, lansoprazol), aprepitant, claritromicina, naldemedina y nitisinona.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura, y sin un vínculo mecanístico plausible, ya que letermovir actúa sobre un blanco viral sin equivalente en *Candida*.

<!-- review:begin co-lic-20261105-letermovir-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción se apoya únicamente en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura, y sin un vínculo mecanístico plausible, ya que letermovir actúa sobre un blanco viral sin equivalente en *Candida*. Además, el único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-letermovir-2 -->

**Para avanzar se necesita:**
- Pruebas de susceptibilidad in vitro de *Candida* spp. frente a letermovir como validación mínima
- Datos del mecanismo de acción desde DrugBank para analizar posibles vínculos mecanísticos
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones) antes de cualquier evaluación de seguridad
- Evaluar la compatibilidad de vía de administración (la presentación registrada es solo oral)
- Aclarar la situación regulatoria del producto en Colombia

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Dado que el único registro está cancelado, actualmente no hay presentación vigente en el mercado colombiano" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Además, el único registro sanitario en Colombia está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

