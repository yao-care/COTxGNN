---
layout: default
title: Alirocumab
parent: Solo Predicción del Modelo (L5)
nav_order: 37
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Alirocumab: nueva indicación predicha, Ictiosis ligada al X sin deficiencia de esteroide sulfatasa (nivel de evidencia L5). Indicación original: ALIROCUMAB"
monitor_inn: "ALIROCUMAB"
predicted_indications: ["ichthyosis, X-linked, without steroid sulfatase deficiency", "disorder of other vitamins and cofactors metabolism and transport", "xanthomatosis (disease)", "46,XY disorder of sexual development due to dihydrotestosterone backdoor pathway biosynthesis defect", "cholesterol catabolic process disease", "46,XY disorder of sex development due to a cholesterol synthesis defect", "dappled diaphyseal dysplasia", "neutral lipid storage disease", "3-hydroxyacyl-CoA dehydrogenase deficiency", "spastic paraplegia-optic atrophy-neuropathy and spastic paraplegia-optic atrophy-neuropathy-related disorder"]
---

# Alirocumab
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

## Alirocumab: De Alirocumab (indicación sin especificar en el registro) a Ictiosis ligada al X sin deficiencia de esteroide sulfatasa
{: .text-alpha }

## Resumen en Una Frase

Alirocumab es un anticuerpo monoclonal contra PCSK9, comercializado en Colombia como Praluent®. Su registro sanitario solo indica el nombre del principio activo, y en la práctica se usa para reducir el colesterol LDL.
El modelo TxGNN predice que podría ser efectivo para **ictiosis ligada al X sin deficiencia de esteroide sulfatasa**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción específica; se trata únicamente de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | ALIROCUMAB (el registro no detalla la indicación; según la literatura, hipercolesterolemia y enfermedad cardiovascular aterosclerótica) |
| Nueva Indicación Predicha | Ictiosis ligada al X sin deficiencia de esteroide sulfatasa |
| Puntaje de Predicción TxGNN | 99.43% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo cancelado (sin registros vigentes) |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, alirocumab es un anticuerpo monoclonal humano que se une a PCSK9 (proproteína convertasa subtilisina/kexina tipo 9). Con ello aumenta la disponibilidad de receptores de LDL en el hígado y reduce el colesterol LDL circulante. Su eficacia en hipercolesterolemia y en la reducción de eventos cardiovasculares está bien documentada.

Para la ictiosis ligada al X, **no se identifica un vínculo mecanístico claro**. Esta enfermedad se relaciona con una alteración en la vía del sulfato de colesterol y la esteroide sulfatasa en los lípidos de la barrera cutánea. La inhibición de PCSK9 reduce el LDL-C circulante, pero no tiene un papel establecido en el manejo epidérmico del sulfato de colesterol.

El puntaje alto (99.43%) refleja solo una asociación basada en grafos de conocimiento. No debe interpretarse como evidencia de eficacia.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20117604 | PRALUENT® 75MG/ML SOLUCIÓN INYECTABLE | Solución inyectable | ALIROCUMAB | Cancelado |
| 20097020 | PRALUENT® 150MG/ML SOLUCIÓN INYECTABLE | Solución inyectable | ALIROCUMAB | Cancelado |

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas:** la consulta se completó y registró una sola entrada, de naturaleza farmacológica y no una interacción con otro medicamento: el objetivo molecular de alirocumab, PCSK9. No se reportan interacciones clínicas con otros fármacos.
- Un análisis agrupado de seguridad del estudio ODYSSEY OUTCOMES (47 296 pacientes-año de observación; PMID 38658193) está disponible en la literatura general de alirocumab, aunque no corresponde a la indicación predicha.

No se dispone de advertencias ni contraindicaciones del prospecto en los datos compilados. Consultar el prospecto para información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para ictiosis ligada al X carece de ensayos clínicos, de literatura y de un vínculo mecanístico plausible; el puntaje del modelo es el único respaldo. Además, el fármaco no tiene registros vigentes en Colombia.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA para revisar advertencias y contraindicaciones.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar estudios preclínicos o de mecanismo que justifiquen un vínculo entre PCSK9 y el metabolismo del sulfato de colesterol en la piel.
- Aclarar el estado regulatorio, dado que ambos registros están cancelados.

---

### Nota sobre otras predicciones evaluadas

Entre las demás predicciones, la que cuenta con más respaldo es **"enfermedad del proceso catabólico del colesterol"**. Tiene literatura abundante (revisiones de terapias dirigidas a PCSK9, resultados del estudio ODYSSEY OUTCOMES y un análisis de seguridad), pero corresponde esencialmente al uso ya aprobado del fármaco para reducir lípidos y no a un reposicionamiento genuino. Por ello, su nivel L1 se basa en citas de literatura y no se pudo verificar de forma independiente. La predicción de **xantomatosis** tiene solo dos reportes de caso (nivel L4) y no demuestra regresión de xantomas con alirocumab. Para el defecto de síntesis de colesterol (46,XY), existe una posible preocupación de seguridad, ya que reducir el LDL-C podría ser contraproducente en un estado de déficit de colesterol.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

