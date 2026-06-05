---
layout: default
title: Eculizumab
parent: 僅模型預測 (L5)
nav_order: 106
evidence_level: L5
indication_count: 10
---

# Eculizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Eculizumab: De Hemoglobinuria Paroxística Nocturna a Hematopoyesis Cíclica

## Resumen en Una Frase

Eculizumab es un anticuerpo monoclonal humanizado inhibidor del complemento C5, reconocido internacionalmente por su eficacia en hemoglobinuria paroxística nocturna (HPN) y síndrome hemolítico urémico atípico (aHUS) — enfermedades donde la activación descontrolada del complemento destruye eritrocitos y daña órganos.
El modelo TxGNN predice que podría ser efectivo para **Hematopoyesis Cíclica** (neutropenia cíclica),
sin embargo, **no existe ningún ensayo clínico ni publicación directa** que respalde esta dirección, y el enlace mecanístico es débil.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Hemoglobinuria paroxística nocturna / Síndrome hemolítico urémico atípico (inferido de literatura; sin registro formal en Colombia) |
| Nueva Indicación Predicha | Hematopoyesis Cíclica (Cyclic Hematopoiesis) |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos formales sobre el mecanismo de acción desde las fuentes consultadas. No obstante, la literatura presente en este Evidence Pack permite inferir con certeza que Eculizumab actúa como **inhibidor de la proteína complemento C5**: bloquea su escisión en C5a y C5b, impidiendo la formación del complejo de ataque a la membrana (MAC/C5b-9). Esta supresión selectiva de la vía terminal del complemento le confiere eficacia en la HPN —donde la ausencia de CD55/CD59 permite hemólisis intravascular masiva— y en el aHUS, donde mutaciones en reguladores del complemento desencadenan microangiopatía trombótica.

La **hematopoyesis cíclica** es un trastorno genético raro causado principalmente por mutaciones en el gen *ELANE* (elastasa de neutrófilos). La acumulación de elastasa mal plegada activa la respuesta a proteínas desplegadas (UPR) y ciclos de apoptosis en precursores mieloides, generando oscilaciones periódicas (~cada 21 días) en el recuento de neutrófilos. **La vía del complemento C5 no tiene ningún papel conocido en este mecanismo patogénico**, y no existe evidencia preclínica ni clínica que sugiera un efecto terapéutico de su inhibición en esta enfermedad.

El alto puntaje TxGNN (0.9997) refleja muy probablemente **proximidad topológica en el grafo de conocimiento biológico** —es decir, que la hematopoyesis cíclica comparte vecindad de nodos con enfermedades hematológicas donde Eculizumab ya tiene indicación, como la HPN— más que similitud mecanística real. El modelo captura relaciones de red, no causalidad farmacológica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para Eculizumab en hematopoyesis cíclica.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para Eculizumab en hematopoyesis cíclica.

---

## Información de Mercado en Colombia

Eculizumab no cuenta con ningún registro sanitario vigente en Colombia. El fármaco no está comercializado en el mercado local, lo que representa una barrera adicional significativa para cualquier uso clínico.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. Los datos de advertencias, contraindicaciones e interacciones farmacológicas no están disponibles en las fuentes consultadas para este análisis.

> **Nota:** Eculizumab es un inmunosupresor que bloquea la defensa del complemento contra bacterias encapsuladas. En todos sus usos aprobados internacionalmente se exige vacunación obligatoria contra *Neisseria meningitidis* antes del inicio del tratamiento, debido al riesgo de infecciones meningocócicas potencialmente fatales. Esta precaución es conocida y crítica, independientemente de la indicación.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción TxGNN para hematopoyesis cíclica carece de fundamento mecanístico directo: la enfermedad está impulsada por mutaciones en *ELANE* que generan ciclos de apoptosis en precursores mieloides, un proceso completamente distinto a la patología mediada por complemento que Eculizumab trata. No existen ensayos clínicos, estudios observacionales ni publicaciones que respalden esta indicación, y el fármaco no cuenta con registro sanitario en Colombia, lo que añade una barrera regulatoria y de acceso adicional.

**Para avanzar se necesita:**
- Evidencia preclínica (modelos animales o estudios in vitro) que demuestre algún efecto de la inhibición de C5 en la neutropenia cíclica
- Datos completos de mecanismo de acción (MOA) desde DrugBank para confirmar o descartar vínculos con la vía ELANE/UPR
- Advertencias y contraindicaciones del prospecto oficial (actualmente con datos faltantes en el Evidence Pack)
- Evaluación de viabilidad regulatoria y de acceso, dado que Eculizumab no está registrado en Colombia y es un biológico de alto costo
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

