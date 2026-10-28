---
layout: default
title: Ocrelizumab
parent: Solo Predicción del Modelo (L5)
nav_order: 476
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
description: "Ocrelizumab: nueva indicación predicha, Carcinoma de mama HER2 positivo (nivel de evidencia L5). Indicación original: Ocrelizumab"
monitor_inn: "OCRELIZUMAB"
predicted_indications: ["HER2 positive breast carcinoma", "progesterone-receptor positive breast cancer", "normal breast-like subtype of breast carcinoma", "breast tumor luminal A or B", "progesterone-receptor negative breast cancer"]
---

# Ocrelizumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Ocrelizumab: De Esclerosis Múltiple a Carcinoma de Mama HER2 Positivo
{: .text-alpha }

## Resumen en Una Frase

Ocrelizumab es un anticuerpo monoclonal anti-CD20 que depleta linfocitos B, utilizado en esclerosis múltiple (formas recurrentes y primaria progresiva). El modelo TxGNN predice que podría ser efectivo para **carcinoma de mama HER2 positivo**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta indicación; la predicción se basa únicamente en el modelo computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ocrelizumab (el registro sanitario solo indica el nombre del principio activo, sin texto de indicación detallado) |
| Nueva Indicación Predicha | Carcinoma de mama HER2 positivo |
| Puntaje de Predicción TxGNN | 0.9989 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado en los datos compilados. Según la información conocida, ocrelizumab es un anticuerpo monoclonal humanizado dirigido contra CD20 que depleta los linfocitos B, y su eficacia está establecida en esclerosis múltiple.

Los datos compilados **no respaldan un vínculo mecanístico** entre la depleción de linfocitos B CD20+ y la biología tumoral dependiente de HER2. No existen ensayos ni literatura que conecten ambos conceptos. El puntaje alto de TxGNN (0.9989) es una predicción del modelo y no constituye evidencia clínica.

Otras predicciones del modelo TxGNN (deep learning) para este fármaco (cáncer de mama con receptor de progesterona positivo: 0.9981; subtipo de carcinoma de mama similar a mama normal: 0.9981; tumor de mama luminal A o B: 0.9981; cáncer de mama con receptor de progesterona negativo: 0.9980) tienen puntuaciones casi idénticas. Esto sugiere que las puntuaciones provienen del modelo TxGNN y pueden reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica específica de cada indicación.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para carcinoma de mama HER2 positivo.

Nota: para otra indicación predicha (tumor de mama luminal A o B) se recuperaron 18 publicaciones, pero todas tratan sobre ocrelizumab en esclerosis múltiple, terapias anti-CD20 en general, hipogammaglobulinemia secundaria o enfermedades autoinmunes. Ninguna aborda cáncer de mama; parecen haberse recuperado por el nombre del fármaco y no por la indicación. Solo son útiles como contexto de seguridad (por ejemplo, riesgo de hipogammaglobulinemia e infecciones por depleción de linfocitos B).

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20115374 (cancelado) | OCREVUS® Concentrado para solución para infusión 300 mg/10 mL | Solución concentrada para infusión | Ocrelizumab |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (100 interacciones registradas; se listan las principales):
  - **Moderadas**: corticosteroides (hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida, prednisolona, prednisona), radiofármacos (iobenguano I-131, ibritumomab tiuxetán, tositumomab, samario-153 lexidronam), albendazol, pentamidina y levamisol.
  - **Menores**: sales de zinc (sulfato, acetato, gluconato, cloruro).
- **Contexto de seguridad de la literatura**: la depleción de linfocitos B se asocia con riesgo de hipogammaglobulinemia secundaria e infecciones.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para carcinoma de mama HER2 positivo está respaldada solo por el modelo (nivel L5), sin ensayos clínicos, sin literatura específica y sin vínculo mecanístico plausible. Además, el producto no tiene registro sanitario vigente en Colombia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción del fármaco (por ejemplo, consulta a DrugBank).
- Estudios preclínicos que evalúen un posible papel de la depleción de linfocitos B CD20+ en cáncer de mama HER2 positivo.
- Descargar y analizar el prospecto de INVIMA para obtener advertencias y contraindicaciones (brecha de datos bloqueante para el tamizaje de seguridad).
- Aclarar el estado regulatorio local, dado que el único registro está cancelado.
- Revisión de literatura dirigida a la indicación (no solo al nombre del fármaco) antes de reconsiderar la prioridad.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

